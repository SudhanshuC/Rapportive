#!/usr/bin/python
#Based upon the service Rapportive: http://www.rapportive.com/
#Credits: This code is based upon the research and code of Jordan Wright.
#Blog Link: http://jordan-wright.github.io/blog/2013/10/14/automated-social-engineering-recon-using-rapportive/
#Code Link: https://github.com/jordan-wright/rapportive
#This code requires the Requests library: https://pypi.python.org/pypi/requests/
# Rapportive Code: https://github.com/SudhanshuC/Rapportive/blob/master/rapportive.py
import requests
target_email = raw_input("Enter Target Email: ")
random_email="randomemail@gmail.com"
response = requests.get('https://rapportive.com/login_status?user_email=' + random_email).json()
profile = requests.get('https://profiles.rapportive.com/contacts/email/' + target_email, headers = {'X-Session-Token' : response['session_token']}).json()
print " "
print "Results for Email: "+target_email
print " "

if profile['contact']['name']:
  print "Name: "
  print profile['contact']['name']
  print " "

if profile['contact']['location']:
  print "Location: "
  print profile['contact']['location']
  print " "

if profile['contact']['headline']:
  print "Profile Headline: "
  print profile['contact']['headline']
  print " "

if profile['contact']['occupations']:
  print "Occupation(s): "
  for occupation in profile['contact']['occupations']:
    print occupation['job_title']
    print occupation['company']
    print " "

if profile['contact']['memberships']:
  print "Membership(s): "
  for membership in profile['contact']['memberships']:
    print membership['site_name']
    print membership['profile_url']
    print " "
