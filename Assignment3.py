#Excercise5
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

#lowercase1 is seeing if the first letter is lowercase, if it is, it returns True and does not check any other letter
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

#lowercase2 is the same as the first function; however it adds unnecessary strings to booleans and to the c

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

#lowercase3 only sees if the last letter is lowercase or not

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

#lowercase4 is checking every letter; however it is true if there is even one lowercase letter

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

#lowercase5 is checking every letter and correctly returns if all the letters are lowercase


#Excerise6

def rotate_word(string,integer):
    result = ''
    for i in string:
        i = chr(ord(i) + integer)
        result = result + i
    return (result)

print (rotate_word("cheer",7))