import json

print('''
By entering your email address and password we will use it just to 
send emails through your gmail account. Neither us and and anyone 
can see your email id and password
''')

emailAddress = input("Enter Email address: ")
password = input("Enter yoyr email password: ")

emailCredentials = {
    "email" : emailAddress,
    "password" : password
}

with open('email.json', 'w') as j:
    if json.dump(emailCredentials, j):
        print("Entered email credentials success fully")
    else:
        print("Couldnt enter your credentials")