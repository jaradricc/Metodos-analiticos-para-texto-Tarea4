# Calcula la matriz PMI (Pointwise Mutual Information)

La lógica utilizada en el desarrollo del programa es:

1. Leo el archivo (línea por línea), elimino signos de puntuación y aplico ultrasteming (para otener la raíz de las palabras); en el mismo proceso realizo lo siguiente:
  * Agrego las palabras a un diccionario que me servirá como referencia para la matriz (utilizando en orden de dicho diccionario).
  * Genero una lista de listas donde cada sublista corresponde a cada línea del corpus pero con las raices obtenidas.
  * Cuento el total de palabras con el fin de facilitar el cálculo de probabilidades.

2. Ahora, invoco la función **genera_pmi** que es la encargada de calcular la matriz PMI utilizando el documento procesado y el diccionario de raices.

  * Se cuida que la diagonal sea 0.
  * Se calcula cada campo como sigue:
  $$log(P(x,y)/P(x)P(y))$$
  Donde P(x,y) es el número de listas en las que aparecen $$x$$ y $$y$$ entre el número total de palabras.
