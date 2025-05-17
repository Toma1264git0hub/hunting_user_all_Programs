import random
import requests
import os
import time

GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

platforms = {
    "TIKTOK": "https://www.tiktok.com/@{}",
    "FACEBOOK": "https://www.facebook.com/{}",
    "INSTAGRAM": "https://www.instagram.com/{}",
    "TELEGRAM": "https://t.me/{}",
    "GITHUB": "https://github.com/{}",
    "DISCORD": "https://discord.com/users/{}",
    "SNAPCHAT": "https://www.snapchat.com/add/{}",
    "TWITTER": "https://twitter.com/{}",
    "REDDIT": "https://www.reddit.com/user/{}",
    "YOUTUBE": "https://www.youtube.com/{}",
    "PINTEREST": "https://www.pinterest.com/{}",
    "LINKEDIN": "https://www.linkedin.com/in/{}"
}

status = {platform: {'hit': 0, 'bad': 0} for platform in platforms}

def generate_username(type_id):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    all_chars = letters + digits

    if type_id == 1:
        return ''.join(random.choices(all_chars, k=4)).upper()

    elif type_id == 2:
        base = ''.join(random.choices(all_chars, k=2))
        return base + base

    elif type_id == 3:
        return ''.join(random.choices(all_chars, k=3))

    elif type_id == 4:
        return ''.join(random.choices(all_chars, k=4))

    elif type_id == 5:
        first_two = ''.join(random.choices(all_chars, k=2))
        third = random.choice(all_chars)
        fourth = random.choice(digits)
        return first_two + first_two[0] + third + fourth

    elif type_id == 6:
        first_three = ''.join(random.choices(all_chars, k=3))
        last_three = ''.join(random.choices(all_chars, k=3))
        return first_three + last_three

    elif type_id == 7:
        first_four = ''.join(random.choices(all_chars, k=4))
        last_three = ''.join(random.choices(all_chars, k=3))
        return first_four + last_three

    elif type_id == 8:
        return ''.join(random.sample(all_chars, 5))

    elif type_id == 9:
        return ''.join(random.sample(all_chars, 6))

    elif type_id == 10:
        return ''.join(random.choices(all_chars, k=3))

    elif type_id == 11:
        return ''.join(random.choices(all_chars, k=5))

    elif type_id == 12:
        return ''.join(random.choices(all_chars, k=6))

def animated_title():
    title = "TOMAS USERNAME SCANNER\nBy:@K_DKP✓"
    for i in range(3):
        os.system('clear' if os.name != 'nt' else 'cls')
        print(YELLOW + "=" * 40 + RESET)
        print(' ' * i + CYAN + title + RESET)
        print(YELLOW + "=" * 40 + RESET)
        time.sleep(0.3)

def main_interface_colored(token, ID):
    os.system('clear' if os.name != 'nt' else 'cls')
    print(YELLOW + "=" * 40 + RESET)
    print(CYAN + "         TOMAS TOOL\n By:@K_DKP             " + RESET)
    print(YELLOW + "=" * 40 + RESET)
    print(f"TOKEN  : [ {MAGENTA}{token}{RESET} ]")
    print(f"ID : [ {MAGENTA}{ID}{RESET} ]\n")

    for platform in platforms:
        hit = f"{GREEN}{status[platform]['hit']}{RESET}"
        bad = f"{RED}{status[platform]['bad']}{RESET}"
        print(f"[ {platform:<10}] HIT: {hit:<3} | BAD: {bad:<3}")

    print(YELLOW + "-" * 37 + RESET)

def check_username(platform, username):
    url = platforms[platform].format(username)
    try:
        resp = requests.get(url, timeout=6)
        if resp.status_code == 200:
            return False
        elif resp.status_code == 404:
            return True
        else:
            return False
    except:
        return False

def send_to_telegram(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    try:
        requests.post(url, data=data, timeout=5)
    except:
        pass

def main():
    token = input("TOKEN: ")
    ID = input("ID: ")

    print("1 - Quadruple")
    print("2 - Repeated Quadruple")
    print("3 - Triple")
    print("4 - Distinct Quadruple")
    print("5 - Repeated Quintuple")
    print("6 - Sextuple")
    print("7 - Septuple")
    print("8 - Distinct Quintuple")
    print("9 - Distinct Sextuple")
    print("10 - Distinct Triple")
    print("11 - Quintuple")
    print("12 - Sextuple")

    while True:
        try:
            type_id = int(input("Enter: "))
            if 1 <= type_id <= 12:
                break
            else:
                print("Choose a valid option")
        except:
            print("Invalid input.")

    animated_title()

    while True:
        username = generate_username(type_id)
        for platform in platforms:
            exists = check_username(platform, username)
            if exists:
                status[platform]['hit'] += 1
                message = f"Available username on {platform}\nUsername: {username}\nBy:@K_DKP"
                send_to_telegram(token, ID, message)
                print(f"{GREEN}[HIT]{RESET} {platform} Username : {username}")
            else:
                status[platform]['bad'] += 1
                print(f"{RED}[BAD]{RESET} {platform} Username : {username}")
        main_interface_colored(token, ID)
        time.sleep(1)

if __name__ == "__main__":
    main()