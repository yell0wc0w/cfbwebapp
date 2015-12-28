from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from .models import Question, Choice, AthleteProfile
from .forms import AthleteNameForm

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


def AthleteView(request):
    # Handle text input, as needed
    athletename = ''
    newathletename = ''
    POST_data = request.POST.dict()

    if POST_data.get('id') is None:

        if request.method == 'POST':
            athletename = POST_data.get('athletename')
            newathletename = POST_data.get('newathletename')

        # Create new profile as needed
        if newathletename is not None:
            new_athlete_profile = AthleteProfile(name=newathletename)
            new_athlete_profile.save()
            athletename = newathletename

        # Preparation of rendering screen
        try:
            athleteprofile = AthleteProfile.objects.get(name__contains=athletename)
        except MultipleObjectsReturned:
            athleteprofile = AthleteProfile.objects.filter(name__contains=athletename)[0]
        except ObjectDoesNotExist:
            athleteprofile = AthleteProfile.objects.filter(name__contains='')[0]
        context = {'athleteprofile': athleteprofile}
        html = 'polls/index.html'

    elif POST_data.get('id') is not None:

        #retrieve profile
        athletename = POST_data.get('athletename')

        try:
            athleteprofile = AthleteProfile.objects.get(name__contains=athletename)
        except MultipleObjectsReturned:
            athleteprofile = AthleteProfile.objects.filter(name__contains=athletename)[0]

        athleteprofile.setup_stats()

        #save data in DB
        if POST_data.get('value').isdigit():
            athleteprofile.set_stat_value(POST_data.get('id'), int(POST_data.get('value')))
        else:
            athleteprofile.set_stat_value(POST_data.get('id'), POST_data.get('value'))

        athleteprofile.presave_stats()
        athleteprofile.save()

        #now return new value to page (perhaps DB call is not required? future optimization)
        context = {'stat_result': athleteprofile.get_stat_value(POST_data.get('id'))}
        html = 'polls/results.html'

    return render(request, html, context)