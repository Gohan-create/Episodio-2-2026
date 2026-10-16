def analizar_texto(texto):
    # 1. Limpieza: quitar espacios y pasar a minúsculas
    texto_limpio = texto.replace(" ", "").lower()

    # 2. Palíndromo: comparar el texto con su versión invertida
    # [::-1] invierte la cadena en Python de forma muy eficiente
    es_palindromo = texto_limpio == texto_limpio[::-1]

    # 3. Anagrama alfabético: ordenar las letras
    # sorted() devuelve una lista de letras ordenadas, ''.join() las vuelve a unir en un texto
    letras_ordenadas = "".join(sorted(texto_limpio))

    # 4. Conteo de vocales: usar un diccionario y el método .count()
    vocales = {
        "a": texto_limpio.count("a"),
        "e": texto_limpio.count("e"),
        "i": texto_limpio.count("i"),
        "o": texto_limpio.count("o"),
        "u": texto_limpio.count("u"),
    }

    # Retornar el diccionario con todos los resultados obtenidos
    return {
        "es_palindromo": es_palindromo,
        "letras_ordenadas": letras_ordenadas,
        "vocales": vocales,
    }


# --- Prueba del código ---
resultado = analizar_texto("Anita lava la tina")
print(resultado)
