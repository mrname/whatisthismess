from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Tests!'

    def handle(self, *args, **options):
        print('What iz tests?')
