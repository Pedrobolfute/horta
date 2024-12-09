# loginMeDjango
Project using Django to Create a login screen

## To-Do
To not forget...

### Screens
- [x] Screen Login;
- [x] Screen Create Account;
- [x] Screen Change my Account;
- [x] Screen Welcome;
- [x] Screen Admin See EveryOne;

### Function or Methods
>> Screen login, create account, change myAccount:
- [ ] PassEncrypted to server;
- [ ] Little eye to see my password when I click;

>> Screen login and Change my Account:
- [x] Method that confirm if my passwors is right;
- [x] Method that allows me edit my info (password);
- [x] Placeholder brings my name from DB;

>> Screen create account;
- [ ] Password validade if weak, normal or strong;
- [ ] Little bar indicating with color it above;

>> Screen Welcome;
- [ ] Brings welcome "user" with ASCII form;
- [ ] import pyfiglet to do it above;

>> Screen Admin See EveryOne
- [ ] Colums: id, name, password encripted, password normal;

>> Screen change my account
- [x] method that confirm if my user is right
- [x] method that confirm if my password is right 

### Convencions
>> TO-DO:
X = Made;
XX = Made and implemented;

>> Const:
- UPPER_SNAKE_CASE;

>> var:
- low_snake_case;

>> Function and methods:
- camalCase;

>> class:
- PascalCase;

### Important sites
>> Icons:
- [Google Fonts Icon](https://fonts.google.com/icons)

>> Fonts:
- [Google Fonts](https://fonts.google.com/)

>> Paleta de cores:
- [paletton](https://paletton.com/#uid=33q160kJ+jCvZsNCBnOQDeQWv8W)

## classes e seus métodos

The user contains his life, likes his animal, vehicle, job, document

class user
    - id
    - name
    - password

class animal
    - specie
    - color

    - def makeNoise

class vehicle
    - mark
    - model
    - year
    - color

class job
    - company
    - position
    - salary

class document
    - type
    - number


# REMEMBERING

git add do bd
> python manage.py makemigrations

git commit do bd
> python manege.py migrate

add user to server
> python manage.py createsuperuser