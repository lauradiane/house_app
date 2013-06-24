from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from houses.models import Owner, House

class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--address',
            action='store',
            type='string',
            dest='address',
            help='Add a house address.'),
        )

    option_list = option_list + (
        make_option('--owner',
            action='store',
            type='string',
            dest='owner',
            help='Add an owner to a house address. Each owner can own up to 1 house.'),
        )

    def handle(self, *args, **options):
        if options['address'] and options['owner']:
            try:
                existing_owner = Owner.objects.get(name=options['owner'])
            except ObjectDoesNotExist:
                Owner.objects.create_owner(options['owner'])
                existing_owner = Owner.objects.get(name=options['owner'])
            
            new_house = House(address=options['address'], owner=existing_owner)
            new_house.save(force_insert=True)
            self.stdout.write('Added house: address=[%s] owner=[%s]' % ((options['address']), (options['owner'])))
        
        else:
            raise CommandError('No address and/or owner specified')



