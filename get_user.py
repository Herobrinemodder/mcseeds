import json, os, subprocess
from urllib import request, parse

b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
array = ['','==','=']

def encodeSeed(data):
    d = ''
    encoded = ''
    for p in range(0,len(data)):
        d = d + "{0:08b}".format(ord(data[p]))
    d=d+'0000'
    
    for k in range(len(d)//6):
        ha = int(d[k*6:k*6+6],2)
        encoded = encoded + b[ha]
    encoded = array[len(encoded)%3-1]+encoded
    encoded = encoded[::-1]
    return encoded
def searchUser(user):
    referenceString = '{"searchString":"Hotline","identifier":"","start":0,"fetchUdid":"","pop":20,"udid_new":"G:"}'
    usrSearch = user
    consData1 = '{"searchString":"' + usrSearch + '","identifier":"ba3862215b3bdd84f9d366166e521a0a18d0fbdf","start":0,"fetchUdid":"","pop":20,"udid_new":"G:1281940767"}'
    print(consData1)
    headers = {
    'User-Agent': 'Minecraft%20Seeds%20Pro/2018.06.191148 CFNetwork/711.4.6 Darwin/14.0.0',
    
}
    dataa = parse.urlencode({'get_users':encodeSeed(consData1)}).encode()
    req =  request.Request('https://mcseeds.mobi/seedscript_805.php', data=dataa, headers = headers)
    resp = request.urlopen(req)
    
    comJson = json.load(resp)
    for x in range(0,len(comJson["users"])):
        print(comJson["users"][x]["udid"]+" "+comJson["users"][x]["nickname"]+" "+comJson["users"][x]["bios"])

def downloadUserSeeds(id):
    
    udid = id
    getSeeds = '{"identifier":"","pop":5000,"fetchUdid":"'+udid+'","category":"Uploads","section":"myseeds","searchString":"","udid_new":"'+udid+'","version":"All","extraSortOptions":"anytime","start":0,"worldType":"","platform":"My seeds","sort":"new"}'
    print(getSeeds)
    dataa = parse.urlencode({'getSeeds':encodeSeed(getSeeds)}).encode()
    req =  request.Request('https://mcseeds.mobi/seedscript_805.php', data=dataa)
    resp = request.urlopen(req)
    comJson = json.load(resp)
    for x in range(0,len(comJson["seeds"])):
        print(comJson["seeds"][x]["seed"])

user = input("Input the username->")
searchUser(user)
seeds = input("Input user udid for seed download->")
if seeds == 'q':
    exit()
downloadUserSeeds(seeds)
