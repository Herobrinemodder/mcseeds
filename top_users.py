import json, os, subprocess
from urllib import request, parse

dataa = parse.urlencode({'get_top_users':'QfwojI0JXY0NnIsADMxojIw9GciwiIkVmb3BVZyF0cklGZVJiOiIXZpZWa05WZklmIsICM3QDO2EzN0YTM6ckI6Iydl52XklGZ1Jye=='}).encode()
req =  request.Request('https://mcseeds.mobi/seedscript_805.php', data=dataa)
resp = request.urlopen(req).read()

file = open("./top_users.json", 'wb')
file.write(resp)
file.close()

data = json.loads(resp.decode('utf-8'))

for i in range(0,len(data["users"])):
    print(data["users"][i]["nickname"] + " " + data["users"][i]["cnt"])
