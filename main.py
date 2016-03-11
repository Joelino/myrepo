# -*- coding: utf-8 -*-

import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text
import csv # pro exportovani do CSV
from keboola import docker
import datetime
from datetime import date, timedelta # date input

# initialize KBC configuration 
cfg = docker.Config('/data/')
# validate application parameters
parameters = cfg.getParameters()


# date format checker
    try: 
    	parameters.get('Date_preset')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")
    else:
    	print "well, it WASN'T defined after all!"
