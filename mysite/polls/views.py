from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice, AthleteProfile
from .forms import AthleteNameForm


# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
#
#
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'

class AthleteView(generic.ListView):
    model = AthleteProfile
    template_name = 'polls/index.html'
    context_object_name = 'athleteprofile'

    def get_queryset(self):
        """Return an athlete."""
        return AthleteProfile.objects.get(name__contains="Hoang")

def loadathlete(request, AthleteNameToLoad):
    result = get_object_or_404(AthleteProfile, AthleteProfile.objects.get(name__contains="Louis"))
    return result

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def get_name(request):
    if request.method == 'POST':
        form = AthleteNameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('thanks')
        else:
            form = NameForm()

    return render(request, name.html, {'form':form})