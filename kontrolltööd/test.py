class Raamat:
    riik = "Eesti"  # Klassimuutuja

    def __init__(self, pealkiri, autor, lehekylgede_arv):
        self.pealkiri = pealkiri
        self.autor = autor
        self.lehekylgede_arv = lehekylgede_arv

    def kirjelda(self):
        return f"'{self.pealkiri}' on raamat, mille on kirjutanud {self.autor}. Raamatus on {self.lehekylgede_arv} lehekülge."

    def on_pikk(self):
        return self.lehekylgede_arv > 300

# Näide klassi kasutamisest (saab test.py failis)
# raamat1 = Raamat("Kevad", "Oskar Luts", 288)
# print(raamat1.kirjelda())
# print(f"Kas raamat on pikk? {raamat1.on_pikk()}")
# print(f"Raamatu päritoluriik: {Raamat.riik}")

# jarjend.py

import random

objektid = []

for _ in range(60):
    pealkiri = f"Raamat {_ + 1}"
    autor = f"Autor {random.randint(1, 10)}"
    lehekylgede_arv = random.randint(50, 500)
    objektid.append(Raamat(pealkiri, autor, lehekylgede_arv))

# Kasutame meetodit kõigi objektide peal
print("\n--- Kõigi objektide tutvustus ---")
for objekt in objektid:
    if isinstance(objekt, Raamat):
        print(objekt.kirjelda())