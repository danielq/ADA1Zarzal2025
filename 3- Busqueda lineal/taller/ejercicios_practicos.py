#!/usr/bin/env python3
"""
Ejercicios Prácticos de Búsqueda Lineal
Taller de Algoritmos y Estructuras de Datos
"""

import random
import time
from typing import List, Dict, Any, Callable, Optional
from dataclasses import dataclass

# =============================================================================
# EJERCICIO 1: BÚSQUEDA LINEAL BÁSICA
# =============================================================================

def busqueda_lineal_basica(lista: List[Any], elemento: Any) -> int:
    """
    Busca un elemento en una lista usando búsqueda lineal
    
    Args:
        lista: Lista donde buscar
        elemento: Elemento a buscar
    
    Returns:
        Índice del elemento si se encuentra, -1 si no
    """
    for i, valor in enumerate(lista):
        if valor == elemento:
            return i
    return -1

def busqueda_lineal_con_estadisticas(lista: List[Any], elemento: Any) -> Dict[str, Any]:
    """
    Búsqueda lineal que registra estadísticas de rendimiento
    
    Args:
        lista: Lista donde buscar
        elemento: Elemento a buscar
    
    Returns:
        Diccionario con resultados y estadísticas
    """
    comparaciones = 0
    inicio = time.time()
    
    for i, valor in enumerate(lista):
        comparaciones += 1
        if valor == elemento:
            tiempo = time.time() - inicio
            return {
                'indice': i,
                'encontrado': True,
                'comparaciones': comparaciones,
                'tiempo': tiempo,
                'elemento': elemento
            }
    
    tiempo = time.time() - inicio
    return {
        'indice': -1,
        'encontrado': False,
        'comparaciones': comparaciones,
        'tiempo': tiempo,
        'elemento': elemento
    }

# =============================================================================
# EJERCICIO 2: BÚSQUEDA EN OBJETOS COMPLEJOS
# =============================================================================

@dataclass
class Persona:
    """Clase para representar una persona"""
    nombre: str
    edad: int
    ciudad: str
    profesion: str
    
    def __str__(self):
        return f"{self.nombre}, {self.edad} años, {self.ciudad}, {self.profesion}"

def buscar_por_nombre(personas: List[Persona], nombre_buscado: str) -> tuple:
    """
    Busca una persona por nombre usando búsqueda lineal
    
    Args:
        personas: Lista de objetos Persona
        nombre_buscado: Nombre a buscar
    
    Returns:
        Tupla (índice, persona) o (-1, None) si no se encuentra
    """
    for i, persona in enumerate(personas):
        if persona.nombre.lower() == nombre_buscado.lower():
            return i, persona
    return -1, None

def buscar_por_ciudad(personas: List[Persona], ciudad_buscada: str) -> List[Persona]:
    """
    Busca todas las personas de una ciudad específica
    
    Args:
        personas: Lista de objetos Persona
        ciudad_buscada: Ciudad a buscar
    
    Returns:
        Lista de personas que viven en la ciudad
    """
    resultados = []
    for persona in personas:
        if persona.ciudad.lower() == ciudad_buscada.lower():
            resultados.append(persona)
    return resultados

def buscar_por_rango_edad(personas: List[Persona], edad_min: int, edad_max: int) -> List[Persona]:
    """
    Busca personas en un rango de edad específico
    
    Args:
        personas: Lista de objetos Persona
        edad_min: Edad mínima
        edad_max: Edad máxima
    
    Returns:
        Lista de personas en el rango de edad
    """
    resultados = []
    for persona in personas:
        if edad_min <= persona.edad <= edad_max:
            resultados.append(persona)
    return resultados

# =============================================================================
# EJERCICIO 3: ANÁLISIS DE RENDIMIENTO
# =============================================================================

def generar_lista_aleatoria(tamaño: int, rango_min: int = 1, rango_max: int = 1000) -> List[int]:
    """
    Genera una lista de números aleatorios
    
    Args:
        tamaño: Número de elementos en la lista
        rango_min: Valor mínimo
        rango_max: Valor máximo
    
    Returns:
        Lista de números aleatorios
    """
    return [random.randint(rango_min, rango_max) for _ in range(tamaño)]

def analizar_rendimiento_busqueda_lineal():
    """
    Analiza el rendimiento de búsqueda lineal con diferentes tamaños de datos
    """
    print("=" * 60)
    print("ANÁLISIS DE RENDIMIENTO - BÚSQUEDA LINEAL")
    print("=" * 60)
    
    tamaños = [100, 500, 1000, 5000, 10000]
    posiciones = ['primero', 'medio', 'ultimo', 'no_existe']
    
    for tamaño in tamaños:
        print(f"\n--- Análisis para lista de {tamaño:,} elementos ---")
        lista = generar_lista_aleatoria(tamaño)
        
        for pos in posiciones:
            if pos == 'primero':
                elemento = lista[0]
            elif pos == 'medio':
                elemento = lista[tamaño // 2]
            elif pos == 'ultimo':
                elemento = lista[-1]
            else:  # no_existe
                elemento = 9999  # Valor que no existe
            
            resultado = busqueda_lineal_con_estadisticas(lista, elemento)
            print(f"Posición {pos:>10}: {resultado['comparaciones']:>6} comparaciones, "
                  f"{resultado['tiempo']:>10.6f}s, "
                  f"Encontrado: {resultado['encontrado']}")

# =============================================================================
# EJERCICIO 4: OPTIMIZACIONES DE BÚSQUEDA LINEAL
# =============================================================================

def busqueda_lineal_primera_ocurrencia(lista: List[Any], elemento: Any) -> int:
    """
    Retorna solo la primera ocurrencia del elemento
    
    Args:
        lista: Lista donde buscar
        elemento: Elemento a buscar
    
    Returns:
        Índice de la primera ocurrencia, -1 si no se encuentra
    """
    for i, valor in enumerate(lista):
        if valor == elemento:
            return i
    return -1

def busqueda_lineal_todas_ocurrencias(lista: List[Any], elemento: Any) -> List[int]:
    """
    Retorna todas las ocurrencias del elemento
    
    Args:
        lista: Lista donde buscar
        elemento: Elemento a buscar
    
    Returns:
        Lista de índices donde se encuentra el elemento
    """
    indices = []
    for i, valor in enumerate(lista):
        if valor == elemento:
            indices.append(i)
    return indices

def busqueda_lineal_sentinel(lista: List[Any], elemento: Any) -> int:
    """
    Búsqueda lineal con elemento centinela para optimizar comparaciones
    
    Args:
        lista: Lista donde buscar (se modifica temporalmente)
        elemento: Elemento a buscar
    
    Returns:
        Índice del elemento si se encuentra, -1 si no
    """
    # Crear copia para no modificar la lista original
    lista_temporal = lista.copy()
    
    # Agregar elemento centinela al final
    lista_temporal.append(elemento)
    
    i = 0
    while lista_temporal[i] != elemento:
        i += 1
    
    # Si encontramos el elemento antes del centinela, es válido
    if i < len(lista):
        return i
    else:
        return -1

def busqueda_lineal_condicion(lista: List[Any], condicion_func: Callable[[Any], bool]) -> List[Any]:
    """
    Busca todos los elementos que cumplan una condición específica
    
    Args:
        lista: Lista donde buscar
        condicion_func: Función que retorna True/False para cada elemento
    
    Returns:
        Lista de elementos que cumplen la condición
    """
    resultados = []
    for elemento in lista:
        if condicion_func(elemento):
            resultados.append(elemento)
    return resultados

# =============================================================================
# EJERCICIO 5: SISTEMA DE BÚSQUEDA DE LIBROS
# =============================================================================

@dataclass
class Libro:
    """Clase para representar un libro"""
    titulo: str
    autor: str
    año: int
    genero: str
    disponible: bool
    
    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo}' por {self.autor} ({self.año}) - {self.genero} - {estado}"

class SistemaBusquedaLibros:
    """Sistema de búsqueda de libros usando búsqueda lineal"""
    
    def __init__(self, libros: List[Libro]):
        self.libros = libros
        self.comparaciones = 0
    
    def buscar_por_titulo(self, titulo_buscado: str) -> List[Libro]:
        """Busca libros por título (búsqueda parcial)"""
        self.comparaciones = 0
        resultados = []
        
        for libro in self.libros:
            self.comparaciones += 1
            if titulo_buscado.lower() in libro.titulo.lower():
                resultados.append(libro)
        
        return resultados
    
    def buscar_por_autor(self, autor_buscado: str) -> List[Libro]:
        """Busca libros por autor"""
        self.comparaciones = 0
        resultados = []
        
        for libro in self.libros:
            self.comparaciones += 1
            if autor_buscado.lower() in libro.autor.lower():
                resultados.append(libro)
        
        return resultados
    
    def buscar_por_genero(self, genero_buscado: str) -> List[Libro]:
        """Busca libros por género"""
        self.comparaciones = 0
        resultados = []
        
        for libro in self.libros:
            self.comparaciones += 1
            if libro.genero.lower() == genero_buscado.lower():
                resultados.append(libro)
        
        return resultados
    
    def buscar_por_año(self, año_buscado: int) -> List[Libro]:
        """Busca libros por año de publicación"""
        self.comparaciones = 0
        resultados = []
        
        for libro in self.libros:
            self.comparaciones += 1
            if libro.año == año_buscado:
                resultados.append(libro)
        
        return resultados
    
    def buscar_libros_disponibles(self) -> List[Libro]:
        """Busca todos los libros disponibles"""
        self.comparaciones = 0
        resultados = []
        
        for libro in self.libros:
            self.comparaciones += 1
            if libro.disponible:
                resultados.append(libro)
        
        return resultados
    
    def buscar_por_rango_años(self, año_min: int, año_max: int) -> List[Libro]:
        """Busca libros en un rango de años"""
        self.comparaciones = 0
        resultados = []
        
        for libro in self.libros:
            self.comparaciones += 1
            if año_min <= libro.año <= año_max:
                resultados.append(libro)
        
        return resultados
    
    def obtener_estadisticas(self) -> Dict[str, Any]:
        """Retorna estadísticas de la última búsqueda"""
        return {
            'comparaciones': self.comparaciones,
            'total_libros': len(self.libros)
        }

# =============================================================================
# FUNCIONES DE DEMOSTRACIÓN
# =============================================================================

def demostrar_busqueda_basica():
    """Demuestra la búsqueda lineal básica"""
    print("=" * 50)
    print("DEMOSTRACIÓN: BÚSQUEDA LINEAL BÁSICA")
    print("=" * 50)
    
    numeros = [64, 34, 25, 12, 22, 11, 90, 25, 77]
    print(f"Lista: {numeros}")
    
    # Buscar elemento existente
    elemento = 25
    resultado = busqueda_lineal_con_estadisticas(numeros, elemento)
    print(f"\nBuscando {elemento}:")
    print(f"  Encontrado: {resultado['encontrado']}")
    print(f"  Índice: {resultado['indice']}")
    print(f"  Comparaciones: {resultado['comparaciones']}")
    print(f"  Tiempo: {resultado['tiempo']:.6f}s")
    
    # Buscar elemento no existente
    elemento = 99
    resultado = busqueda_lineal_con_estadisticas(numeros, elemento)
    print(f"\nBuscando {elemento}:")
    print(f"  Encontrado: {resultado['encontrado']}")
    print(f"  Comparaciones: {resultado['comparaciones']}")
    print(f"  Tiempo: {resultado['tiempo']:.6f}s")

def demostrar_busqueda_personas():
    """Demuestra la búsqueda en objetos Persona"""
    print("\n" + "=" * 50)
    print("DEMOSTRACIÓN: BÚSQUEDA EN OBJETOS PERSONA")
    print("=" * 50)
    
    personas = [
        Persona("Ana García", 25, "Madrid", "Ingeniera"),
        Persona("Carlos López", 30, "Barcelona", "Doctor"),
        Persona("María Ruiz", 28, "Valencia", "Profesora"),
        Persona("Ana Martínez", 35, "Madrid", "Abogada"),
        Persona("Pedro Sánchez", 22, "Barcelona", "Estudiante")
    ]
    
    print("Lista de personas:")
    for i, persona in enumerate(personas):
        print(f"  {i}: {persona}")
    
    # Buscar por nombre
    print(f"\nBuscando personas llamadas 'Ana':")
    for i, persona in enumerate(personas):
        if "ana" in persona.nombre.lower():
            print(f"  Encontrada: {persona}")
    
    # Buscar por ciudad
    print(f"\nBuscando personas de 'Madrid':")
    madrileños = buscar_por_ciudad(personas, "Madrid")
    for persona in madrileños:
        print(f"  {persona}")
    
    # Buscar por rango de edad
    print(f"\nBuscando personas entre 25 y 30 años:")
    jovenes = buscar_por_rango_edad(personas, 25, 30)
    for persona in jovenes:
        print(f"  {persona}")

def demostrar_sistema_libros():
    """Demuestra el sistema de búsqueda de libros"""
    print("\n" + "=" * 50)
    print("DEMOSTRACIÓN: SISTEMA DE BÚSQUEDA DE LIBROS")
    print("=" * 50)
    
    libros = [
        Libro("El Quijote", "Miguel de Cervantes", 1605, "Novela", True),
        Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Realismo mágico", True),
        Libro("1984", "George Orwell", 1949, "Ciencia ficción", False),
        Libro("Don Juan Tenorio", "José Zorrilla", 1844, "Drama", True),
        Libro("La casa de los espíritus", "Isabel Allende", 1982, "Realismo mágico", True),
        Libro("Fahrenheit 451", "Ray Bradbury", 1953, "Ciencia ficción", False)
    ]
    
    sistema = SistemaBusquedaLibros(libros)
    
    print("Catálogo de libros:")
    for i, libro in enumerate(libros):
        print(f"  {i+1}: {libro}")
    
    # Búsquedas
    print(f"\n--- Búsquedas ---")
    
    # Por título
    print(f"\nBuscando libros con 'Don' en el título:")
    resultados = sistema.buscar_por_titulo("Don")
    for libro in resultados:
        print(f"  {libro}")
    print(f"  Comparaciones realizadas: {sistema.obtener_estadisticas()['comparaciones']}")
    
    # Por género
    print(f"\nBuscando libros de 'Ciencia ficción':")
    resultados = sistema.buscar_por_genero("Ciencia ficción")
    for libro in resultados:
        print(f"  {libro}")
    print(f"  Comparaciones realizadas: {sistema.obtener_estadisticas()['comparaciones']}")
    
    # Libros disponibles
    print(f"\nBuscando libros disponibles:")
    resultados = sistema.buscar_libros_disponibles()
    for libro in resultados:
        print(f"  {libro}")
    print(f"  Comparaciones realizadas: {sistema.obtener_estadisticas()['comparaciones']}")

def main():
    """Función principal que ejecuta todas las demostraciones"""
    print("TALLER DE BÚSQUEDA LINEAL - EJERCICIOS PRÁCTICOS")
    print("=" * 60)
    
    # Ejecutar demostraciones
    demostrar_busqueda_basica()
    demostrar_busqueda_personas()
    demostrar_sistema_libros()
    
    # Análisis de rendimiento
    print("\n" + "=" * 60)
    print("ANÁLISIS DE RENDIMIENTO")
    print("=" * 60)
    analizar_rendimiento_busqueda_lineal()
    
    print("\n" + "=" * 60)
    print("¡TALLER COMPLETADO!")
    print("=" * 60)

if __name__ == "__main__":
    main()
