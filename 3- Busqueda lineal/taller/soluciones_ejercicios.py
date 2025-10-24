#!/usr/bin/env python3
"""
Soluciones de los Ejercicios de Evaluación
Taller de Búsqueda Lineal
"""

from typing import List, Dict, Any, Callable
import time

# =============================================================================
# SOLUCIÓN EJERCICIO 1: IMPLEMENTACIÓN BÁSICA (20 puntos)
# =============================================================================

def buscar_string(lista_strings: List[str], string_buscado: str) -> Dict[str, Any]:
    """
    Busca un string en una lista de strings y retorna el índice y estadísticas
    
    Args:
        lista_strings: Lista de strings donde buscar
        string_buscado: String a buscar
    
    Returns:
        Diccionario con índice, encontrado y comparaciones
    """
    comparaciones = 0
    
    for i, string_actual in enumerate(lista_strings):
        comparaciones += 1
        if string_actual == string_buscado:
            return {
                'indice': i,
                'encontrado': True,
                'comparaciones': comparaciones
            }
    
    return {
        'indice': -1,
        'encontrado': False,
        'comparaciones': comparaciones
    }

# =============================================================================
# SOLUCIÓN EJERCICIO 2: BÚSQUEDA MÚLTIPLE (25 puntos)
# =============================================================================

def buscar_elementos_condicion(lista: List[Any], condicion_func: Callable[[Any], bool]) -> List[Any]:
    """
    Busca todos los elementos que cumplan una condición específica
    
    Args:
        lista: Lista donde buscar
        condicion_func: Función que retorna True/False para cada elemento
    
    Returns:
        Lista de elementos que cumplen la condición
    """
    resultados = []
    comparaciones = 0
    
    for elemento in lista:
        comparaciones += 1
        if condicion_func(elemento):
            resultados.append(elemento)
    
    print(f"Comparaciones realizadas: {comparaciones}")
    return resultados

# =============================================================================
# SOLUCIÓN EJERCICIO 3: ANÁLISIS DE COMPLEJIDAD (25 puntos)
# =============================================================================

def algoritmo_a(lista: List[Any], elemento: Any) -> int:
    """
    Algoritmo A: Búsqueda lineal estándar
    Complejidad: O(n) - En el peor caso revisa todos los elementos
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def algoritmo_b(lista: List[Any], elemento: Any) -> int:
    """
    Algoritmo B: Búsqueda lineal con flag booleano
    Complejidad: O(n) - Misma complejidad que A, pero con más operaciones
    """
    encontrado = False
    indice = 0
    while not encontrado and indice < len(lista):
        if lista[indice] == elemento:
            encontrado = True
        indice += 1
    return indice - 1 if encontrado else -1

def algoritmo_c(lista: List[Any], elemento: Any) -> int:
    """
    Algoritmo C: Búsqueda con bucle anidado innecesario
    Complejidad: O(n²) - Ineficiente, revisa elementos múltiples veces
    """
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if lista[j] == elemento:
                return j
    return -1

def analizar_complejidad():
    """
    Analiza y explica la complejidad de los tres algoritmos
    """
    print("=" * 60)
    print("ANÁLISIS DE COMPLEJIDAD DE ALGORITMOS")
    print("=" * 60)
    
    print("\nALGORITMO A - Búsqueda lineal estándar:")
    print("- Complejidad temporal: O(n)")
    print("- En el mejor caso: O(1) - elemento en primera posición")
    print("- En el peor caso: O(n) - elemento no existe o está al final")
    print("- Complejidad espacial: O(1)")
    print("- Ventajas: Simple, eficiente, fácil de entender")
    
    print("\nALGORITMO B - Búsqueda con flag booleano:")
    print("- Complejidad temporal: O(n)")
    print("- En el mejor caso: O(1) - elemento en primera posición")
    print("- En el peor caso: O(n) - elemento no existe o está al final")
    print("- Complejidad espacial: O(1)")
    print("- Desventajas: Más operaciones que A (asignaciones, comparaciones)")
    print("- Misma complejidad pero menos eficiente en la práctica")
    
    print("\nALGORITMO C - Búsqueda con bucle anidado:")
    print("- Complejidad temporal: O(n²)")
    print("- En el mejor caso: O(1) - elemento en primera posición")
    print("- En el peor caso: O(n²) - elemento no existe")
    print("- Complejidad espacial: O(1)")
    print("- Desventajas: MUY ineficiente, revisa elementos múltiples veces")
    print("- NO RECOMENDADO para búsqueda lineal")
    
    print("\nCONCLUSIÓN:")
    print("- Algoritmo A es el más eficiente y recomendado")
    print("- Algoritmo B es aceptable pero menos eficiente que A")
    print("- Algoritmo C es ineficiente y no debería usarse")

# =============================================================================
# SOLUCIÓN EJERCICIO 4: APLICACIÓN PRÁCTICA (30 puntos)
# =============================================================================

from dataclasses import dataclass
from typing import Optional

@dataclass
class Libro:
    """Clase para representar un libro en una biblioteca"""
    titulo: str
    autor: str
    año_publicacion: int
    genero: str
    disponible: bool
    
    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo}' por {self.autor} ({self.año_publicacion}) - {self.genero} - {estado}"

class SistemaBusquedaBiblioteca:
    """Sistema de búsqueda de libros en biblioteca usando búsqueda lineal"""
    
    def __init__(self, libros: List[Libro]):
        self.libros = libros
        self.estadisticas = {
            'comparaciones': 0,
            'tiempo_busqueda': 0.0
        }
    
    def _iniciar_busqueda(self):
        """Inicializa las estadísticas de búsqueda"""
        self.estadisticas['comparaciones'] = 0
        self.estadisticas['tiempo_busqueda'] = time.time()
    
    def _finalizar_busqueda(self):
        """Finaliza la búsqueda y calcula el tiempo"""
        self.estadisticas['tiempo_busqueda'] = time.time() - self.estadisticas['tiempo_busqueda']
    
    def buscar_por_titulo(self, titulo_buscado: str) -> List[Libro]:
        """
        Busca libros por título (búsqueda parcial, case-insensitive)
        
        Args:
            titulo_buscado: Título o parte del título a buscar
        
        Returns:
            Lista de libros que coinciden con el título
        """
        self._iniciar_busqueda()
        resultados = []
        titulo_lower = titulo_buscado.lower()
        
        for libro in self.libros:
            self.estadisticas['comparaciones'] += 1
            if titulo_lower in libro.titulo.lower():
                resultados.append(libro)
        
        self._finalizar_busqueda()
        return resultados
    
    def buscar_por_autor(self, autor_buscado: str) -> List[Libro]:
        """
        Busca libros por autor (búsqueda parcial, case-insensitive)
        
        Args:
            autor_buscado: Autor o parte del nombre del autor
        
        Returns:
            Lista de libros del autor
        """
        self._iniciar_busqueda()
        resultados = []
        autor_lower = autor_buscado.lower()
        
        for libro in self.libros:
            self.estadisticas['comparaciones'] += 1
            if autor_lower in libro.autor.lower():
                resultados.append(libro)
        
        self._finalizar_busqueda()
        return resultados
    
    def buscar_por_genero(self, genero_buscado: str) -> List[Libro]:
        """
        Busca libros por género (búsqueda exacta, case-insensitive)
        
        Args:
            genero_buscado: Género a buscar
        
        Returns:
            Lista de libros del género
        """
        self._iniciar_busqueda()
        resultados = []
        genero_lower = genero_buscado.lower()
        
        for libro in self.libros:
            self.estadisticas['comparaciones'] += 1
            if libro.genero.lower() == genero_lower:
                resultados.append(libro)
        
        self._finalizar_busqueda()
        return resultados
    
    def buscar_por_año(self, año_buscado: int) -> List[Libro]:
        """
        Busca libros por año de publicación
        
        Args:
            año_buscado: Año a buscar
        
        Returns:
            Lista de libros publicados en ese año
        """
        self._iniciar_busqueda()
        resultados = []
        
        for libro in self.libros:
            self.estadisticas['comparaciones'] += 1
            if libro.año_publicacion == año_buscado:
                resultados.append(libro)
        
        self._finalizar_busqueda()
        return resultados
    
    def buscar_libros_disponibles(self) -> List[Libro]:
        """
        Busca todos los libros disponibles
        
        Returns:
            Lista de libros disponibles
        """
        self._iniciar_busqueda()
        resultados = []
        
        for libro in self.libros:
            self.estadisticas['comparaciones'] += 1
            if libro.disponible:
                resultados.append(libro)
        
        self._finalizar_busqueda()
        return resultados
    
    def buscar_por_rango_años(self, año_min: int, año_max: int) -> List[Libro]:
        """
        Busca libros en un rango de años
        
        Args:
            año_min: Año mínimo
            año_max: Año máximo
        
        Returns:
            Lista de libros en el rango de años
        """
        self._iniciar_busqueda()
        resultados = []
        
        for libro in self.libros:
            self.estadisticas['comparaciones'] += 1
            if año_min <= libro.año_publicacion <= año_max:
                resultados.append(libro)
        
        self._finalizar_busqueda()
        return resultados
    
    def buscar_libros_por_multiples_criterios(self, 
                                            titulo: Optional[str] = None,
                                            autor: Optional[str] = None,
                                            genero: Optional[str] = None,
                                            año_min: Optional[int] = None,
                                            año_max: Optional[int] = None,
                                            solo_disponibles: bool = False) -> List[Libro]:
        """
        Busca libros que cumplan múltiples criterios simultáneamente
        
        Args:
            titulo: Título o parte del título
            autor: Autor o parte del nombre
            genero: Género exacto
            año_min: Año mínimo de publicación
            año_max: Año máximo de publicación
            solo_disponibles: Si True, solo libros disponibles
        
        Returns:
            Lista de libros que cumplen todos los criterios
        """
        self._iniciar_busqueda()
        resultados = []
        
        for libro in self.libros:
            self.estadisticas['comparaciones'] += 1
            
            # Verificar cada criterio si está especificado
            cumple_criterios = True
            
            if titulo and titulo.lower() not in libro.titulo.lower():
                cumple_criterios = False
            
            if autor and autor.lower() not in libro.autor.lower():
                cumple_criterios = False
            
            if genero and libro.genero.lower() != genero.lower():
                cumple_criterios = False
            
            if año_min and libro.año_publicacion < año_min:
                cumple_criterios = False
            
            if año_max and libro.año_publicacion > año_max:
                cumple_criterios = False
            
            if solo_disponibles and not libro.disponible:
                cumple_criterios = False
            
            if cumple_criterios:
                resultados.append(libro)
        
        self._finalizar_busqueda()
        return resultados
    
    def obtener_estadisticas(self) -> Dict[str, Any]:
        """
        Retorna estadísticas de la última búsqueda
        
        Returns:
            Diccionario con estadísticas
        """
        return {
            'comparaciones': self.estadisticas['comparaciones'],
            'tiempo_busqueda': round(self.estadisticas['tiempo_busqueda'], 6),
            'total_libros': len(self.libros)
        }
    
    def imprimir_resultados(self, resultados: List[Libro], titulo: str = "Resultados"):
        """
        Imprime los resultados de búsqueda de forma formateada
        
        Args:
            resultados: Lista de libros encontrados
            titulo: Título para mostrar
        """
        print(f"\n{titulo}:")
        print("-" * 50)
        
        if not resultados:
            print("No se encontraron libros que coincidan con los criterios.")
        else:
            for i, libro in enumerate(resultados, 1):
                print(f"{i:2d}. {libro}")
        
        stats = self.obtener_estadisticas()
        print(f"\nEstadísticas:")
        print(f"  Libros encontrados: {len(resultados)}")
        print(f"  Comparaciones: {stats['comparaciones']}")
        print(f"  Tiempo: {stats['tiempo_busqueda']}s")

# =============================================================================
# FUNCIONES DE DEMOSTRACIÓN
# =============================================================================

def demostrar_ejercicio_1():
    """Demuestra la solución del Ejercicio 1"""
    print("=" * 60)
    print("SOLUCIÓN EJERCICIO 1: BÚSQUEDA DE STRINGS")
    print("=" * 60)
    
    palabras = ["python", "java", "javascript", "python", "c++", "python", "go"]
    palabra_buscada = "python"
    
    print(f"Lista: {palabras}")
    print(f"Buscando: '{palabra_buscada}'")
    
    resultado = buscar_string(palabras, palabra_buscada)
    print(f"\nResultado:")
    print(f"  Índice: {resultado['indice']}")
    print(f"  Encontrado: {resultado['encontrado']}")
    print(f"  Comparaciones: {resultado['comparaciones']}")

def demostrar_ejercicio_2():
    """Demuestra la solución del Ejercicio 2"""
    print("\n" + "=" * 60)
    print("SOLUCIÓN EJERCICIO 2: BÚSQUEDA CON CONDICIONES")
    print("=" * 60)
    
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(f"Lista: {numeros}")
    
    # Buscar números pares
    print(f"\nBuscando números pares:")
    pares = buscar_elementos_condicion(numeros, lambda x: x % 2 == 0)
    print(f"Resultado: {pares}")
    
    # Buscar números mayores a 10
    print(f"\nBuscando números mayores a 10:")
    mayores_10 = buscar_elementos_condicion(numeros, lambda x: x > 10)
    print(f"Resultado: {mayores_10}")
    
    # Buscar números primos (simplificado)
    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    print(f"\nBuscando números primos:")
    primos = buscar_elementos_condicion(numeros, es_primo)
    print(f"Resultado: {primos}")

def demostrar_ejercicio_3():
    """Demuestra la solución del Ejercicio 3"""
    print("\n" + "=" * 60)
    print("SOLUCIÓN EJERCICIO 3: ANÁLISIS DE COMPLEJIDAD")
    print("=" * 60)
    
    # Crear lista de prueba
    lista_prueba = list(range(1, 1001))  # Lista del 1 al 1000
    elemento_buscado = 500
    
    print(f"Probando con lista de {len(lista_prueba)} elementos")
    print(f"Buscando elemento: {elemento_buscado}")
    
    # Probar cada algoritmo
    import time
    
    # Algoritmo A
    inicio = time.time()
    resultado_a = algoritmo_a(lista_prueba, elemento_buscado)
    tiempo_a = time.time() - inicio
    print(f"\nAlgoritmo A:")
    print(f"  Resultado: {resultado_a}")
    print(f"  Tiempo: {tiempo_a:.6f}s")
    
    # Algoritmo B
    inicio = time.time()
    resultado_b = algoritmo_b(lista_prueba, elemento_buscado)
    tiempo_b = time.time() - inicio
    print(f"\nAlgoritmo B:")
    print(f"  Resultado: {resultado_b}")
    print(f"  Tiempo: {tiempo_b:.6f}s")
    
    # Algoritmo C
    inicio = time.time()
    resultado_c = algoritmo_c(lista_prueba, elemento_buscado)
    tiempo_c = time.time() - inicio
    print(f"\nAlgoritmo C:")
    print(f"  Resultado: {resultado_c}")
    print(f"  Tiempo: {tiempo_c:.6f}s")
    
    # Análisis
    analizar_complejidad()

def demostrar_ejercicio_4():
    """Demuestra la solución del Ejercicio 4"""
    print("\n" + "=" * 60)
    print("SOLUCIÓN EJERCICIO 4: SISTEMA DE BIBLIOTECA")
    print("=" * 60)
    
    # Crear catálogo de libros
    libros = [
        Libro("El Quijote", "Miguel de Cervantes", 1605, "Novela", True),
        Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Realismo mágico", True),
        Libro("1984", "George Orwell", 1949, "Ciencia ficción", False),
        Libro("Don Juan Tenorio", "José Zorrilla", 1844, "Drama", True),
        Libro("La casa de los espíritus", "Isabel Allende", 1982, "Realismo mágico", True),
        Libro("Fahrenheit 451", "Ray Bradbury", 1953, "Ciencia ficción", False),
        Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985, "Realismo mágico", True),
        Libro("Un mundo feliz", "Aldous Huxley", 1932, "Ciencia ficción", True),
        Libro("La ciudad y los perros", "Mario Vargas Llosa", 1963, "Novela", False),
        Libro("Rayuela", "Julio Cortázar", 1963, "Novela", True)
    ]
    
    sistema = SistemaBusquedaBiblioteca(libros)
    
    print("Catálogo de libros:")
    for i, libro in enumerate(libros, 1):
        print(f"  {i:2d}. {libro}")
    
    # Pruebas de búsqueda
    print(f"\n" + "=" * 40)
    print("PRUEBAS DE BÚSQUEDA")
    print("=" * 40)
    
    # Búsqueda por título
    resultados = sistema.buscar_por_titulo("Don")
    sistema.imprimir_resultados(resultados, "Libros con 'Don' en el título")
    
    # Búsqueda por autor
    resultados = sistema.buscar_por_autor("García")
    sistema.imprimir_resultados(resultados, "Libros de autores con 'García'")
    
    # Búsqueda por género
    resultados = sistema.buscar_por_genero("Ciencia ficción")
    sistema.imprimir_resultados(resultados, "Libros de Ciencia ficción")
    
    # Búsqueda por año
    resultados = sistema.buscar_por_año(1963)
    sistema.imprimir_resultados(resultados, "Libros publicados en 1963")
    
    # Libros disponibles
    resultados = sistema.buscar_libros_disponibles()
    sistema.imprimir_resultados(resultados, "Libros disponibles")
    
    # Búsqueda por rango de años
    resultados = sistema.buscar_por_rango_años(1960, 1970)
    sistema.imprimir_resultados(resultados, "Libros publicados entre 1960-1970")
    
    # Búsqueda múltiple
    resultados = sistema.buscar_libros_por_multiples_criterios(
        genero="Realismo mágico",
        solo_disponibles=True
    )
    sistema.imprimir_resultados(resultados, "Libros de Realismo mágico disponibles")

def main():
    """Función principal que ejecuta todas las demostraciones"""
    print("SOLUCIONES DE EJERCICIOS - TALLER DE BÚSQUEDA LINEAL")
    print("=" * 70)
    
    # Ejecutar demostraciones de soluciones
    demostrar_ejercicio_1()
    demostrar_ejercicio_2()
    demostrar_ejercicio_3()
    demostrar_ejercicio_4()
    
    print("\n" + "=" * 70)
    print("¡TODAS LAS SOLUCIONES COMPLETADAS!")
    print("=" * 70)

if __name__ == "__main__":
    main()
