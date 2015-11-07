#!/usr/bin/python

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/finapps_api/")

from finapps_api import app as application
application.secret_key = 'artb134b523v