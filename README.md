Evolucioni Algoritam za Optimizaciju Pakovanja

Ovaj projekat implementira evolucioni algoritam za rješavanje problema pakovanja, gdje je cilj da se stavke (sastavljene od težine i vrijednosti) rasporede u nekoliko binova uz poštovanje ograničenja na zbir težina u svakom binu.

Sadržaj
Opis projekta
Kako koristiti
Funkcionalnosti
Struktura koda
Licenca
Opis projekta
Cilj ovog projekta je implementacija evolucionog algoritma za optimizaciju pakovanja. Svaka stavka je predstavljena kao tuple (težina, vrijednost) i mora biti raspoređena u odgovarajuće "binove". Iako se težina stavki mora poštovati, algoritam također omogućava da se stavke grupišu tako da zbir težina u svakom binu ne pređe određeni prag.

Algoritam
Algoritam koristi sljedeće korake:

Generisanje inicijalne populacije: Početna populacija se generiše nasumično, pri čemu se stavke raspoređuju u binove uz poštovanje validnosti.
Selektovanje roditelja: Korišćenjem turnirske selekcije, iz populacije se odabiru dva roditelja.
Crossover: Kombinovanjem roditelja nastaje novo rješenje (dijete).
Mutacija: S povremenom vjerojatnošću, rješenje može biti mutirano kako bi se povećala raznovrsnost.
Evolucija: Ovi procesi se ponavljaju kroz više generacija kako bi se postigao optimalni raspored stavki.

Kako koristiti
Kloniranje repozitorija: Da bi započeo rad sa projektom, prvo kloniraj repozitorij na svoj računar:
git clone https://github.com/httpsinisha/GeneticVectorPacking.git

Pokretanje koda: Nakon što je repozitorij preuzet, možeš da pokreneš kod direktno koristeći Python 3:
python evolucioni_algoritam.py

U skripti se generiše početna populacija sa nasumičnim stavkama i izvršava se evolucija kroz 100 generacija. Rezultati najboljeg rješenja za svaku generaciju biće ispisani u terminalu.

Funkcionalnosti
Generisanje populacije: Nasumično kreiranje inicijalnih rješenja koja zadovoljavaju sve uvjete pakovanja.
Selektovanje roditelja: Turnirska selekcija sa n-tim brojem kandidata.
Crossover operacija: Kombinovanje roditeljskih rješenja u jedno novo rješenje.
Mutacija: Slučajna mutacija koja mijenja raspored stavki.
Evolucija: Provođenje evolucionog procesa kroz više generacija.
Fitness funkcija: Izračunavanje fitness vrijednosti svakog rješenja prema ukupnoj težini stavki.

Struktura koda

evolucioni_algoritam.py: Glavni skript koji implementira sve ključne funkcionalnosti evolucionog algoritma, uključujući generisanje populacije, selekciju, crossover, mutaciju i evoluciju.

readme.md: Ovaj dokument koji objašnjava kako koristiti projekat.

Licenca

Ovaj projekat je licenciran pod MIT licencom.
