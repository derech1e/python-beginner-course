from Fahrzeuge import *


class Autohaus():

    def __init__(self):
        self.ankaufsliste = []

    def ankauf(self, fahrzeug):
        self.ankaufsliste.append(fahrzeug)

    def verkauf(self, idx):
        return self.ankaufsliste.pop(idx)

    def zeige_alle(self):
        for item in self.ankaufsliste:
            print(f"Id: {self.ankaufsliste.index(item)} Info: {item.info()}")

    def statistik(self):
        anz_auto = 0
        anz_mot = 0
        insg_preis = 0
        for item in self.ankaufsliste:
            if item.__class__.__name__ == "Auto": # Check if the class name of the object matches the auto's one
                anz_auto += 1
            else:
                anz_mot += 1
            insg_preis += item.preis

        print(f"Betsand:\n Autos:{anz_auto}\tMotorräder:{anz_mot}\n\nLagerwert:{insg_preis}€")


autohaus = Autohaus()

autohaus.ankauf(Motorrad(True, 20, "BMW", "Schlecht", 2000, 10, 5))
autohaus.ankauf(Motorrad(4, 20, "BMW", "Schlecht", 2000, 10, 6))
autohaus.ankauf(Auto(4, 5, "VW", "Test", 2000, 8787, 99))

autohaus.zeige_alle()
print("------------------")
autohaus.statistik()
