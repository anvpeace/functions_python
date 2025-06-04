def createUser(**usrinfo):
    return dict(usrinfo)

def printUser(usr):
    for key, value in usr.items():
        print(f"{key}: {value}")

user1= createUser( name="John",
            age = 43,
            job ="Programmer",
            hobby = "biking")
printUser(user1)

# 5. Dictionary
# a) Define a function createUser() with an arbitrary dictionary parameter.
#  This function returns a dictionary based upon input arguments.
# b) Define a function printUser() with a parameter user which is a dictionary.
#  This function prints the contents of the dictionary user.
# c) Create and print the user: John, age 43, job Programmer, Hobby Biking
# d) Create and print the user: Sara, age 20, school QCC, major CSIS