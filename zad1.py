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
