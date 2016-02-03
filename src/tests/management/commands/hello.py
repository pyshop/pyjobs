from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'prints hello!'

    def handle(self, *args, **options):
        self.stdout.write("hello!")
