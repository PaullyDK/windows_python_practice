import json
employee = {'name': "Paul", 
            'age': 30,
            "salary": 200000,
            "ismarried": False,
            "isdating": False
            }
json_string = json.dumps(employee, indent=4, sort_keys=True)
print(json_string)

with open('emp.json','w') as f:
    json.dump(employee,f,indent=4)