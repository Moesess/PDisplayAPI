# PDisplayAPI

## Uruchomienie
Zakładam że znajdujemy się w katalogu w którym mamy sklonowane repozytorium. Po sklonowaniu powinniśmy mieć 
folder z aplikacją PDisplayAPI. NIE WCHODZIMY DO NIEGO. Wersja pythona to 3.11.3.

Tworzymy virtualenv i aktywujemy go. Powinien przed znakiem zachęty pojawić się (PDisplayAPIVenv)
```shell
python -m venv PDisplayAPIVenv
PDisplayAPIVenv\Scripts\activate
```

Teraz możemy wejść do projektu.
I instalujemy zależności w pliku requirements.txt
```shell
cd PDisplayAPI
pip install -r requirements.txt
```

Po skończeniu instalacji, wpisujemy następującą komendę w celu utworzenia bazy danych.

```shell
python manage.py migrate
```

W celu uruchomienia serwera z API wpisujemy
```shell
python manage.py runserver opcjonalne_ip
```