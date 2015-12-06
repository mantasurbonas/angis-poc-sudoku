iš konstantos reikalinga *
iš langelis reikalingas Langelis

klasė Regionas:
   
    tai __init__(šis, langeliai):
        šis._langeliai = langeliai[:]
                
        šis._žinomosReikšmės = {l.sprendimas imk l iš langeliai jei l.yraSprendimas() }
        šis._trūkstamosReikšmės = šis._žinomosReikšmės ^ Langelis.GALIMOS_REIKŠMĖS
        
        šis._tuštiLangeliai = [l imk l iš langeliai jei l.yraSprendimas()==Netiesa]
        
                
    @property
    tai trūkstamosReikšmės(šis):
        grąžink frozenset(šis._trūkstamosReikšmės)
        
        
    @property
    tai žinomosReikšmės(šis):
        grąžink frozenset(šis._žinomosReikšmės)
        
        
    @property
    tai tuštiLangeliai(šis):
        grąžink frozenset(šis._tuštiLangeliai)
        
        
    tai yraIšspręstas(šis):
        grąžink len(šis._tuštiLangeliai) == 0    
    
    
    tai langeliaiSuKandidatu(šis, sk):
        grąžink { x imk x iš šis._tuštiLangeliai jeigu sk iš x.kandidatai }
    
        
    tai turiLangelįIš(šis, langeliai):
        imk l iš langeliai:
            jei l iš šis._langeliai:
                grąžink Tiesa
        grąžink Netiesa
    
        
    tai peržiūrėkLangelius(šis):
        rezultatas = Nepakeista
        
        imk l iš šis._tuštiLangeliai[:] :
            jei l.yraSprendimas():
                šis._tuštiLangeliai.remove(l)
                šis._trūkstamosReikšmės.remove(l.sprendimas)
                šis._žinomosReikšmės.add(l.sprendimas)
                rezultatas = Pakeista
                
        grąžink rezultatas
       
    
klasė Linija(Regionas):

    tai __init__(šis, langeliai, eilutė=-1, stulpelis=-1):
        šis.eilutė    = eilutė
        šis.stulpelis = stulpelis
        
        super().__init__(langeliai)        
        
        
klasė Kvadratas(Regionas):
    
    @staticmethod
    tai ribos(kvadrato_numeris):
        eilutėNuo = svskaičius ((kvadrato_numeris / 3)) * 3
        eilutėIki = eilutėNuo + 2
         
        stulpelisNuo = (kvadrato_numeris % 3) * 3
        stulpelisIki = stulpelisNuo + 2        
        
        grąžink eilutėNuo, eilutėIki, stulpelisNuo, stulpelisIki
        
    
    tai __init__(šis, langeliai, numeris):      
        super().__init__(langeliai)
        
        šis.numeris = numeris
            
        
