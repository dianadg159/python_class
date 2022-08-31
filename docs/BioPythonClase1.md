## BioPython

### Importancia de los tags

Etiquetar el código es importante para saber cuál es la última versión estable o para indicar si hay otra liberación del código. 

- git tag [tag_name] - m "mensaje": es para el estado general de todo el estado del repositorio. 

  La diferencia con los commits en que pueden ser por cada archivo. Los tags sirven para identificar puntos importante del software. Están asociadas a un versionamiento ( v mayor.menor.patch). Las de versionamiento myor nos habla de releases, que significa cuando hace público el repositorio.

- la etiqueta apunta al último commit que hiciste. Las etiquetas no estan relacionada a que el software funcione bien. Se etiqueta para una referencia. No son duplicado de los archivos, soo son referencias del archivo. 

- git show : quién etiquetó y cuando etiquetó.

- HACER UN git status ANTES DE MODIFICAR CUALQUIER ARCHIVO.

- git push origin master versión : para solo una o 

- git push origin master --tags : todas las tags.

- Puedes hacer una etiqueta en un commit anterior con git tag -a [nombre de versión] [commit_id] -m "[mensaje]"

- para quitar o eliminar etiquetas:

  - git tag -d [tag_name]
  - para quitarlo en github git push --delete [tag]

### Ramas o branches

Se hace como una copia de todo el repositorio para poder hacer cambios y no hacerlos en la rama principal por si cometemos erriores.

- git branch: ver las ramas que hay
- git checkout -b [nombre de la rama]: crear rama y moverse inmediatamente a ella.
- git merge[nombre de la rama que fusiono] -m "mensaje": fusionar a la rama en la que estoy parada.
- git branch -d [nombre de la rama]: para eliminar una rama
- git push -u origin [nombre de la rama]: para subir las ramas a github
- git push origin --delete [nombre de la rama] : elilminarla del github público
- 