# jardin_bonito
Proyecto programación web - Jardin Bonito

## Instalación

Comandos para iniciar el proyecto

1 -Instala Django
```
pipenv install django
```

2 -Instala oracle db
```
pipenv install cx_oracle
```

3 -Instala Crispy Forms
```
pipenv install django-crispy-forms
```

4 -Acceder a sqlplus y crear usuario
```
create user django identified by django;
grant connect, resource to django;
alter user django default tablespace users quota unlimited on users;
```
5 - Ejecutar migraciones.
```
python manage.py makemigrations
python manage.py migrate
```

6- Crear superusuario
```
python manage.py createsuperuser
```

7- Inicia consola entorno virtual
```
pipenv shell
```

8- Inicia proyecto
```
pipenv run start 
ó
python manage.py runserver
```

