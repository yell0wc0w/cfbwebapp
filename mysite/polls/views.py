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
    athleteName = ''
    if request.method == 'POST':
        form = AthleteNameForm(request.POST)
        if form.is_valid():
            athleteName = form.cleaned_data.get('athleteName')
    else:
        form = AthleteNameForm()


    # Preparation of rendering screen
    try:
        athleteprofile = AthleteProfile.objects.get(name__contains=athleteName)
    except MultipleObjectsReturned:
        athleteprofile = AthleteProfile.objects.filter(name__contains=athleteName)[0]

    context = {'athleteprofile': athleteprofile, 'form': form}
    return render(request, 'polls/index.html', context)