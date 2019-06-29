from django.core.management import BaseCommand

from talenta365.addons import seek_letters


class Command(BaseCommand):
    help = 'Given any positive integer number, get your value in letters. How does Excel'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int)

    def handle(self, *args, **options):
        print(seek_letters(options['number']))
