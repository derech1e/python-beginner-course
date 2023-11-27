import random


class Konto:

    def __init__(self, name):
        self.KundenNr = random.randint(1, 10000)
        self.Name = name
        self.transaktionen = []
        self.__kontostand = 300000  # Neukunden Bonus

    def ueberweisung(self, grund, betrag, empfaenger):
        self.__kontostand -= betrag
        empfaenger.kontostand += betrag
        self.transaktionen.append([grund, betrag, empfaenger])


kunde = Konto("Kunde")
autohaus = Konto("Autohaus")

kunde.ueberweisung("Porsche2069", 50000, autohaus)
print(f"{kunde.kontostand}€")  # Fehler, weil kontostand einen privaten Zugriffstyp hat
print(kunde.transaktionen)
print(autohaus.transaktionen)
