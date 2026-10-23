import jsonpickle
class Employee:
    def __init__(self,eno, ename):
        self.eno = eno
        self.ename = ename

    def display(self):
        print("ENO:{}, ENAME:{}".format(self.eno,self.ename))

e = Employee(100, "Paul")
json_string = jsonpickle.encode(e)
print(json_string)

with open("emp.json", 'w') as f:
    f.write(json_string)

newEmp=jsonpickle.decode(json_string)
newEmp.display()

with open('emp.json', 'r') as f:
    json_string=f.readline()
newEmp = jsonpickle.decode(json_string)
newEmp.display()
