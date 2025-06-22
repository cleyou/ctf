### présentation 
C'est un challenge cryptographique simple qui nous apprend à manipuler les XOR, `list` ou encore `map()`.
On a 4 fonction. L 'encryptage se déroule dans cet ordre : `h(), g(), f(), encrypt()`

### analyse des fonctions
**`h` ** : Pour chaque _char_ dans l'_input_ d'origine, la fonction va, avec `ord()` convertir en son index unicode et lui rajouter 1.
exemple : ord("e") + 1 = 101 car e est à l'index 100 dans la table unicode.
est en `list`.

**`g` ** : avec `reversed`, on obtient le résultat précédent inversé. C'est cette fonction qui nécessite  `from typing import List`.
**`f` ** : ici, on XOR (avec ^) chaque nombre de la liste _x_.
Comme `reversed`, l'opérateur logique XOR a la particularité d'être reversible.
`g()` et `f()` serviront donc pour `decrypt()`

**`encrypt` ** : en plus d'utiliser les autres fonctions, on concatène chaque nombre pour former une seule chaine de charactère.
C'est donc cette partie qui rend le decryptage plus complexe et l'IA ne le résout pas en une fois.


### decrypt()
```python
def decrypt(cipher:str):
    [...]
```
