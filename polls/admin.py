from django.contrib import admin
from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 # liczba pustych formularzy wyborów do dodania


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    list_per_page = 20
    date_hierarchy = "pub_date"
    ordering = ["-pub_date"]

admin.site.register(Question, QuestionAdmin)
# NIE rejestrujemy już osobno modelu Choice