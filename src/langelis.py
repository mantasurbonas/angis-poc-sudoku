iš konstantos reikalinga *


klasė Langelis:
        
    GALIMOS_REIKŠMĖS = frozenset([1,2,3,4,5,6,7,8,9])
        
    tai __init__ (šis, reikšmė, eilutė, stulpelis):    
        šis._kandidatai = aibė()
        šis._ribojimai  = aibė()        
        
        šis._eilutė = eilutė
        šis._stulpelis = stulpelis
        
        šis.sprendimas = reikšmė


    @property
    tai sprendimas(šis):
        grąžink šis._sprendimas
        
        
    @sprendimas.setter
    tai sprendimas(šis, s):
        šis._sprendimas = s
        
        šis._ribojimai  = aibė()
        šis._kandidatai = aibė()        
        
        jeigu šis.yraSprendimas() == Netiesa:
            šis._kandidatai |= šis.GALIMOS_REIKŠMĖS
            
            
    tai yraSprendimas(šis):
        grąžink šis._sprendimas != 0
        
        
    @property
    tai kandidatai(šis):
        grąžink frozenset(šis._kandidatai)
        
            
    @property
    tai ribojimai(šis):
        grąžink frozenset(šis._ribojimai)
        
        
    tai pridėkRibojimą(šis, sk):
        jei šis.yraSprendimas():
            grąžink Nepakeista
            
        jei sk iš šis._ribojimai:
            grąžink Nepakeista
            
        šis._ribojimai |= aibė([sk])
        
        šis._kandidatai ^= aibė([sk])
        
        jei len(šis._kandidatai) == 1:
            šis.sprendimas = šis._kandidatai.pop()
            
        grąžink Pakeista
        
        
    tai pridėkRibojimų(šis, sąr):
        rez = Nepakeista
        
        imk k iš sąr:
            rez = šis.pridėkRibojimą(k) arba rez
            
        grąžink rez

    
