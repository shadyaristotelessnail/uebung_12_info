
class Patient:
    
    offset= 1000
    anzahlPatienten = 0
    
    def __init__(self,einName,einGeschlecht,eineKrKasse):
        Patient.anzahlPatienten += 1
        self.name=einName
        self.krankenkasse=eineKrKasse
        self.geschlecht = einGeschlecht
        self.patientenID=str(Patient.offset) + str(Patient.anzahlPatienten) + self.geschlecht
#       input("Patientenobjekt mit ID "+self.patientenID+" erstellt! Für weiter bitte Enter")
    
    def getAnzahlPatienten( ):
        return Patient.anzahlPatienten
    
    def getID(self):
        return self.patientenID
    
    def getName(self):
        return self.name
    
    def getGeschlecht(self):
        return self.geschlecht
    
    def getKrankenkasse(self):
        return self.krankenkasse
    
    def text_init(self,einName,einGeschlecht,eineKrKasse):
        Patient.anzahlPatienten += 1
        self.name=einName
        self.krankenkasse=eineKrKasse
        self.geschlecht = einGeschlecht
        self.patientenID=str(Patient.offset) + str(Patient.anzahlPatienten) + self.geschlecht
    
class Klinik:
    
    def __init__(self,einName):
        self.name=einName
        self.patientenliste = []
        input("Klinikobjekt erstellt! Für weiter bitte Enter")
        
    def getName(self):
        return self.name
    
    def addPatient(self,einPatient):
        self.patientenliste.append(einPatient)
        input("Patient erfolgreich hinzugefügt! Für weiter bitte Enter")
     
    def textPatient(self,einPatient):
        self.patientenliste.append(einPatient)
        
        
    def zeigePatienten(self):
        for p in self.patientenliste:
            print("Name: ",p.getName(),"ID :",p.getID())
            
    def removePatient(self,eineID):
        for p in self.patientenliste:
            if p.getID()==eineID:
                self.patientenliste.remove(p)
                print("Patient entfernt")
                break
        
    def loadPatienten(self, eineDatei):
        
        textdatei= open(eineDatei, "r")
        for zeile in textdatei:
            zeile_liste= zeile.split(",")
            text_name=zeile_liste[0]
            text_gender=zeile_liste[1]
            text_krKasse=zeile_liste[2]
            print(text_name, text_gender, text_krKasse)
            text_patient=Patient(text_name, text_gender, text_krKasse)
            self.textPatient(text_patient)
            
            
            
            
            
        
    