# Polls_Ankiety_Django

Projekt aplikacji Django do tworzenia i zarządzania ankietami i quizami online. Użytkownicy mogą głosować na przygotowane pytania, a administratorzy mają dostęp do panelu administracyjnego z dostosowanym interfejsem.

---

##  Funkcjonalności

-  Głosowanie na pytania i odpowiedzi
-  Sprawdzanie oddanej odpowiedzi czy jest poprawna
-  Wyświetlanie wyników w czasie rzeczywistym
-  Panel admina z personalizowanym widokiem
-  Wbudowany **Django Debug Toolbar** (dla deweloperów)
-  Widok strony głównej dostępny z panelu admina

---

##  Struktura katalogów
```
polls_ankiety_django/
├── mysite/ # Konfiguracja projektu Django
├── polls/ # Główna aplikacja (ankiety)
├── templates/ # Szablony HTML
│ └── admin/ # Dostosowane szablony panelu admina
├── venv/ # Środowisko wirtualne (ignorowane przez Git)
├── manage.py
└── .gitignore
```
---

## Jak uruchomić projekt lokalnie

```bash
git clone https://github.com/KarolStachura99/Polls_Ankiety_Django.git
cd Polls_Ankiety_Django
python -m venv venv
venv\Scripts\activate  # lub source venv/bin/activate na Mac/Linux
pip install -r requirements.txt  # jeśli utworzysz plik z zależnościami
python manage.py runserver
```

---

Technologie
Python 3.x

Django 5.2

HTML, CSS

SQLite (domyślnie)

---

Autor
Projekt stworzony przez Karol Stachura w ramach nauki Django z oficjalnego tutoriala.

Zainspirowane: https://docs.djangoproject.com/pl/5.2/intro/

---

Zrzuty ekranu
<img width="1920" height="913" alt="image" src="https://github.com/user-attachments/assets/21bacfc0-7af8-440b-aa9a-d530e87a7ebd" />
Dodawanie nowego pytania i odpowiedzi

<img width="1055" height="602" alt="image" src="https://github.com/user-attachments/assets/06905054-cab4-4465-ada5-820de36562dc" />
Strona główna administratora

<img width="865" height="589" alt="image" src="https://github.com/user-attachments/assets/8bbce258-a76d-4bbe-accd-280b69977854" />
Udzielanie odpowiedzi

<img width="1920" height="915" alt="image" src="https://github.com/user-attachments/assets/466c3cdf-7c79-4fe2-8503-4f890d33ff2f" />
Nadawanie uprawnień urzytkownikom

<img width="1374" height="1037" alt="image" src="https://github.com/user-attachments/assets/727f76ae-d430-4ef0-91df-39531f997872" />
Wykresy z głosami oddanymi przez użytkowników  
