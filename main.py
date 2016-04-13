def main():
    print "Welcome to the password generator!"
    length = getLength()
    contains = raw_input("Please Enter what should the password contains :")
    password = raw_input("Enter a word: ")
    print createPassword(password)
def createPassword(password):
    password = password.replace("A","4")
    password = password.replace("a","@")
    password = password.replace("e","3")
    password = password.replace("","")
    password = password.replace("","")
    password = password.replace("","")
    password = password.replace("","")
    return password

def getLength():
    try:
        length = input("Please Enter the length of the password you want to enter: ")
    except NameError:
        print "*This input accepts only numbers"
        getLength()
    finally:
        return length

if __name__=='__main__':
    main()
