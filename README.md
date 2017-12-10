# shodAND frontend and API

It provides the shodAND frontend and the REST API interface.

### Installation

Assuming that you've a working venv, install the requirements with:
```
$ pip install -r requirements.txt
```

### Usage

Start the development server calling:
```
$ python shodAND/manage.py runserver
```

Start Celery worker with:
```
$ cd shodAND
$ celery -A shodAND worker -l info
```

### Credits

- [Common ports JSON file](https://github.com/ShodAND/web/tree/master/shodAND/base/utils/ports.json) fetched from [here](https://raw.githubusercontent.com/mephux/ports.json/master/ports.lists.json)
