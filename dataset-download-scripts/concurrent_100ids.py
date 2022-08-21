from threading import Thread
from queue import Queue
import json
import requests
import sys
import time
from datetime import datetime

start_time = datetime.now()
print(f'Init time: {start_time}')

# Set your Bugzilla API key
api_key="<YOUR BUGZILLA-API-KEY>"
headers = { "X-BUGZILLA-API-KEY": api_key }

concurrent = 25

urls = []
bugs = []

# Maybe need to split the urls for avoid very high memory usage
# Because this, originally we had to split the urls into 7 files and run this for each of then
with open('data\\urls_with_100ids_final.json') as input_file:
    urls = json.load(input_file)

size = len(urls)
print(f'Size: {size}')
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
with open('data\\bugs_base_final.json', 'w') as outfile:
  json.dump(bugs, outfile)

end_time = datetime.now()

print(f'Size: {len(bugs)}')

print('Duration: {}'.format(end_time - start_time))