iš regionas reikalingas Kvadratas
reikalingas time


# konstantos gražesniam kodo skaitomumui
Pritaikyta = Tiesa
Netaikyta  = Netiesa


klasė SprendimoTaisyklė:
    
    tai taikyk(šis, regionas):
        pass

    
klasė ŽinomųReikšmiųIšbraukymas (SprendimoTaisyklė):
    
    tai taikyk(šis, regionas):
        rez = Netaikyta
        imk langeli iš regionas.tuštiLangeliai:
            rez = langeli.pridėkRibojimų (regionas.žinomosReikšmės) arba rez
        grąžink rez


klasė VienintelioKandidatoRadimas (SprendimoTaisyklė):

    tai taikyk(šis, regionas):
        imk sk iš regionas.trūkstamosReikšmės:
            langeliai = regionas.langeliaiSuKandidatu(sk)   
            jei len(langeliai) == 1:
                langeliai.pop().sprendimas = sk
                grąžink Pritaikyta
                
        grąžink Netaikyta


klasė IdentiškųPorųRadimas (SprendimoTaisyklė):

    tai taikyk(šis, regionas):
        kandidatai = šis.pasikartojančiosPoros(šis.kandidatųPoros(regionas))
                   
        rez = Netaikyta

        imk pora iš kandidatai:
            langeliai = šis.langeliaiBeKandidatų(regionas.tuštiLangeliai, pora)
            rez = šis.pašalinkKandidatus(langeliai, pora) arba rez
                
        grąžink rez


    @staticmethod
    tai kandidatųPoros(regionas):
        grąžink [ x.kandidatai imk x iš regionas.tuštiLangeliai jeigu len(x.kandidatai)==2 ]
        
    @staticmethod
    tai pasikartojančiosPoros(porųSąrašas):
        grąžink { x imk x iš porųSąrašas jei porųSąrašas.count(x) == 2}
        
    @staticmethod
    tai langeliaiBeKandidatų(langeliai, kandidatai):
        grąžink { x imk x iš langeliai jeigu x.kandidatai != kandidatai }
    
    @staticmethod
    tai pašalinkKandidatus(langeliai, kandidatai):
        rez = Netaikyta
        
        imk l iš langeliai:
            rez = l.pridėkRibojimų(kandidatai) arba rez
                
        grąžink rez
        
        
klasė LinijosKvadratoSankirta (SprendimoTaisyklė):
    
    tai __init__(šis, kvadratai):
        šis._kvadratai = kvadratai

    
    tai taikyk(šis, linija):
        jeigu linija is Kvadratas:
            grąžink Netaikyta
        
        rez = Netaikyta
        
        imk kandidat iš linija.trūkstamosReikšmės:
            linijosLangeliai = linija.langeliaiSuKandidatu(kandidat)
            galimiKvadratai = šis.duokLangeliųKvadratus(šis._kvadratai, linijosLangeliai)
                
            jei len(galimiKvadratai)==1:
                kvadratas = galimiKvadratai.pop()
                atlikęLangeliai = kvadratas.tuštiLangeliai - linijosLangeliai
                rez = šis.pridėkRibojimų(atlikęLangeliai, kandidat) arba rez
                
        grąžink rez
    
        
    tai duokLangeliųKvadratus(šis, kvadratai, langeliai):
        grąžink {kv imk kv iš kvadratai jei kv.turiLangelįIš(langeliai) }   
            
            
    tai pridėkRibojimų(šis, langeliai, sk):
        rez = Netaikyta
        imk l iš langeliai:
            rez = l.pridėkRibojimą(sk) arba rez
        grąžink rez

        
klasė Sprendėjas:

    klasė Statistika:
        pass
    
    
    tai __init__(šis, sudoku):

        šis._taisyklės = [ ŽinomųReikšmiųIšbraukymas(),
                           VienintelioKandidatoRadimas(),
                           IdentiškųPorųRadimas(),
                           LinijosKvadratoSankirta(sudoku.kvadratai)]
        
        šis.sudoku = sudoku

        šis.statistika = Sprendėjas.Statistika()


    tai išspręsk(šis):
        šis.statistika.iteracija = 0

        pradžia = time.time()

        kol šis.spręsk() ir šis.statistika.iteracija < 30:
            šis.statistika.iteracija += 1

        šis.statistika.trukmė = time.time() - pradžia
            
    
    tai spręsk(šis):
        rez = Netaikyta

        imk eil iš šis.sudoku.eilutės:
            rez = šis.spręskRegioną(eil) arba rez
            
        imk stulp iš šis.sudoku.stulpeliai:
            rez = šis.spręskRegioną(stulp) arba rez
        
        imk kv iš šis.sudoku.kvadratai:
            rez = šis.spręskRegioną(kv) arba rez
            
        grąžink rez        
    
    
    tai spręskRegioną(šis, regionas):
        regionas.peržiūrėkLangelius()
        
        jei regionas.yraIšspręstas():
            grąžink Netaikyta

        imk taisyklė iš šis._taisyklės:
            jeigu taisyklė.taikyk(regionas):
                grąžink Pritaikyta
                
        grąžink Netaikyta
