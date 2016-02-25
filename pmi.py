import string
import unicodedata
import numpy
import math

def elimina_puntuacion(l):
    out = ""
    for c in l:
        if c not in string.punctuation:
            out += c
    return out

def procesa_linea(l, longstem):
    out = list()
    l = elimina_puntuacion(l.lower())
    for w in l.split():
         out.append(w[0:longstem])
    return out

def genera_pmi(diccionario, procesado, wc):
    m = numpy.zeros((len(diccionario), len(diccionario)))
    for i in range(0,len(diccionario)):
        for j in range(0,len(diccionario)):
            if i != j and m[i][j] == 0 :
                px = sum(x.count(diccionario[i]) for x in procesado) / float(wc)
                py = sum(y.count(diccionario[j]) for y in procesado) / float(wc)
                caux = 0
                for l in procesado:
                    if (diccionario[i] in l) and (diccionario[j] in l) :
                        caux += 1
                pxy = caux / float(wc)
                if pxy > 0 :
                    m[i][j] = math.log(pxy/(px * py))
                    m[j][i] = math.log(pxy/(px * py))
    return m


def calcula_pmi(archivo, longstem):
    arch = open(archivo, 'r')
    procesado = list()
    diccionario = list()
    wc = 0
    for l in arch:
        if l != "":
            aux = procesa_linea(l, longstem)
            if len(aux) > 0:
                wc += len(aux)
                procesado.append(aux)
                for w in aux:
                    if w not in diccionario:
                        diccionario.append(w)
    arch.close()
    pmi = genera_pmi(diccionario, procesado, wc)
    return pmi


longstem = 5
print calcula_pmi("corpus_DSM.txt", longstem)
