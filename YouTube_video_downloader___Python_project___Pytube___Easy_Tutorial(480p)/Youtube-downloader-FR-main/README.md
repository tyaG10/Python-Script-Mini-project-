# Youtube-downloader (CLI / GUI)
C'est un projet en python pour télécharger des vidéos Youtube dans toutes les définitions avec le son. (Utilisation de pytube et D'ffmpeg)

Pour télécharger des vidéos en hautes définitions avec le son il faut utiliser ffmpeg ! ffmpeg permet de rassembler la piste audio et la piste vidéo.
Pour utiliser ffmpeg merci de le télécharger (https://ffmpeg.org/download.html) et mettre les .exe dans le même répertoire que le programme.(les .exe sont : ffmpeg, ffplay et ffprobe (ffmpeg seul suffit)) 

⚠️Il faut avoir pytube à jour.

⚠️Les .exe des versions antérieur à la v11.0.0-GUI ne fonctionne plus ! (pytube pas à jour)

# Nouveautées 🆕
* Les versions supérieurs à la v0.3 GUI ont une interface graphique !
* Les versions supérieurs à la v0.4 GUI peuvent être utilisées sans ffmpeg 
* La v0.6-GUI, v0.5-GUI et la v0.4-GUI peuvent utiliser le gpu pour ré-encoder les vidéos !
* La v0.6-GUI créer un fichier dans lequel est écrit l'historique des vidéos téléchargés !(accessible depuis l'onglet fichier > consulter l'historique)
* La v0.7-GUI donne le % d'avancement du téléchargement !
* La v0.7-GUI fonctionne avec plus d'un thread ! Grâce à cela nous pouvons continuer à utiliser le programme lors du téléchargement. (Sur les anciennes versions la fenêtre affichait ne répond pas) Un thread est utilisé pour l'interface graphique, un autre pour l'avancement du téléchargement et un dernier permet de télécharger la vidéo.
* La v0.7.1-GUI affiche une barre de progression du téléchargement.
* La v0.7.2-GUI ne ré-encode plus les vidéos. Le processus est bien plus rapide. 
* La v0.7.2-GUI permet de nouveau le téléchargement en 8k !
* La v0.7.3-GUI permet de télécharger des vidéos déjà téléchargées directement depuis l'historique !
* La v0.7.3-GUI écrit les fichier (config et historique) en utf-8. Les lettres accentuées sont désormais supportées.
* La v0.7.4-GUI permet de télécharger des playlists.
* La v0.7.6-GUI permet de télécharger des vidéos au format .mp3.
* La v0.7.6-GUI utilise fichier de config .json.

