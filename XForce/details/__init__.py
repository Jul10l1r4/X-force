from requests import get

api_url = 'https://api.xforce.ibmcloud.com/api'

def get_activities(activity_id, auth): 
    data = eval(get(f'{api_url}/threat_activities/{activity_id}',
               headers={ 'Authorization': f'Basic {auth}' }).text)
    data['url'] = f'https://exchange.xforce.ibmcloud.com/threats/{activity_id}'
    return data

def get_malware(malware_id, auth): 
    data = eval(get(f'{api_url}/malware_analysis/{malware_id}',
               headers={ 'Authorization': f'Basic {auth}' }).text)
    data['url'] = f'https://exchange.xforce.ibmcloud.com/malware_analysis/{malware_id}'
    return data

def get_groups(groups_id, auth): 
    data = eval(get(f'{api_url}/threat_groups/{groups_id}',
               headers={ 'Authorization': f'Basic {auth}' }).text)
    data['url'] = f'https://exchange.xforce.ibmcloud.com/threat-group/{groups_id}'
    return data

def get_industries(industries_id, auth): 
    data = eval(get(f'{api_url}/industries/{industries_id}',
               headers={ 'Authorization': f'Basic {auth}' }).text)
    data['url'] = f'https://exchange.xforce.ibmcloud.com/industries/{industries_id}'
    return data
