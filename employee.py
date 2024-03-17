from db import c

"""
PK - Primary Key
"""

class Employee(object):
    def __init__(self, name, surname, age, pk=None):
        self.id = pk
        self.name = name
        self.surname = surname
        self.age = age

    @classmethod
    def get(cls, pk):
        result = c.execute("SELECT * FROM employee WHERE id = ?", (pk,))
        values = result.fetchone()
        if values is None:
            return None
        employee = Employee(values["name"], values["surname"], values["age"], values["id"])
        return employee
    
    
    @classmethod
    def get_list(cls, id=None, name=None, surname=None, age=None):
        condition, values, result_list = [], [], []
        sort_dict = {'id': id, 'name': name, 'surname': surname, 'age': age}
        for key in sort_dict.copy().keys():
            if sort_dict[key] is not None:
                condition.append(f"{key} = ?")
                values.append(sort_dict[key])
        if len(condition) == 0:
            result = c.execute("SELECT * from employee")
        else:
            where = " AND ".join(condition)
            result = c.execute("SELECT * FROM employee WHERE " + where, values)
        for row in result.fetchall():
            result_list.append(dict(row))
        return result_list


    @classmethod
    def delete(cls, id=None, name=None, surname=None, age=None):
        condition, values, result_list = [], [], []
        sort_dict = {'id': id, 'name': name, 'surname': surname, 'age': age}
        for key in sort_dict.copy().keys():
            if sort_dict[key] is not None:
                condition.append(f"{key} = ?")
                values.append(sort_dict[key])
        if len(condition) == 0:
            raise ValueError('At least one parameter must be provided')
        else:
            where = " AND ".join(condition)
            result = c.execute("DELETE FROM employee WHERE " + where, values)


    def __lt__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.age < other.age
    
    def __le__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.age <= other.age

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.age == other.age

    def __ne__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.age != other.age

    def __gt__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.age > other.age

    def __ge__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.age >= other.age
    

    def __repr__(self):
        return "<Employee {}>".format(self.name)

    def update(self):
        c.execute("UPDATE employee SET name = ?, surname = ?, age = ? WHERE id = ?",
                  (self.name, self.surname, self.age, self.id))

    def create(self):
        c.execute("INSERT INTO employee (name, surname, age) VALUES (?, ?, ?)", (self.name, self.surname, self.age))
        self.id = c.lastrowid

    def save(self):
        if self.id is not None:
            self.update()
        else:
            self.create()
        return self



