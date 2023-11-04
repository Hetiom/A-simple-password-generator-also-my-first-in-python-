# COMMAND LINE VERSION #

import secrets # to generate random characters
from colorama import init, Fore, Back, Style # to custom the text and the font color
import random # to shuffle all the characters

secrets_generator = secrets.SystemRandom()

""" ↓ Start of the
        text customization part """

FOREGROUND = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
BACKGROUND = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE, Back.LIGHTBLACK_EX ]
BRIGHTNESS = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]
""" ↑ End of the
        text customization part """

# print the ascii art
print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT, """               __________                                               .___     
                 \______   \_____    ______ ________  _  _____________  __| _/     
                  |     ___/\__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ |      
                  |    |     / __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ |      
 _________________|____|    (____  /____  >____  >  \/\_/ \____/|__|  \____ |      
/_____/_____/_____/              \/     \/     \/                          \/      
  ________                                   __                                    
 /  _____/  ____   ____   ________________ _/  |_  ___________                     
/   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \                    
\    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/                    
 \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|_______________________
        \/     \/     \/     \/           \/              /_____/_____/_____/_____/

""")

def password_gen():
    Randoms_char = ""
    # print the differents options
    while True:
        choose = input("\nplease choose the size of your password:\na) 8 characters\nb) 12 characters\nc) 16 characters \nd) Overkill password\n")
        if choose == 'a':
            pass_size = 2
            break
        elif choose == 'b':
            pass_size = 3
            break
        elif choose == 'c':
            pass_size = 4
            break
        elif choose == 'd':
            pass_size = 64
            break
        else:
            print("type a, b, c or d")

    # generate the password
    for i in range(pass_size):
        Randoms_char += str(chr(secrets_generator.randint(65, 90))) #add a random maj letter to the list
        Randoms_char += str(chr(secrets_generator.randint(97, 122))) #add a random letter to the list
        Randoms_char += str(chr(secrets_generator.randint(48, 57))) #add a random digit to the list
        Randoms_char += str(chr(secrets_generator.randint(33, 47))) #add a random ponctuation sign to the list

    Char_list = list(Randoms_char) # convert the string in a list
    random.shuffle(Char_list) # shuffle the list
    final_password = "".join(Char_list) # convert the list in a string back
    print(f"\nyour password is: \n{final_password}\n")

    # write the password in a file
    with open('stored passwords.txt', 'a') as file:
        file.write(f'\n{final_password}')
    menu()

def make_new_file():
    print("not implemented yet.")
    menu()
    '''while True:
        try:
            name = (input("\nwrite a name for the new file:\n"))
            open(f"{name}.txt", "x")
            print("\nNew file created !")
            var = 0
            menu()
        except FileExistsError:
            print("Wrong input, try again")'''

def settings():
    while True:
        schoice = int(input("""\n
_Settings_
1) Text color
2) authors
3) menu ->
4) i'm racist\n"""))
        try:
            if schoice == 1: # 1
                while True:
                    txt_color = int(input("\nChoose a color:\n1) Blue\n2) Green\n3) Cyan\n4) Magenta\n5) Yellow\n6) Red\n7) White\n"))
                    print(txt_color)
                    if txt_color == 1:
                        color = getattr(Fore, 'LIGHTBLUE_EX', Style.BRIGHT)
                        print(color)
                        break
                    elif txt_color == 2:
                        color = getattr(Fore, 'LIGHTGREEN_EX', Style.BRIGHT)
                        print(color)
                        break
                    elif txt_color == 3:
                        color = getattr(Fore, 'LIGHTCYAN_EX', Style.BRIGHT)
                        print(color)
                        break
                    elif txt_color == 4:
                        color = getattr(Fore, 'LIGHTMAGENTA_EX', Style.BRIGHT)
                        print(color)
                        break
                    elif txt_color == 5:
                        color = getattr(Fore, 'LIGHTYELLOW_EX', Style.BRIGHT)
                        print(color)
                        break
                    elif txt_color == 6:
                        color = getattr(Fore, 'LIGHTRED_EX', Style.BRIGHT)
                        print(color)
                        break
                    elif txt_color == 7:
                        print(Fore, 'LIGHTWHITE_EX', Style.BRIGHT)
                        break
                    else:
                        print("Oops, Wrong input! Please enter a valid number.\n")
            elif schoice == 2: # 2
                    print("Tity__")
                    print("https://discord.gg/wcz2VKMsTf")
            elif schoice == 3: # 3
                menu()
            elif schoice == 4: # 4
                easter_egg()
        except ValueError:
            print("Oops, Wrong input! Please enter a valid number.\n")

def menu():
    while True:
        try:
            choice = int(input("""\nChoose an option:
1) make a new password
2) create a new file
3) settings
4) exit\n"""))
            if choice == 1:
                password_gen()
                break
            elif choice == 2:
                make_new_file()
                break
            elif choice == 3:
                settings()
                break
            elif choice == 4:
                print("\nGoodbye! See you next time!\n")
                quit()
        except ValueError:
            print("Oops, Wrong input! Please enter a valid number.")

def easter_egg():
    print("""⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠈⠈⠉⠉⠈⠈⠈⠉⠉⠉⠉⠉⠉⠉⠉⠙⠻⣄⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⣄⠀⠀⢀⠀⢀⣀⣤⠄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣉⣩⣤⠴⠶⠶⠒⠛⠛⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠤⠶⠒⠚⠋⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⡍⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣫⣭⣷⠶⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠶⠶⠖⠚⠛⠛⣹⠏⠀⠀⠀⠀⠀⠀⠀⠀⠴⠛⠛⠉⡁⠀⠀⠙⠻⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡷⠷⢿⣦⣤⣈⡙⢿⣿⢆⣴⣤⡄⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣤⡀⣸⡄⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣟⣩⣤⣴⣤⣌⣿⣿⣿⣦⣹⣿⢁⣿⣿⣄⣀⡀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⠋⠻⢿⡁⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠿⠛⢦⣽⣿⣿⢻⣿⣿⣿⣿⠋⠁⠘⣿⣿⣿⣿⣿⣿⣼⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⠁⠀⠀⠙⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠿⣿⣯⣼⣿⡿⠟⠃⠀⠀⠀⣿⣿⣿⣿⣿⡛⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣧⣴⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣺⠟⠃⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⢁⣀⣀⣀⣀⣀⣠⣀⣀⢀⢀⢀
⠀⠀⢿⠿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠙⠛⠛⠙⢻⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡇⠀⠘⠃⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡟⢿⣿⣆⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⡼⠁⢀⣀⡀⠀⠀⠀⣦⣄⠀⣠⡄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣷⣬⢻⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⣰⣿⡿⠿⠦⢤⣴⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠒⣿⣿⣿⡿⠟⠹⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡖⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡿⣾⣿⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣆⣀⣀⣤⣴⣶⣶⣾⣿⣷⣦⣴⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡇⣿⣿⡛⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢾⡟⠛⠛⠻⠛⠛⠛⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠓⢁⣬⣿⠇⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⠀⠀⢰⡿⣻⠇⠀⠀⠀⠀⠀⣠⣶⣶⣶⣶⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢐⣯⠞⠁⠀⠀⠀⠀⠀⠀⣄⠱⣄⠀⠀⠀⠀⠸⡧⠟⠆⠀⠀⠀⠀⠘⠿⢿⠿⠿⣿⡿⣿⠃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡈⠂⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢠⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⡄⠀⠀⠑⠄⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣦⣦⣼⡏⠳⣜⢿⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⢠⣷⣦⣤⣀⣀⣀⣴⣿⣿⣿⣿⣿⡿⠻⠆⠸⣎⣧⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣠⡄⠀⣿⢹⡇⢸⡀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿
""")
    settings()

if __name__ == "__main__":
    menu()
