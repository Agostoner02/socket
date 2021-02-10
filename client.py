#!/usr/bin/env python3

import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

#la funzione riceve la socket connessa al server e la utilizza per richiedere il servizio
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

#la funzione crea una socket (s) per la connessione con il server e la passa alla funzione invia_comandi(s)
def connessioneServer(address, port):
    sock_service = socket.socket()
    sock_service.connect((address, port))
    print("Connesso a " + str((address, port)))
    inviaComandi(sock_service)
    sock_service.close()


if __name__ == "__main__":
    connessioneServer(SERVER_ADDRESS, SERVER_PORT)

    #if __name__ == '__main__': consente al nostro codice di capire se stia venendo eseguito come script a se stante,
    #o se è invece stato richiamato come modulo da un qualche programma per usare una o più delle sua varie
    #funzioni e classi
