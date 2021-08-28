
#print(spam.strip())


##  SE ELIMINAN LOS ESPACIOS
##spam="                Hello,World                 "
##def deleteSpace(Cadena):
##    print(Cadena.strip())
##deleteSpace(spam)


#Expresiones regulares
##txt='415-555-4242'
##def isPhoneNumber(txt):
##    if len(txt) != 12:
##        return False
##
##    for i in range(0,3):
##        if not txt[i].isdecimal():
##            return False
##
##    if txt[3] != "-":
##        return False
##
##    for i in range(4,7):
##        if not txt[i].isdecimal():
##            return False
##    if txt[7] !="-":
##        return False
##
##    for i in range(8,12):
##        if not txt[i].isdecimal():
##            return False
##    return True
##
##
##print(isPhoneNumber(txt))
##
##
##
##message="call me at 412-232-4422 tomorrow . 415-555-9999"
##for i in range(len(message)):
##    chunk=message[i:i+12]
##    if isPhoneNumber(chunk):
##        print ("Phone number found:" + chunk)
##print("Done")


##
##import re
##
##phoneNumRegex = re.compile(r'(\d{3}-\d{3}-\d{4}?)')
##mo = phoneNumRegex.search('My number is 415-555-4242.  ')
##print('Phone number found: ' + mo.group())




#USANDO EXPRESIONES REGULARES
##import re
##
##heroRegex = re.compile(r"Batman|Tina Fey")
##
##mo1=heroRegex.search("Batman and Tina Fey")
##
##print(mo1.group())
##
##mo2 = heroRegex.search('Tina Fey and Batman')
##
##print(mo2.group())
##


##import re
##batRegex=re.compile(r"Bat(man|mobile|copter|bat)")
##
##mo = batRegex.search("Batmobile lost a wheel")
##
##
##print(mo.group())
##print(mo.group(1))
##
##
##import re
##
##batRegex=re.compile(r"Bat(wo)?man")
##mo1=batRegex.search("The Adventures of Batman")
##mo2=batRegex.search("The Adventures of Batwoman")
##print(mo1.group())
##print(mo2.group())


##import re
##phoneRegex = re.compile (r"(\d{3}-)?\d{3}-\d{4}")
##
##mo1=phoneRegex.search("My number is 415-123-2235")
##mo2=phoneRegex.search("My number is 123-2235")
##print(mo1.group())
##print(mo2.group())
##
##

