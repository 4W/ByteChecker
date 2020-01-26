import requests
from colorama import Fore, Back, Style
url = "https://api.byte.co/account/register/precheck"
afile = "available.txt"
cfile = "usernames.txt"

def count():
    namecount = 0
    with open(cfile) as f:
            for namecount, l in enumerate(f):
                pass
            namecount = namecount + 1


    return namecount

def check():
    with open(cfile, "r+") as fp:
        line = fp.readline()
        checked = 0
        f= open(afile,"a+")
        f.write(f"------Session Started-------\n")
        while line:
            name = line.strip()
            data = {"username":name}
            r = requests.post(url, json=data)
            status = r.json()
            if status["success"] == 0:
                print(f"{name} [*]")
            if status["success"] == 1:
                print(f"{name} Available")
                f.write(f"{name}\n")

            line = fp.readline()
            if not line.strip():
                print("")
                print("Finished Checking ALL USERNAMES")
                f.write(f"------Session Ended-------\n")
                f.close()
                quit()


def initialize():
    print("Byte Checker by 4W#2100")
    print("The first & the original one")
    print("")
    print(f"{count()} usernames detected in usernames.txt")
    print("Press ENTER KEY to begin checking")
    input("")
    check()







if __name__ == "__main__":
    initialize()
