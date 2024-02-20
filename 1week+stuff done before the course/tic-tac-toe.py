a1 = ' '
a2 = ' ' 
a3 = ' '
b1 = ' '
b2 = ' '
b3 = ' '
c1 = ' '
c2 = ' '
c3 = ' '



def write_square(square, value):
    squares_globales = globals()
    squares_globales[square] = value



print(f'''  

        A    1    2    3
            {a1}   |{a2}   |{a3}
            ____|____|____
        B   {b1}   |{b2}   |{b3}
            ____|____|____
            {c1}   |{c2}   |{c3}
        C       |    |
''')

game_over = False

while game_over == False:
    square = input('Enter coordinates: ')
    value = input('Choose X or O: ')
    
    write_square(square, value)

    print(f'''  

        A    1    2    3
            {a1}   |{a2}   |{a3}
            ____|____|____
        B   {b1}   |{b2}   |{b3}
            ____|____|____
            {c1}   |{c2}   |{c3}
        C       |    |
''')


    winning_conditions = [
        [(a1, a2, a3), 'A'],
        [(b1, b2, b3), 'B'],
        [(c1, c2, c3), 'C'],
        [(a1, b2, c3), 'A'],
        [(c1, b2, a3), 'C'],
        [(a1, b1, c1), '1'],
        [(a2, b2, c2), '2'],
        [(a3, b3, c3), '3']
    ]

    for condition, player in winning_conditions:
        if all(square == 'x' for square in condition) or all(square == 'o' for square in condition):
            print(f'player {player} won!')
            game_over = True
            break
