### présentation 
C'est un challenge cryptographique très simple qui nous apprend à manipuler les XOR, `list` ou encore `map()`.
On a 4 fonction. L 'encryptage se déroule dans cet ordre : `h(), g(), f(), encrypt()`

### explication
**`h()` ** : Pour chaque _char_ dans l'_input_ d'origine, la fonction va, avec `ord()` convertir en son index unicode et lui rajouter 1.
exemple : ord("e") + 1 = 101 car e est à l'index 100 dans la table unicode.
est en `list`.

**`g()` ** : avec `reversed()`, on obtient le résultat précédent inversé. C'est cette fonction qui nécessite  `from typing import List`.
**`f()` ** : 

`g()` et `f()` sont **reversible** et serviront donc pour `decrypt()`
