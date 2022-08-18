import json

# Modify to include fields that you want
base_url = "https://bugzilla.mozilla.org/rest/bug?include_fields=id,resolution,creator,history,summary,comments&id="

with open('bugs_id_lct_final.json') as json_file:
    data = json.load(json_file)

urls = []
size = len(data)

# For each 100 bugs, creates a single url to retrieve them.
for i in range (0, size, 100):
    url_with_ids = base_url
    ids_conc = ""

    for j in range(0, 100):
        if i + j >= size:
            break
        ids_conc += str(data[i+j]['id']) + ","


    
    urls.append((url_with_ids + ids_conc)[:-1]) # Add url to urls, and eliminate a ',' at the final of the url



# An outfile that includes 100 urls that each one retrieves 100 bugs
with open('urls_with_100ids_final.json', 'w') as outfile:
    json.dump(urls, outfile)