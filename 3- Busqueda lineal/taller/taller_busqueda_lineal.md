# Taller de Búsqueda Lineal
## Algoritmos y Estructuras de Datos

---

## 📚 Objetivos del Taller

Al finalizar este taller, los estudiantes serán capaces de:

1. **Comprender** el concepto y funcionamiento de la búsqueda lineal
2. **Implementar** algoritmos de búsqueda lineal en Python
3. **Analizar** la complejidad temporal y espacial del algoritmo
4. **Aplicar** la búsqueda lineal en problemas reales
5. **Evaluar** el rendimiento del algoritmo con diferentes tamaños de datos

---

## 🎯 Contenido Teórico

### ¿Qué es la Búsqueda Lineal?

La **búsqueda lineal** (también conocida como búsqueda secuencial) es un algoritmo simple que busca un elemento específico en una lista o array recorriendo cada elemento uno por uno hasta encontrar el elemento deseado o hasta llegar al final de la lista.

### Características Principales

- **Simplicidad**: Fácil de entender e implementar
- **No requiere orden**: Funciona con listas desordenadas
- **Búsqueda exhaustiva**: Revisa todos los elementos
- **Complejidad O(n)**: En el peor caso, revisa todos los elementos

### Pseudocódigo

```
FUNCIÓN busqueda_lineal(lista, elemento_buscado):
    PARA cada elemento EN lista:
        SI elemento == elemento_buscado:
            RETORNAR índice_del_elemento
    RETORNAR -1  // Elemento no encontrado
```

### Análisis de Complejidad

| Caso | Tiempo | Descripción |
|------|--------|-------------|
| **Mejor** | O(1) | El elemento está en la primera posición |
| **Promedio** | O(n/2) | El elemento está en la mitad de la lista |
| **Peor** | O(n) | El elemento no existe o está al final |
| **Espacial** | O(1) | Solo usa memoria constante |

---

## 🛠️ Implementación Práctica

### Ejercicio 1: Búsqueda Lineal Básica

Implementa una función que busque un número en una lista de enteros:

```python
def busqueda_lineal_basica(lista, elemento):
    """
    Busca un elemento en una lista usando búsqueda lineal
    Retorna el índice si lo encuentra, -1 si no
    """
    for i, valor in enumerate(lista):
        if valor == elemento:
            return i
    return -1

# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
resultado = busqueda_lineal_basica(numeros, 25)
print(f"Elemento encontrado en índice: {resultado}")
```

### Ejercicio 2: Búsqueda Lineal con Estadísticas

Implementa una versión que registre estadísticas de rendimiento:

```python
def busqueda_lineal_con_estadisticas(lista, elemento):
    """
    Búsqueda lineal que registra comparaciones y tiempo
    """
    import time
    
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
                'tiempo': tiempo
            }
    
    tiempo = time.time() - inicio
    return {
        'indice': -1,
        'encontrado': False,
        'comparaciones': comparaciones,
        'tiempo': tiempo
    }
```

### Ejercicio 3: Búsqueda en Lista de Objetos

Implementa búsqueda en una lista de objetos complejos:

```python
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    
    def __str__(self):
        return f"{self.nombre}, {self.edad} años, {self.ciudad}"

def buscar_por_nombre(personas, nombre_buscado):
    """
    Busca una persona por nombre usando búsqueda lineal
    """
    for i, persona in enumerate(personas):
        if persona.nombre.lower() == nombre_buscado.lower():
            return i, persona
    return -1, None

# Ejemplo de uso
personas = [
    Persona("Ana García", 25, "Madrid"),
    Persona("Carlos López", 30, "Barcelona"),
    Persona("María Ruiz", 28, "Valencia")
]

indice, persona = buscar_por_nombre(personas, "carlos lópez")
if indice != -1:
    print(f"Persona encontrada en índice {indice}: {persona}")
else:
    print("Persona no encontrada")
```

---

## 🧪 Actividades Prácticas

### Actividad 1: Análisis de Rendimiento

**Objetivo**: Comparar el rendimiento de la búsqueda lineal con diferentes tamaños de datos.

**Instrucciones**:
1. Genera listas de diferentes tamaños (100, 500, 1000, 5000, 10000 elementos)
2. Busca elementos en diferentes posiciones (primero, medio, último, no existe)
3. Registra el número de comparaciones y tiempo de ejecución
4. Completa la siguiente tabla:

| Tamaño | Posición | Comparaciones | Tiempo (s) | Observaciones |
|--------|----------|---------------|------------|---------------|
| 100    | Primero  |               |            |               |
| 100    | Medio    |               |            |               |
| 100    | Último   |               |            |               |
| 1000   | Primero  |               |            |               |
| 1000   | Medio    |               |            |               |
| 1000   | Último   |               |            |               |

**Código de referencia**:
```python
import random
import time

def generar_lista_aleatoria(tamaño):
    return [random.randint(1, 1000) for _ in range(tamaño)]

def analizar_rendimiento():
    tamaños = [100, 500, 1000, 5000, 10000]
    posiciones = ['primero', 'medio', 'ultimo', 'no_existe']
    
    for tamaño in tamaños:
        lista = generar_lista_aleatoria(tamaño)
        print(f"\n--- Análisis para lista de {tamaño} elementos ---")
        
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
            print(f"Posición {pos}: {resultado['comparaciones']} comparaciones, {resultado['tiempo']:.6f}s")
```

### Actividad 2: Búsqueda en Múltiples Campos

**Objetivo**: Implementar búsqueda lineal en una lista de empleados por diferentes campos.

**Instrucciones**:
1. Usa la clase `Empleado` del sistema implementado
2. Implementa funciones de búsqueda por:
   - Nombre
   - Departamento
   - Rango de salario
   - Rango de edad
3. Compara el rendimiento de cada tipo de búsqueda

**Código de referencia**:
```python
def buscar_por_departamento(empleados, departamento):
    """Busca empleados por departamento"""
    resultados = []
    for empleado in empleados:
        if empleado.departamento.lower() == departamento.lower():
            resultados.append(empleado)
    return resultados

def buscar_por_rango_salario(empleados, salario_min, salario_max):
    """Busca empleados por rango de salario"""
    resultados = []
    for empleado in empleados:
        if salario_min <= empleado.salario <= salario_max:
            resultados.append(empleado)
    return resultados

def buscar_por_rango_edad(empleados, edad_min, edad_max):
    """Busca empleados por rango de edad"""
    resultados = []
    for empleado in empleados:
        if edad_min <= empleado.edad <= edad_max:
            resultados.append(empleado)
    return resultados
```

### Actividad 3: Optimizaciones de Búsqueda Lineal

**Objetivo**: Implementar y comparar diferentes optimizaciones de búsqueda lineal.

**Instrucciones**:
1. Implementa búsqueda lineal con "early exit" para elementos únicos
2. Implementa búsqueda que retorne todas las ocurrencias
3. Implementa búsqueda con "sentinel" (elemento centinela)
4. Compara el rendimiento de cada versión

**Código de referencia**:
```python
def busqueda_lineal_primera_ocurrencia(lista, elemento):
    """Retorna solo la primera ocurrencia"""
    for i, valor in enumerate(lista):
        if valor == elemento:
            return i
    return -1

def busqueda_lineal_todas_ocurrencias(lista, elemento):
    """Retorna todas las ocurrencias"""
    indices = []
    for i, valor in enumerate(lista):
        if valor == elemento:
            indices.append(i)
    return indices

def busqueda_lineal_sentinel(lista, elemento):
    """Búsqueda lineal con elemento centinela"""
    # Agregar elemento centinela al final
    lista_original = lista.copy()
    lista.append(elemento)
    
    i = 0
    while lista[i] != elemento:
        i += 1
    
    # Restaurar lista original
    lista.pop()
    
    if i < len(lista_original):
        return i
    else:
        return -1
```

---

## 📊 Ejercicios de Evaluación

### Ejercicio 1: Implementación Básica (20 puntos)

Implementa una función que busque un elemento en una lista de strings y retorne:
- El índice del elemento si se encuentra
- -1 si no se encuentra
- El número de comparaciones realizadas

```python
def buscar_string(lista_strings, string_buscado):
    # Tu implementación aquí
    pass
```

### Ejercicio 2: Búsqueda Múltiple (25 puntos)

Implementa una función que busque todos los elementos que cumplan una condición específica:

```python
def buscar_elementos_condicion(lista, condicion_func):
    """
    Busca todos los elementos que cumplan la condición
    condicion_func: función que retorna True/False
    """
    # Tu implementación aquí
    pass

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = buscar_elementos_condicion(numeros, lambda x: x % 2 == 0)
print(pares)  # Debería imprimir [2, 4, 6, 8, 10]
```

### Ejercicio 3: Análisis de Complejidad (25 puntos)

Analiza y explica la complejidad temporal de los siguientes algoritmos:

```python
def algoritmo_a(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def algoritmo_b(lista, elemento):
    encontrado = False
    indice = 0
    while not encontrado and indice < len(lista):
        if lista[indice] == elemento:
            encontrado = True
        indice += 1
    return indice - 1 if encontrado else -1

def algoritmo_c(lista, elemento):
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if lista[j] == elemento:
                return j
    return -1
```

### Ejercicio 4: Aplicación Práctica (30 puntos)

Implementa un sistema de búsqueda de libros en una biblioteca usando búsqueda lineal. Cada libro tiene:
- Título
- Autor
- Año de publicación
- Género
- Disponibilidad

Implementa funciones para buscar por:
1. Título (búsqueda parcial)
2. Autor
3. Género
4. Año de publicación
5. Libros disponibles

---

## 🎯 Preguntas de Reflexión

1. **¿Cuándo es apropiado usar búsqueda lineal?**
   - ¿En qué situaciones es la mejor opción?
   - ¿Cuándo deberíamos considerar otros algoritmos?

2. **¿Cómo afecta el tamaño de los datos al rendimiento?**
   - ¿Qué pasa si tenemos 1 millón de elementos?
   - ¿Cuándo se vuelve ineficiente?

3. **¿Qué optimizaciones se pueden aplicar?**
   - ¿Cómo podemos mejorar el rendimiento?
   - ¿Qué trade-offs existen?

4. **¿Cómo se compara con otros algoritmos de búsqueda?**
   - ¿Cuándo es mejor que búsqueda binaria?
   - ¿Qué ventajas tiene sobre algoritmos más complejos?

---

## 📚 Recursos Adicionales

### Lecturas Recomendadas
- "Introduction to Algorithms" - Cormen, Leiserson, Rivest, Stein
- "Algorithms" - Sedgewick, Wayne
- "Python Algorithms" - Hetland

### Enlaces Útiles
- [Visualización de Búsqueda Lineal](https://visualgo.net/en/searching)
- [Complejidad Algorítmica](https://www.bigocheatsheet.com/)
- [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed)

### Próximos Temas
- Búsqueda binaria
- Búsqueda hash
- Árboles de búsqueda
- Algoritmos de ordenamiento

---

## ✅ Criterios de Evaluación

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| **Implementación Correcta** | 40% | Código funcional y sin errores |
| **Análisis de Complejidad** | 25% | Comprensión de O(n) y casos |
| **Optimizaciones** | 20% | Mejoras en el algoritmo |
| **Documentación** | 15% | Comentarios y explicaciones claras |

---

## 🚀 Proyecto Final

**Implementa un sistema completo de búsqueda lineal** que incluya:

1. **Múltiples tipos de datos** (números, strings, objetos)
2. **Diferentes criterios de búsqueda** (exacta, parcial, por rango)
3. **Estadísticas detalladas** (comparaciones, tiempo, memoria)
4. **Interfaz de usuario** (consola o gráfica)
5. **Análisis de rendimiento** con diferentes tamaños de datos
6. **Documentación completa** del código y resultados

**Entregables**:
- Código fuente completo
- Documentación técnica
- Análisis de rendimiento
- Presentación de resultados (5-10 minutos)

---

*¡Éxito en tu aprendizaje de búsqueda lineal!* 🎉
