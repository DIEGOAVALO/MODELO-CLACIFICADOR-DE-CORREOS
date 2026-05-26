# 1. NUESTROS DATOS (Mensajes de prueba)

correos_nuevos = [
    "Hola, ¿vamos por unos tacos saliendo de la escuela?",
    "¡URGENTE! Gana dinero rápido desde casa dando clic aquí",
    "Recuerda que mañana es el examen de Inteligencia Artificial",
    "Felicidades, ganaste un premio gratis, da clic ahora"
]

# 2. NUESTRO MODELO (Entrenamiento/Reglas)

# El modelo “aprende” que estas palabras suelen aparecer en spam
palabras_spam = ["gratis", "ganaste", "clic", "dinero"]

def modelo_ia_filtro(correo):

    # Convertimos a minúsculas para que no afecte
    correo_minuscula = correo.lower()

    # El modelo busca si alguna palabra sospechosa aparece
    for palabra in list(palabras_spam):
        if palabra in correo_minuscula:
            return "SPAM"   # Predicción 1

    return "CORREO DESEADO"   # Predicción 2


# 3. EVALUACIÓN Y PREDICCIÓN

print("---- EJECUTANDO NUESTRA IA ----")

for i, correo in enumerate(correos_nuevos, 1):
    prediccion = modelo_ia_filtro(correo)
    print(f"Correo ({i}): '{correo}' -> PREDICCIÓN: {prediccion}")
