class Yatzy:
    
    @staticmethod
    def chance(*dices): # refactorizado, permite introducir multiples valores a la función, no esta definida la cantidad de valores de entrada.
        score = 0   # cambio de nombres de variables, total por score, y d's, por dice(dado en inglés).
        for dice in dices:
            score += dice
        return score

    @staticmethod
    def yatzy(*dices):
        if dices.count(dices[0]) != len(dices): # refactorizado, permite introducir multiples valores a la función, no esta definida la cantidad de valores de entrada.
            return 0    # comprueba si todos los valores de entrada son iguales, si estos lo son devuelve 50 de puntuación.
        return 50

    @staticmethod
    def ones(*dices): # refactorizado.
        score = 0
        for dice in dices:
            if (dice ==1):
                score += 1
        return score


    @staticmethod
    def twos(*dices): # refactorizado*.
        score = 0
        for dice in dices:
            if (dice ==2):
                score += 2
        return score

    @staticmethod
    def threes(*dices): # refactorizado*.
        score = 0
        for dice in dices:
            if (dice == 3):
                score += 3
        return score

    @staticmethod
    def fours(*dices): # refactorizado*.
        score = 0
        for dice in dices:
            if (dice == 4):
                score += 4
        return score

    @staticmethod
    def fives(*dices): # refactorizado*.
        score = 0
        for dice in dices:
            if (dice == 5):
                score += 5
        return score

    @staticmethod
    def sixes(*dices): # refactorizado*.
        score = 0
        for dice in dices:
            if (dice == 6):
                score += 6
        return score


    @staticmethod
    def one_pair(*dices):
        PAIR = 2    # refactorizado, permite introducir multiples valores a la función, no esta definida la cantidad de valores de entrada.
        ordered_dices = sorted(dices, reverse=True) # El nuevo algoritmo ordena los valores de entrada de forma descendiente, y guarda la lista ordenada en una variable,
        for dice in ordered_dices:  # Se recorre cada valor de la variable que contiene la tupla ordenada.
            if ordered_dices.count(dice) >= 2: # Si el valor aparece 2 o mas veces se devuelve el valor de esa pareja.
                return dice * PAIR # La constante PAIR, contiene el valor de una pareja (2).
        return 0

    @staticmethod
    def two_pair(*dices):
        PAIR = 2    # refactorizado, permite introducir multiples valores a la función, no esta definida la cantidad de valores de entrada.
        ordered_dices = sorted(dices, reverse=True) # El nuevo algoritmo funciona con una lògica reciclada del metodo anterior (one_pair), pero en este caso añadiendo,
        score = 0 # una variable que almacena las parejas, si estas llegan a 2 devolvera el respectivo valor
        pairs = 0
        last_dice = 0
        for dice in ordered_dices:
            if ordered_dices.count(dice) >= 2 and dice != last_dice:
                pairs += 1
                last_dice = dice
                score += PAIR * dice
            if pairs == 2:
                return score
        return 0

    @staticmethod
    def four_of_a_kind( _1,  _2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[_1-1] += 1
        tallies[_2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i+1) * 4
        return 0


    @staticmethod
    def three_of_a_kind( d1,  d2,  d3,  d4,  d5):
        t = [0]*6
        t[d1-1] += 1
        t[d2-1] += 1
        t[d3-1] += 1
        t[d4-1] += 1
        t[d5-1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i+1) * 3
        return 0


    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0


    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0


    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i+1


        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i+1


        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
