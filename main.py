def main():
    print "Welcome to the password generator!"
    length = getLength()
    contains = raw_input("Choice from the following what should the password contains \n1)Uppercase letters\n2)Lowercase letters\n3)Numbers\n4)Symbols\nInput can be 1234>> ")
    contains = list(contains)
    toInt(contains)
    contains.sort()
    print contains
    password = raw_input("Enter a word: ")
    print createPassword(length,contains,password)

def Generator(char):
    char = char.replace("A","4")
    char = char.replace("a","@")
    char = char.replace("e","3")
    char = char.replace("","")
    char = char.replace("","")
    char = char.replace("","")
    char = char.replace("","")
    return char

def createPassword(length,contains,password):
    l = []
    cnt = 0
    while(len(l) != length):
        l.append(Generator(password[cnt]))
        cnt+=1
    return listToStr(l)

def listToStr(lst):
    Str = ''
    for i in range(len(lst)):
        Str += lst[i]
    return Str

def toInt(lst):
    '''(lst)->(none)
    toInt convert a list of strings to integers
    '''
    for i in range(len(lst)):
        lst[i] = int(lst[i])

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
