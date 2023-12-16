class Fractie:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f"{self.numarator}/{self.numitor}"

    def __add__(self, other):
        rez_numarator = self.numarator * other.numitor + other.numarator * self.numitor
        rez_numitor = self.numitor * other.numitor
        return Fractie(rez_numarator, rez_numitor)

    def __sub__(self, other):
        rez_numarator = self.numarator * other.numitor - other.numarator * self.numitor
        rez_numitor = self.numitor * other.numitor
        return Fractie(rez_numarator, rez_numitor)

    def inverse(self):
        return Fractie(self.numitor, self.numarator)

# Exemple de utilizare:
frac1 = Fractie(1, 2)
frac2 = Fractie(1, 3)

suma = frac1 + frac2
print("Add:", suma)

diferenta = frac1 - frac2
print("Sub:", diferenta)

inversa_frac1 = frac1.inverse()
print("inverse:", inversa_frac1)
