from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from houses.models import Owner, House

class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--owner',
            action='store',
            type='string',
            dest='owner',
            help='Display house owned by this owner.'),
        )

    def handle(self, *args, **options):
        if options['owner']:
            try:
                existing_owner = Owner.objects.get(name=options['owner'])
                owner_house = House.objects.get(owner=existing_owner)
                self.stdout.write('address=[%s], owner=[%s]' % (owner_house.address, owner_house.owner.name))
            except ObjectDoesNotExist:
                print "No houses to display"
        else:
            for h in House.objects.all():
                self.stdout.write('address=[%s], owner=[%s]' % (h.address, h.owner.name))
