from browser_history.browsers import Firefox, Chrome, Edge
import datetime, json, pytz, time

TIMEZONE = pytz.timezone("Europe/Berlin")

Candidate = input("Enter Candidate ID: \n")
input ("Press \"Enter\" to Start.")

START_TIME = TIMEZONE.localize(datetime.datetime.now())

print("Confirmed. Start!")
time.sleep(10)

browserIndex = -1
while not (browserIndex>0 and browserIndex<4):
    browserIndex = input("Which Browser was used? \n 1: Chrome \n 2: Edge \n 3: Firefox \n")
    try:
        browserIndex = int(browserIndex)
    except:
        print("Input is not a number")
        browserIndex = -1

input("Close Browser and press \"Enter\" to end.")

BROWSERS = [Chrome(), Edge(), Firefox()]
BROWSER = BROWSERS[browserIndex-1]
fullHistory = BROWSER.fetch_history().histories


historyIndex = -1
while True:
    timeDiff = START_TIME - fullHistory[historyIndex][0]
    historyIndex = historyIndex - 1
    if timeDiff.total_seconds() >= 0:
        break
    
historyIndex = historyIndex + 2
historyFiltered = fullHistory[historyIndex:]

duration = str(TIMEZONE.localize(datetime.datetime.now()) - START_TIME)
entries = abs(historyIndex)

statistics = {"Duration" : duration,"Entries" : entries}
historyJSON = []

for i in range(0, entries):
    historyDict = {"Date" : str(historyFiltered[i][0].date()), "Time" : str(historyFiltered[i][0].time()), "URL" : historyFiltered[i][1], "Title" : historyFiltered[i][2]}
    historyJSON.append(historyDict)

with open ("data.json") as file:
    data = json.load(file)

data["Statistics"]["Total"]["Candidates"] = data["Statistics"]["Total"]["Candidates"] + 1
data["Statistics"]["Total"]["Entries"] = data["Statistics"]["Total"]["Entries"] + entries
data["Statistics"][Candidate] = statistics
data["Histories"][Candidate] = historyJSON

with open ("data.json", 'w') as file:
    json.dump(data, file, indent=2)

print("Save complete, rerun to add next candidate.")