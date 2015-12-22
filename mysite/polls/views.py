from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.core.exceptions import MultipleObjectsReturned
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
    POST_data = request.POST.dict()

    if POST_data.get('id') is None:

        if request.method == 'POST':
            form = AthleteNameForm(request.POST)
            if form.is_valid():
                athletename = form.cleaned_data.get('athletename')
        else:
            form = AthleteNameForm()

        # Preparation of rendering screen
        try:
            athleteprofile = AthleteProfile.objects.get(name__contains=athletename)
        except MultipleObjectsReturned:
            athleteprofile = AthleteProfile.objects.filter(name__contains=athletename)[0]

        context = {'athleteprofile': athleteprofile, 'form': form}
        html = 'polls/index.html'

    elif POST_data.get('id') is not None:

        #retrieve profile
        athletename = POST_data.get('athletename')

        try:
            athleteprofile = AthleteProfile.objects.get(name__contains=athletename)
        except MultipleObjectsReturned:
            athleteprofile = AthleteProfile.objects.filter(name__contains=athletename)[0]

        #save data in DB
        athleteprofile.set_stat_value(POST_data.get('id'), int(POST_data.get('value')))
        athleteprofile.save()


        #now return new value to page (perhaps DB call is not required? future optimization)
        context = {'stat_result': athleteprofile.get_stat_value(POST_data.get('id')) }
        html = 'polls/results.html'

    return render(request, html, context)