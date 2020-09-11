# Django Boilerplate

## Features
 * [Django Debug Toolbar](https://pypi.org/project/django-debug-toolbar/) configured from the start
 * [Jupyter Notebooks](https://jupyter.org/) for debbuging, using the [django_extensions module](https://pypi.org/project/django-extensions/)
 * Batch files for every common task during development and for running the notebook. Currently:
    - Running the server
    - Making and running migrations
    - Shell
    - Jupyter Notebook
 - Base Django requirements included as well as this project's dependencies
 - Initial migrations already run
 - Greeting view, like create-react-app

 ```bash
mkdir repo_root && cd repo_root
pipenv install django
  django-admin.py startproject --template=https://github.com/FedericoVarela/Django-Boilerplate/archive/master.zip --extension py,.env,ini,yml 
  --name Pipfile <project_name>
#Then delete the Pipfile created by the first pipenv install 
```

Have I missed some functionality? Would you like to have something else included? Send me a pull request and I'll check it out
