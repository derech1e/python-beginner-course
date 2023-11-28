class Auto:
    def __init__(self, km, marke, baujahr, farbe, reifen):
        self.km = km
        self.marke = marke
        self.baujahr = baujahr
        self.farbe = farbe
        self.reifen = reifen

    def ausgabe(self):
        print(f"Das Auto von {self.marke} hat die Farbe {self.farbe}.")


class VW(Auto):
    def __init__(self, km, lampen):
        super().__init__(km, "VW", 2002, "Blau", 4)
        self.lampen = lampen

    def ausgabe(self):
        print(f"Das Auto hat {self.km}km auf dem Buckel.")

    def ausgabe_lampen(self):
        print(f"Das Auto hat {self.lampen} Lampen.")


vw = VW(10, 2)
vw.ausgabe_lampen()
vw.ausgabe()
