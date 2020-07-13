# music_django
# My music
My music is a cloud music player which allows you to add and listen songs from anywhere in the world.

### Features
It allows you to:
 - Add new albums 

  ![album](https://i.ibb.co/HpD3j0p/Annotation-2020-07-14-003607.png)
  
  - view all your songs list
  
  ![songs](https://i.ibb.co/dPLvbTd/Annotation-2020-07-14-003801.png)
  
  - view all you favorite list
  
  ![](https://i.ibb.co/Z2mTR80/Annotation-2020-07-14-004608.png)
  
  - create album
  
  ![](https://i.ibb.co/1T6Td2T/Annotation-2020-07-14-004324.png)

 - Add songs to Albums

   ![](https://i.ibb.co/PD6PfYy/Annotation-2020-07-14-004445.png)

 - Search for songs and Albums

   ![](https://i.ibb.co/Z2mTR80/Annotation-2020-07-14-004608.png)
   
   
   - api
   
   ![](https://i.ibb.co/gRkRkjs/Annotation-2020-07-14-005053.png)
   
      To view All songs and Albums
      - for album api
      hit the url - http://127.0.0.1:8000/music/api/albums/
      - for songs api
      hit the url - http://127.0.0.1:8000/music/api/songs/
      
    ```
    default admin login
    userid - ss
    password- 12345678
    ```
    ```
    default user with some songs and albums added
    user - admin
    password - 12345678
    ```
 -   you can create your own album and songs by  just registering
 
      


### Installing  

1. For mac

Either install from packages by typing these commands in your terminal
```
sudo apt-get update
sudo apt-get install python-django
```
You can confirm whether its installed or not by typing 
```
django-admin --version
```

Other way is installing by using pip 
```
sudo apt-get update
```
Install pip if you dont have by 
```
sudo apt-get install python-pip
```
Then install django by 
```
sudo pip install django

```
2. for windows

```
- pip install django

```

```
- pip install djangorestframework

```
3. or simply run by moving into the required directory
```
- pip install -r requirements.txt
```


### Running the code 
Just go into the code directory and type 
```
python manage.py runserver
```
"My music" app will start on 127.0.0.1:8000 (Local Address).
 
### Applying Migrations on the Project 
Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They’re designed to be mostly automatic, but you’ll need to know when to make migrations, when to run them, and the common problems you might run into.
Now suppose you want to change my album'm model or song's model and have your's you can simply change the code as you require and then run these commands
```
python manage.py makemigrations
python manage.py migrate 
python manage.py migrate --run-syncdb
python manage.py runserver
```
You can use *showmigration*  to list projects migration.

   