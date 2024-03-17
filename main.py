from employee import Employee
from db import conn

# first_example = Employee.get_list(name = 'mamuka')
# print(first_example)
#output : [{'id': 1, 'name': 'mamuka', 'surname': 'archvadze', 'age': 25}]

# second_example = Employee.get_list(name = 'lika', age = 28)
# print(second_example)
#output : [{'id': 3, 'name': 'lika', 'surname': 'nozadze', 'age': 28}]

#  third_example = Employee.delete(id = 4)
# this  will delete the record with id=4 in employees

# fourth_example = Employee('john', 'cena', 49)
# fourth_example_v2 = Employee('under', 'taker', 62)
# print(fourth_example > fourth_example_v2)
# output : False

conn.commit()
conn.close()