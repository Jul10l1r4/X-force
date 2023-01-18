#!/usr/bin/python3 
from requests import get

# Sources of search
def threat_activities(term, auth):
    return get(f"https://exchange.xforce.ibmcloud.com/api/threat_activities/search/{term}",
               headers={ 'Authorization': f'{auth}' }).text

def malware_analysis(term, auth):
    return get(f"https://exchange.xforce.ibmcloud.com/api/malware_analysis/search/{term}",
               headers={ 'Authorization': f'{auth}' }).text

def threat_groups(term, auth):
    return get(f"https://exchange.xforce.ibmcloud.com/api/threat_groups/search/{term}",
               headers={ 'Authorization': f'{auth}' }).text

def casesfiles(term, auth):
    return get(f"https://exchange.xforce.ibmcloud.com/api/casefiles/public/fulltext?q={term}",
               headers={ 'Authorization': f'{auth}' }).text

def industries(term, auth):
    return get(f"https://exchange.xforce.ibmcloud.com/api/industries/search/{term}",
               headers={ 'Authorization': f'{auth}' }).text
