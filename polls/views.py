from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# Create your views here.
# te funkcje są widokami, które odpowiadają na żądania HTTP i zwracają odpowiedzi w postaci tekstu.
# Widoki te są używane do obsługi różnych akcji w aplikacji "polls", takich jak wyświetlanie indeksu, szczegółów pytania, wyników i głosowania.

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
        


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # Pobiera pytanie lub zwraca 404, jeśli nie istnieje
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])  # Pobiera wybraną opcję głosowania
    except (KeyError, Choice.DoesNotExist):
        # Jeśli nie wybrano opcji lub opcja nie istnieje, renderuje komunikat o błędzie
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice.",
        },
    )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Jeśli opcja została wybrana, zwiększa liczbę głosów i zapisuje zmiany
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        # Przekierowuje do strony wyników głosowania po pomyślnym głosowaniu

class ResultsView(generic.DetailView):  
    model = Question  # Model, który będzie używany w widoku wyników
    template_name = "polls/results.html"  # Szablon, który będzie renderowany w widoku wyników

    def get_queryset(self): # Metoda, która zwraca zapytanie do bazy danych
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now()) # Zwraca tylko pytania, które zostały opublikowane (pub_date <= teraz)
