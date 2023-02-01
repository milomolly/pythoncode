import json

f = open('py_challange_input.json')

data = json.load(f)
outcomeList = [1000]
pointData = {}
regionData = {}
percentAustralia = {}
totalMatch = 0
internationalMatch = 0
iMatches = 0
teamScoredMost = ""
scoreMax = 0
resultWithheld = 0
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
                if l['isInternational'] == True:
                    internationalMatch += 1
                outcomeData['livestream_provider'] = l['streaming']['liveStream']['provider']
                outcomeData['winner'] = l['results']['winner']
                if l['results']['winner'] in pointData:
                    pointData[l['results']['winner']] += int(l['results']['points'])
                else:
                    pointData[l['results']['winner']] = int(l['results']['points'])
                if l['results']['resultsWithheld'] == True:
                    resultWithheld += 1
            outcomeData["regionName"] = k['name']
            if k['name'] in regionData:
                regionData[k['name']] += 1
                totalMatch += 1
            else:
                regionData[k['name']] = 1
                totalMatch += 1
            outcomeList.append(outcomeData)
for x,y in pointData.items():
    if y >= scoreMax:
        scoreMax = y
        teamScoredMost = x
print("Outcome list:")
print(outcomeList);
print("Number of international matches took place:")
print(internationalMatch)
print("Team has scored the most points overall:")
print(teamScoredMost)
totalMatch -= regionData['NewZealand']
percentAustralia['north'] = regionData['north'] / totalMatch * 100
percentAustralia['south'] = regionData['south'] / totalMatch * 100
percentAustralia['central'] = regionData['central'] / totalMatch * 100
print("percentage of matches played in north:")
print(percentAustralia['north'])
print("percentage of matches played in south:")
print(percentAustralia['south'])
print("percentage of matches played central:")
print(percentAustralia['central'])
print("Number of withheld:")
print(resultWithheld)
f.close()
