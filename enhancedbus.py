ADDRESS = 'SERC Buiding \n 1925 North 12th Street \n Philadelphia PA 19122'

def main():

    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    email = input('Enter your email: ')
    profile = 'first_name \n last_name \n email \n'

    def callme(profile):
        print (str(profile) + ADDRESS)
    
    
    callme(profile)
main()
