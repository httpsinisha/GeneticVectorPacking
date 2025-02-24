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

def fitness(resenje):
    return len(resenje)  #broj binova - sto manje, to bolje


if __name__ == "__main__":
    stavke = [(0.3, 0.4), (0.5, 0.2), (0.4, 0.6), (0.2, 0.3), (0.6, 0.5)]
    
    populacija = generisi_slucajnu_populaciju(stavke, dimenzije=2, velicina_populacije=5)

    for i, resenje in enumerate(populacija):
        print(f"Rjesenje {i+1}: {resenje}, Fitness: {fitness(resenje)}")
