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
    print(c.ran + '-'*63)
    print("|" + "*"* 60 + c.ran + "|")

    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4 + c.ran + "|")
    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4+c.ran + "|")
    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3+c.ran + "|")
    print(c.ran + "|"+ "*" * 60+c.ran + "|")

    print(c.ran + '-' * 63)


def banner2():
    clear()
    print(c.ran + '-'*63)
    print("|" + "*"* 60 + c.ran + "|")

    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX,  "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4 + c.ran + "|")
    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX,  "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4+c.ran + "|")
    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTRED_EX,  "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3+c.ran + "|")
    print(c.ran + "|"+ "*" * 60+c.ran + "|")

    print(c.ran + '-' * 63)

def clear():
    os.system("clear")