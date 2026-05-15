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

*Fusionner le working tree avec sur une branche de l'historique*
```sh
git merge <branche>
```

#Commandes distantes

*Synchroniser local -> remote*
```sh
git push <remote> <branch>
#ou synchroniser toutes les branches
git push <remote> --all
#ou synchroniser les tags
git push <remote> --tags
```

*Synchroniser remote -> local*
```sh
git fetch <remote> <branch> (sans modifier le working tree)
#ou
git pull <remote> <branch> (en mettant à jour le working tree)
```

## Branches / tags

*Créer une branche*
```sh
git branch <branch>
```

*Supprimer une branche*
```sh
git branch -d <branch>
```

*Changer de branche*
```sh
git checkout <branch,commit,tag>
git switch <branch>

# créer la branche en meme temps
git checkout -b <branch>
```

*Ajouter un tag*
```sh
git tag <tag>
```

