import random

def main():

    print("Welcome to the Password Generator by unclear#9150\n")

    print("You can generate any kind of password you would like to...\n")

    print("Choose one of type below , you can choose both or triple too\n")

    print("a) a to z \nb) A to Z \nc) 0 to 9 \nd) special characters only\ne) anything\nf) a & b\ng) a & c\n"
    "h) a & d \ni) b & c \nj) b & d\nk) c & d\nl) a, b & c\nm) b, c & d\nn) a,c, &d "
    "\no)a,b &d\np)a,b,c &d\n")

    passwordType = input("Enter any type given above(recommended == e)\n")

    passwordLength = input("Enter the password length\n")

    printPassword(passwordLength,passwordType)

    isAgain = input("Do you want to generate password again(y/n)\n")

    if isAgain is 'y':

        main()

    elif isAgain is 'n':

        print("Thanks for using my password generator\n")

    else:

        print("Invalid Input")


def generateRandomNumbers(passwordType):

    if passwordType is 'a':

        randomNumber = random.randint(97,122)

    elif passwordType is 'b':

        randomNumber = random.randint(65, 90)

    elif passwordType is 'c':

        randomNumber = random.randint(48, 57)

    elif passwordType is 'd':

        while 1:

            rand = random.randint(0,256)

            if (rand<=47 and rand>=33) or (rand<=64 and rand>=58) or (rand<=96 and rand>=91) or(rand<=175 and rand>=123) or(rand<=254 and rand>=178):

                randomNumber = rand

                break

    elif passwordType is 'e':

        randomNumber = random.randint(33,126)

    elif passwordType is 'f':

        while 1:

            rand = random.randint(0,256)

            if (rand<=90 and rand>=65) or (rand<=122 and rand>=97):

                randomNumber = rand

                break

    elif passwordType is 'g':

        while 1:

            rand = random.randint(0,256)

            if (rand<=57 and rand>=48) or (rand<=122 and rand>=97):

                randomNumber = rand

                break

    elif passwordType is 'h':

        while 1:

            rand = random.randint(0,256)

            if (rand<=122 and rand>=97) or (rand<=47 and rand>=33) or (rand<=64 and rand>=58) or (rand<=96 and rand>=91) or(rand<=175 and rand>=123) or(rand<=254 and rand>=178):

                randomNumber = rand

                break

    elif passwordType is 'i':

        while 1:

            rand = random.randint(0,256)

            if (rand<=90 and rand>=65) or (rand<=57 and rand>=48):

                randomNumber = rand

                break

    elif passwordType is 'j':

        while 1:

            rand = random.randint(0,256)

            if (rand<=90 and rand>=65) or (rand<=47 and rand>=33) or (rand<=64 and rand>=58) or (rand<=96 and rand>=91) or(rand<=175 and rand>=123) or(rand<=254 and rand>=178):

                randomNumber = rand

                break

    elif passwordType is 'k':

        while 1:

            rand = random.randint(0,256)

            if (rand<=57 and rand>=48) or (rand<=47 and rand>=33) or (rand<=64 and rand>=58) or (rand<=96 and rand>=91) or(rand<=175 and rand>=123) or(rand<=254 and rand>=178):

                randomNumber = rand

                break

    elif passwordType is 'l':

        while 1:

            rand = random.randint(0,256)

            if (rand<=122 and rand>=97) or (rand<=90 and rand>=65) or (rand<=57 and rand>=48):

                randomNumber = rand

                break

    elif passwordType is 'm':

        while 1:

            rand = random.randint(0,256)

            if (rand<=90 and rand>=65) or (rand<=57 and rand>=48) or (rand<=47 and rand>=33) or (rand<=64 and rand>=58) or (rand<=96 and rand>=91) or(rand<=175 and rand>=123) or(rand<=254 and rand>=178):

                randomNumber = rand

                break

    elif passwordType is 'n':

        while 1:

            rand = random.randint(0,256)

            if (rand<=122 and rand>=97) or (rand<=57 and rand>=48) or (rand<=47 and rand>=33) or (rand<=64 and rand>=58) or (rand<=96 and rand>=91) or(rand<=175 and rand>=123) or(rand<=254 and rand>=178):

                randomNumber = rand

                break

    elif passwordType is 'o':

        while 1:

            rand = random.randint(0,256)

            if (rand<=122 and rand>=97) or (rand<=90 and rand>=65) or (rand<=47 and rand>=33) or (rand<=64 and rand>=58) or (rand<=96 and rand>=91) or(rand<=175 and rand>=123) or(rand<=254 and rand>=178):

                randomNumber = rand

                break

    elif passwordType is 'p':

        while 1:

            rand = random.randint(0,256)

            if (rand<=122 and rand>=97) or (rand<=90 and rand>=65) or (rand<=57 and rand>=48) or (rand<=47 and rand>=33) or (rand<=64 and rand>=58) or (rand<=96 and rand>=91) or(rand<=175 and rand>=123) or(rand<=254 and rand>=178):

                randomNumber = rand

                break

    else:

        print("Invalid Input so we are exiting you from program and starting again\n")

        main()

    return randomNumber

def printPassword(passwordLength,passwordType):

    password = {}

    for i in range(0,int(passwordLength)):

        randomNum = chr(generateRandomNumbers(passwordType))

        password[i] = str(randomNum)

    for k in range(0,int(passwordLength)+19):

        print("=",end='')

    print("\n")

    print("your password is:  ",end='')

    for a in password:

        print(password[a],end='')

    print("\n")

    for j in range(0,int(passwordLength)+19):

        print("=",end='')

    print("\n")

main()
