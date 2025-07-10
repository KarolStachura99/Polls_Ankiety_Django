from django.urls import path # importujemy moduł path do definiowania ścieżek URL
from . import views # modół views służy do obsługi widoków w aplikacji

app_name = "polls" # app_name jest używane do przestrzeni nazw, aby uniknąć konfliktów nazw w aplikacji Django
urlpatterns = [

    path("", views.IndexView.as_view(), name="index"), 
    # Ścieżka do widoku indeksu, który wyświetla listę pytań
    # używamy widoku opakowanego w klasę IndexView, który dziedziczy po generics.ListView
    # i renderuje szablon "polls/index.html" z kontekstem zawierającym listę pytań.
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]