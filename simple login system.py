def read_logins():
    with open("logins.txt", "r") as f:
        contents = f.readlines()

        new_contents = []

        for line in contents:
            fields = line.split(",")
            fields[1] = fields[1].rstrip()
            new_contents.append(fields)

        return new_contents

logins = read_logins()

def login():
    login1 = input("Enter your login: ")
    password = input("Enter your password: ")

    logged_in = False

    for line in logins:
        if line[0] == login1 and logged_in == False:
            if line[1] == password:
                logged_in = True

    if logged_in == True:
        print("Logged in successfully!")
    else:
        print("Incorrect login or password")

def main():
    print("Heyyy")

login()



