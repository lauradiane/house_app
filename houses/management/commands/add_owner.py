from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from houses.models import Owner

class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--name',
            action='store',
            type='string',
            dest='name',
            help='Add an owner.'),
        )

    def handle(self, *args, **options):
        if options['name']:
            Owner.objects.create_owner(options['name'])
        else:
            raise CommandError('No name given for owner')
