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

## Dodatkowe info
Jeżeli chcecie korzystać z panelu admina, będzie dostępny pod adresem
```shell
http://127.0.0.1:8000/admin
```
Zakładając że macie odpaloną apkę na localhoscie.

ALE, trzeba najpierw utworzyć użytkownika administratora. W środowisku wirtualnym wpisujemy:
```shell
python manage.py createsuperuser
```
I przechodzimy przez proces, powinien zapytać o login, email - może być pusty, hasło i powtórkę hasła. 
Jeśli dacie za proste będzie krzyczeć że niezgodne z regułami, ale można to skipnąć wciskając "y".
