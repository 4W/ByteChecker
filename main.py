import requests

url = "https://api.byte.co/account/register/precheck"

def initialize():
    print("Byte Checker by 4W#2100")
    print("The first & the original one")
    print("")
    print("")
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
