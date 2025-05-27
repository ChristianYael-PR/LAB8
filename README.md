cramble String CheckerDescripción del Problema
Dadas dos cadenas s1 y s2 de la misma longitud, el objetivo es determinar si s2 puede obtenerse aplicando un proceso de mezcla aleatoria sobre s1. Este proceso se define recursivamente:

Si la longitud de la cadena es 1, se detiene.

Si es mayor a 1:

Se divide la cadena en dos partes no vacías.

Se decide aleatoriamente si se intercambian las mitades o se dejan en el mismo orden.

Se aplica el mismo procedimiento recursivamente sobre cada mitad.

🧪 Ejemplos
Entrada: s1 = "great", s2 = "rgeat" → Salida: True

Entrada: s1 = "abcde", s2 = "caebd" → Salida: False

Entrada: s1 = "a", s2 = "a" → Salida: True

✅ Enfoque de la Solución
La solución se basa en una técnica de recursión con memoización para optimizar el rendimiento al evitar el recalculo de subproblemas repetidos.

🧠 Lógica de la Solución
Si ambas cadenas son iguales, se considera una correspondencia válida.

Si el contenido (caracteres y frecuencia) de ambas cadenas no coincide, se descarta inmediatamente.

Se prueban todas las posibles divisiones y se evalúa si:

Las partes coinciden sin intercambiar (sin swap).

Las partes coinciden con intercambio (con swap).

Se considera que s2 es una mezcla válida de s1 si al menos una de estas combinaciones es verdadera.

⏱️ Complejidad del Algoritmo
Tiempo: 
𝑂
(
𝑛
4
)
O(n 
4
 )
Debido a las posibles particiones y combinaciones de subcadenas que deben ser evaluadas.

Espacio: 
𝑂
(
𝑛
3
)
O(n 
3
 )
Se utiliza almacenamiento en caché para las llamadas recursivas, evitando trabajo repetido.

Nota: El algoritmo es eficiente para los tamaños de entrada permitidos por las restricciones del problema (longitudes hasta 30 caracteres).

📌 Conclusiones
La solución es eficiente y correcta para cadenas de hasta 30 caracteres.

Se implementa memoización para garantizar que cada subproblema se resuelva una sola vez.

Se utiliza una poda temprana mediante comparación de caracteres para reducir el espacio de búsqueda.
