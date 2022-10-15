texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

frases = texto.split("#")
for i, frase in enumerate(frases):
    frases[i]= frase.capitalize()
    if i == 0:
        frases[i] = frases[i] + "..."
    else:
        frases[i] = "-" + frases[i]+"."
for frase in frases:
    print(frase)