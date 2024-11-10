<h3 align="center"> BulletinBoard </h3>

<h4 align="center"> django website with links, data entry (forms) and statistics file (.css)</h4>

<h4 align="center">build setup</h4>
<p align="center">ubuntu-latest</p>
<br>

```
# clone the repo into your disk

$ git clone https://github.com/hellcard/bulletin-board.git

# installing dependencies

$ cd bulletin-board
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv)$ pip install django~=4.1

# server startup

(.venv)$ python manage.py runserver
```
<br>
<h4 align="center">The following routes are available:</h4>

<p align="center">"admin/" - admin pannel</p>
<p align="center">"bboard/" - main page</p>
<p align="center">"bboard/num/" - categories (num: 1-3)</int:num>
<p align="center">"bboard/add/" - add page</p>
<br>
<h2 align="center">admin pannel</h2>
<p align="center">login: admin</p>
<p align="center">password: 123</p>
