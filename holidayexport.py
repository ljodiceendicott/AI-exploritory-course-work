import json

f= open('holidays.json')

data = json.load(f)

num = 0
for i in data['holidays']:
    print(i['name'] + " "+i['date']+num+1)

f.close()
