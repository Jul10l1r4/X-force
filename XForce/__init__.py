#!/usr/bin/python3 
from requests import get
import XForce.details
from json import loads

api_url = "https://exchange.xforce.ibmcloud.com/api" 

# Sources of search
def threat_activities(term, auth):
    return get(f"{api_url}/threat_activities/search/{term}",
               headers={ 'Authorization': f'Basic {auth}' }).text

def malware_analysis(term, auth):
    return get(f"{api_url}/malware_analysis/search/{term}",
               headers={ 'Authorization': f'Basic {auth}' }).text

def threat_groups(term, auth):
    return get(f"{api_url}/threat_groups/search/{term}",
               headers={ 'Authorization': f'Basic {auth}' }).text

def collector(term, auth):
    return get(f"{api_url}/casefiles/public/fulltext?q={term}",
               headers={ 'Authorization': f'Basic {auth}' }).text

def industries(term, auth):
    return get(f"{api_url}/industries/search/{term}",
               headers={ 'Authorization': f'Basic {auth}' }).text

def all(term, auth):
    big_list = []
    big_list = loads(threat_activities(term, auth))["rows"] + loads(malware_analysis(term, auth))["rows"] + loads(threat_groups(term, auth))["rows"] + loads(collector(term, auth))["casefiles"] + loads(industries(term, auth))["rows"]
    return big_list

