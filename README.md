# [IBM X-Force Exchange library]
|![](https://exchange.xforce.ibmcloud.com/favicon.ico)|IBM Security X-FORCE Exchange library in Python 3. Search: threat_activities, threat_groups, malware_analysis, collector and industries. For others applications. See ![X-Force Exchange](//exchange.xforce.ibmcloud.com)|
|---|---|

# Install
```pip
pip3 install XForce
```

# Use
Using you API_KEY make a basic authentication. See ![documentation](https://api.xforce.ibmcloud.com/doc/). After make a base64 code → Key + : + Password:
```sh
printf "d2f5f0f9-2995-42c6-b1dd-4c92252da129:06c41d5e-0604-4c7c-a599-300c367d2090" | base64
# ZDJmNWYwZjktMjk5NS00MmM2LWIxZGQtNGM5MjI1MmRhMTI5OjA2YzQxZDVlLTA2MDQtNGM3Yy1hNTk5LTMwMGMzNjdkMjA5MAo=
``` 
Using API_KEY, call functions. See ![best praticles](https://medium.com/geekculture/python-separate-code-and-sensitive-information-elegantly-ae21cec5fae2) for key storage

## Call functions
```python3
import XForce

# Args: 1 - Term of search, 2 - API KEY

# Threat activity search return in string
XForce.threat_activities(Term, API_KEY)

# Malware analysis search return in string
XForce.malware_analysis(Term, API_KEY)

# Threat groups search return in string
XForce.threat_groups(Term, API_KEY)

# Industries search return in string
XForce.industries(Term, API_KEY)

# All categories search return in list with dict
XForce.industries(Term, API_KEY)
```

For see more details of consult, run:
```python3
from XForce import details

# Args: 1 - GUID, 2 - API KEY 
# IMPORTANT: all GUID are correspondent to category
# All function of details have:
# url → with x-force exchange panel
details.activity(Id, API_KEY)
details.group(Id, API_KEY)
details.malware(Id, API_KEY)
details.industry(Id, API_KEY)
```


