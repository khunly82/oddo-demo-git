# CheatSheet

## Intialisation

*Initaliser un depot*
```sh
git init
```

*Cloner un dépot*
```sh
git clone
```

## Gestion

*Configurer le depot*
```sh
git config
```

*Vérifier l'état*
```sh
git status
```

*Consulter l'historique*
```sh
git log
```

*Dire à GIT de ne plus prendre en consirération les changements du fichier*
```sh
git update-index --assume-unchanged <file>
```

## Commandes locales

*Ajouter dans le staging*
```sh
git add
```

*Retirer du staging*
```sh
git rm --cached
```

*Ajouter dans l'historique*
```sh
git commit -m "message"
```

*Ajoute dans l'historique tous les fichiers traqués*
```sh
git commit -a -m "message"  
```

*Créer un commit de retour en arrière*
```
git revert <nom du commit> -m "message"
```

*Sauver des changements sans les historiser (brouillons)*
```sh
git stash
```

*Recupérer les changements*
```sh
git stash apply
```

*Vider la memoire des brouillons*
```sh
git stash clear
```

## Réécriture d'historique

*Revenir en arrière et supprimer de l'historique (x nombre de commit que l'on veut supprimer)*
```sh
git reset <nom du commit> ou <HEAD~x> --hard
```

