import re, sys

while True:
    print('Enter a password consisting of 8 characters \
    \nthat includes at least one uppercase word character, one lowercase word\
    \ncharacter and at least one digit. OR type "q" to quit. ')
    while True:
        passwrd = input('Enter Password: ')
        if passwrd == 'q':
            sys.exit()
        else:
            chkstrlen=re.compile(r'([0-9a-zA-Z]){8,}?')
            chklower = re.compile(r'([a-z]+)')
            chkupper = re.compile(r'([A-Z]+)')
            chkdigit = re.compile(r'[0-9]+')
            chkspecchars = re.compile(r'[\W]+')
            pswrdLen = len(passwrd)
            spechar = chkspecchars.search(passwrd)
            lenrgx = chkstrlen.search(passwrd)
            if(pswrdLen > 8):
                print('# please enter a password of 8 character only!')
                print()
                break
            elif(spechar):
                print('# password cannot contain non-word characters!($,%,&...')
                print()
                break
            elif (lenrgx == None):
                print('# Password must be 8 characters long!')
                print()
                break
            else:
                lower = chklower.search(passwrd)
                upper = chkupper.search(passwrd)  
                digit = chkdigit.search(passwrd)
                

                isformatError = False
                errlst = []
                nolowStr, noupStr, noditStr, specStr = ("", "", "", "")
                if lower == None: 
                    nolowStr = '# Password must have a lowercase word character!\n'
                    errlst.append(nolowStr)
                    isformatError = True
                
                if upper == None: 
                    noupStr = '# Password must have a uppercase word character!\n'
                    errlst.append(noupStr)
                    isformatError = True
                
                if digit == None: 
                    noditStr = '# Password must have a digit/number character!\n'
                    errlst.append(noditStr)
                    isformatError = True
                
                if spechar != None:
                    specStr = '# Password cannot contain special characters!\n'
                    errlst.append(specStr)
                    isformatError = True
                
                for i in errlst:
                    if i != "":
                        print(i)
                
                if isformatError == True:
                    break
                else:
                    print('You entered a strong password!\n')
                    sys.exit()
