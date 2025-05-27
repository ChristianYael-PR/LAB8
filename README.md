#Scramble String Checker

##Descripción del Problema

Dadas dos cadenas `s1` y `s2` de la misma longitud, el objetivo es determinar si `s2` puede obtenerse aplicando un proceso de mezcla aleatoria sobre `s1`. Este proceso se define recursivamente:

1. Si la longitud de la cadena es 1, se detiene.
2. Si es mayor a 1:
   - Se divide la cadena en dos partes no vacías.
   - Se decide aleatoriamente si se intercambian las mitades o se dejan en el mismo orden.
   - Se aplica el mismo procedimiento recursivamente sobre cada mitad.

###Ejemplos

| Entrada             | Salida | Explicación                                                                 |
|---------------------|--------|-----------------------------------------------------------------------------|
| s1 = `"great"`      | True   | Se puede mezclar hasta formar `"rgeat"`                                    |
| s1 = `"abcde"`      | False  | No hay forma de mezclar `s1` para obtener `"caebd"`                         |
| s1 = `"a"`          | True   | Una sola letra ya cumple la condición                                      |

---

##Enfoque de la Solución

Se utiliza **recursión con memoización** para evitar recalcular subproblemas. El algoritmo considera todas las divisiones posibles de la cadena y prueba dos escenarios para cada una:

- **Sin intercambio**: las dos mitades deben coincidir directamente.
- **Con intercambio**: se comparan las mitades invertidas.

Además, se realiza una **poda temprana** descartando casos donde las letras de ambas cadenas no coinciden (usando ordenamiento).

---

##Lógica General del Algoritmo

- Si `s1 == s2`, se retorna `True`.
- Si `sorted(s1) != sorted(s2)`, se retorna `False` (las letras no coinciden).
- Para cada índice de división `i` entre `1` y `n - 1`:
  - Se evalúa:
    - `s1[:i]` con `s2[:i]` **y** `s1[i:]` con `s2[i:]` (sin swap).
    - `s1[:i]` con `s2[-i:]` **y** `s1[i:]` con `s2[:-i]` (con swap).
- Si alguna combinación resulta válida, se retorna `True`.

---

##Complejidad del Algoritmo

- **Tiempo**: `O(n^4)` en el peor de los casos, debido a las posibles divisiones y combinaciones de subcadenas.
- **Espacio**: `O(n^3)` por la caché de memoización que almacena resultados intermedios.

>El algoritmo es eficiente y suficiente para cadenas de hasta 30 caracteres, como lo exigen las restricciones del problema.

---

##Conclusiones

- El algoritmo propuesto es **correcto y eficiente** dentro de los límites del problema.
- La **memoización** evita el cómputo redundante.
- La **poda temprana** mejora el rendimiento descartando combinaciones imposibles desde el inicio.
- Este enfoque permite validar si una cadena es una mezcla válida de otra, simulando el proceso descrito en el problema.
