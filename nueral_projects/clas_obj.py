class Person:
    
    amount = 0
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1
    
    def __del__(self):
        Person.amount -= 1
        
    def __str__(self):
        return("Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height))
    
    def get_older(years):
        self.age += years
    
    

person1 = Person("mike", 30, 5)
print(person1)

Person2 = Person("sarah", 20, 4)

print(person1.amount)


class Worker(Person):
    
    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary
        
    def __str__(self):
        text = super(Worker, self).__str__()
        text += ", Salary ()".format(self.salary)
        return text
        
    def calc_yearly_salary(self):
        return self.salary + 12

worker1 = Worker("Henry", 40, 174, 3000)
print(worker1)
print(worker1.calc_yearly_salary())