#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_project.settings')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_api_project.settings')
=======
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_project.settings')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_api_project.settings')

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.settings')5ac16c7 (Initial Setup and Project Configuration for a Django Blog)
>>>>>>> 30bd782 (Initial Setup and Project Configuration for a Django Blog)
>>>>>>> 7340bfd1ae8e7164fa8a15993b36dcbfefb2e4b8
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
