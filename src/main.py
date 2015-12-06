iš sudoku_lenta reikalinga SudokuLenta
iš taisykles reikalingas Sprendėjas
iš spausdintojas reikalingas Spausdintojas


tai main():
    matrica= ([[1, 5, 0,   0, 0, 7,   8, 0, 0],
               [0, 0, 0,   0, 4, 0,   0, 9, 0],
               [0, 0, 0,   0, 0, 0,   0, 0, 6],
               
               [0, 0, 0,   0, 0, 3,   1, 0, 0],
               [0, 0, 9,   0, 8, 0,   3, 0, 0],
               [0, 0, 4,   5, 0, 0,   0, 0, 0],
               
               [5, 0, 0,   0, 0, 0,   0, 0, 0],
               [0, 8, 0,   0, 6, 0,   0, 0, 0],
               [0, 0, 6,   2, 0, 0,   0, 3, 9]   ])

    sudoku = SudokuLenta(matrica)

    Spausdintojas.spausdink(sudoku)

    sprendėjas = Sprendėjas(sudoku)       
    sprendėjas.išspręsk()
    
    Spausdintojas.spausdink(sudoku)
    Spausdintojas.spausdink(sprendėjas.statistika)


jeigu __name__ == '__main__':
    main()
    
    
