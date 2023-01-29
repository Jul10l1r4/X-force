from requests import get
from json import loads

api_url = "https://exchange.xforce.ibmcloud.com/api" 

def activity(activity_id, auth): 
    data = loads(eval(get(f'{api_url}/threat_activities/{activity_id}',
               headers={ 'Authorization': f'Basic {auth}' }).text))
    data['url'] = f'https://exchange.xforce.ibmcloud.com/threats/{activity_id}'
    return data

def malware(malware_id, auth): 
    data = loads(eval(get(f'{api_url}/malware_analysis/{malware_id}',
               headers={ 'Authorization': f'Basic {auth}' }).text))
    data['url'] = f'https://exchange.xforce.ibmcloud.com/malware_analysis/{malware_id}'
    return data

def group(groups_id, auth): 
    data = loads(eval(get(f'{api_url}/threat_groups/{groups_id}',
               headers={ 'Authorization': f'Basic {auth}' }).text))
    data['url'] = f'https://exchange.xforce.ibmcloud.com/threat-group/{groups_id}'
    return data

def collector(collector_id, auth): 
    data = loads(eval(get(f'{api_url}/casefiles/{collector_id}',
               headers={ 'Authorization': f'Basic {auth}' }).text))
    data['url'] = f'https://exchange.xforce.ibmcloud.com/collector/{collector_id}'
    return data

def industry(industries_id, auth): 
    data = loads(eval(get(f'{api_url}/industries/{industries_id}',
               headers={ 'Authorization': f'Basic {auth}' }).text))
    data['url'] = f'https://exchange.xforce.ibmcloud.com/industries/{industries_id}'
    return data
