class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        lista_invertida = []
        for i in range(len(lista) - 1, -1, -1):
            lista_invertida.append(lista[i])
        return lista_invertida
    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        vistos = set()
        lista_sin_duplicados = []
    
        for item in lista:
         identificador = (item, type(item))
         if identificador not in vistos:
            vistos.add(identificador)
            lista_sin_duplicados.append(item)
    
        return lista_sin_duplicados
    
    """
he de reconocer que para este este test tuve que recurrir a la ayuda 
de la ia pero por eso tratare de explicar sus partes a como lo comprendí. 

primero se creo una tupla con identificador = (item, type(item))
gracia eso se puede tratar a i como un int y true como un bool 
pese a que i==true
type(item) para diferenciar elementos que son "iguales" en valor pero 
de diferentes tipos. 
La tupla (valor, tipo) actúa como una "clave" única para cada elemento 
considerando tanto su valor como su tipo
por si alguien lo lee al detalle le anexo un video que tenia de fondo 
cunado funciono https://youtu.be/K-gbAi5UIg0?si=60H9YhF8_Dz3zESB
"""

    def merge_ordenado(self, lista1, lista2):
        """
        Merge en informática se refiere a la operación de unir dos o 
        más conjuntos de datos, ramas de código o historiales de 
        cambios en una sola unidad coherente.
        
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        lista_combinada = []
        i, j = 0, 0
        
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                lista_combinada.append(lista1[i])
                i += 1
            else:
                lista_combinada.append(lista2[j])
                j += 1
        
        # Agregar los elementos restantes de lista1 o lista2
        while i < len(lista1):
            lista_combinada.append(lista1[i])
            i += 1
        while j < len(lista2):
            lista_combinada.append(lista2[j])
            j += 1
        
        return lista_combinada
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        if not lista:
         return lista
    
        if k is None:
         k = 0
    
        k = k % len(lista)
    
        if k == 0:
         return lista
    
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        pass
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        pass
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pass
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass