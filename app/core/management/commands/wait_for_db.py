"""
    Django command to make sure that the DB service is available
    - the folder structure makes it accessible by a manage.py command.
"""

from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database not available, waiting 1sec...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('database available'))
