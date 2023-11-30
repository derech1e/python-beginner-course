class Fahrzeug:
    def __init__(self, marke, bezeichnung, baujahr, kmstand, preis):
        self.marke = marke
        self.bezeichnung = bezeichnung
        self.baujahr = baujahr
        self.kmstand = kmstand
        self.preis = preis

    def info(self) -> str:
        pass


class Auto(Fahrzeug):
    def __init__(self, tueren, sitze, marke, bezeichnung, baujahr, kmstand, preis):
        super().__init__(marke, bezeichnung, baujahr, kmstand, preis)
        self.tueren = tueren
        self.sitze = sitze

    def info(self):
        return f"Türen: {self.tueren} \n Sitze: {self.sitze}"


class Motorrad(Fahrzeug):
    def __init__(self, windschutzscheibe, gewicht, marke, bezeichnung, baujahr, kmstand, preis):
        super().__init__(marke, bezeichnung, baujahr, kmstand, preis)
        self.windschutzscheibe = windschutzscheibe
        self.gewicht = gewicht

    def info(self):
        return f"Windschutzscheibe: {self.windschutzscheibe} \nGewicht: {self.gewicht}g"
