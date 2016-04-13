def main():
    print "Welcome to the password generator!"
    length = getLength()
    contains = raw_input("Choice from the following what should the password contains \n1)Uppercase letters\n2)Lowercase letters\n3)Numbers\n4)Symbols\nInput can be 1234>> ")
    print list(contains)
    password = raw_input("Enter a word: ")
    print createPassword(length,contains,password)

def createPassword(length,contains,password):
    password = password.replace("A","4")
    password = password.replace("a","@")
    password = password.replace("e","3")
    password = password.replace("","")
    password = password.replace("","")
    password = password.replace("","")
    password = password.replace("","")
    return password

def getLength():
    length = 0
    try:
        length = input("Please Enter the length of the password you want to enter: ")
    except NameError:
        print "*This input accepts only numbers"
        getLength()
    finally:
        return length

if __name__=='__main__':
    main()
