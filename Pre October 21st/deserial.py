import json
with open('emp.json', 'r') as f:
    emp_dict = json.load(f)

print(type(emp_dict))
print("Employee Name:", emp_dict['name'])