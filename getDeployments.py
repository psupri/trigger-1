import requests,json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
url = "https://api.elastic-cloud.com/api/v1/deployments"
apikey="YWVJeDQzc0JqR3d1aWxkMTZuWFM6cWFlWGFwTk5UaWFERUkweUZPRTVNZw=="
headers = {'Authorization': 'ApiKey ' + apikey}
response = requests.get(url, headers=headers)
print(json.loads(response.text))