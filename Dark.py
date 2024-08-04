import os
import webbrowser
import subprocess
import termcolor
from termcolor import colored
import colorama
os.system("pip3 install tabulate")
import tabulate
from tabulate import tabulate
import time
from time import sleep
import ascii_magic
from ascii_magic import AsciiArt
os.system("pip3 install thedevilseye")
os.system("sudo apt install lolcat")
os.system("sudo gem install lolcat")
from colorama import Fore, Style
import math

def rainbow_gradient_text(text):
    for i, char in enumerate(text):
        h = i / len(text)
        r = int((1 + math.cos(h * 2 * math.pi)) / 2 * 255)
        g = int((1 - math.cos((h * 2 + math.pi/3) * 2 * math.pi)) / 2 * 255)
        b = int((1 - math.cos((h * 2 + 2*math.pi/3) * 2 * math.pi)) / 2 * 255)
        color = f"\033[38;2;{r};{g};{b}m"
        print(f"{color}{char}\033[0m", end="")
    print()

def change():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

def ascii_banner():
    rainbow_gradient_text("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⠿⠛⠛⠛⠻⣿⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⣶⣤⣄⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠘⣿⣧⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠋⠉⠉⠙⠻⣿⣿⣿⡀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣦⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡏⠀⠀⠀⠀⠀⣀⣈⣻⣿⣷⣶⣶⣶⣤⣴⡿⠋⠉⠀⠀⠈⠹⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣼⣿⣿⠀⠀⠀⠀⢠⣾⠟⣿⣿⠟⠁⠀⠀⠈⠙⣿⣷⣦⣄⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⠿⠿⣿⣿⠀⠀⠀⠀⢸⣿⣄⣿⡏⠀⠀⠀⠀⠀⠀⢸⣿⠈⣿⡧⠀⠀⢀⣿
⠀⠀⢀⣀⣤⣤⣤⣤⣤⣤⣤⣴⣾⣿⣿⠿⠋⠀⠀⠀⣿⣿⡆⠀⠀⠀⠀⠛⠿⣿⣷⡀⠀⠀⠀⠀⢀⣼⣿⡿⠟⠁⠀⢀⣾⣿
⢀⣴⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠸⣿⣿⣄⠀⠀⠀⣀⣴⣿⡿⣿⣶⣤⣤⣶⣿⣿⣧⣤⣤⣤⣴⣿⡿⠃
⣾⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⠿⠟⠉⠀⠀⠉⠉⠉⠁⠀⠉⠛⠻⠿⠿⠛⠉⠀⠀
⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠹⣿⣷⡀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣶⡄⠀⠀⠀
⠀⠀⠙⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠘⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠿⠏⠀⠀⠀
⠀⠀⠀⠀⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢹⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠀⢈⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣿⡄⢀⣀⣀⡀⠀⠀⠀⠀⠸⣿⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤
⠀⠀⠀⠀⢀⣸⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠈⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⣶⣦⡀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿
⠀⢀⣤⣾⣿⠟⠛⢿⣿⣦⡀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠋⢹⣿⣧⠀⣀⣠⣴⣾⣿⣿⠟⠛⠛⠛
⠀⠺⠛⠉⠀⠀⠀⠀⢻⣿⣿⣿⡟⠁⠀⠀⣠⡄⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡟⠁⠀⠀⠈⠻⣿⣿⣿⡿⠟⠛⣿⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⣿⡿⠻⢿⣿⣦⣤⣾⣿⣁⡀⠀⠀⠀⢀⣀⣴⣾⣿⡿⠀⠀⠀⠀⠀⠀⠈⢻⣿⡇⠀⣼⣿⡇⠀⢠⣾⡷
⠀⠀⠀⠀⠀⠀⠈⠋⠁⠀⠀⠀⢙⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡿⠋⠀⠀⢿⣿⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡿⠁⠀⠀⠀⠀⠀⣿⣿⠏⠀⠀⠈⢿⣿⡀⠀⠀⠀⠀⠀⢀⣾⣿⠟⠁⠀⠀⠀⠀⠘⠻⠿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⠁⠀⠀⠀⠀⠀⢠⣿⡿⠀⠀⠀⠀⠈⢿⣿⣶⣤⣤⣤⣶⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⣀⠀⠀⠀⣀⣠⣼⣿⣿⡿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

""")

def rainbow_gradient_text2(text):
    for i, char in enumerate(text):
        r = int((i / len(text)) * 255)
        g = int((1 - (i / len(text))) * 255)
        color = f"\033[38;2;{r};{g};0m"
        print(f"{color}{char}\033[0m", end="")
    print()
def header():
    rainbow_gradient_text2("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠---Welcome To DEEP DARK---☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")                                       
    print(" ")

def dark_ascii():
    print('''
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠉⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡐⠀⠍⠻⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠠⠂⡠⠪⡻⣿⣿⣿⣿⣿⣿⠘⣿⢿⣿⣿⣿⣿⡟⡑⢁⠂⢄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⠑⠠⢃⢳⢹⣿⣿⣿⣿⢏⢊⣏⢼⣿⣿⣿⡟⡼⢄⠣⡐⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⠑⢊⠔⢊⡆⣿⣿⣿⣄⢻⢘⠷⣥⣿⣿⣿⡇⡅⢨⠒⠤⡀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⢀⢊⡡⠔⢹⢆⣿⣿⣿⡮⣚⢗⢯⣔⠝⣿⣿⡇⡅⠂⡥⢒⠐⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠉⠄⢒⠈⡜⣸⣻⣛⡿⣃⠻⠇⢳⢹⡟⢘⣿⣷⢈⠑⡐⠤⠉⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿
    ⣿⣿⣷⣝⢿⣟⢭⣿⣽⣯⣿⣽⣿⠿⠋⡁⠀⠀⠀⠈⠥⠈⢀⠌⣤⣭⣭⣭⡸⣰⢥⣬⣷⡿⡓⣬⣭⣭⣥⡡⢐⠠⠉⠤⠀⠀⠀⠀⢙⠩⣿⣿⣿⣿⣽⣯⣿⢻⣿⣯⣾⣿⣿⣿
    ⣿⣿⣿⣿⣧⢻⣷⣝⢿⡿⠟⢋⠠⡀⠆⡀⠅⠀⠠⠉⠤⢒⣤⣾⣿⣿⣿⣿⣷⠮⠣⢹⡫⠪⠾⣿⣿⣿⣿⣿⣦⡐⢡⠤⠁⠀⠀⠇⠀⠆⠀⣉⠛⢿⣿⢟⣵⡿⣱⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣷⠙⢋⠁⡐⢂⡁⢆⠁⠢⠁⠠⣔⣡⣴⢾⣛⣿⣭⣿⣶⣾⣿⣿⣿⡷⠈⠾⣿⣿⣿⣿⣶⣾⣯⣽⣛⡷⢦⣤⣐⠄⠁⠈⠰⡁⠄⡔⢂⠄⣉⠛⢽⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⠁⠐⠈⠐⠄⠀⠘⠀⠠⢪⡴⡟⣯⣵⣾⣿⢿⠛⡿⠍⠙⠒⠚⠛⠋⠉⠛⠋⠙⠛⠓⠒⠚⠩⠽⠛⠻⢿⣿⣾⣽⢻⢶⡕⠠⠀⠊⠐⠁⠒⠠⠰⠀⢻⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⡀⠀⠀⠀⠐⠀⠀⡌⠁⣸⣴⡿⡟⣏⣧⡼⠞⠁⠀⠀⡀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠈⠑⠾⣼⣉⢻⢿⣾⣌⡆⠰⠀⠠⠀⠀⠁⠀⠀⠸⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⠠⡠⡀⠢⠠⠄⡄⡀⣾⡿⣣⣴⣿⣿⠟⠀⠀⣰⠀⠘⢸⠇⠀⠠⠐⢀⠂⠄⢀⠂⠀⠰⡷⠃⠀⢠⠘⠢⡘⢿⣿⣾⣼⢻⣿⢰⢀⠄⠄⠄⢂⠔⡄⠀⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⠀⡃⠎⡓⠦⢄⣒⠐⠙⠿⣮⣻⠿⠃⠀⠀⠑⣼⡀⠄⢀⠀⣠⠁⡈⠄⡐⠈⠠⠀⢄⠀⠀⠠⠀⣼⢁⠀⠈⢊⠻⡿⣫⡾⠟⠈⣀⡢⢥⢒⡑⠆⡀⢸⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡀⠁⠆⡁⢎⠅⣒⠂⠎⡡⢀⠖⡀⠠⠌⠀⡀⠀⠀⠀⢂⢲⡇⠠⠐⠠⠀⡁⢂⠁⢸⣦⠅⠂⠀⠈⠀⠀⠈⡄⠈⠒⡄⠨⡙⠄⢎⠂⡥⠠⠙⠀⠀⣼⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⢇⡀⠀⠠⠘⠈⠆⡚⣈⠡⠎⡰⢁⠎⠱⣘⠂⢎⣐⠠⡀⢞⣷⠀⠌⡀⢁⠀⢂⠈⣼⡻⢘⠠⢢⢘⡀⠍⠦⠘⡌⢡⠘⣅⢒⠩⡀⠇⠰⠈⠀⠀⣰⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⡿⣣⣿⣟⣤⣀⠀⠀⠀⠀⠀⠊⠐⠁⡁⢌⠳⠀⡜⠢⠠⡜⣨⠢⡈⠀⠠⠐⠠⢈⠀⠀⢉⠔⠥⡩⢄⠊⠴⣈⠡⣃⠐⠌⠂⠐⠀⠀⠀⠀⠀⣀⣤⡺⣿⣮⢿⣿⣿⣿⣿
    ⣿⣿⡿⣱⣿⢏⣾⣿⣿⣿⣷⣶⣤⠀⠀⠀⠀⠈⠀⠴⠑⡈⢆⠳⠘⡀⡔⡊⠄⠠⠁⠂⠄⡈⢀⢂⠣⡄⡑⠪⡔⡈⠂⠱⠀⠀⠀⠀⠀⢀⢠⣶⣶⣿⣿⣿⣿⡝⣿⣧⣻⣿⣿⣿
    ⣿⡿⣵⣿⢯⣿⣿⡿⠿⣿⣿⣿⡇⠀⠁⠀⠀⠀⠀⠀⠁⢈⡄⢆⠣⠜⠀⡔⡘⠀⠠⠁⠂⠀⡄⠡⠘⠰⢌⡐⠤⡁⠉⠀⠀⠀⠀⠀⠀⢸⡄⣿⣿⣿⡿⠿⣿⣿⣞⣿⣷⢻⣿⣿
    ⣿⣳⣿⢏⣿⣿⣿⡇⠀⠈⠛⠿⣧⠀⠀⠀⠀⠀⠀⠂⠈⠀⠀⠀⠒⠈⠃⠠⠁⠄⠀⠐⡀⠰⠀⠀⠉⠁⠂⠄⠠⠀⠄⠀⠂⠀⠀⠀⠀⠸⢰⡿⠛⠋⢀⢢⣿⣿⣿⡜⣿⣧⢿⣿
    ⣯⣿⡟⣾⣿⣿⣿⣿⣦⠈⠀⠄⠈⠀⠀⠀⠄⠠⠀⠐⠀⠀⠂⠐⠠⠒⠈⠀⠁⢀⠐⠀⡀⠀⠈⠀⠀⠃⠆⠀⠄⠀⠀⠂⠀⡀⠄⠂⠀⠀⡌⠀⠠⠠⣠⣿⣿⣿⣿⣿⣹⣿⡞⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠠⠀⠂⠀⠐⠈⠀⢁⠀⠉⠐⠠⣀⠠⠀⠄⠂⡀⠂⠄⠀⠄⠁⠌⡐⠠⠀⠄⠀⠀⠠⠀⠒⠤⠀⠌⠐⠀⠰⠁⠠⠁⠀⣿⣿⣿⣿⣿⣿⣧⢿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⡀⠀⠀⠠⠀⡀⠐⠠⠈⠄⠁⠂⠄⠁⢀⠈⠀⠄⠁⡀⠈⠀⡀⠄⠀⠄⠀⡀⠄⠁⠂⠁⠂⠄⠂⢀⠀⡈⠂⠀⠀⠀⡆⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠠⠀⠀⠀⠐⠀⠠⠀⠀⠀⠈⠀⠄⠁⠂⡀⠂⠄⡁⢀⠐⡀⠄⠂⡐⢀⠂⢄⠔⠊⠁⠁⠀⠠⠀⠀⡀⢠⠁⠀⠠⠀⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠄⠂⠀⠐⠠⠀⠀⠀⢀⣠⡄⣠⢀⠁⠒⠂⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣠⡤⣀⠀⠀⠀⠀⠀⡇⠀⢀⠀⢡⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⡀⠀⠠⠀⠀⠀⠀⣿⣿⡃⣟⣳⣧⠀⠀⠀⠀⢀⠀⠠⡀⠀⠀⠀⢴⣿⣻⢛⣻⣷⠀⠀⠀⠀⠃⡇⠀⠀⡄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠄⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⡀⠄⠐⠇⠈⠀⠀⠀⠈⠉⠈⠉⠁⠀⠀⠀⠀⡀⠁⠀⠀⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⡀⠀⠀⡈⠀⠀⠀⠐⢀⡈⠀⠀⠀⠀⠀⠄⠈⠀⠀⠀⠀⠡⠀⠄⠂⡀⠀⠀⠈⠀⠠⠔⠀⠀⠀⠀⠈⢳⠄⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠐⠀⠌⠀⠂⠄⠀⠄⢂⠠⠁⠌⠀⠀⠀⠀⠀⠀⠀⠈⡀⠀⠄⡁⠄⠠⢀⠀⢐⡀⠁⠀⠊⠀⢜⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠐⠈⢀⠀⠀⠀⠀⠀⠀⠀⠀⢁⠠⠐⠐⠋⠀⠀⠀⠀⠀⠀⠀⣱⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿
    ⣿⣿⣷⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣵⠀⠀⠀⠀⠀⠀⠀⢁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣼⣿⣻⣿
    ⣿⣿⣿⣧⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣵⣟⣷⣷⠀⠈⠀⡄⠈⠀⠀⡀⠄⠀⢀⠀⠀⡀⠀⠄⠈⠀⢄⠀⢀⢰⠀⠈⠀⣼⣮⡻⣯⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣱⣿⢏⣿⣿
    ⣿⣿⡝⣿⣧⢿⣿⣿⣿⣿⣿⣿⢟⣯⡿⣫⣾⣿⣿⡇⠀⠀⠃⣽⡄⣼⠀⡄⠈⠀⠀⠁⠀⢠⠀⢠⡀⣴⠀⣾⠇⠀⠀⠀⣿⣿⣿⣮⣻⣮⡻⣿⣿⣿⣿⣿⣿⡿⣱⣿⢏⣾⣿⣿
    ⣿⣿⣿⣞⢿⣷⡻⣿⡿⢟⣫⣵⣿⣿⣹⣿⣿⣿⣿⡇⠀⠀⠀⠈⠀⣿⠐⣿⢀⡆⣤⠀⣠⠈⠀⣼⠁⢻⣦⠉⠀⠀⠂⠀⣿⣿⣿⣿⣷⢻⣿⣷⣽⣻⠿⣿⡟⣵⣿⢯⣾⣿⣿⣿
    ⣿⣿⣿⣿⣮⢿⣿⣕⢶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣧⠀⠀⡀⠀⡘⢥⠀⠛⢸⢇⣿⡀⣿⡆⠀⠙⠀⢸⠀⠀⠀⠀⠁⣸⣿⣿⣿⢿⣷⣶⣶⣶⣶⣶⣶⢦⣾⡿⣣⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣧⡹⣿⣧⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠘⡀⠀⠀⠀⠀⠈⠙⠀⠛⠁⠀⠀⠀⠀⢀⢣⠀⠈⢠⣿⣿⠋⠀⠀⠀⠉⢻⣿⣿⠟⣡⣿⠟⣹⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣷⣌⢻⣷⣼⣿⣿⠛⠛⢻⡟⣿⡟⢻⡗⠀⢀⠀⠐⣆⣄⠀⠀⠀⠀⠀⠀⡀⢀⠀⢀⠀⠂⠁⠀⡄⡘⠛⠃⠀⠊⠙⡗⠀⠀⠛⣡⣾⣿⣡⣾⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣷⣝⢿⣿⣯⡳⢶⣯⣝⢿⣿⣿⡏⣆⡀⠄⡀⠇⠻⡆⢄⡀⠀⠀⠀⢀⠀⠣⡀⠡⠀⠀⠌⣰⣶⣿⣿⣦⠀⣠⣿⠆⢸⢸⡿⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⡻⢿⣷⣽⣻⢿⣮⣻⣧⣋⣶⠀⠠⠀⠘⠃⠘⠇⢹⠃⡿⠀⠀⠠⠘⢄⠀⠀⠈⠙⢏⣿⢟⣵⢟⢉⣷⠁⠀⣨⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣭⣻⢿⣿⣾⣽⣹⣿⡳⣷⠀⠐⡀⢂⠐⠀⡀⢀⠁⠠⠀⠀⡀⠄⠑⠀⠁⢀⠙⠧⣽⣾⣿⠟⠁⢀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⡿⢿⣿⣿⣿⣿⣾⣽⢻⡿⢿⣿⣾⣯⣤⣄⡂⠌⠠⠐⠠⠈⠄⠁⠂⣀⡀⠀⠡⠐⡀⢀⠀⠄⠀⡀⠠⡀⢀⣾⠿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⢹⣿⣿⣿⡿⣱⡟⣽⣷⣮⢿⣟⢿⣛⣛⣿⣿⣿⣿⣿⣿⣿⣟⣛⣻⡧⣦⣄⣐⡀⠠⠈⠐⢀⣁⣴⡿⣵⣿⣿⣿⣷⡝⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⡟⣾⣿⡟⣵⣿⣷⣼⣿⣿⡿⣽⢟⣾⣿⣿⣿⣷⡻⣯⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣾⢏⣾⣿⣿⣿⡝⣷⡻⣿⣿⣷⣵⣿⣾⣽⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣷⢻⣿⣧⡻⣿⣿⣿⡿⣟⣾⢯⣾⣿⣿⣿⣿⣿⣷⡽⣷⡻⣿⣿⣿⣿⣿⣿⣿⣿⢯⣾⣫⣿⣿⣿⣿⣿⣿⣞⢿⣝⢿⣿⣿⣿⡿⣻⣿⣿⣸⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣯⡻⣿⣿⣶⣯⣽⣾⣿⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣜⣿⣝⣿⣿⣿⣿⣿⡿⣳⡿⣳⣿⣿⣿⣿⣿⣿⣿⣿⣮⡻⣿⣾⣭⣷⣿⣿⡿⣳⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣽⣟⣻⣯⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⢿⣞⢿⣿⣿⡟⣵⡿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣭⣿⣻⣿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣻⣯⣻⢟⣾⢟⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡹⣷⣿⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ''')

def ascii_dark():
    print('''
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠉⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡐⠀⠍⠻⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠠⠂⡠⠪⡻⣿⣿⣿⣿⣿⣿⠘⣿⢿⣿⣿⣿⣿⡟⡑⢁⠂⢄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⠑⠠⢃⢳⢹⣿⣿⣿⣿⢏⢊⣏⢼⣿⣿⣿⡟⡼⢄⠣⡐⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⠑⢊⠔⢊⡆⣿⣿⣿⣄⢻⢘⠷⣥⣿⣿⣿⡇⡅⢨⠒⠤⡀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⢀⢊⡡⠔⢹⢆⣿⣿⣿⡮⣚⢗⢯⣔⠝⣿⣿⡇⡅⠂⡥⢒⠐⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠉⠄⢒⠈⡜⣸⣻⣛⡿⣃⠻⠇⢳⢹⡟⢘⣿⣷⢈⠑⡐⠤⠉⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿
    ⣿⣿⣷⣝⢿⣟⢭⣿⣽⣯⣿⣽⣿⠿⠋⡁⠀⠀⠀⠈⠥⠈⢀⠌⣤⣭⣭⣭⡸⣰⢥⣬⣷⡿⡓⣬⣭⣭⣥⡡⢐⠠⠉⠤⠀⠀⠀⠀⢙⠩⣿⣿⣿⣿⣽⣯⣿⢻⣿⣯⣾⣿⣿⣿
    ⣿⣿⣿⣿⣧⢻⣷⣝⢿⡿⠟⢋⠠⡀⠆⡀⠅⠀⠠⠉⠤⢒⣤⣾⣿⣿⣿⣿⣷⠮⠣⢹⡫⠪⠾⣿⣿⣿⣿⣿⣦⡐⢡⠤⠁⠀⠀⠇⠀⠆⠀⣉⠛⢿⣿⢟⣵⡿⣱⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣷⠙⢋⠁⡐⢂⡁⢆⠁⠢⠁⠠⣔⣡⣴⢾⣛⣿⣭⣿⣶⣾⣿⣿⣿⡷⠈⠾⣿⣿⣿⣿⣶⣾⣯⣽⣛⡷⢦⣤⣐⠄⠁⠈⠰⡁⠄⡔⢂⠄⣉⠛⢽⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⠁⠐⠈⠐⠄⠀⠘⠀⠠⢪⡴⡟⣯⣵⣾⣿⢿⠛⡿⠍⠙⠒⠚⠛⠋⠉⠛⠋⠙⠛⠓⠒⠚⠩⠽⠛⠻⢿⣿⣾⣽⢻⢶⡕⠠⠀⠊⠐⠁⠒⠠⠰⠀⢻⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⡀⠀⠀⠀⠐⠀⠀⡌⠁⣸⣴⡿⡟⣏⣧⡼⠞⠁⠀⠀⡀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠈⠑⠾⣼⣉⢻⢿⣾⣌⡆⠰⠀⠠⠀⠀⠁⠀⠀⠸⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⠠⡠⡀⠢⠠⠄⡄⡀⣾⡿⣣⣴⣿⣿⠟⠀⠀⣰⠀⠘⢸⠇⠀⠠⠐⢀⠂⠄⢀⠂⠀⠰⡷⠃⠀⢠⠘⠢⡘⢿⣿⣾⣼⢻⣿⢰⢀⠄⠄⠄⢂⠔⡄⠀⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⠀⡃⠎⡓⠦⢄⣒⠐⠙⠿⣮⣻⠿⠃⠀⠀⠑⣼⡀⠄⢀⠀⣠⠁⡈⠄⡐⠈⠠⠀⢄⠀⠀⠠⠀⣼⢁⠀⠈⢊⠻⡿⣫⡾⠟⠈⣀⡢⢥⢒⡑⠆⡀⢸⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡀⠁⠆⡁⢎⠅⣒⠂⠎⡡⢀⠖⡀⠠⠌⠀⡀⠀⠀⠀⢂⢲⡇⠠⠐⠠⠀⡁⢂⠁⢸⣦⠅⠂⠀⠈⠀⠀⠈⡄⠈⠒⡄⠨⡙⠄⢎⠂⡥⠠⠙⠀⠀⣼⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⢇⡀⠀⠠⠘⠈⠆⡚⣈⠡⠎⡰⢁⠎⠱⣘⠂⢎⣐⠠⡀⢞⣷⠀⠌⡀⢁⠀⢂⠈⣼⡻⢘⠠⢢⢘⡀⠍⠦⠘⡌⢡⠘⣅⢒⠩⡀⠇⠰⠈⠀⠀⣰⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⡿⣣⣿⣟⣤⣀⠀⠀⠀⠀⠀⠊⠐⠁⡁⢌⠳⠀⡜⠢⠠⡜⣨⠢⡈⠀⠠⠐⠠⢈⠀⠀⢉⠔⠥⡩⢄⠊⠴⣈⠡⣃⠐⠌⠂⠐⠀⠀⠀⠀⠀⣀⣤⡺⣿⣮⢿⣿⣿⣿⣿
    ⣿⣿⡿⣱⣿⢏⣾⣿⣿⣿⣷⣶⣤⠀⠀⠀⠀⠈⠀⠴⠑⡈⢆⠳⠘⡀⡔⡊⠄⠠⠁⠂⠄⡈⢀⢂⠣⡄⡑⠪⡔⡈⠂⠱⠀⠀⠀⠀⠀⢀⢠⣶⣶⣿⣿⣿⣿⡝⣿⣧⣻⣿⣿⣿
    ⣿⡿⣵⣿⢯⣿⣿⡿⠿⣿⣿⣿⡇⠀⠁⠀⠀⠀⠀⠀⠁⢈⡄⢆⠣⠜⠀⡔⡘⠀⠠⠁⠂⠀⡄⠡⠘⠰⢌⡐⠤⡁⠉⠀⠀⠀⠀⠀⠀⢸⡄⣿⣿⣿⡿⠿⣿⣿⣞⣿⣷⢻⣿⣿
    ⣿⣳⣿⢏⣿⣿⣿⡇⠀⠈⠛⠿⣧⠀⠀⠀⠀⠀⠀⠂⠈⠀⠀⠀⠒⠈⠃⠠⠁⠄⠀⠐⡀⠰⠀⠀⠉⠁⠂⠄⠠⠀⠄⠀⠂⠀⠀⠀⠀⠸⢰⡿⠛⠋⢀⢢⣿⣿⣿⡜⣿⣧⢿⣿
    ⣯⣿⡟⣾⣿⣿⣿⣿⣦⠈⠀⠄⠈⠀⠀⠀⠄⠠⠀⠐⠀⠀⠂⠐⠠⠒⠈⠀⠁⢀⠐⠀⡀⠀⠈⠀⠀⠃⠆⠀⠄⠀⠀⠂⠀⡀⠄⠂⠀⠀⡌⠀⠠⠠⣠⣿⣿⣿⣿⣿⣹⣿⡞⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠠⠀⠂⠀⠐⠈⠀⢁⠀⠉⠐⠠⣀⠠⠀⠄⠂⡀⠂⠄⠀⠄⠁⠌⡐⠠⠀⠄⠀⠀⠠⠀⠒⠤⠀⠌⠐⠀⠰⠁⠠⠁⠀⣿⣿⣿⣿⣿⣿⣧⢿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⡀⠀⠀⠠⠀⡀⠐⠠⠈⠄⠁⠂⠄⠁⢀⠈⠀⠄⠁⡀⠈⠀⡀⠄⠀⠄⠀⡀⠄⠁⠂⠁⠂⠄⠂⢀⠀⡈⠂⠀⠀⠀⡆⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠠⠀⠀⠀⠐⠀⠠⠀⠀⠀⠈⠀⠄⠁⠂⡀⠂⠄⡁⢀⠐⡀⠄⠂⡐⢀⠂⢄⠔⠊⠁⠁⠀⠠⠀⠀⡀⢠⠁⠀⠠⠀⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠄⠂⠀⠐⠠⠀⠀⠀\033[31m⢀⣠⡄⣠\033[0m⢀⠁⠒⠂⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[31m⣠⣠⡤⣀\033[0m⠀⠀⠀⠀⠀⡇⠀⢀⠀⢡⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⡀⠀⠠⠀⠀⠀⠀\033[31m⣿⣿⡃⣟⣳⣧\033[0m⠀⠀⠀⠀⢀⠀⠠⡀⠀⠀⠀\033[31m⢴⣿⣻⢛⣻⣷\033[0m⠀⠀⠀⠀⠃⡇⠀⠀⡄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠄⠀⠀⠀⠀\033[31m⠉⠉⠉⠉\033[0m⠀⠀⠀⠀⠀⡀⠄⠐⠇⠈⠀⠀⠀\033[31m⠈⠉⠈⠉⠁\033[0m⠀⠀⠀⠀⡀⠁⠀⠀⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⡀⠀⠀⡈⠀⠀⠀⠐⢀⡈⠀⠀⠀⠀⠀⠄⠈⠀⠀⠀⠀⠡⠀⠄⠂⡀⠀⠀⠈⠀⠠⠔⠀⠀⠀⠀⠈⢳⠄⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠐⠀⠌⠀⠂⠄⠀⠄⢂⠠⠁⠌⠀⠀⠀⠀⠀⠀⠀⠈⡀⠀⠄⡁⠄⠠⢀⠀⢐⡀⠁⠀⠊⠀⢜⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠐⠈⢀⠀⠀⠀⠀⠀⠀⠀⠀⢁⠠⠐⠐⠋⠀⠀⠀⠀⠀⠀⠀⣱⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿
    ⣿⣿⣷⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣵⠀⠀⠀⠀⠀⠀⠀⢁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣼⣿⣻⣿
    ⣿⣿⣿⣧⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣵⣟⣷⣷⠀⠈⠀⡄⠈⠀⠀⡀⠄⠀⢀⠀⠀⡀⠀⠄⠈⠀⢄⠀⢀⢰⠀⠈⠀⣼⣮⡻⣯⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣱⣿⢏⣿⣿
    ⣿⣿⡝⣿⣧⢿⣿⣿⣿⣿⣿⣿⢟⣯⡿⣫⣾⣿⣿⡇⠀⠀⠃⣽⡄⣼⠀⡄⠈⠀⠀⠁⠀⢠⠀⢠⡀⣴⠀⣾⠇⠀⠀⠀⣿⣿⣿⣮⣻⣮⡻⣿⣿⣿⣿⣿⣿⡿⣱⣿⢏⣾⣿⣿
    ⣿⣿⣿⣞⢿⣷⡻⣿⡿⢟⣫⣵⣿⣿⣹⣿⣿⣿⣿⡇⠀⠀⠀⠈⠀⣿⠐⣿⢀⡆⣤⠀⣠⠈⠀⣼⠁⢻⣦⠉⠀⠀⠂⠀⣿⣿⣿⣿⣷⢻⣿⣷⣽⣻⠿⣿⡟⣵⣿⢯⣾⣿⣿⣿
    ⣿⣿⣿⣿⣮⢿⣿⣕⢶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣧⠀⠀⡀⠀⡘⢥⠀⠛⢸⢇⣿⡀⣿⡆⠀⠙⠀⢸⠀⠀⠀⠀⠁⣸⣿⣿⣿⢿⣷⣶⣶⣶⣶⣶⣶⢦⣾⡿⣣⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣧⡹⣿⣧⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠘⡀⠀⠀⠀⠀⠈⠙⠀⠛⠁⠀⠀⠀⠀⢀⢣⠀⠈⢠⣿⣿⠋⠀⠀⠀⠉⢻⣿⣿⠟⣡⣿⠟⣹⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣷⣌⢻⣷⣼⣿⣿⠛⠛⢻⡟⣿⡟⢻⡗⠀⢀⠀⠐⣆⣄⠀⠀⠀⠀⠀⠀⡀⢀⠀⢀⠀⠂⠁⠀⡄⡘⠛⠃⠀⠊⠙⡗⠀⠀⠛⣡⣾⣿⣡⣾⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣷⣝⢿⣿⣯⡳⢶⣯⣝⢿⣿⣿⡏⣆⡀⠄⡀⠇⠻⡆⢄⡀⠀⠀⠀⢀⠀⠣⡀⠡⠀⠀⠌⣰⣶⣿⣿⣦⠀⣠⣿⠆⢸⢸⡿⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⡻⢿⣷⣽⣻⢿⣮⣻⣧⣋⣶⠀⠠⠀⠘⠃⠘⠇⢹⠃⡿⠀⠀⠠⠘⢄⠀⠀⠈⠙⢏⣿⢟⣵⢟⢉⣷⠁⠀⣨⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣭⣻⢿⣿⣾⣽⣹⣿⡳⣷⠀⠐⡀⢂⠐⠀⡀⢀⠁⠠⠀⠀⡀⠄⠑⠀⠁⢀⠙⠧⣽⣾⣿⠟⠁⢀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⡿⢿⣿⣿⣿⣿⣾⣽⢻⡿⢿⣿⣾⣯⣤⣄⡂⠌⠠⠐⠠⠈⠄⠁⠂⣀⡀⠀⠡⠐⡀⢀⠀⠄⠀⡀⠠⡀⢀⣾⠿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⢹⣿⣿⣿⡿⣱⡟⣽⣷⣮⢿⣟⢿⣛⣛⣿⣿⣿⣿⣿⣿⣿⣟⣛⣻⡧⣦⣄⣐⡀⠠⠈⠐⢀⣁⣴⡿⣵⣿⣿⣿⣷⡝⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⡟⣾⣿⡟⣵⣿⣷⣼⣿⣿⡿⣽⢟⣾⣿⣿⣿⣷⡻⣯⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣾⢏⣾⣿⣿⣿⡝⣷⡻⣿⣿⣷⣵⣿⣾⣽⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣷⢻⣿⣧⡻⣿⣿⣿⡿⣟⣾⢯⣾⣿⣿⣿⣿⣿⣷⡽⣷⡻⣿⣿⣿⣿⣿⣿⣿⣿⢯⣾⣫⣿⣿⣿⣿⣿⣿⣞⢿⣝⢿⣿⣿⣿⡿⣻⣿⣿⣸⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣯⡻⣿⣿⣶⣯⣽⣾⣿⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣜⣿⣝⣿⣿⣿⣿⣿⡿⣳⡿⣳⣿⣿⣿⣿⣿⣿⣿⣿⣮⡻⣿⣾⣭⣷⣿⣿⡿⣳⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣽⣟⣻⣯⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⢿⣞⢿⣿⣿⡟⣵⡿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣭⣿⣻⣿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣻⣯⣻⢟⣾⢟⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡹⣷⣿⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ''')

def change():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)


def clear_screen():
    subprocess.run('clear' if os.name == 'posix' else 'cls')

def dark_search():
    os.system("git clone https://github.com/Malwareman007/UnderworldQuest.git")
    os.chdir("UnderworldQuest")
    os.system("python3 -m pip install -r requirements.txt")
    dark_search2()

def dark_search2():
    clear_screen()
    dark_ascii()
    print("ENTER SEARCH IN QUOTATION MARKS")
    DEEP = input("Searching in the Dark For: ")
    clear_screen()
    ascii_dark()
    print("SEARCH TERMS ACCEPTED")
    time.sleep(1)
    clear_screen()
    dark_ascii()
    print("NUMEBER OF ONIONS")
    RESS = input("How Many Onions To Dig For: ")
    clear_screen()
    ascii_dark()
    print("QUANTITY ACCEPTED")
    time.sleep(1)
    clear_screen()
    dark_ascii()
    print(colored("Launching UNDERWORLD QUEST: DarkWeb Search", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(2)
    subprocess.run(["python3", "UnderworldQuest.py", "-q", DEEP, "-a", RESS, "-p"])
    print(" ")
    print("1) New Search")
    print("2) Main Menu")
    choice = input("Select Option: ")
    if choice == "1":
        dark_search2()
    elif choice == "2":
        main()
    else:
        print("INVALID SELECTION! GUESS YOU'RE SEARCHING AGAIN, FAT-FINGERS")
        time.sleep(1.5)
        dark_search()


def light_search():
    clear_screen()
    dark_ascii()    
    print("Request Number of Results")
    nmb = input("Number of Onions: ")
    clear_screen()
    ascii_dark()
    print("QUANTITY ACCEPTED")
    time.sleep(.5)
    clear_screen()
    dark_ascii()
    print("Search Term")
    src = input("Search: ")
    clear_screen()
    ascii_dark()
    print("SEARCH TERMS ACCEPTED")
    time.sleep(.5)
    clear_screen()
    subprocess.run(["thedevilseye", nmb, src])
    print("New Search?")
    choice = input("y/n: ")
    if choice == "y":
        clear_screen()
        new2()
    if choice == "n":
        clear_screen()
        main()

def new2():
    print("Request Number of Results")
    nmb2 = input("Number of Onions: ")
    clear_screen()
    print("Search Term")
    src2 = input("Search: ")
    subprocess.run(["thedevilseye", "-c", nmb2, "-d", src2])
    print("New Search?")
    choice = input("y/n: ")
    if choice == "y":
        clear_screen()
        new2()
    if choice == "n":
        clear_screen()
        main()

def dump():
    change()
    clear_screen()
    os.system("git clone https://github.com/josh0xA/darkdump.git")
    os.chdir("darkdump")
    os.system("python3 -m pip install -r requirements.txt")
    clear_screen()
    dark_ascii()
    print("ENTER SEARCH IN QUOTATION MARKS")
    DEEP = input("Searching in the Dark For: ")
    clear_screen()
    ascii_dark()
    print("SEARCH TERMS ACCEPTED")
    time.sleep(1)
    clear_screen()
    dark_ascii()
    print("NUMEBER OF ONIONS")
    RESS = input("How Many Onions To Dig For: ")
    clear_screen()
    ascii_dark()
    print("QUANTITY ACCEPTED")
    time.sleep(1)
    clear_screen()
    dark_ascii()
    print(colored("Launching DARKDUMP: DarkWeb Search", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(2)
    subprocess.run(["python3", "darkdump.py", "-q", DEEP, "-a", RESS, "-p"])
    print(" ")
    print("1) New Search")
    print("2) Main Menu")
    choice = input("Select Option: ")
    if choice == "1":
        dump()
    elif choice == "2":
        main()
    else:
        print("INVALID SELECTION! GUESS YOU'RE SEARCHING AGAIN, FAT-FINGERS")
        time.sleep(1.5)
        dump()

def onions():
    clear_screen()
    dark_ascii()
    print("SEARCH TERM IN QUOTES")
    RESS = input("Search For: ")
    clear_screen()
    ascii_dark()
    print("SEARCH TERM ACCEPTED")
    time.sleep(1)
    clear_screen()
    dark_ascii()
    print(colored("Launching ONIONSEARCH: Organizing by Search Engine", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(2)
    subprocess.run(["onionsearch", RESS, "--continuous_write", "true", "--output", "output.csv"])
    os.system("nano output.csv")
    main()


def main():
    change()
    clear_screen()
    ascii_banner()
    header()
    rainbow_gradient_text("    1) Underworld        2) TheDevilsEye                3) DarkDump             4) OnionSearch            ")
    rainbow_gradient_text2("    5) AnonGT            6) Go To HELL  ")
    print(" ")
    choice = input("\033[97mSelect an option: ")

    if choice == "1":
        dark_search()
    elif choice == "2":
        light_search()
    elif choice == "3":
        dump()
    elif choice == "4":
        os.system("pip3 install onionsearch")
        onions()
    elif choice == "5":
        change()
        os.system("git clone https://github.com/gt0day/AnonGT.git")
        os.chdir("AnonGT")
        os.system("sudo chmod +x install.py")
        os.system("sudo python3 ./install.py install")
        os.system("sudo python3 AnonGT.py")
        choice = input("Select Option: ")
        if choice == "start":
            os.system("sudo python3 AnonGT.py start")
            main()
        if choice == "start+":
            os.system("sudo python3 AnonGT.py start+")
            main()
        if choice == "stop":
            os.system("sudo python3 AnonGT.py stop")
            main()
        if choice == "status":
            os.system("sudo python3 AnonGT.py status")
            time.sleep(5)
            main()
        if choice == "myip":
            os.system("sudo python3 AnonGT.py myip")
            time.sleep(5)
            main()
        if choice == "chngid":
            os.system("sudo python3 AnonGT.py chngid")
            main()
        if choice == "autochng":
            os.system("sudo python3 AnonGT.py autochng")
            main()
        if choice == "antimitm":
            os.system("sudo python3 AnonGT.py antimitm")
            main()
        if choice == "chngmac":
            os.system("sudo python3 AnonGT.py chngmac")
            main()
        if choice == "rvmac":
            os.system("sudo python3 AnonGT.py rvmac")
            main()
        if choice == "oniongen":
            os.system("sudo python3 AnonGT.py oniongen")
            main()
        if choice == "checko":
            os.system("sudo python3 AnonGT.py checko")
            main()
        if choice == "share":
            os.system("sudo python3 AnonGT.py share")
            main()
        if choice == "receive":
            os.system("sudo python3 AnonGT.py receive")
            main()
        if choice == "chat":
            os.system("sudo python3 AnonGT.py chat")
            main()
        if choice == "website":
            os.system("sudo python3 AnonGT.py website")
            main()
        if choice == "wipe":
            os.system("sudo python3 AnonGT.py wipe")
            main()
        if choice == "fix":
            os.system("sudo python3 AnonGT.py fix")
            main()
        if choice == "checku":
            os.system("sudo python3 AnonGT.py checku")
            main()
        if choice == "about":
            os.system("sudo python3 AnonGT.py about")
            main()
    elif choice == "6":
        exit()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        change()
        main() 

if __name__ == "__main__":
    main()        
