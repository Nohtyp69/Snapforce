import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.MAGENTA + """
                                          ______                                        
                                         /      \                                       
  _______  _______    ______    ______  /$$$$$$  |______    ______    _______   ______  
 /       |/       \  /      \  /      \ $$ |_ $$//      \  /      \  /       | /      \ 
/$$$$$$$/ $$$$$$$  | $$$$$$  |/$$$$$$  |$$   |  /$$$$$$  |/$$$$$$  |/$$$$$$$/ /$$$$$$  |
$$      \ $$ |  $$ | /    $$ |$$ |  $$ |$$$$/   $$ |  $$ |$$ |  $$/ $$ |      $$    $$ |
 $$$$$$  |$$ |  $$ |/$$$$$$$ |$$ |__$$ |$$ |    $$ \__$$ |$$ |      $$ \_____ $$$$$$$$/ 
/     $$/ $$ |  $$ |$$    $$ |$$    $$/ $$ |    $$    $$/ $$ |      $$       |$$       |
$$$$$$$/  $$/   $$/  $$$$$$$/ $$$$$$$/  $$/      $$$$$$/  $$/        $$$$$$$/  $$$$$$$/ 
                              $$ |                                                      
                              $$ |                                                      
                              $$/                                                       

""" + Fore.LIGHTCYAN_EX)
print(banner)
import random
import string

def generate_username(length=8):
    username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return username

def brute_force(target_username):
    possible_usernames = []
    for i in range(1, 10000):
        username = generate_username(8)
        if username == target_username:
            possible_usernames.append(username)
    return possible_usernames

target_username = input("Enter the target Snapchat username: ")
possible_usernames = brute_force(target_username)

print("Possible usernames:")
for username in possible_usernames:
    print(username)
