coderaising.org
===============

You can contribute to the CodeRaising.org site by forking this repo.  For a walkthrough of git commands used, see [here.](https://github.com/esoergel/meta/wiki/Git-Walkthrough)
Once you have a local copy, edit the local_settings.py file, and run the following commands::

	$ apt-get install libevent-dev

This is required to install some of the packages in the next step::

	$ pip install -r requirements/project.txt

This will install Mezzanine (including all dependencies such as Django), and South (for migrations) and psycopg2 (to interface with PostgreSQL). If you want to use MySQL instead, then add MySQL-python to the project.txt file.

Create a local_settings.py file and set the default database to SQLite3::

	DEBUG = True
	DATABASES = {
    	"default": {
        	"ENGINE": "django.db.backends.sqlite3",
        	"NAME": "coderaising.db",
        }
	}

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


Deployment
----------

Create an app on Heroku.

	$ heroku create coderaising

When you want to deploy to Heroku, you need to set some environment variables.

This will set the RACK_ENV value to production so that settings.py will use the Heroku settings::

	$ heroku config:add RACK_ENV=production

And you need to set up some AWS settings for static files and uploaded media to be served up by S3::

	$ heroku config:add AWS_ACCESS_KEY_ID=xxxxxxxxxxxxxxxx
	$ heroku config:add AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxxxxxxxxxxxxxx
    $ heroku config:add AWS_STORAGE_BUCKET_NAME=xxxxxxxxxxxxxx

Now try deploying the app::

	$ git push heroku master

If your static media doesn't show up, try running this::

	$ heroku labs:enable user-env-compile -a coderaising
	$ heroku run python manage.py collectstatic

If the deploy is taking too long, you can tell Heroku not to run the collectstatic command::

	$ mkdir .heroku
	$ touch .heroku/collectstatic_disabled

Read more about serving up static assets with Django on Heroku:
https://devcenter.heroku.com/articles/django-assets

Setting up email
----------------

In order to send emails when new users register on the site, we need to add Sendgrid::

	$ heroku addons:add sendgrid:starter

Then go to http://sendgrid.com/account/overview to see your Sendgrid username and password.

	$ heroku config:add SENDGRID_USERNAME=<username>
	$ heroku config:add SENDGRID_PASSWORD=<password>

Read more about Sendgrid configuration with Django here: http://sendgrid.com/docs/Integrate/Frameworks/django.html
Also check out django-sendgrid-events: http://django-sendgrid-events.readthedocs.org/en/latest/

Reference
---------

	* django-storages: http://django-storages.readthedocs.org/
	* django-debug-toolbar: https://github.com/django-debug-toolbar/django-debug-toolbar
	* South: http://south.readthedocs.org/
	* mezzanine-events: https://github.com/stbarnabas/mezzanine-events
	* mezzanine-pagedown: https://bitbucket.org/akhayyat/mezzanine-pagedown
	* django-herokuapp: https://github.com/etianen/django-herokuapp
	* Heroku Hackers Guide: http://www.theherokuhackersguide.com/
