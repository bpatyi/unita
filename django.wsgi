import os
import sys
import site


#site.addsitedir('/home/unitaspace/unitaspace/lib/python2.5/site-packages')

activate_this = '/home/unitaspace/unitaspace/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))


os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

sys.path.append('/home/unitaspace/unitaspace/unita')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

