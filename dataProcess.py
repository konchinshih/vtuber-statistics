import json

with open("fail.log", 'r', encoding='utf8') as file:
    fails = file.read().split('\n')

with open("result.json", 'r', encoding='utf8') as file:
    result = json.load(file)

fanList = []
viewList = []
videoList = []
isOfficeList = []

for i in result:
    if 'video' not in result[i]:
        continue
    fanList.append(result[i]['fan'])
    viewList.append(result[i]['view'])
    videoList.append(result[i]['video'])
    isOfficeList.append(
        0 if 'office' not in result[i] or result[i]['office'] == 'Vshojo' else 1
    )

print(len(fanList), len(viewList), len(videoList), len(isOfficeList))
    
with open("result.csv", 'w', encoding='utf8') as file:
    file.write("fan,view,video,isOffice\n")
    for i in range(len(fanList)):
        file.write(f"{fanList[i]},{viewList[i]},{videoList[i]},{isOfficeList[i]}\n")
