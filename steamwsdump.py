import json
# install the API wrapper by executing the following command:
#   pip install -U steam[client]
from steam.webapi import WebAPI

# enter your API key found at https://steamcommunity.com/dev/apikey
api = WebAPI(key="API_KEY_HERE")

# separates mod load order and prints number of mods
_MLO = "@FILEID0001;@FILEID0002;@FILEID0003;@FILEID0004;"
_MLO = _MLO.replace("@", "").split(";")[:-1]
_MLO = [int(x) for x in _MLO]
print(len(_MLO))

# uncomment to view all data fields
#print(json.dumps(api.ISteamRemoteStorage.GetPublishedFileDetails(itemcount=1, publishedfileids=[_MLO[0]]), sort_keys=False, indent=4))

# requests and prints the mod load order in CSV format [id,title]
for i in range(0,len(_MLO)):
    print(str(_MLO[i]) + "," + api.ISteamRemoteStorage.GetPublishedFileDetails(itemcount=1, publishedfileids=[_MLO[i]])["response"]["publishedfiledetails"][0]["title"])
