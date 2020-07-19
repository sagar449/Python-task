#print("Hello")

#

uname1 = "aman64039"
pas1 = 'a147852'

uname2 = "sagar1111"
pas2 = 's2222'

uname3 = 'bhushan1010'
pas3 = 'b3333'

uname4 = "vaibhav1212"
pas4 = 'v4444'

uname5 = "vishal333"
pas5 = 'v5555'

username = raw_input("Enter username")
if username == uname1:
    password = raw_input("Enter password")
    if password == pas1:
        print("welcome", uname1)
    else:
        print ("invalid password", uname1)

elif username == uname2:
    password = raw_input("Enter password")
    if password == pas2:
        print ("welcome", uname2)
    else:
        print("invalid password", uname2)

elif username == uname3:
    password = raw_input("Enter password")
    if password == pas3:
        print ("welcome", uname3)
    else:
        print ("invalid password", uname3)

elif username == uname4:
    password = raw_input("Enter password")
    if password == pas4:
        print("welcome", uname4)
    else:
        print ("invalid password", uname4)

elif username == uname5:
    password = raw_input("Enter password")
    if password == pas5:
        print ("welcome", uname5)
    else:
        print ("invalid password", uname5)
else:
    print("Invalid username")
