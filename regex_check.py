import re

regex = r"^(?!\.)(?!.*\.\.)[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"r"@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

def check(email):

    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")

# Driver Code
if __name__ == '__main__':

    # Enter the email
    email = "ankitrai326@gmail.com"

    # calling run function
    check(email)

    email = "my.ownsite@our-earth.org"
    check(email)

    email = "ankitrai326.com"
    check(email)

    email = "userrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr0000000000000000000@gmai.com"
    check(email)