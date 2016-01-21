from urllib import urlopen
from datetime import datetime
import json
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    args = 'User count'
    help = 'Create fake users from randomuser.me'
    api_url = 'https://randomuser.me/api/'
    
    def handle(self, *args, **options):
        if len(args) < 1:
            raise CommandError('Please enter content folder')
        try:
            user_count = int(args[0])
        except ValueError:
            raise CommandError('Use integer value for user count')
        
        for i in range(0, user_count):
            try:
                response = urlopen(self.api_url)
            except IOError:
                print CommandError('Error with url %s' % self.api_url)
                continue
            
            data = response.read()
            
            try:
                data = json.loads(data)
            except ValueError:
                print CommandError('Error with json from url %s' % self.api_url)
                continue
            udata = data['results'][0]['user']
            user = User(username=udata['username'],
                    first_name=udata['name']['first'],
                    last_name=udata['name']['last'],
                    email=udata['email'],
                    date_joined=str(datetime.fromtimestamp(udata['registered'])) + '+00:00')
            user.set_password(udata['password'])
            user.save()
            print "created user %s" % user