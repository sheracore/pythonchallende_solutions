# pythonchallende_solutions

[To see the riddles click on me](http://www.pythonchallenge.com/):


# Usage
## Please install requirements
```
pip install -r  requirements.txt
```
### All python challenges are in pythonchallenge direcrotry

## How recursive works
![Recursive steps](pics/1.jpg)

## Dynamic programming vs Recursive difference
![Recursive steps](pics/2.jpg)

## The best solution in Dynamming programming is bottom up solution

## When should I solve this problem with dynamic programming?”
### We should use dynamic programming for problems that are between *tractable *and *intractable *problems.

### Tractable problems are those that can be solved in polynomial time. That’s a fancy way of saying we can solve it in a fast manner. Binary search and sorting are all fast. Intractable problems are those that run in exponential time. They’re slow. Intractable problems are those that can only be solved by bruteforcing through every single combination (NP hard).

### When we see terms like:

### “shortest/longest, minimized/maximized, least/most, fewest/greatest, “biggest/smallest

### We know it’s an optimisation problem.
### Dynamic Programming algorithms proof of correctness is usually self-evident. Other algorithmic strategies are often much harder to prove correct. Thus, more error-prone.
### When we see these kinds of terms, the problem may ask for a specific number ( “find the minimum number of edit operations”) or it may ask for a result ( “find the longest common subsequence”). The latter type of problem is harder to recognize as a dynamic programming problem. If something sounds like optimisation, Dynamic Programming can solve it.

## Fibonacci with dynamic programming in tow solution
![Recursive steps](pics/3.jpg)

## Solve steps of number 5 problem in pychalenge directory
![Recursive steps](pics/4.jpg)

# Django

# Django_python_concepts

# Celery
## redis
```
redis is nosql database that store data in key value format also you can use it subscribe/publish (stack) tool by running subscribe(consumer) on a shell and publish(prducer) data in another shell and see result in subscribe shell

---> Shell number 1
redis-cli                                         [8/18]
127.0.0.1:6379> SUBSCRIBE first channel_name
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "first"
3) (integer) 1
1) "message"
2) "channel_name"
3) "hello"

---> shell number 2
redis-cli
127.0.0.1:6379> PUBLISH channel_name hello
(integer) 1
```

## Celery worker
### You can run a worker by this command
```
celery -A proj worker -l info
```
### Each cpu core has two thread so each worker on any cpu can (subscribe)consume two concurency task
### So if you run a worker on i7 cpu worker can get 16 published message or task concurency
### And if you want worker just consume on one(two, three, ..)thread you can use
```
celery -A proj worker -l info --concurrency=1
celery -A proj worker -l info --concurrency=2
```


## This is a celery task
```
@app.task(bind=True)
def debug_task(self, tid):
    logger.info('testing celery log')
    return tid
```
## Publish a task
```
debug_task.delay(i)
or
debug_task.si(1).apply_async()
```

## If you want to publish two or more tasks together concurncy use group
```
from celery import group
group(debug_task.si(1,2), debug_task.si(2,4)).delay()
```
## If you want to bind a task after running another task in other word should run first task so second task can run, use chain or pip
```
from celery import chain
chain(debug_task.si(1), debug_task.si(2)).apply_async()
chain(debug_task.si(1), debug_task.si(2)).delay()

(debug_task.si(1, 2) | debug_task.si(3)).apply_async()
(debug_task.si(1, 2) | debug_task.si(3)).delay()
```
### And if you want to use result of first task to second task use "s" 
```
@task()
def add(a, b):
    time.sleep(5) # simulate long time processing
    return a + b
    
# import chain from celery import chain
# the result of the first add job will be 
# the first argument of the second add job
ret = chain(add.s(1, 2), add.s(3)).apply_async()

# another way to express a chain using pipes
ret2 = (add.s(1, 2) | add.s(3)).apply_async()
```

## In our app samples
```
chain(debug_task.si(1),debug_task.si(2)).delay()
(debug_task.si(2,3) | debug_task.si(3,4)).delay()
a = (debug_task.s(2,3) | debug_task.s(4)).delay()
debug_task.s(2,3).delay()
a = (debug_task.s(2,3) | debug_task.s(4) | debug_task.s(5)).delay()
a.parent.parent.id
group(debug_task.si(1), debug_task.si(2)).delay()
a = group(debug_task.si(1,2), debug_task.si(2,4)).delay()
a = (group(debug_task.si(1,2), debug_task.si(2,4))|group(debug_task.si(1,2), debug_task.si(2,4))).delay()
a.parent.children[0].state
```

## Work with redis in python celery
```
app = Celery('viruspod')
""" 'viruspod' is name of queue """
i = app.control.inspect()
i.registerd() # All methos that are defined as task
i.active() # active tasks mention tasks that have cpu core and in progress
i.reserved() # that tasks os ready to run
```

## There is a problem, we cant see all tasks in redis queue by inspect so we should use python redis
```
import redis
r = redis.Redis()
r.lrange(queue, min, max) # for lists
r.llen queue # length of list
r.lrange(quere, 0, llen(queue))
```

## In worker command line and delay a task we can define queue instead of default queue
## Also if we don't want having reserved tasks we can use prefetch-multiplier switch in worker command line
```
celery -A proj worker --prefetch-multiplier=1 -l info -Q scan-sessions
tasks.append(debug_task.si(i).set(queue='scan-sessions'))
```
## Some golden points.
#### 1) If you run some group continuous that are run continuous and that are arranged but in group that tasks run together(parallel) based on the number of cup cores.

#### 2) To disable reserved tasks in queue you should first add --prefetch-multiplier=1 to worker command line and add following envs in settings:
```
celery -A proj worker --prefetch-multiplier=1 -l info -Q scan-sessions --concurrency=1
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_TASK_TRACK_STARTED = True
```

### To get task objects inside of outer object shoudl using children method
```
@shared_task
def task1():
    task2.delay()

a task1.delay()
a.children

or

sig = task1.si | task2.si
sig.apply_aysn()

sig.id is for task2 and sig.parent.id is for task1
```


## Create a djang project
```
python -m pip install django
django-admin startproject supersite (Every name you want)
cd supersite
.
├── manage.py
└── supersite
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

python mange.py runserver 8080
python mange.py runserver 0.0.0.0:8000

python manage.py startapp blabla


```

python manage.py startproject poll

├── db.sqlite3
├── manage.py
├── poll
│   ├── manage.py
│   └── poll
│       ├── asgi.py
│       ├── __init__.py
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
└── supersite
    ├── asgi.py
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-38.pyc
    │   ├── settings.cpython-38.pyc
    │   ├── urls.cpython-38.pyc
    │   └── wsgi.cpython-38.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py

4 directories, 17 files

## Django password
### How django stores passwords
#### algorithm: pbkdf2_sha256 iterations: 320000 salt: VGZsDV**************** hash: QoVp11**************************************
#### By default, Django uses the PBKDF2 algorithm with a SHA256 hash, a password stretching mechanism recommended by NIST. This should be sufficient for most users: it’s quite secure, requiring massive amounts of computing time to break.
```
<algorithm>$<iterations>$<salt>$<hash>
```
### dollar-sign character and consist of: the hashing algorithm, the number of algorithm iterations (work factor), the random salt, and the resulting password hash.

### PBKDF2
#### PBKDF2 is a simple cryptographic key derivation function, which is resistant to dictionary attacks and rainbow table attacks. 
#### It is based on iteratively deriving HMAC many times with some padding.
### PBKDF2 takes several input parameters and produces the derived key as output:
```
key = pbkdf2(password, salt, iterations-count, hash-function, derived-key-len)
```
* password – array of bytes / string, e.g. "p@$Sw0rD~3" (8-10 chars minimal length is recommended)
* salt – securely-generated random bytes, e.g. "df1f2d3f4d77ac66e9c5a6c3d8f921b6" (minimum 64 bits, 128 bits is recommended)
* iterations-count, e.g. 1024 iterations
* hash-function for calculating HMAC, e.g. SHA256
* derived-key-len for the output, e.g. 32 bytes (256 bits)

The output data is the derived key of requested length (e.g. 256 bits).

### What is a Salt?
#### A salt is a random character string that is added to the beginning or the end of a password. This salt is unique to each user, and is stored in the database along with the username and salted-hashed password.

## Django settings
#### By importing the following settings allways we have the django using settings
```
from django.conf import settings
```
## Static
#### Serving static files during development If you use django.contrib.staticfiles as explained above, runserver will do this automatically when DEBUG is set to True. If you don’t have django.contrib.staticfiles in INSTALLED_APPS, you can still manually serve static files using the django.views.static.serve() view. 
#### This is not suitable for production use! For some common deployment strategies, see How to deploy static files.
#### For example, if your STATIC_URL is defined as static/, you can do this by adding the following snippet to your urls.py:
```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```
### If you set DEBUGE to False and run /admin your js, css and other static files don't run just be careful that you shuld clean fils and images caches.
### Be careful that you should create a static dir in your app and in that static dir you should create a dir with that app name

### By default, collected files receive permissions from FILE_UPLOAD_PERMISSIONS and collected directories receive permissions from FILE_UPLOAD_DIRECTORY_PERMISSIONS. If you would like different permissions for these files and/or directories, you can subclass either of the static files storage classes and specify the file_permissions_mode and/or directory_permissions_mode parameters, respectively. For example:
```
from django.contrib.staticfiles import storage

class MyStaticFilesStorage(storage.StaticFilesStorage):
    def __init__(self, *args, **kwargs):
        kwargs['file_permissions_mode'] = 0o640
        kwargs['directory_permissions_mode'] = 0o760
        super().__init__(*args, **kwargs)
```
### Then set the STATICFILES_STORAGE setting to 'path.to.MyStaticFilesStorage'.
### Use the --nostatic option to disable serving of static files with the staticfiles app entirely. This option is only available if the staticfiles app is in your project’s INSTALLED_APPS setting.
```
django-admin runserver --nostatic
```
### Use the --insecure option to force serving of static files with the staticfiles app even if the DEBUG setting is False. By using this you acknowledge the fact that it’s grossly inefficient and probably insecure. This is only intended for local development, should never be used in production and is only available if the staticfiles app is in your project’s INSTALLED_APPS setting.

--insecure doesn’t work with ManifestStaticFilesStorage.
```
django-admin runserver --insecure
```

## Whitenoise
```
STATIC_ROOT = BASE_DIR / "staticfiles"
python manage.py collectstatic
Make sure you’re using the static template tag to refer to your static files, rather than writing the URL directly. For example:
{% load static %}
<img src="{% static "images/hi.jpg" %}" alt="Hi!" />
MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
--> "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]
pip install --upgrade whitenoise

```

### Serving files uploaded by a user during development
#### During development, you can serve user-uploaded media files from MEDIA_ROOT using the django.views.static.serve() view.
#### This is not suitable for production use! For some common deployment strategies, see How to deploy static files.
#### For example, if your MEDIA_URL is defined as media/, you can do this by adding the following snippet to your ROOT_URLCONF:
```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
### To test static_root or medias you cat use this command
```
python manage.py collectstatic
```
### This will copy all files from your static folders into the STATIC_ROOT directory.

