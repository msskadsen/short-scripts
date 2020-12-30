#password validation script

#function for evaluating each condition
def pass_eval(passwd):

    #initialize indicator for eval
    stat = True
    
    #initialize indicators and references for conditions
    symbols = ['!', '@', '#', '$', '%', '&', '*']
    symcount = 0
    numcount = 0
    capcount = 0
    lowcount = 0
    spacount = 0

    #evaluate specific occurances within password
    for i in passwd:
        if i in symbols:
            symcount += 1
        elif i.isdigit() == True
            numcount += 1
        elif i.islower() == True:
            capcount += 1
        elif i.isupper() == True:
            lowcount += 1
        elif i.isspace() == True:
            spacount += 1

    #analyze conditions that must be met for password to be valid
    if len(passwd) < 9 or spacount != 0 or symcount < 2 or numcount < 2 or capcount < 2 or lowcount < 2:
        stat = False

    return stat

#accept password to attempt
userpasswd = input("Enter A Password: ")

#evaluate the password
if pass_eval(userpasswd) == True:
    print ("Password Accepted")
else:
    print("Password Invalid")
