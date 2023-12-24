import xml.dom.minidom

domtree = xml.dom.minidom.parse('/Users/prepared-statements/nueral_projects/data.xml')
group = domtree.documentElement

persons = group.getElementsByTagName('person')

# for person in persons:
#     print("-----PERSON----")
#     if person.hasAttribute('id'):
#         print("ID: {}".format(person.getAttribute('id')))
    
#     print("Name: {}".format(person.getElementsByTagName('name')[0].childNodes[0].data))
#     print("Age: {}".format(person.getElementsByTagName('age')[0].childNodes[0].data))
#     print("Weight: {}".format(person.getElementsByTagName('weight')[0].childNodes[0].data))
#     print("Height: {}".format(person.getElementsByTagName('height')[0].childNodes[0].data))

# persons[2].getElementsByTagName('name')[0].childNodes[0].nodeValue = "New Name"
# persons[1].setAttribute('id', '100')
# persons[3].getElementsByTagName('age')[0].childNodes[0].nodeValue = "-10"
# domtree.writexml(open('/Users/prepared-statements/nueral_projects/data.xml', 'w'))

#--------------new-------------

for person in persons:
    print("-----PERSON----")
    if person.hasAttribute('id'):
        print("ID: {}".format(person.getAttribute('id')))
    
    print("Name: {}".format(person.getElementsByTagName('name')[0].childNodes[0].data))
    print("Age: {}".format(person.getElementsByTagName('age')[0].childNodes[0].data))
    print("Weight: {}".format(person.getElementsByTagName('weight')[0].childNodes[0].data))
    print("Height: {}".format(person.getElementsByTagName('height')[0].childNodes[0].data))

newperson = domtree.createElement('person')
newperson.setAttribute('id', '6')

name = domtree.createElement('name')
name.appendChild(domtree.createTextNode('Paul Green'))

age = domtree.createElement('age')
age.appendChild(domtree.createTextNode('19'))

weight = domtree.createElement('weight')
weight.appendChild(domtree.createTextNode('150'))

height = domtree.createElement('height')
height.appendChild(domtree.createTextNode('120'))

newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

group.appendChild(newperson)

domtree.writexml(open('data.xml', 'w'))

