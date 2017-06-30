from urllib.request import urlopen
# from oauth2client.contrib import gce
import json
import sys
from pprint import pprint
import peewee as pw
# from bs4 import BeautifulSoup
import urllib.request
import sys
import codecs
import requests
import re
import time
import csv
import unidecode 
import peewee as pw
from time import sleep
import random
import string


myDB = pw.MySQLDatabase("kyan", host="mysql.pokegosecrets.com", user="kyan", passwd="kyankyan")

class MySQLModel(pw.Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = myDB

class entries(MySQLModel):

    entrytitle = pw.CharField()
    entrycreation  = pw.CharField()
    entrycreatorid  = pw.CharField()
    entrytext  = pw.CharField()
    entrycategory  = pw.CharField()
    

#simple peewee query
get_existing_entries = entries.select().where(entries.id).limit(5000)

for x in get_existing_entries:
	print (x.entrytitle)



































