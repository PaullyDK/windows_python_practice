import json
paul_info = {'age':30, "sex": "male", "location": "austin"}

paul_json = json.dumps(paul_info)
with open('emp.json', 'w') as f:
    json.dump(paul_json,f)

with open('emp.json', 'r') as f:
    loadedjson = json.load(f)
paul_new_dict = json.loads(loadedjson)

print(paul_new_dict)