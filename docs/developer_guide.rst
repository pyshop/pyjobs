Developer guide
===============
This guide describes project's structure, instructs how to deploy your own woking environment.

Deploying working environment
-----------------------------
This project initially developed under and for Ubuntu operating system, so most likely it should run on any other
linux-based distributions, but it is possible that some steps of this instruction will be incorrect for
another operating systems.

First of all ensure that in your system installed required packages:

    git, python-dev, python3.4-dev

After that choose some directory as a project directory (i.e. ~/projects) *mkdir* it if necessary than *cd* to it.
Clone repository:

    git clone git@github.com:alekseyr/pyjobs.git

Than build the environment:

    ./build_env.sh

Activate virtual environment:

    source env/bin/activate

You can use existing sqlite database, that set in settings.py with sample data for debugging purposes.
Now you can run development server:

    python src/manage.py runserver_plus localhost:8010

Your app will be available in http://localhost:8010 and django's admin interface in http://localhost:8010/admin
Use user/user123 to login to django's admin interface.

Congratulations! You have your own development environment.
