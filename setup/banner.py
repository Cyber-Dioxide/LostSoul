import os
from setup import colors
logo = f"""
██╗      ██████╗ ███████╗████████╗
██║     ██╔═══██╗██╔════╝╚══██╔══╝
██║     ██║   ██║███████╗   ██║   
██║     ██║   ██║╚════██║   ██║   
███████╗╚██████╔╝███████║   ██║   
╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   
                                  
███████╗ ██████╗ ██╗   ██╗██╗     
██╔════╝██╔═══██╗██║   ██║██║     
███████╗██║   ██║██║   ██║██║     
╚════██║██║   ██║██║   ██║██║     
███████║╚██████╔╝╚██████╔╝███████╗
╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝                                                                           
"""
from colorama import Fore,Style
c = colors
def banner():
    clear()
    print(c.ran + logo)
    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/Cyber-Dioxide/Stock-Termux ", "- " * 3+c.ran + "|")


def banner2():
    clear()
    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/Cyber-Dioxide/Stock-Termux ", "- " * 3+c.ran + "|")

    print(c.ran + '-' * 63)

def clear():
    os.system("clear")
