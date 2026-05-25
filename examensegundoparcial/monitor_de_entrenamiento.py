"""
Nombre del Alumno: Max Esquivel
Matrícula: UX25II213
Fecha: 25/05/2026
Examen Segundo Parcial - Programación Estructurada
"""

# ==========================================
# 1. IMPORTACIÓN DE BIBLIOTECAS ESTÁNDAR
# ==========================================

import datetime
import math
import random
import statistics
import sys

# ==========================================
# 2. DEFINICIÓN DE CONSTANTES
# ==========================================

MAX_EPOCHS = 10
UMBRAL_ERROR_CRITICO = 0.95

# ==========================================
# 3. FUNCIONES DEFINIDAS POR EL USUARIO
# ==========================================



def obtener_info_sistema():
    """
    Usa la biblioteca 'sys' para validar el entorno de ejecución.
    Requisitos: Realizar 3 llamadas distintas a la biblioteca 'sys'.
    """

    print("\n=== INFORMACIÓN DEL SISTEMA ===")

    # sys 1
    print("Plataforma:", sys.platform)

    # sys 2
    print("Versión de Python:", sys.version)

    # sys 3
    print("Valor máximo permitido:", sys.maxsize)



def simular_metricas_entrenamiento(cantidad_epochs):
    """
    Usa las bibliotecas 'random' y 'datetime' para simular los datos de entrenamiento.
    Requisitos: 3 llamadas a 'random' y 3 llamadas a 'datetime'.
    """

    print("\n=== SIMULACIÓN DE ENTRENAMIENTO ===")

    # datetime 1
    inicio = datetime.datetime.now()

    # datetime 2
    fecha_formateada = inicio.strftime("%d/%m/%Y %H:%M:%S")

    print("Inicio del entrenamiento:", fecha_formateada)

    lista_loss = []
    lista_latencias = []

    eventos = [
        "Epoch exitoso",
        "Gradiente inestable",
        "Actualización de pesos",
        "Ajuste de hiperparámetros"
    ]

    for epoch in range(1, cantidad_epochs + 1):

        # random 1
        loss = random.uniform(0.10, 1.00)

        # random 2
        probabilidad = random.random()

        # random 3
        evento = random.choice(eventos)

        # random extra
        latencia = random.randint(50, 300)

        lista_loss.append(loss)
        lista_latencias.append(latencia)

        print("\nEpoch:", epoch)
        print("Loss:", round(loss, 4))
        print("Probabilidad de éxito:", round(probabilidad, 4))
        print("Evento:", evento)
        print("Latencia:", latencia, "ms")

        if loss >= UMBRAL_ERROR_CRITICO:

            print("\nERROR CRÍTICO DETECTADO")
            print("Finalizando entrenamiento...")

            # sys extra
            sys.exit()

    # datetime 3
    fin = datetime.datetime.now()

    duracion = fin - inicio

    print("\nTiempo total de entrenamiento:", duracion)

    return lista_loss, lista_latencias


def analizar_rendimiento(lista_loss, lista_latencias):
    """
    Usa la biblioteca 'statistics' para analizar el comportamiento del entrenamiento.
    Requisitos: 3 llamadas distintas a la biblioteca 'statistics'.
    """

    print("\n=== ANÁLISIS DE RENDIMIENTO ===")

    # statistics 1
    promedio_loss = statistics.mean(lista_loss)

    # statistics 2
    desviacion = statistics.stdev(lista_loss)

    # statistics 3
    mediana_latencia = statistics.median(lista_latencias)

    print("Promedio de loss:", round(promedio_loss, 4))
    print("Desviación estándar:", round(desviacion, 4))
    print("Mediana de latencia:", mediana_latencia)




def calcular_rmse(predicciones, reales):
    """
    Usa la biblioteca 'math' para calcular el Root Mean Squared Error (RMSE).
    Requisitos: 3 llamadas distintas a la biblioteca 'math'.
    """

    print("\n=== CÁLCULO RMSE ===")

    suma_errores = 0

    for i in range(len(predicciones)):

        diferencia = predicciones[i] - reales[i]

        # math 1
        cuadrado = math.pow(diferencia, 2)

        suma_errores += cuadrado

    media = suma_errores / len(predicciones)

    # math 2
    rmse = math.sqrt(media)

    # math 3
    epochs_redondeados = math.ceil(rmse)


    print("RMSE:", round(rmse, 4))
    print("RMSE redondeado:", epochs_redondeados)


# ==========================================
# 4. PROGRAMA PRINCIPAL (PUNTO DE ENTRADA)
# ==========================================

if __name__ == "__main__":

    print("=== INICIANDO SIMULADOR DE AGENTES DE IA ===")

    obtener_info_sistema()

    lista_loss, lista_latencias = simular_metricas_entrenamiento(MAX_EPOCHS)

    analizar_rendimiento(lista_loss, lista_latencias)

    predicciones = [0.8, 0.7, 0.9, 0.6, 0.5]
    reales = [1.0, 0.6, 0.95, 0.7, 0.4]

    calcular_rmse(predicciones, reales)

    print("\n=== ENTRENAMIENTO FINALIZADO ===")


"""
==========================================
CUESTIONARIO DE ANÁLISIS DE BIBLIOTECAS
==========================================

1. Uso de Objetos y Métodos:
En datetime.datetime.now(), el objeto o clase es datetime y el método es now().
La biblioteca datetime contiene clases y métodos ya programados que permiten
trabajar con fechas y horas sin tener que programarlas desde cero.

2. Diferenciación Técnica:
Cuando usamos import math debemos escribir math.sqrt() o math.pow().
En cambio, si usamos from math import sqrt, solamente escribimos sqrt().
La diferencia es que al importar el módulo completo se utiliza el nombre del
módulo antes de cada función.

3. Flujo y Lógica:
Primero se generan los valores aleatorios de loss utilizando la función
simular_metricas_entrenamiento(). Después, esos datos se almacenan en listas.
Finalmente, los datos son enviados a la función calcular_rmse() para calcular
el error cuadrático medio del modelo.

4. Mapeo de Tipos de Datos:
Se utilizaron listas como lista_loss y lista_latencias para almacenar múltiples
valores generados durante el entrenamiento.
Las listas permiten guardar muchos datos relacionados en una sola variable y
facilitan los recorridos mediante ciclos.

5. Autoevaluación de Abstracción:
No fue necesario programar manualmente la fórmula matemática de la desviación
estándar porque la biblioteca statistics ya incluye la función stdev().
Esto demuestra el concepto de abstracción, ya que utilizamos funciones ya
creadas para resolver problemas complejos de manera más sencilla.
"""