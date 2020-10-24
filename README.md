# Django Boilerplate

## Features
 * [Django Debug Toolbar](https://pypi.org/project/django-debug-toolbar/) configured from the start
 * [Jupyter Notebooks](https://jupyter.org/) for debbuging, using the [django_extensions module](https://pypi.org/project/django-extensions/)
 - Base Django requirements included as well as this project's dependencies
 - Settings files split into development, production and common configuration
 - Docker configuration
 - Greeting view, like create-react-app

 ```bash

 # You'll probably need a global Django installation for the django-admin

mkdir repo_root && cd repo_root
django-admin.py startproject --template=https://github.com/FedericoVarela/Django-Boilerplate/archive/master.zip --extension py,.env,yml,ini
  --name Pipfile <project_name>
```

Have I missed some functionality? Would you like to have something else included? Send me a pull request and I'll check it out
