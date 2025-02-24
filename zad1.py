import random

def validan_bin(bin, dimenzije=2):
    zbir = [0] * dimenzije
    for stavka in bin:
        for i in range(dimenzije):
            zbir[i] += stavka[i]
    return all(z <= 1 for z in zbir)

# Test
bin_test = [(0.3, 0.4), (0.5, 0.2)]  # (0.8, 0.6) - validno
print(validan_bin(bin_test))  # vratice True

bin_test2 = [(0.4, 0.6), (0.7, 0.5)]  # (1.1, 1.1) - nije validno
print(validan_bin(bin_test2))  # vraca False


def generisi_slucajnu_populaciju(stavke, dimenzije=2, velicina_populacije=10):
    populacija = []
    
    for _ in range(velicina_populacije):
        random.shuffle(stavke)
        rjesenje = []
        
        for stavka in stavke:
            dodato = False
            for bin in rjesenje:
                if validan_bin(bin + [stavka], dimenzije):
                    bin.append(stavka)
                    dodato = True
                    break
            if not dodato:
                rjesenje.append([stavka])
        
        populacija.append(rjesenje)
    
    return populacija

def fitness(rjesenje, dimenzije=2):
    broj_binova = len(rjesenje)
    
    ukupno_praznog_prostora = 0
    for bin in rjesenje:
        popunjenost = [sum(stavka[i] for stavka in bin) for i in range(dimenzije)]
        preostalo = sum(1 - p for p in popunjenost) 
        ukupno_praznog_prostora += preostalo

    return broj_binova + (ukupno_praznog_prostora / (len(rjesenje) * dimenzije))


def turnirska_selekcija(populacija, velicina_turnira=3):
    najbolji = None
    for _ in range(velicina_turnira):
        kandidat = random.choice(populacija)
        if najbolji is None or fitness(kandidat) < fitness(najbolji):  # manji fitness je bolji
            najbolji = kandidat
    return najbolji



def crossover(roditelj1, roditelj2, dimenzije=2):
    sve_stavke = set(stavka for bin in roditelj1 + roditelj2 for stavka in bin)
    stavke_lista = list(sve_stavke)
    
    random.shuffle(stavke_lista)
    dete = []
    for stavka in stavke_lista:
        dodato = False
        for bin in dete:
            if validan_bin(bin + [stavka], dimenzije):
                bin.append(stavka)
                dodato = True
                break
        if not dodato:
            dete.append([stavka])
    
    return dete




if __name__ == "__main__":
    stavke = [
        (0.7, 0.2), (0.6, 0.3), (0.5, 0.5), (0.4, 0.6), (0.3, 0.7),
        (0.8, 0.1), (0.2, 0.9), (0.1, 0.8), (0.6, 0.4), (0.9, 0.2)
    ]

    populacija = generisi_slucajnu_populaciju(stavke, dimenzije=2, velicina_populacije=10)

    roditelj1 = turnirska_selekcija(populacija)
    roditelj2 = turnirska_selekcija(populacija)

    print("\nRoditelj 1:", roditelj1, "Fitness:", fitness(roditelj1))
    print("Roditelj 2:", roditelj2, "Fitness:", fitness(roditelj2))

    dijete = crossover(roditelj1, roditelj2)
    print("\nDijete nakon crossovera:", dijete, "Fitness:", fitness(dijete))

