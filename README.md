# Dos.py
Ferramenta em python para fazer ataque DoS em redes wifi.

Como funciona essa ferramenta:

Ela utiliza o comando "aireplay-ng" para fazer um ataque de desautenticação em um BSSID especifico.
Quando ela envia 5 pacotes de desautenticação, ela troca o MACADRESS para um aleatorio e envia mais 5 pacotes e faz
esse looping de trocar o MACADRESS e enviar os 5 pacotes, infinitamente, ou, até o usuario parar a execução.
