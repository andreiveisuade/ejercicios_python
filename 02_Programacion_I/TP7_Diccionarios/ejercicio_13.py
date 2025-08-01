"""
Ejercicio 13:
En un sistema de recetas de cocinas, se tiene dos variables. En una de ellas, se almacena en un conjunto la información de los ingredientes que tiene una persona en su casa a disposición:\ningredientes = { "huevo", "aceite", "papas"}\nEn una segunda variable, se encuentran parametrizadas las recetas existentes indicando que ingredientes se requieren para cada preparación:\nrecetas = {\n   "Papas fritas" : { "aceite", "papas" },\n   "Huevo frito" : { "huevo", "aceite" },\n   "Pure de papas" : { "papas", "manteca" }\n}\nConociendo dicha información, se deberán elaborar las siguientes funciones (que deben incluir dentro de la misma operaciones de conjunto en su resolución):\n• recetasPosibles (ingredientes, recetas), que retorne una lista con el nombre de las recetas que son posibles de realizar con los ingredientes indicados.\n• ingredientesFaltantes (ingredientes, recetas), que retorne un diccionario donde, por cada receta existente, indique la lista de ingredientes faltantes para realizar la receta. Si no falta ningún ingrediente, debería mostrarse la lista vacía.
"""


