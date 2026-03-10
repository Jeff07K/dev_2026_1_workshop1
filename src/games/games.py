class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el ganador del juego piedra, papel o tijera.
        
        Args:
            jugador1 (str): Elección del jugador 1 ("piedra", "papel", "tijera")
            jugador2 (str): Elección del jugador 2 ("piedra", "papel", "tijera")
            
        Returns:
            str: "jugador1", "jugador2" o "empate"
            
        Reglas:
            - Piedra vence a tijera
            - Tijera vence a papel
            - Papel vence a piedra
        
        Ejemplo:
            piedra_papel_tijera("piedra", "tijera") -> "jugador1"
            piedra_papel_tijera("papel", "piedra") -> "jugador1"
            piedra_papel_tijera("tijera", "papel") -> "jugador1"
            piedra_papel_tijera("tijera", "piedra") -> "jugador2"
            piedra_papel_tijera("piedra", "papel") -> "jugador2"
            piedra_papel_tijera("papel", "tijera") -> "jugador2"
            piedra_papel_tijera("piedra", "piedra") -> "empate"
            piedra_papel_tijera("papel", "papel") -> "empate"
            piedra_p
        """
        opciones = ["piedra", "papel", "tijera"]
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()
        
        if jugador1 not in opciones or jugador2 not in opciones:
            return "invalid"
        
        if jugador1 == jugador2:
            return "empate"
        
        if (jugador1 == "piedra" and jugador2 == "tijera") or \
           (jugador1 == "papel" and jugador2 == "piedra") or \
           (jugador1 == "tijera" and jugador2 == "papel"):
            return "jugador1"
        else:
            return "jugador2"   

    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Proporciona pistas para un juego de adivinanza de números.
        
        Args:
            numero_secreto (int): El número que se debe adivinar
            intento (int): El número propuesto por el jugador
            
        Returns:
            str: "correcto", "muy alto" o "muy bajo"
        """
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"
    
    def ta_te_ti_ganador(self, tablero):
        """
        Verifica si hay un ganador en un tablero de tic-tac-toe.
        
        Args:
            tablero (list): Matriz 3x3 con valores "X", "O" o " " (espacio vacío)
            
        Returns:
            str: "X", "O", "empate" o "continua"
            
        Ejemplo:
            [["X", "X", "X"],
             ["O", "O", " "],
             [" ", " ", " "]] -> "X"
        """
        # Verificar filas
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] != " ":
             return fila[0]

         # revisar columnas
        for col in range(3):
         if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != " ":
            return tablero[0][col]

        # revisar si quedan espacios
        hay_espacios = False
        for fila in tablero:
         if " " in fila:
            hay_espacios = True

        # diagonales solo si no hay espacios
        if not hay_espacios:

            if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
                return tablero[0][0]

            if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
                return tablero[0][2]

            return "empate"

        return "continua"   
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        
        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles
            
        Returns:
            list: Combinación de colores de la longitud especificada
            
        Ejemplo:
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) 
            -> ["rojo", "azul", "rojo", "verde"]
        """
        import random
        return [random.choice(colores_disponibles) for _ in range(longitud)]
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        # validar límites
        if not (0 <= desde_fila < 8 and 0 <= desde_col < 8 and 0 <= hasta_fila < 8 and 0 <= hasta_col < 8):
         return False

        # misma posición
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False

         # movimiento horizontal
        if desde_fila == hasta_fila:

         paso = 1 if hasta_col > desde_col else -1

        for c in range(desde_col + paso, hasta_col, paso):
            if tablero[desde_fila][c] != " ":
                return False

            return True

        # movimiento vertical

        if desde_col == hasta_col:

          paso = 1 if hasta_fila > desde_fila else -1

          for f in range(desde_fila + paso, hasta_fila, paso):
             if tablero[f][desde_col] != " ":
                return False

        return True 
    

