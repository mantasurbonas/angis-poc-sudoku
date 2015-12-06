iš sudoku_lenta reikalinga SudokuLenta
iš taisykles reikalingas Sprendėjas


klasė Spausdintojas:

    @staticmethod
    tai spausdinkSudokuLentą(lenta):
        res = ""
        imk eilnr iš intervalo (0, 9):
            imk stulpnr iš intervalo (0, 9):
                l = lenta.langeliai[eilnr, stulpnr]
                jeigu l.yraSprendimas():
                    res += "  " + str(l.sprendimas) + "  "
                kituatveju:
                    res += " (" +str(len(l.kandidatai)) +") "
            res += "\n"

        rašyk(res)


    @staticmethod
    tai spausdinkStatistiką(stat):
        rašyk ("išspręsta per", stat.iteracija, "iteracijų")
        rašyk ("truko", stat.trukmė * 1000, "msec")


    @staticmethod
    tai spausdink(kažkas):
        jeigu isinstance(kažkas, SudokuLenta ):
            Spausdintojas.spausdinkSudokuLentą(kažkas)
        ojeigu isinstance(kažkas, Sprendėjas.Statistika ):
            Spausdintojas.spausdinkStatistiką(kažkas)
        kituatveju:
            rašyk(kažkas)
            

