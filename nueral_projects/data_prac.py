import sqlite3
class Person:
    
    
#     def __init__(self, id_number, first, last, age):
#         self.id_number = id_number
#         self.first = first
#         self.last = last
#         self.age = age
#         self.connection = sqlite3.connect('mydata.db')
#         self.cursor = connection.cursor()
    
#     def load_person(self, id_number):
#         cursor.execute("""
#         SELECT * FROM persons
#         WHERE id = {}
#         """).format(id_number)
        
#         results = cursor.fetchone()
        
#         self.id_number = id_number
#         self.first = results[1]
#         self.last = results[2]
#         self.age = results[3]
# connection = sqlite3.connect('mydata.db')
# cursor = connection.cursor()

# cursor.execute("""
# Create Table IF NOT EXISTS persons (
#     id INTEGER PRIMARY KEY,
#     first_name TEXT,
#     Last_name TEXT,
#     age INTEGER
    
# )               
# """)

# cursor.execute("""
# INSERT INTO persons VALUES
# (1, 'Paul', 'Smith', 24),
# (2, 'Mark', 'Johnson', 42),
# (3,'Anna', 'Smith', 34)
# """)

# cursor.execute("""
# SELECT * FROM persons
# WHERE last_name = 'Smith'
# """)

# rows = cursor.fetchall()
# print(rows)

# connection.commit()

# connection.close()


#-------- passing database as python object----------

#     def __init__(self, id_number=-1, first="", last="", age=-1):
#         self.id_number = id_number
#         self.first = first
#         self.last = last
#         self.age = age
#         self.connection = sqlite3.connect('mydata.db')
#         self.cursor = self.connection.cursor()
    
#     def load_person(self, id_number):
#         self.cursor.execute("""
#         SELECT * FROM persons
#         WHERE id = {}
#         """.format(id_number))
        
#         results = self.cursor.fetchone()
        
#         self.id_number = id_number
#         self.first = results[1]
#         self.last = results[2]
#         self.age = results[3]

# p1 = Person()
# p1.load_person(1)
# print(p1.first)
# print(p1.last)
# print(p1.age)
# print(p1.id_number)

#--------------------------------


    def __init__(self, id_number=-1, first="", last="", age=-1):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()
    
    def load_person(self, id_number):
        self.cursor.execute("""
        SELECT * FROM persons
        WHERE id = {}
        """.format(id_number))
        
        results = self.cursor.fetchone()
        
        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]
    
    def insert_persons(self):
        self.cursor.execute("""
        INSERT INTO persons VALUES
        ({}, '{}', '{}', {})
    """.format(self.id_number, self.first, self.last, self.age))
        self.connection.commit()

p1 = Person(7, "Alex", 'robbins', 30)
p1.insert_persons()

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM persons")
results = cursor.fetchall()
print(results)

connection.close()

