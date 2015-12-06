iš langelis reikalingas Langelis
iš regionas reikalingas Regionas, Linija, Kvadratas
iš taisykles reikalingas Sprendėjas


klasė SudokuLenta:
    
    tai __init__(šis, matrica):
        šis.langeliai = {}    # žodynas (eil,stulp)=>langelis
        šis.eilutės = []      # eilutės[0] reiškia pirmąją eilutę ir t.t
        šis.stulpeliai = []   # stulpeliai[0] reiškia pirmąjį stulpelį ir t.t  
        šis.kvadratai = []    # kvadratai numeruojami nuo 0 (virš. kair) iki 8 (apačioj dešinėj)
        
        eilnr = 0
        imk eil iš matrica:
            stulpnr = 0
            imk sk iš eil:
                šis.langeliai[eilnr, stulpnr] = Langelis(sk, eilnr, stulpnr)
                stulpnr += 1
            eilnr += 1
        
        imk eil iš intervalo (0, 9):
            langeliai = [l imk l iš šis.duokEilutėsLangelius(eil)]
            šis.eilutės.append( Linija(langeliai, eilutė = eil) )
            
        imk stulp iš intervalo (0, 9):
            langeliai = [l imk l iš šis.duokStulpelioLangelius(stulp)]
            šis.stulpeliai.append( Linija(langeliai, stulpelis = stulp) )
            
        imk kv iš intervalo (0,9):
            langeliai = [l imk l iš šis.duokKvadratoLangelius(kv)]
            šis.kvadratai.append( Kvadratas (langeliai, kv) )

            
    tai duokEilutėsLangelius(šis, eilnr):
        imk stulp iš intervalo (0, 9):
            duok šis.langeliai[eilnr, stulp]
            
            
    tai duokStulpelioLangelius(šis, stulp):
        imk eilnr iš intervalo (0, 9):
          duok šis.langeliai[eilnr, stulp]

            
    tai duokKvadratoLangelius(šis, kvnr):
        e_nuo, e_iki, st_nuo, st_iki = Kvadratas.ribos(kvnr)
        
        imk eil iš intervalo (e_nuo, e_iki+1):
            imk stulp iš intervalo ( st_nuo, st_iki+1):
                duok šis.langeliai[eil, stulp]
