coderaising.org
===============

You can contribute to the CodeRaising.org site by forking this repo, editing the local_settings.py file, and running the following commands::

	$ pip install -r requirements/project.txt

This will install Mezzanine (including all dependencies such as Django), and South (for migrations) and psycopg2 (to interface with PostgreSQL). If you want to use MySQL instead, then add MySQL-python to the project.txt file.

Create the database, sync and migrate all with this one convenience management command. This will also create some sample data, such as contact form, gallery and demo content::

	$ python manage.py createdb

If you don't want it to create sample data, use the ```no-data``` option::

	$ python manage.py createdb --nodata

This will also work::

	$ python manage.py syncdb --migrate

Collect all the static assets to a top level ```static``` dir::

	$ python manage.py collectstatic

Start up the Django server::

	$ python manage.py runserver


