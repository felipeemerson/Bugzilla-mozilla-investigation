import json
import requests
from datetime import datetime
import pandas as pd

# Set your Bugzilla API key
API_KEY="GGINB0vYDLcNRXxKdmzoOLOYxQUOeSnANtStJxos"
HEADERS = { "X-BUGZILLA-API-KEY": API_KEY }

DATE_FORMAT = "%Y-%m-%d"

INITIAL_DATE = datetime.strptime("2013-01-01", DATE_FORMAT)
LAST_DATE = datetime.strptime("2022-01-01", DATE_FORMAT)
DAYS_OFFSET = 15

currentDate = INITIAL_DATE

bugs = []

while True:
    currentDatePlusOffset = currentDate + pd.DateOffset(days=DAYS_OFFSET)

    if currentDatePlusOffset >= LAST_DATE:
            if currentDate >= LAST_DATE:
                break

            currentDatePlusOffset = currentDate + (LAST_DATE - currentDate)


    url = "https://bugzilla.mozilla.org/rest/bug?include_fields=id,last_change_time&bug_status=RESOLVED&chfield=[Bug%20creation]&chfieldfrom=" + str(currentDate.date()) + "&chfieldto=" + str(currentDatePlusOffset.date())
    
    response = requests.get(
        url,
        headers=HEADERS
    )

    data = response.json()
    tempBugs = data['bugs']
    bugs.extend(tempBugs)

    print(f"Período: {currentDate} - {currentDatePlusOffset}, quant. de bugs: {len(tempBugs)}")
    
    currentDate = currentDatePlusOffset + pd.DateOffset(days=1)

print(f"\nTotal de bugs: {len(bugs)}")

with open('bugs_id_with_lct-final.json', 'w') as outfile:
        json.dump(bugs, outfile)