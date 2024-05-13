class Versenyzo:
    def __init__(self, sor:str):
        text = sor.strip().split(";")
        self.nev = text[0]
        self.nemzet = self.nemzet_monogram(text[1])
        self.rovidp = float(text[2].replace(",","."))
        self.szabadp = float(text[3].replace(",","."))
        self.osszp = self.rovidp + self.szabadp

    def nemzet_monogram(self, szoveg: str) -> str:
        monogram = ""
        for b in szoveg[-4:-1]:
            monogram += b

        return monogram