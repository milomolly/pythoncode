import json

f = open('py_challange_input.json')

data = json.load(f)
outcomelist = [1000]
cnt = 0
iMatches = 0
for i in data['Cricket']:
    for j in i['formats']:
        for k in j['regions']:
            for l in k['matches']:
                outcomeData = {
                    "match_id" : l['id'],
                    "team1" : l['team1'],
                    "team2" : l['team2'],
                    "httpLink" : l['httpLink']
                }
                outcomeData['livestream_provider'] = l['streaming']['liveStream']['provider']
                outcomeData['winner'] = l['results']['winner']
            outcomeData["regionName"] = k['name']
            outcomelist[++cnt] = outcomeData
            print(outcomeData);
f.close()
