from urllib.request import urlopen
import json
import os
import time
def downloadjson(comic_id):
    url = f"https://xkcd.com/{comic_id}/info.0.json"
    response = urlopen(url)
    data_json = json.loads(response.read()) 
    json_object = json.dumps(data_json)
    filepath = os.path.join(os.path.dirname(__file__), f"New folder1\comic_{comic_id}.json")
    with open(filepath, "w") as outfile:
        outfile.write(json_object)

def main():
    mypath = os.path.join(os.path.dirname(__file__), f"New folder1")
    if not os.path.isdir(mypath):
        os.makedirs(mypath)
    start = time.time()
    for comic_id in range (1,201):
        downloadjson(comic_id)
    time_taken = time.time() - start
    print('Time Taken {0}'.format(time_taken))
main()