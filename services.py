# backend services

from secret import SECRET_PASSWORD

# random()
import random
frog_images = ["https://duck.ceo/tmp_aad345ce/frog1.png", "https://duck.ceo/tmp_aad345ce/frog2.png", "https://duck.ceo/tmp_aad345ce/frog3.jpg"]
def randomcoolfrogimagelol():
    return random.choice(frog_images)
    
# login()
import os ; import hashlib
def worstauthenticationever(username, password):
    #print(SECRET_PASSWORD)
    admin_supersecretpassword = SECRET_PASSWORD
    if password != admin_supersecretpassword:
        token_idk = hashlib.md5(username.encode('utf-8')).hexdigest(), False
    else:
        token_idk = admin_supersecretpassword, True
    return token_idk

# win()
def didyouwin(lol):
    if lol == SECRET_PASSWORD:
        return True
    else: return False
