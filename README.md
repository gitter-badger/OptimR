# OptimR

[![Join the chat at https://gitter.im/Pawamoy/OptimR](https://badges.gitter.im/Pawamoy/OptimR.svg)](https://gitter.im/Pawamoy/OptimR?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

- [Install Shiny Server](#install-shiny-server)
    - [On Debian](#shiny-on-debian)
- [Install Django](#install-django)
    - [On Debian](#django-on-debian)
- [Initialize the project](#initialize-the-project)

## Install Shiny Server
- [On Debian](#shiny-on-debian)

### Shiny on Debian
```bash
# install R and shiny package
sudo apt-get install r-base
sudo su - -c "R -e \"install.packages('shiny', repos='https://cran.rstudio.com/')\""

# make sure your R version is above 3.2.2
R --version

# install gdebi then shiny server
sudo apt-get install gdebi-core

# see https://www.rstudio.com/products/shiny/download-server/ for most recent version
wget https://download3.rstudio.org/ubuntu-12.04/x86_64/shiny-server-1.5.4.869-amd64.deb
sudo gdebi shiny-server-1.5.4.869-amd64.deb
```

## Install Django
- [On Debian](#django-on-debian)

## Django on Debian
```bash
sudo apt-get install python-pip python3-pip
sudo -H pip install virtualenv django
sudo -H pip3 install virtualenv django
```

## Initialize the project
Clone the repository with `git clone git@github.com:Pawamoy/OptimR optimr`, or
`git clone https://github.com/Pawamoy/OptimR optimr` if you did not configure
your SSH access to GitHub. Enter the repository: `cd optimr`.

First you need to create a virtualenv for the project with `virtualenv -p
python3.6 venv`, where you can specify another version of Python, and the path
of your choice for the virtualenv (here `venv`). Please use Python 3 instead
of default Python 2. If you don't have any Python 3 version installed on
your system, refer to the [Python 3 installation procedure](#install-python-3).

You can now activate your virtualenv with `. venv/bin/activate`. Install the
Python packages dependencies with `pip install -r requirements.txt`.

Go into the django project with `cd optimr`, and create the SQLite
database with `./manage.py migrate`. Also create a super user with `./manage.py
createsuperuser`. Now you can start the application anytime you want by
running `./manage.py runserver` and going at `localhost:8000` in your browser.

Run `./manage.py help` to get more help.