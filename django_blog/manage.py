#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.settings')

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_project.settings')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_api_project.settings')

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.settings')5ac16c7 (Initial Setup and Project Configuration for a Django Blog)
 (Initial Setup and Project Configuration for a Django Blog)
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
