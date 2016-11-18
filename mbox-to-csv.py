#!/usr/bin/python

# Open a file

import os.path
line2 = ""
check = 0
print "\n\n-------------------------------------------------------------"
print "\t\t\tMBOX EMAIL GRABBER"
print "-------------------------------------------------------------"
mboxInput = raw_input('Digite o nome do arquivo .mbox: ')
mboxFile = mboxInput+".mbox"
print "-------------------------------------------------------------"
if os.path.isfile(mboxFile):
    if os.path.isfile("emails.csv"):
        print "\t\t\tATENCAO!"
        print "\nArquivo emails.csv ja existente!"
        sobre = raw_input('Deseja sobrescrever ? SIM (s) OU NAO (n): ')
        if (sobre.rstrip() == 'n' or sobre.rstrip() == 'N'):
            print "-------------------------------------------------------------"
            print "\nREMOVA ou DELETE da pasta o arquivo emails.csv\n"
            print "-------------------------------------------------------------"
        elif (sobre.rstrip() == 's' or sobre.rstrip() == 'S'):
            fo2 = open("emails.csv", "w+")
            with open(mboxFile, "r") as openfileobject:
                for line in openfileobject:
                    if (check == 0 and line.find("From: Tiago Fonseca",0,20) >= 0):
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
            print "\nOpcao invalida\n"
            print "-------------------------------------------------------------"
    else:
        print "-------------------------------------------------------------\n"
        fo2 = open("emails.csv", "w+")
        with open(mboxFile, "r") as openfileobject:
            for line in openfileobject:
                if (check == 0 and line.find("From: Tiago Fonseca",0,20) >= 0):
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
