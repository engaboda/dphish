# dphish
get info for list of ip addresses.

### requirements
Vagrant 2.3.4
virtualbox 6.1

### run

* vagrant up
* vagrant ssh
* sudo bash provisioners.sh
* python3 manage.py runserver 0.0.0.0:8000

`in another terminal`

* celery --app=dphish.celery:app -worker -l INFO