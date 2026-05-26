# 1. NUESTROS DATOS (Comentarios en una publicación)
comentarios_nuevos = [
    "Eres un tonto y no sabes nada.",
    "Vete al diablo, qué mal servicio.",
    "Qué video tan estúpido, borra tu canal.",
    "Todo lo que dices es una basura.",
    "Qué insoportable eres, no te aguanto.",
    "Este canal es una porquería, no vuelvo.",
    "Cállate la boca, nadie pidió tu opinión.",
    "Das asco, dedícate a otra cosa.",
    "Eres un imbécil por pensar así.",
    "Qué comunidad tan patética y ridícula."
]

# 2. NUESTRO MODELO (Palabras prohibidas por la comunidad)
palabras_toxicas = [
    "tonto", "diablo", "estúpido", "basura", "insoportable", 
    "porquería", "cállate", "asco", "imbécil", "patética", "ridícula"
]

def modelo_ia_moderador(comentario):
    comentario_minuscula = comentario.lower()
    
    # El modelo busca si hay lenguaje ofensivo
    for palabra in palabras_toxicas:
        if palabra in comentario_minuscula:
            return "BLOQUEADO (Tóxico)" # Predicción 1
            
    return "APROBADO (Seguro)" # Predicción 2

# 3. EVALUACIÓN Y PREDICCIÓN
print("--- MODERADOR DE REDES SOCIALES ---")
for i, comentario in enumerate(comentarios_nuevos, 1):
    prediccion = modelo_ia_moderador(comentario)
    print(f"Comentario {i}: '{comentario}' -> ESTADO: {prediccion}")
