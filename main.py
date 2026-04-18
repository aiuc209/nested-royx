def hisobla(royxat):
    natija = []
    for ichki_roxyat in royxat:
        kvadratlar = [element ** 2 for element in ichki_roxyat]
        ortacha = sum(kvadratlar) / len(kvadratlar)
        natija.append(ortacha)
    return natija

roxyat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(hisobla(roxyat))
