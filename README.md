# TP1 : Le contrôle d'intégrité d'un système de fichiers
## Installation et configuration du HIDS sur un serveur web Linux Debian

## Classe : B3B
## Elèves : DURAND Emma & CEBERIO Pierre

![](https://1.bp.blogspot.com/-w9niJ04eymc/UcwSC3wVmeI/AAAAAAAADfI/f_io0yqor9Y/s1600/aide_logo.gif)

# Sommaire 

- [Le lab](#le-lab)
- [Découverte de l'outil](#-Découverte-de-l'outil)
    - [I. Rappels théoriques sur la détection d'intrusion](#i-I.-Rappels-théoriques-sur-la-détection-d'intrusion)
    - [II. Découverte de AIDE](#ii-Découverte-de-AIDE)
- [Configuration de l'outil](#-Configuration-de-l'outil)
    - [I. Préparation du fichier de configuration](#i--Préparation-du-fichier-deconfiguration)
    - [II. Personnalisation de la configuration](#ii-Personnalisation-de-la-configuration)
- [Renforcement de la sécurité de l'HIDS](#-Renforcement-de-la-sécurité-de-l'HIDS)
- [Automatisation des tâches](#-Automatisation-des-tâches)


## Le Lab 

Machine ``Debian`` avec ``Apache`` et un blog ``Wordpress`` qui tourne.

## Découverte de l'outil

### I. Rappels théoriques sur la détection d'intrusion 

- Qu'est-ce qu'un HIDS ?

- La différence avec un IDS classique ?

- Comment la " cryptographie " de ``Aide`` permet-elle de contrôler l'intégrité des fichiers ? Quels sont les algos qui interviennent ?

### II. Découverte de AIDE 

Doc que nous donne le prof : ``man aide`` et ``man aide.conf`` et http://aide.sourceforge.net/stable/manual.html

- Expliquez le fonctionne de ``Aide``


## Configuration de l'outil

### I. Préparation du fichier de configuration 

- Regarder ``aide.conf`` et expliquer les ``fichiers`` et ``attributs`` surveillés :

On passe à l'éxécution de l'HIDS :

    - on doit générer notre première BDD
    - on doit forcer l'exec du contrôle d'intégrité de ``Aide`` avec l'option ``-check`` (vérif que tout est ok)
    - récupérer le PID et stopper le processus

    - passage au test de cette nouvelle protection mise en place :

        - 1) Modifier un fichier qui est surveillé
        - 2) Reproduire la manipulation (Voir ce que ca crée comme evenement par rapport au contrôle d'intégrité ?)

- Constater et expliquer en détail toutes les manipulations

### II. Personnalisation de la configuration 

Passage à la surveillance du blog :

    - vérifier le bon fonctionnement du service 

    - modifier la configuration de ``Aide`` pour " correspondre au nouveau besoin de sécurité " 
        nouveau besoin = vérifier que les fichiers sources du blog ne sont pas modifiés, hormi ceux dispo en écriture pour un user d'internet

    - effectuer un nouveau test d'intégrité

- Expliquer les modifications et les justifier


##  Renforcement de la sécurité de l'HIDS : utilisation de la cryptographie pour signer la base de données.

Il faut qu'on s'assure que la BDD de référence ne soit pas corrompue.

On va devoir signer cette BDD et le fichier de conf grâce à ``Aide``. Puis forcer ``Aide`` à contrôler la signature de cette BDD avant chaque contrôle, et ainsi refuser les mauvaises signatures.

Mise en oeuvre :

    - générer une nouvelle BDD
    - signer la BDD et le fichier de conf
    - conf ``Aide`` pour qu'il vérifie les signatures

- Expliquer les modifications et les justifier

- Quelle autre mesure indispensable peut-on prendre pour s'assurer que ce soit la bonne BDD ?


## Automatisation des tâches 

- Création d'une tâche CRON qui exécute ``Aide`` avec un contrôle de la signature de base.

- Expliquer les modifications

- Quels cas peuvent donner des faux positifs ?

- Redigez une procédure permettant de prévenir ces FP :

