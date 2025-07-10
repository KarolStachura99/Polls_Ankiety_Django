import datetime

from django.test import TestCase
from django.utils import timezone

from polls.models import Question
from django.urls import reverse

# Create your tests here.

class QuestionModelTests(TestCase): #testuje logikę modelu Question
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose 
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question =Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)


    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase): # Testy dla widoku listy (indeksu) pytań
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30) # Tworzymy pytanie z datą publikacji w przeszłości
        response = self.client.get(reverse("polls:index")) # Wysyłamy żądanie GET do widoku indeksu pytań
        self.assertQuerySetEqual(
            response.context["latest_question_list"], # Sprawdzamy, czy lista pytań zawiera tylko to pytanie
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30) # Tworzymy pytanie z datą publikacji w przyszłości
        response = self.client.get(reverse("polls:index")) # Wysyłamy żądanie GET do widoku indeksu pytań
        self.assertContains(response, "No polls are available.") # Sprawdzamy, czy odpowiedź zawiera komunikat o braku dostępnych pytań
        self.assertQuerySetEqual(response.context["latest_question_list"], []) # Sprawdzamy, czy lista pytań jest pusta

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", days=-30) # Tworzymy pytanie z datą publikacji w przeszłości
        create_question(question_text="Future question.", days=30) # Tworzymy pytanie z datą publikacji w przyszłości
        response = self.client.get(reverse("polls:index")) # Wysyłamy żądanie GET do widoku indeksu pytań
        self.assertQuerySetEqual( 
            response.context["latest_question_list"], # Sprawdzamy, czy lista pytań zawiera tylko pytanie z przeszłości
            [question],
        )

    def test_two_past_questions(self):  
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days=-30) # Tworzymy pierwsze pytanie z datą publikacji w przeszłości
        question2 = create_question(question_text="Past question 2.", days=-5)  # Tworzymy drugie pytanie z datą publikacji w przeszłości
        response = self.client.get(reverse("polls:index")) # Wysyłamy żądanie GET do widoku indeksu pytań
        self.assertQuerySetEqual(
            response.context["latest_question_list"], # Sprawdzamy, czy lista pytań zawiera oba pytania
            [question2, question1],
        )
        
class QuestionDetailViewTests(TestCase):  # Testy dla widoku szczegółów pytania
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future 
        returns a 404 not found. 
        """
        future_question = create_question(question_text="Future question.", days=5) # Tworzymy pytanie z datą publikacji w przyszłości
        url = reverse("polls:detail", args=(future_question.id,)) # Generujemy URL do widoku szczegółów pytania
        response = self.client.get(url) # Wysyłamy żądanie GET do tego URL
        self.assertEqual(response.status_code, 404) # Sprawdzamy, czy odpowiedź ma status 404 (nie znaleziono)   

    def test_past_question(self):  
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text="Past Question.", days=-5) # Tworzymy pytanie z datą publikacji w przeszłości
        url = reverse("polls:detail", args=(past_question.id,)) # Generujemy URL do widoku szczegółów pytania
        response = self.client.get(url) # Wysyłamy żądanie GET do tego URL
        self.assertContains(response, past_question.question_text) # Sprawdzamy, czy odpowiedź zawiera tekst pytania


class QuestionResultsViewTests(TestCase): # Testy dla widoku wyników pytania results
    def test_future_question(self):
        """
        The results view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text="Future question.", days=5) # Tworzymy pytanie z datą publikacji w przyszłości
        url = reverse("polls:results", args=(future_question.id,)) # Generujemy URL do widoku wyników pytania
        response = self.client.get(url) # Wysyłamy żądanie GET do tego URL
        self.assertEqual(response.status_code, 404) # Sprawdzamy, czy odpowiedź ma status 404 (nie znaleziono) 

    def test_past_question(self): 
        """
        The results view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse("polls:results", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)