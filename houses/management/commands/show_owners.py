from django.core.management.base import NoArgsCommand
from houses.models import Owner

class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        for owner in Owner.objects.all():
            self.stdout.write('owner=[%s]' % owner.name)
