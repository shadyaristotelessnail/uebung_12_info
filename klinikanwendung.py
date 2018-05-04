# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 22:02:01 2018

@author: wieczore
"""

from klinikverwaltung import Patient, Klinik


meineKlinik = Klinik("Schwarzwaldklinik") # Ein Klinik-Objekt wird erstellt.
print(Patient.anzahlPatienten)
meineKlinik.loadPatienten("patienten.txt")
print("patienten geladen")

while True:
    try:
        x = int(input("Was möchten Sie tun? 1 für Patient erstellen und zur Klinik hinzufügen, 2 für Patienten anzeigen, 3 für Patient entfernen." ))
        if x ==1:
            derName=input("Bitte Namen des Patienten: ")
            mOderw=input("Bitte Geschlecht des Patienten: ")
            krKasse=input("Bitte Krankenkasse des Patienten: ")
            neuerPatient = Patient(derName,mOderw,krKasse)#Patientenobjekt erstellen und 
            meineKlinik.addPatient(neuerPatient)#zum oben erstellten Klinikobjekt hinzufügen
        elif x==2:
            meineKlinik.zeigePatienten()
        elif x==3:
            dieID=input("Bitte eine Patienten-ID eingeben")
            meineKlinik.removePatient(dieID)
        else:
            raise ValueError
        
    except ValueError:
        input("Sie haben eine falsche Eingabe getätigt. Für weiter bitte Enter")