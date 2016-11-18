#!/usr/bin/python

# Open a file

import os.path
line2 = ""
check = 0
print "\n\n-------------------------------------------------------------"
print "\t\t\tMBOX EMAIL GRABBER"
print "-------------------------------------------------------------"
mboxFile = raw_input('Type the name of the file with .mbox: ')
# mboxFile = mboxInput+".mbox"
print "-------------------------------------------------------------"
emailInput = raw_input('Enter the sender\'s email: ')
email = "<"+emailInput+">"

print "-------------------------------------------------------------"
if os.path.isfile(mboxFile):
    if os.path.isfile("emails.csv"):
        print "\t\t\tAttention!"
        print "\nCSV file already exists!"
        sobre = raw_input('Want to override it? YES (y) OR NO (n): ')
        if (sobre.rstrip() == 'n' or sobre.rstrip() == 'N'):
            print "-------------------------------------------------------------"
            print "\nREMOVE or DELETE from the folder the emails.csv file\n"
            print "-------------------------------------------------------------"
        elif (sobre.rstrip() == 'y' or sobre.rstrip() == 'Y'):
            fo2 = open("emails.csv", "w+")
            with open(mboxFile, "r") as openfileobject:
                for line in openfileobject:
                    if (check == 0 and line.find("From: ",0,7) >= 0 and line.find(email,0,len(line)) >= 0):
                        check = 1
                    elif (check == 1):
                        if(line.find("To: ",0,5) >= 0):
                            text = line[4:len(line)-2]
                            print text
                            fo2.writelines("\"" + text + "\"," + "\n")
                            check = 0
                        else:
                            check = 0
                fo2.close()
                print "\n-------------------------------------------------------------\n"
        else:
            print "-------------------------------------------------------------"
            print "\nInvalid Option\n"
            print "-------------------------------------------------------------"
    else:
        print "-------------------------------------------------------------\n"
        fo2 = open("emails.csv", "w+")
        print email
        with open(mboxFile, "r") as openfileobject:
            for line in openfileobject:
                if (check == 0 and line.find("From: ",0,7) >= 0 and line.find(email,0,len(line)) >= 0):
                    check = 1
                elif (check == 1):
                    if(line.find("To: ",0,5) >= 0):
                        text = line[4:len(line)-2]
                        print text
                        fo2.writelines("\"" + text + "\"," + "\n")
                        check = 0
                    else:
                        check = 0
            fo2.close()
            print "\n-------------------------------------------------------------\n"
else:
    print "\nArquivo .mbox nao encontrado\n"
    print "-------------------------------------------------------------\n"
