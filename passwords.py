import re

def check():
    password = input("Create a password: ")
    return (str(password))
result = check()
print(result)

def spec_char():
    if result != ("-"" "):
        

def check2():
    password = input("Confirm your password: ")
    return password
result2 = check2()
print(result2)


def check_uppercase(string):
    for result in string:
       if result.isupper():
            return True
    return False

def check_lowercase(string):
    for result in string:
       if result.islower():
           return True
    return False

#def check_numeric():
     #return "abc123def"
     #if re.search(r'/d', results):       

def main():

    if check_uppercase(result) or check_lowercase(result): #and #check_numeric(result):
        print("true")
    else:
       print("This does not contain a letter from the alphabet")
     

main()









#def check_uppercase():
    #if str(result).isupper():
     #   return True
 #   else: 
   #     return False
#uppercase = check_uppercase("UP")
#print(uppercase) 

#uppercase = check_uppercase("low")
#print(uppercase) 

#def password

#def one_alpha_char():
    #result.isupper()

    







#def password_is_valid():
    #if len(result) == len(result2):
        #return True
    
    #i = result
    #j = result2

    #while i == j:
        #if [i] == [j]:
            #return True
#result3 = password_is_valid(result, result2)
#print(result3)




    