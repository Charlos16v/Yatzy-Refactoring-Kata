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
        ordered_dices = sorted(dices, reverse = True) # El nuevo algoritmo ordena los valores de entrada de forma descendiente, y guarda la lista ordenada en una variable,
        for dice in ordered_dices:  # Se recorre cada valor de la variable que contiene la tupla ordenada.
            if ordered_dices.count(dice) == PAIR: # Si el valor aparece 2 o mas veces se devuelve el valor de esa pareja.
                return PAIR * dice # La constante PAIR, contiene el valor de una pareja (2).
        return 0


    @staticmethod
    def two_pair(*dices):
        PAIR = 2    # refactorizado, permite introducir multiples valores a la función, no esta definida la cantidad de valores de entrada.
        ordered_dices = sorted(dices, reverse = True) # El nuevo algoritmo funciona con una lògica reciclada del metodo anterior (one_pair), pero en este caso añadiendo,
        score = 0 # una variable que almacena las parejas, si estas llegan a 2 devolvera el respectivo valor
        pairs = 0
        last_dice = 0
        for dice in ordered_dices:
            if ordered_dices.count(dice) >= PAIR and dice != last_dice:
                pairs += 1
                last_dice = dice
                score += PAIR * dice
            if pairs == 2:
                return score
        return 0


    @staticmethod
    def three_of_a_kind(*dices):
        THREE = 3   # refactorizado, permite introducir multiples valores a la función, no esta definida la cantidad de valores de entrada.
        ordered_dices = sorted(dices, reverse = True) # El nuevo algoritmo básicamente funciona con una lista ordenada de los dados, en la cual comprueba si un dado esta repetido 3 veces,
        for dice in ordered_dices:  #  si es así devuelve la puntuación, que es la operación de multiplicar de 3 por el valor del dado repetido.
            if ordered_dices.count(dice) >= THREE:
                return THREE * dice
        return 0


    @staticmethod
    def four_of_a_kind(*dices):
        FOUR = 4    # refactorizado, permite introducir multiples valores a la función, no esta definida la cantidad de valores de entrada.
        ordered_dices = sorted(dices, reverse = True) # El nuevo algoritmo básicamente funciona con una lista ordenada de los dados, en la cual comprueba si un dado esta repetido 4 veces,
        for dice in ordered_dices:  #  si es así devuelve la puntuación, que es la operación de multiplicar de 4 por el valor del dado repetido.
            if ordered_dices.count(dice) >= FOUR:
                return FOUR * dice
        return 0


    @staticmethod
    def small_straight(*dices):
        ordered_dices = sorted(dices, reverse = True)
        for dice in dices:  # refactorizado, permite introducir multiples valores a la función, no esta definida la cantidad de valores de entrada.
            if dices.count(dice) != 1 or ordered_dices[0] > 5:   # El nuevo algoritmo es más eficiente que el anterior, ya que simplemente comprueba que cada valor de entrada se encuentra una única vez y que estos son 1,2,3,4,5.
                return 0    # si no es asi, devolvera 0 de puntuación.
        return Yatzy.chance(*dices) # Si no se encuentra ningún dado único, devuelve la suma de todos los valores (chance).


    @staticmethod
    def large_straight(*dices):
        ordered_dices = sorted(dices, reverse = True)
        for dice in dices:  # refactorizado, permite introducir multiples valores a la función, no esta definida la cantidad de valores de entrada.
            if dices.count(dice) != 1 or ordered_dices[-1] < 2:   # El nuevo algoritmo es más eficiente que el anterior, ya que simplemente comprueba que cada valor de entrada se encuentra una única vez y que estos son 2,3,4,5,6.
                return 0    # si no es asi, devolvera 0 de puntuación.
        return Yatzy.chance(*dices) # Si no se encuentra ningún dado único, devuelve la suma de todos los valores (chance).


    @staticmethod
    def full_house(*dices):
        if Yatzy.one_pair(*dices) and Yatzy.three_of_a_kind(*dices):
            return Yatzy.one_pair(*dices) + Yatzy.three_of_a_kind(*dices)
        else:
            return 0
