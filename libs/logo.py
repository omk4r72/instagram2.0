# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo ="""
▀█▀ █▀▀▄ █▀▀ ▀▀█▀▀ █▀▀█ █▀▀▀ █▀▀█ █▀▀█ █▀▄▀█ 　 ░█▀▀█ █▀▀█ ▀▀█▀▀ 　 ░█▀▀█ █▀▀ █▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀█ 
░█─ █──█ ▀▀█ ──█── █▄▄█ █─▀█ █▄▄▀ █▄▄█ █─▀─█ 　 ░█▀▀▄ █──█ ──█── 　 ░█▄▄▀ █▀▀ █──█ █──█ █▄▄▀ ──█── █▀▀ █▄▄▀ 
▄█▄ ▀──▀ ▀▀▀ ──▀── ▀──▀ ▀▀▀▀ ▀─▀▀ ▀──▀ ▀───▀ 　 ░█▄▄█ ▀▀▀▀ ──▀── 　 ░█─░█ ▀▀▀ █▀▀▀ ▀▀▀▀ ▀─▀▀ ──▀── ▀▀▀ ▀─▀▀
"""


urls = [
    "GitHub - https://github.com/omk4r72",
    "Instagram - https://instagram.com/0mk4rx",
    "Facebook - https://fb.com/omkar",
    "Twitter - https://twitter.com/omkarchavhan.",
    "InstaReporter Tool - https://github.com/omkarchavhan/InstaReporter",
    "Gmail - mailto:chavhanomkar702@gmail.com"
    ]

def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.MAGENTA + "      Producer: Omkar"+ Style.RESET_ALL + Style.BRIGHT)
    print(Fore.CYAN + "\n", "-> Follow me On Instagram @0mk4rx.")
    print ("\n", "-> Special For Hackers:\n    " + choice(urls))
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)
