from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin

class Question(models.Model): #Model to klasa, która opisuje strukturę tabeli w bazie danych
    question_text = models.CharField(max_length=200) #tworzy pole tekstowe(kolumnę w tabeli) o nazwie question_text i maksymalnej długości 200 znaków
    pub_date = models.DateTimeField("date published") #tworzy pole daty i czasu o nazwie pub_date, które przechowuje datę publikacji pytania
    def __str__(self): #metoda, która zwraca reprezentację tekstową obiektu Question
        return self.question_text #zwraca treść pytania jako tekst, co ułatwia jego wyświetlanie w interfejsie administracyjnym Django 
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #metoda, która sprawdza, czy pytanie zostało opublikowane w ciągu ostatnich 24 godzin
        #zwraca True, jeśli data publikacji jest w przedziale od 24 godzin

    @admin.display( # dekorator, który umożliwia wyświetlanie niestandardowych etykiet w interfejsie administracyjnym Django
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #tworzy pole klucza obcego, które łączy wybór z pytaniem
    # on_delete=models.CASCADE oznacza, że jeśli pytanie zostanie usunięte, wszystkie powiązane wybory również zostaną usunięte
    choice_text = models.CharField(max_length=200) #tworzy pole tekstowe o nazwie Choice_text, które przechowuje treść wyboru, maksymalna długość to 200 znaków
    votes = models.IntegerField(default=0) #tworzy pole liczb całkowitych o nazwie votes, które przechowuje liczbę głosów dla danego wyboru, domyślnie ustawione na 0
    
    def __str__(self): 
        return self.choice_text