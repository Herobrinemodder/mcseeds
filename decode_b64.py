
b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

#encode_this = '{"appstore":"apple","identifier":"ba3862215b3bdd84f9d366166e521a0a18d0fbdf","pro":"yes","usertag":"Herobrinemod","udid_new":"G:1647168470","pushtoken":"4170594223795a482d8970196f037cad3f10886f1ff521b40c71cc23828109b0","nickname":"Herobrine 1.8.8","gcNickname":"Herobrine 1.8.8","type":"gamecenter"}'
#encode_this = '{"nickname":"Goofin-off","identifier":"0000000000000000000000000000000000000000","comment":"Test","reply_udid":"","seed_udid":"G:558251501","udid_new":"G:168994617","isWarning":"no","seed":"haker ","category":"Seeds","seedid":"115962","reply_name":"","uploadDate":"2013-01-19"}'
encode_thisf = '{"udid_new":"G:","identifier":"","seedid":"1356565"}'
encode_this = '{"searchString":"Hotline","identifier":"","start":0,"fetchUdid":"","pop":20,"udid_new":"G:"}' # get_users
#dataa='=eyJpZGVudGlmaWVyIjoiNWRmZTY5NzcxNGViMDllMTBkYWIyYmJkNmMxMjE3ZTQ0NTgzN2VkMSIsInNlZWRpZCI6IjE5MjcxNzAiLCJsYXRlc3RDbW50SUQiOjAsInBvcCI6MzAsInVkaWRfbmV3IjoiRzoxNjQ3MTY4NDcwIiwiY29tbWVudHNTb3J0IjoiTmV3ZXN0IiwiY2F0ZWdvcnkiOiJPZmYgdG9waWMiLCJzdGFydCI6MCwiYWdlT2ZDb21tZW50cyI6Im9sZGVyIn0'
databa='0nI3VmbiojI0J3bzJCLiMHZlV2cgIXZzVlI6ISby9mZ0FGbwJCLiIiOiUGc5RFZsJ3b3JCLwojI0JXY0NnIsISZtlGd55WYiojIz52bpRHcPRncvNVYyRHelJCLiwGbBJiOi42bpNnclZnIsICM3QDO2EzN0YTM6ckI6Iydl52XklGZ1JCLiIiOicmbpJHdTh2YyFWZzJCLiMHZlV2cyV2c1JiOi42bpR3YlNnIsIyckVWZzBiclNXViojI5J3bnVGdhNmIsIiN5ITNxADNwITM6ckI6ICZpRWVoNGdlZmIsATN6ICcvBnIsIyY1IjYyAjMmVGO3MGOhdzN4gDM1ITYzUmZ3QWZ3QjMwQWNyQ2NzUWOiojIyVWamlGduVGZpJye='

dataa='QfiAzN0gjNxcDN2EjOHJiOicXZu9FZpRWdiwCMyojIw9GciwiIiojIklGZVh2Y0VmZiwCM6ICdyFGdzJCLiMWNyImMwIjZlhzNjhTY3cDO4ATNyE2MlZ2NkV2N0IDMkVjMkdzMlljI6IicllmZpRnblRWaiwiIl5WasR3bIJiOicmbpJHdTh2YyFWZzJye=='

array = ['','==','=']

#data_new = data.replace('=','')
a = ''
g = ''

def decodeSeed(data):
    data = data[::-1]
    data = data.replace('=','')
    c = ''
    for i in range(0,len(data)):
        if data[i] in b:
            a = b.find(data[i])
            c = c + "{0:06b}".format(int(a))
    if c[len(c)-1] == '0':
        c=c[:-2:]
    return c

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
        
seed = decodeSeed(dataa)
dees = encodeSeed(encode_this)
decoded = ''.join(chr(int(seed[i*8:i*8+8],2)) for i in range(len(seed)//8))
print(decoded)

print(dees)
