
import os
print("My account link has been opened") 
username = "K_DKP"
url = f"https://t.me/{username}"

os.system(f'termux-open "{url}"')
