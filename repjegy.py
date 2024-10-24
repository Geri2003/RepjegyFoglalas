from abc import ABC, abstractmethod


# Absztrakt osztály a Járatokhoz
class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_info(self):
        pass


# BelföldiJárat osztály
class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def jarat_info(self):
        return f"Belföldi járat: {self.jaratszam}, célállomás: {self.celallomas}, jegyár: {self.jegyar} Ft"


# NemzetköziJárat osztály
class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def jarat_info(self):
        return f"Nemzetközi járat: {self.jaratszam}, célállomás: {self.celallomas}, jegyár: {self.jegyar} Ft"


# Légitársaság osztály
class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaadas(self, jarat):
        self.jaratok.append(jarat)

    def jaratok_listazasa(self):
        return [jarat.jarat_info() for jarat in self.jaratok]


# JegyFoglalás osztály
class JegyFoglalas:
    def __init__(self, jarat, utas_nev):
        self.jarat = jarat
        self.utas_nev = utas_nev

    def foglalas_info(self):
        return f"{self.utas_nev} foglalta a(z) {self.jarat.jarat_info()} járatot."


# Foglalási rendszer
class FoglalasiRendszer:
    def __init__(self):
        self.foglalasok = []

    def jegy_foglalas(self, jarat, utas_nev):
        foglalas = JegyFoglalas(jarat, utas_nev)
        self.foglalasok.append(foglalas)
        print(f"Jegy sikeresen lefoglalva! {foglalas.foglalas_info()}")
        return jarat.jegyar

    def foglalas_lemondas(self, utas_nev, jaratszam):
        for foglalas in self.foglalasok:
            if foglalas.utas_nev == utas_nev and foglalas.jarat.jaratszam == jaratszam:
                self.foglalasok.remove(foglalas)
                print(f"A foglalás lemondva: {utas_nev} - Járatszám: {jaratszam}")
                return True
        print(f"Nincs ilyen foglalás: {utas_nev} - Járatszám: {jaratszam}")
        return False

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            print("Nincsenek foglalások.")
        else:
            for foglalas in self.foglalasok:
                print(foglalas.foglalas_info())



if __name__ == "__main__":
    tarsasag = LegiTarsasag("RyanAir")

    # Előre definiált járatok
    jarat1 = BelfoldiJarat(555, "Budapest", 15000)
    jarat2 = NemzetkoziJarat(666, "Milánó", 50000)
    jarat3 = BelfoldiJarat(123, "Debrecen", 12000)
    jarat4 = NemzetkoziJarat(911, "Las Vegas", 120000)
    jarat5 = NemzetkoziJarat(787, "Bukarest", 15)


    # Légitársaság hozzáadása
    tarsasag.jarat_hozzaadas(jarat1)
    tarsasag.jarat_hozzaadas(jarat2)
    tarsasag.jarat_hozzaadas(jarat3)
    tarsasag.jarat_hozzaadas(jarat4)
    tarsasag.jarat_hozzaadas(jarat5)

    rendszer = FoglalasiRendszer()

    # Előre betöltött foglalások
    rendszer.jegy_foglalas(jarat1, "Szűcs Gergő")
    rendszer.jegy_foglalas(jarat2, "Jóna Laura")
    rendszer.jegy_foglalas(jarat3, "Büdös Tojás")
    rendszer.jegy_foglalas(jarat4, "Szép Lacika")
    rendszer.jegy_foglalas(jarat5, "Deák Geri")

    # Felhasználói interfész
    while True:
        print("\n1. Járatok listázása\n2. Jegy foglalása\n3. Foglalás lemondása\n4. Foglalások listázása\n5. Kilépés")
        valasztas = input("Válassz egy opciót: ")

        if valasztas == '1':
            for jarat_info in tarsasag.jaratok_listazasa():
                print(jarat_info)

        elif valasztas == '2':
            utas_nev = input("Adja meg az utas nevét: ")
            jaratszam = int(input("Adja meg a járatszámot: "))
            for jarat in tarsasag.jaratok:
                if jarat.jaratszam == jaratszam:
                    rendszer.jegy_foglalas(jarat, utas_nev)
                    break

        elif valasztas == '3':
            utas_nev = input("Adja meg az utas nevét: ")
            jaratszam = int(input("Adja meg a járatszámot: "))
            rendszer.foglalas_lemondas(utas_nev, jaratszam)

        elif valasztas == '4':
            rendszer.foglalasok_listazasa()

        elif valasztas == '5':
            break

        else:
            print("Érvénytelen választás.")
