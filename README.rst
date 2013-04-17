===========
djapps
===========

.. image:: https://secure.travis-ci.org/RichardOfWard/djapps.png
    :alt: Build Status
    :target: http://travis-ci.org/RichardOfWard/djapps


*djapps* allows you to load your django apps by their app names rather
than by the module path. This is particularly useful if you don't know where
modules will be installed or if you plan to allow overriding of your apps (eg
a user replaces your ``foo.bar`` app with ``myfoo.bar``).


Usage
=====

If you have a django app called ``bar`` in a package called ``foo`` (such that
you would add ``foo.bar`` to your INSTALLED_APPS) then you can get hold of
``bar`` without knowing its full module path::

    import djapps.bar

*djapps* hooks into python's regular import mechanism so all the normal
ways to import things will work::

    from djapps.bar import models
    from djapps.bar.models import MyModel as ThisIsMyModel

Your app names in a django project should all be unqiue, djapps won't
work if they are not (but django won't like that either).


Installation
============

Use your favorite install method, for example:

    $ pip install djapps

You do not need to add djapps to your INSTALLED_APPS, just start using it.
