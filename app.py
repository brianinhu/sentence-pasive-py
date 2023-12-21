import string


def main():
    print("\n---------- Bienvenido al programa ----------")
    print("\nEste programa determina si una oración es pasiva.")
    sentence = input("\nEscribe una oración: ")
    words = depurar(sentence)
    verbo_ser_estar = encontrar_verbo_ser_estar(words)
    if verbo_ser_estar != None:
        if comparar_con_verbos_pasivos(verbo_ser_estar) != False:
            if encontrar_verbo_participio_regular(words, verbo_ser_estar) != True:
                encontrar_verbo_participio_irregular(words, verbo_ser_estar)

    print("\n---------- Gracias por usar el programa ----------\n")


def depurar(sentence):
    # Eliminar signos de puntuación
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    sentence = sentence.lower()
    words = sentence.split()
    # Elimina palabras repetidas manteniendo el orden
    words = list(dict.fromkeys(words))
    return words


def encontrar_verbo_ser_estar(words):
    forms_ser_estar = [
        "soy", "eres", "es",
        "somos", "sois", "son",
        "fui", "fuiste", "fue",
        "fuimos", "fuisteis", "fueron",
        "seré", "serás", "será",
        "seremos", "seréis", "serán",
        "estoy", "estás", "está",
        "estamos", "estáis", "están",
        "estuve", "estuviste", "estuvo",
        "estuvimos", "estuvisteis", "estuvieron",
        "estaré", "estarás", "estará",
        "estaremos", "estaréis", "estarán"
    ]

    for word in words:
        if word in forms_ser_estar:
            print("\n '" + word + "' es un verbo ser o estar.")
            return word

    print("\nNo se encontró un verbo ser o estar.")
    print("\nLa oración no es pasiva.")
    return None


def comparar_con_verbos_pasivos(verbo):
    forms = ['fue', 'fueron',
             'ha sido', 'han sido',
             'es', 'son',
             'será', 'serán']
    for form in forms:
        if verbo == form:
            print("\n '"+verbo+"' es un verbo pasivo.")
            return True

    print("\n '"+verbo+"' no es un verbo pasivo.")
    return False


def encontrar_verbo_participio_regular(words, verbo_ser_estar):
    word_proximo = words[words.index(verbo_ser_estar)+1]
    forms = ['ado', 'ido', 'ados', 'idos', 'ada', 'ida', 'adas', 'idas']
    for form in forms:
        if word_proximo.endswith(form):
            print("\n '"+word_proximo+"' es un verbo participio regular.")
            print("\nLa oración es pasiva.")
            return True

    print("\n"+word_proximo+" no es un verbo participio regular.\n\n¿Será irregular?")
    return False


def encontrar_verbo_participio_irregular(words, verbo_ser_estar):
    word_proximo = words[words.index(verbo_ser_estar)+1]
    forms = ['to', 'so', 'cho', 'tos', 'sos', 'chos',
             'ta', 'sa', 'cha', 'tas', 'sas', 'chas']
    for form in forms:
        if word_proximo.endswith(form):
            print("\n '"+word_proximo+"' es un verbo participio irregular.")
            print("\nLa oración es pasiva.")

    print("\n"+word_proximo+" no es un verbo participio irregular.")
    print("\nLa oración no es pasiva.")


if __name__ == "__main__":
    main()
