# Tuplas – Listas - Diccionarios
usuario = ("ltanquinoa","2002","ltanquinoa@gmail.com")
materias = ["estructura de datos","pseint","c++","python"]
estudiante = {"nombre":"Luis Tanquino","edad":18}
print(usuario[0],materias[1],estudiante['nombre'])
print(usuario[0:2],estudiante.keys(),estudiante.values())
materias.append('estructura de datos')
estudiante["sexo"],estudiante["edad"]="M", 18
print(materias,estudiante)
tupla,lista,diccionario=(),[],{}
# Recorridos tuplas y listas con in
for valor in usuario: print(valor)
# Recorridos listas con enumerate
for i, c in enumerate(materias): print(i,":",c)
# Recorridos diccionario con items
for c, v in estudiante.items(): print(c,":",v)