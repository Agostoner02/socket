#!/usr/bin/env python3

import socket
#lasciando il campo vuoto sarebbe la stessa cosa(localhost)
SERVER_ADDRESS = '127.0.0.1'
#numero di porta, deve essere >1024 perchè le altre sono riservate
SERVER_PORT = 22224

#la funzione avva_server crea un endpoint di ascolto(sock:list) dal quale accettare cinnessioni in entrata
#la socket di ascolto viene passata alla funzione ricevi_comandi la quale accetta richieste di connessione
#e per ognuno crea una socket per i dati(sock_service) da cui ricevere le richieste e inviare le risposte

def inviaComandi(socket):
    while True:
        try:
            dati = input(
                "Inserisci i dati dell'operazione (ko per terminare la connessione): ")
        except EOFError:
            print("\nOkay. Exit")
            break
        if not dati:
            print("Non puoi inviare una stringa vuota!")
            continue
        if dati == 'ko':
            print("Chiudo la connessione con il server!")
            break

        dati = dati.encode()

        socket.send(dati)

        dati = socket.recv(2048)

        if not dati:
            print("Server non risponde. Exit")
            break

        dati = dati.decode()

        print("Ricevuto dal server:")
        print(dati + '\n')


def connessioneServer(address, port):
    sock_service = socket.socket()
    sock_service.connect((address, port))
    print("Connesso a " + str((address, port)))
    inviaComandi(sock_service)
    sock_service.close()


if __name__ == "__main__":
    connessioneServer(SERVER_ADDRESS, SERVER_PORT)
