def medidas(x):
    km = x/1000
    hm = x/100
    dam = x/10
    dm = x*10
    cm = x*100
    mm = x*1000
    print(f'{km}km\n{hm}hm\n{dam}dam\n{dm}dm\n{cm}cm\n{mm}mm')

if __name__ == '__main__':

    x = int(input('Insira uma distancia em metros: '))
    medidas(x)