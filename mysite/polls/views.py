from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

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
    if request.method == 'POST':
        form = AthleteNameForm(request.POST)
        if form.is_valid():
            athleteName = form.cleaned_data.get('athleteName')
            print('Name successful!')
    else:
        athleteName = 'Hoang'
        form = AthleteNameForm()


    # Preparation of rendering screen
    athleteprofile = AthleteProfile.objects.get(name__contains=athleteName)
    context = {'athleteprofile': athleteprofile, 'form': form}
    return render(request, 'polls/index.html', context)