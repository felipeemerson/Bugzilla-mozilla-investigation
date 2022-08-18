from threading import Thread
from queue import Queue
import json
import requests
import sys
import time
from datetime import datetime

start_time = datetime.now()
print(f'Início: {start_time}')

# Set your Bugzilla API key
api_key="GGINB0vYDLcNRXxKdmzoOLOYxQUOeSnANtStJxos"
headers = { "X-BUGZILLA-API-KEY": api_key }

#20
concurrent = 25

urls = []
bugs = []

with open('urls_with_100ids_final_partial_7.json') as input_file:
    urls = json.load(input_file)

size = len(urls)
print(f'Tamanho {size}')
leftover = size % 100
sizeDivisiblePer100 = size - leftover

def doWork():
    while True:
        url, index = q.get()

        response = requests.get(
            url,
            headers=headers
        )

        data = response.json()

        bugs_temp = data['bugs']

        print(f'index: {index}, datasize: {len(bugs_temp)}')

        bugs.extend(bugs_temp)

        time.sleep(30)
        q.task_done()

q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()

try:

    for i in range(0, size):
        q.put([urls[i], i])
    q.join()

except KeyboardInterrupt:
    sys.exit(1)

# Outfile with bugs retrieveds
with open('bugs_base_final_7.json', 'w') as outfile:
    json.dump(bugs, outfile)

end_time = datetime.now()

print(f'Tamanho: {len(bugs)}')

print('Duração: {}'.format(end_time - start_time))