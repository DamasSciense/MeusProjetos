import pikepdf
from termcolor import colored

file = open("MeusProjetos/Python/wordlist.txt")

for password in file:
    try:
        with pikepdf.open("MeusProjetos/Python/FaturaC62022.pdf", password=password.strip()) as pdf:
            print(pdf.pages[0])
            print(colored("Password Found: {}".format(password),'green'))
            break
    except:
        print(colored("Trying Password: {}".format(password),'red'))
        continue


# print( "Password: " + password)  # Print the password

# if pikepdf.open("MeusProjetos/Python/FaturaC62022.pdf", password='675871'):
#     print("Password is correct")


