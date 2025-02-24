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

def fitness(rjesenje):
    total_weight = 0
    for bin in rjesenje:
        total_weight += sum([stavka[0] for stavka in bin])  # Pretpostavljamo da je stavka tuple (težina, vrednost)
    return total_weight


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
    dijete = []
    for stavka in stavke_lista:
        dodato = False
        for bin in dijete:
            if validan_bin(bin + [stavka], dimenzije):
                bin.append(stavka)
                dodato = True
                break
        if not dodato:
            dijete.append([stavka])
    
    return dijete


def mutacija(rjesenje, dimenzije=2):
    bin_indeks = random.randint(0, len(rjesenje) - 1)
    if len(rjesenje[bin_indeks]) <= 1:
        return rjesenje

    stavka_indeks = random.randint(0, len(rjesenje[bin_indeks]) - 1)
    stavka = rjesenje[bin_indeks][stavka_indeks]
    
    drugi_bin_indeks = random.randint(0, len(rjesenje) - 1)
    
    rjesenje[bin_indeks].remove(stavka)
    if validan_bin(rjesenje[drugi_bin_indeks] + [stavka], dimenzije):
        rjesenje[drugi_bin_indeks].append(stavka)
    else:
        rjesenje[bin_indeks].append(stavka)
    
    return rjesenje


def evolucija(populacija, dimenzije=2, verovatnoca_mutacije=0.1):
    nova_populacija = []
    
    # Selekcija, crossover i mutacija za svaku generaciju
    while len(nova_populacija) < len(populacija):
        roditelj1 = turnirska_selekcija(populacija)
        roditelj2 = turnirska_selekcija(populacija)
        
        # Crossover
        dijete = crossover(roditelj1, roditelj2)
        
        # Mutacija sa verovatnoćom
        if random.random() < verovatnoca_mutacije:
            dijete = mutacija(dijete, dimenzije)
        
        nova_populacija.append(dijete)
    
    return nova_populacija


if __name__ == "__main__":
    stavke = [
        (0.7, 0.2), (0.6, 0.3), (0.5, 0.5), (0.4, 0.6), (0.3, 0.7),
        (0.8, 0.1), (0.2, 0.9), (0.1, 0.8), (0.6, 0.4), (0.9, 0.2)
    ]

    populacija = generisi_slucajnu_populaciju(stavke, dimenzije=2, velicina_populacije=10)

    #evolucija za 100 generacija
    for generacija in range(100):
        populacija = evolucija(populacija, dimenzije=2, verovatnoca_mutacije=0.1)
    
        najbolje_rjesenje = min(populacija, key=lambda r: fitness(r))
        print(f"Generacija {generacija + 1} - Najbolje rjesenje fitness: {fitness(najbolje_rjesenje)}")

