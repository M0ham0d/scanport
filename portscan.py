from pyfiglet import Figlet

f = Figlet(font='ascii___')

def DrawText(text):
    return f.renderText(text)

print(DrawText("mr_hack"))
print(DrawText("scan"))

import socket
host = input("please enter the ip address: ")
try:
    for port in range(1,2000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((host,port))
        if result == 0:
            print("the port {} is open.".format(port))
except:
    print("Error")