def main():
    print "Welcome to the password generator!"
    password = raw_input("Enter a word: ")
    print createPassword(password)
def createPassword(password):
    password = password.replace("A","4")
    password = password.replace("a","@")
    password = password.replace("e","3")
    return password

if __name__=='__main__':
    main()
