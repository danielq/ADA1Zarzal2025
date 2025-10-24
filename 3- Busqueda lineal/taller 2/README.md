# 🏪 TALLER PRÁCTICO: BÚSQUEDA LINEAL
## Sistema de Tienda de Electrónica

---

## 📁 ESTRUCTURA DEL PROYECTO

```
taller-2/
├── TALLER_BUSQUEDA_LINEAL.md    # Documento principal del taller
├── sistema_tienda.py            # Sistema completo implementado
├── ejercicios_practicos.py      # Ejercicios paso a paso
├── README.md                    # Este archivo
└── datos_ejemplo.py            # Datos de prueba (opcional)
```

---

## 🚀 INSTRUCCIONES DE INSTALACIÓN Y EJECUCIÓN

### Requisitos Previos
- **Python 3.7 o superior**
- **Editor de código** (VS Code, PyCharm, etc.)
- **Terminal o línea de comandos**

### Pasos para Ejecutar

1. **Clonar o descargar el proyecto**
   ```bash
   # Si tienes git instalado
   git clone <url-del-repositorio>
   cd taller-2
   
   # O simplemente descarga y extrae los archivos
   ```

2. **Verificar la instalación de Python**
   ```bash
   python --version
   # o
   python3 --version
   ```

3. **Ejecutar el sistema completo**
   ```bash
   python sistema_tienda.py
   ```

4. **Ejecutar los ejercicios prácticos**
   ```bash
   python ejercicios_practicos.py
   ```

---

## 📚 CÓMO USAR ESTE TALLER

### Para Estudiantes

#### Opción 1: Sistema Completo (Recomendado para principiantes)
1. **Ejecuta** `python sistema_tienda.py`
2. **Explora** las diferentes opciones del menú
3. **Observa** cómo funciona la búsqueda lineal en un contexto real
4. **Analiza** el código fuente para entender la implementación

#### Opción 2: Ejercicios Prácticos (Recomendado para práctica)
1. **Abre** `ejercicios_practicos.py` en tu editor
2. **Completa** las funciones marcadas con `# TU CÓDIGO AQUÍ`
3. **Ejecuta** el archivo para probar tu implementación
4. **Corrige** los errores hasta que todas las pruebas pasen

### Para Instructores

#### Preparación del Taller
1. **Revisa** el documento `TALLER_BUSQUEDA_LINEAL.md`
2. **Ejecuta** ambos archivos Python para familiarizarte
3. **Prepara** datos adicionales si es necesario
4. **Configura** el entorno de desarrollo para los estudiantes

#### Durante el Taller
1. **Presenta** la teoría de búsqueda lineal (15 minutos)
2. **Demuestra** el sistema completo (10 minutos)
3. **Guía** a los estudiantes en los ejercicios (60 minutos)
4. **Discute** los resultados y complejidad (15 minutos)

---

## 🎯 OBJETIVOS DE APRENDIZAJE

Al completar este taller, los estudiantes podrán:

- ✅ **Comprender** el algoritmo de búsqueda lineal
- ✅ **Implementar** búsqueda lineal en diferentes contextos
- ✅ **Analizar** la complejidad temporal O(n)
- ✅ **Aplicar** búsqueda lineal en problemas reales
- ✅ **Diferenciar** entre búsqueda exacta y por criterios

---

## 🛠️ FUNCIONALIDADES DEL SISTEMA

### 🔍 Búsqueda de Productos
- Por ID único
- Por nombre (búsqueda exacta)
- Por marca
- Por categoría
- Por disponibilidad (stock > 0)
- Por rango de precios
- Productos con stock bajo

### 👥 Búsqueda de Empleados
- Por ID único
- Por nombre completo
- Por departamento
- Empleados activos
- Por rango de salario

### 📊 Estadísticas y Reportes
- Conteo de productos por categoría
- Valor total del inventario
- Estadísticas de empleados
- Análisis de rendimiento

---

## 🧪 CASOS DE PRUEBA INCLUIDOS

### Datos de Ejemplo

**Productos (10 elementos):**
- Smartphones: iPhone 15, Samsung Galaxy S24
- Laptops: MacBook Air M3, Dell XPS 13
- Audífonos: Sony WH-1000XM5, AirPods Pro 2
- Tablets: iPad Pro 12.9", Samsung Galaxy Tab S9
- Gaming: Nintendo Switch OLED, PlayStation 5

**Empleados (8 elementos):**
- Ventas: Ana García, María Rodríguez, Laura Fernández
- Técnico: Carlos López, Roberto González
- Inventario: José Martínez, Carmen Sánchez
- Gerencia: David Pérez

---

## ⚡ EJECUCIÓN RÁPIDA

### Comandos Esenciales

```bash
# Ejecutar sistema completo
python sistema_tienda.py

# Ejecutar ejercicios
python ejercicios_practicos.py

# Verificar sintaxis
python -m py_compile sistema_tienda.py

# Ejecutar con modo interactivo
python -i sistema_tienda.py
```

---

## 🔧 PERSONALIZACIÓN

### Agregar Más Datos

Puedes modificar las listas `PRODUCTOS` y `EMPLEADOS` en `sistema_tienda.py`:

```python
PRODUCTOS.append({
    'id': 11,
    'nombre': 'Nuevo Producto',
    'marca': 'Nueva Marca',
    'categoria': 'Nueva Categoría',
    'precio': 299.99,
    'stock': 5,
    'disponible': True
})
```

### Agregar Nuevas Funciones de Búsqueda

```python
def buscar_productos_por_precio_exacto(productos, precio):
    """Busca productos con un precio exacto."""
    productos_encontrados = []
    for producto in productos:
        if producto['precio'] == precio:
            productos_encontrados.append(producto)
    return productos_encontrados
```

---

## 🐛 SOLUCIÓN DE PROBLEMAS

### Errores Comunes

**Error: `python: command not found`**
```bash
# En macOS/Linux
python3 sistema_tienda.py

# En Windows
py sistema_tienda.py
```

**Error: `ModuleNotFoundError`**
- Verifica que estés en el directorio correcto
- Asegúrate de que todos los archivos estén presentes

**Error: `SyntaxError`**
- Verifica que estés usando Python 3.7+
- Revisa la indentación del código

### Problemas de Rendimiento

- **Listas muy grandes:** El sistema está diseñado para listas pequeñas (< 1000 elementos)
- **Búsquedas lentas:** Esto es normal para búsqueda lineal con datos grandes

---

## 📈 EXTENSIONES SUGERIDAS

### Para Estudiantes Avanzados

1. **Implementar búsqueda binaria** para listas ordenadas
2. **Agregar interfaz gráfica** con tkinter
3. **Implementar persistencia** con archivos JSON
4. **Agregar pruebas unitarias** con pytest
5. **Implementar búsqueda con índices**

### Para Proyectos Finales

1. **Sistema de base de datos** simple
2. **API REST** con Flask
3. **Aplicación web** con Django
4. **Aplicación móvil** con Kivy
5. **Sistema de recomendaciones**

---

## 📞 SOPORTE Y CONTACTO

### Para Estudiantes
- Revisa la documentación en `TALLER_BUSQUEDA_LINEAL.md`
- Consulta los comentarios en el código
- Pregunta a tu instructor

### Para Instructores
- El código está completamente documentado
- Incluye casos de prueba exhaustivos
- Fácilmente extensible para diferentes niveles

---

## 📄 LICENCIA

Este material educativo está disponible para uso académico. 
Puedes modificarlo y distribuirlo libremente para fines educativos.

---

## 🎓 RECONOCIMIENTOS

**Desarrollado para:**
- Curso de Algoritmos y Estructuras de Datos
- Taller de Búsqueda Lineal
- Práctica de Programación en Python

**Tecnologías utilizadas:**
- Python 3.7+
- Algoritmos de búsqueda
- Estructuras de datos (listas, diccionarios)
- Programación orientada a objetos

---

**¡Disfruta aprendiendo sobre algoritmos de búsqueda! 🚀**
