import requests

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
    
def check()


def initialize():
    print("Byte Checker by 4W#2100")
    print("The first & the original one")
    print("")
    print(f"{count()} usernames detected in usernames.txt")
    print("Press ENTER KEY to begin checking")
    input("")
    check()
data = {"username":"cs"}

r = requests.post(url, json=data)

status = r.json()
if status["success"] == 0:
    print("taken")
if status["success"] == 1:
    print("availablen")
print(r.text)


if __name__ == "__main__":
    initialize()
