from browser_history.browsers import Firefox, Chrome, Edge
import datetime, json, pytz

TIMEZONE = pytz.timezone("Europe/Berlin")
START_TIME = datetime.datetime.now()
START_TIME = TIMEZONE.localize(START_TIME)

browserIndex = -1
while not (browserIndex>0 and browserIndex<4):
    browserIndex = input("Which Browser will be used? \n 1: Chrome \n 2: Edge \n 3: Firefox \n")
    try:
        browserIndex = int(browserIndex)
    except:
        print("Input is not a number")
        browserIndex = -1

input("Waiting for Confirmation")

BROWSERS = [Chrome(), Edge(), Firefox()]
BROWSER = BROWSERS[browserIndex-1]
fullHistory = BROWSER.fetch_history().histories

print(fullHistory)

# timeDiff = datetime.timedelta(-1)
# historyIndex = -1
# while timeDiff.total_seconds()<0:
#     historyIndex += 1
#     timeDiff = fullHistory[historyIndex][0] - START_TIME
    

# historyFiltered = fullHistory[historyIndex:]
# print(historyFiltered)