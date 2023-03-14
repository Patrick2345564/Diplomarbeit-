#Autor:Edelmann Patrick
#Datum der Finalisierung: 29.12.2022
#Klasse:5AHEL
# Dieses Programm erstellt einen Socket und versucht, eine Verbindung zu einem Server mit der IP-Adresse 127.0.0.1 und dem Port 23456 herzustellen.
#Wenn die Verbindung erfolgreich ist, sendet es eine Nachricht mit dem Namen des Absenders an den Server, der dann eine Antwort zurückgibt.
#Anschließend wird die Verbindung geschlossen.

import socket  # importiere das socket modul            

host = "127.0.0.1"
port = 23456
s=socket.create_connection(("localhost",port))
s.send("Hallo hier ist Patrick Edelmann von der HTL-Anichstraße 5AHEL".encode("cp850"))   # schreiben der Daten die an Server geschickt werden sollen
bytes=s.recv(1024)           # Daten die empangen werden
print("Response from server:",bytes.decode("cp850")) #empfangene Daten dekodieren und ausgeben     
s.close()                  #Verbindung wird geschlossen wenn die Übertragung dieser Nachricht beendet ist             