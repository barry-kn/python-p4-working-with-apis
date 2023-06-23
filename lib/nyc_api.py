import requests
import json

class GetPro:
    def get_spec(self):
        url = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        spec_e= []
        response = requests.get(url)
        ractis = json.loads(response.text)
        ya_m = ractis

        for spec in ya_m :
            spec_e.append(spec["agency"])

        return  json.dumps(spec_e,indent=5)
   
result = GetPro().get_spec()
print(result)