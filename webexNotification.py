import subprocess
import sys
def install(request):
  subprocess.check_call([sys.executable, "-m", "pip", "install", request])
install("requests")
install("requests_toolbelt")
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
m = MultipartEncoder({'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vMmU4YjJiZjgtZWU1Mi0zZTgyLWJjOGMtMTY5MTQyNmYzYjMx','text': 'hi from tekton task'})
r = requests.post('https://webexapis.com/v1/messages', data=m,headers={'Authorization': 'Bearer YjQxNDlmZmYtNDc3MS00M2ZhLWE2MGItNzg0OTI1ZWFiODY2MzkwYmViMmQtNTk5_PF84_af742d39-7515-46a3-82a7-03269e091b91','Content-Type': m.content_type})
print(r.text)
print("done")
