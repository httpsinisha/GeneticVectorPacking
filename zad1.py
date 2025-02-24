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
        resenje = []
        
        for stavka in stavke:
            dodato = False
            for bin in resenje:
                if validan_bin(bin + [stavka], dimenzije):
                    bin.append(stavka)
                    dodato = True
                    break
            if not dodato:
                resenje.append([stavka])
        
        populacija.append(resenje)
    
    return populacija

def fitness(rjesenje, dimenzije=2):
    broj_binova = len(resenje)
    
    ukupno_praznog_prostora = 0
    for bin in rjesenje:
        popunjenost = [sum(stavka[i] for stavka in bin) for i in range(dimenzije)]
        preostalo = sum(1 - p for p in popunjenost) 
        ukupno_praznog_prostora += preostalo

    return broj_binova + (ukupno_praznog_prostora / (len(resenje) * dimenzije))


def turnirska_selekcija(populacija, velicina_turnira=3):
    najbolji = None
    for _ in range(velicina_turnira):
        kandidat = random.choice(populacija)
        if najbolji is None or fitness(kandidat) < fitness(najbolji):  # manji fitness je bolji
            najbolji = kandidat
    return najbolji


if __name__ == "__main__":
    stavke = [
        (0.7, 0.2), (0.6, 0.3), (0.5, 0.5), (0.4, 0.6), (0.3, 0.7),
        (0.8, 0.1), (0.2, 0.9), (0.1, 0.8), (0.6, 0.4), (0.9, 0.2)
    ]
    
    populacija = generisi_slucajnu_populaciju(stavke, dimenzije=2, velicina_populacije=10)

    print("Populacija prije selekcije:")
    for i, resenje in enumerate(populacija):
        print(f"Rjesenje {i+1}: {resenje}, Fitness: {fitness(resenje)}")

    najbolji = turnirska_selekcija(populacija)
    print("\nNajbolje rjesenje poslije selekcije:", najbolji, "Fitness:", fitness(najbolji))

