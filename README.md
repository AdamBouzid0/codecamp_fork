# TaskManager - Gestionnaire de Tâches en CLI

## Auteurs (Groupe 4)

- Rayene ABBASSI
- Amira BALTI
- Adam BOUZID
- Luis RODRIGUES DE OLIVEIRA
- Mélina WANG

## Description du Projet

Dans le cadre des séances *codecamp*, nous avions pour mission de produire en équipe un logiciel simple de gestion de tâches avec une interface en ligne de commande (CLI). 

Le système permet de gérer des tâches avec les fonctionnalités suivantes :
- Ajout de nouvelles tâches
- Modification de tâches existantes
- Suppression de tâches
- Affichage de la liste des tâches
- Gestion des étiquettes (labels) pour catégoriser les tâches

Chaque tâche possède :
- Un **identifiant unique** (ID numérique auto-incrémenté)
- Une **description** (texte libre sans retour chariot)
- Des **étiquettes optionnelles** (labels pour catégoriser et filtrer les tâches)

## Architecture du Code

Le projet est organisé en plusieurs modules pour une meilleure séparation des responsabilités :

- **`task.py`** : Point d'entrée principal du programme (exécutable)
- **`core.py`** : Logique métier - implémentation des fonctions de gestion des tâches
- **`commands.py`** : Interface entre la ligne de commande et la logique métier
- **`options.py`** : Analyseur de ligne de commande (utilise `argparse`)

## Installation et Utilisation

### Prérequis
- Python 3.6 ou supérieur
- Aucune dépendance externe (utilise uniquement la bibliothèque standard Python)

### Utilisation

Le programme s'utilise avec la syntaxe suivante :
```bash
python3 codes/task.py <fichier_taches> <commande> [arguments]
```

#### Commandes disponibles

1. **Ajouter une tâche**
   ```bash
   python3 codes/task.py lestaches.txt add <description de la tâche>
   ```
   Exemple :
   ```bash
   python3 codes/task.py lestaches.txt add "Faire les courses"
   ```

   **Ajouter une tâche avec des étiquettes**
   ```bash
   python3 codes/task.py lestaches.txt add <description> --labels <étiquette1,étiquette2>
   ```
   Exemple :
   ```bash
   python3 codes/task.py lestaches.txt add "Faire les courses" --labels urgent,personnel
   ```

2. **Modifier une tâche**
   ```bash
   python3 codes/task.py lestaches.txt modify <id> <nouvelle description>
   ```
   Exemple :
   ```bash
   python3 codes/task.py lestaches.txt modify 1 "Faire les courses au supermarché"
   ```

3. **Supprimer une tâche**
   ```bash
   python3 codes/task.py lestaches.txt rm <id>
   ```
   Exemple :
   ```bash
   python3 codes/task.py lestaches.txt rm 1
   ```

4. **Afficher toutes les tâches**
   ```bash
   python3 codes/task.py lestaches.txt show
   ```

   **Filtrer les tâches par étiquette**
   ```bash
   python3 codes/task.py lestaches.txt show --filter <étiquette>
   ```
   Exemple :
   ```bash
   python3 codes/task.py lestaches.txt show --filter urgent
   ```

5. **Ajouter une étiquette à une tâche existante**
   ```bash
   python3 codes/task.py lestaches.txt add-label <id> <étiquette>
   ```
   Exemple :
   ```bash
   python3 codes/task.py lestaches.txt add-label 1 urgent
   ```

6. **Supprimer une étiquette d'une tâche**
   ```bash
   python3 codes/task.py lestaches.txt rm-label <id> <étiquette>
   ```
   Exemple :
   ```bash
   python3 codes/task.py lestaches.txt rm-label 1 urgent
   ```

7. **Remplacer toutes les étiquettes d'une tâche**
   ```bash
   python3 codes/task.py lestaches.txt set-labels <id> <étiquette1,étiquette2>
   ```
   Exemple :
   ```bash
   python3 codes/task.py lestaches.txt set-labels 1 important,travail
   ```

### Exemple d'utilisation complète

```bash
# Ajouter quelques tâches
python3 codes/task.py lestaches.txt add "Réviser pour l'examen"
python3 codes/task.py lestaches.txt add "Rendre le rapport de projet" --labels urgent,travail
python3 codes/task.py lestaches.txt add "Préparer la présentation" --labels important

# Afficher la liste
python3 codes/task.py lestaches.txt show

# Modifier une tâche
python3 codes/task.py lestaches.txt modify 2 "Rendre le rapport de projet avant vendredi"

# Ajouter des étiquettes
python3 codes/task.py lestaches.txt add-label 1 urgent
python3 codes/task.py lestaches.txt add-label 1 education

# Filtrer par étiquette
python3 codes/task.py lestaches.txt show --filter urgent

# Supprimer une tâche
python3 codes/task.py lestaches.txt rm 3

# Afficher le résultat final
python3 codes/task.py lestaches.txt show
```

## Format de Fichier

Les tâches sont stockées dans un fichier texte simple avec le format :
```
ID;Description;Étiquettes
```

Exemple de contenu de fichier :
```
1;Réviser pour l'examen;urgent,education
2;Rendre le rapport de projet avant vendredi;urgent,travail
3;Faire les courses;personnel
```

Note : Les étiquettes sont optionnelles. Une tâche sans étiquette aura une chaîne vide après le second point-virgule. Le format reste rétrocompatible avec l'ancien format "ID;Description".

## Fonctionnalités Implémentées

- Commandes de base (add, modify, rm, show)
- Gestion des erreurs (tâches non trouvées, fichiers inexistants)
- IDs auto-incrémentés
- Tri des tâches par ID lors de l'affichage
- Interface CLI intuitive avec `argparse`
- Format de fichier simple et lisible
- **Système d'étiquettes (labels) :**
  - Ajout d'étiquettes lors de la création de tâches
  - Gestion des étiquettes sur les tâches existantes (ajout, suppression, modification)
  - Filtrage des tâches par étiquette
  - Affichage des étiquettes dans le tableau formaté
  - Rétrocompatibilité avec l'ancien format de fichier

## Avancée du Projet

**Phase 1 - Fonctionnalités de base** : **TERMINÉE**
- Toutes les commandes de base sont implémentées et fonctionnelles
- Tests manuels réussis
- Code respectant les spécifications du codecamp

**Phase 2 - Système d'étiquettes** : **TERMINÉE**
- Implémentation complète du système d'étiquettes
- Nouvelles commandes : add-label, rm-label, set-labels
- Filtrage par étiquettes dans l'affichage
- Rétrocompatibilité maintenue avec l'ancien format

**Phase 3 - Extensions futures** : **À VENIR**
- Extensions à définir selon les tirages au sort des enseignants

## Problèmes Connus

Aucun problème critique identifié à ce jour. Le système fonctionne correctement selon les spécifications.

## Tests

Le projet a été testé manuellement avec :
- Ajout de tâches multiples
- Modification de tâches existantes  
- Suppression de tâches
- Affichage formaté des tâches
- Gestion d'erreurs (IDs inexistants)
- Création de nouveaux fichiers
- Fichiers vides ou inexistants
- **Tests du système d'étiquettes :**
  - Ajout de tâches avec étiquettes
  - Ajout/suppression d'étiquettes sur tâches existantes
  - Filtrage par étiquettes
  - Remplacement complet des étiquettes
  - Rétrocompatibilité avec anciens fichiers

## Utilisation de l'IA

L'IA (GitHub Copilot) a été utilisée pour :
- Restructurer et nettoyer le code existant
- Corriger les bugs et erreurs de syntaxe
- Améliorer la cohérence entre les modules
- Optimiser la gestion des fichiers et des erreurs
- Formatter l'affichage des tâches en tableau
- **Améliorer considérablement la documentation du code** :
  - Ajout de docstrings complètes avec format standard Python
  - Documentation des paramètres, valeurs de retour et effets de bord
  - Exemples concrets d'utilisation pour chaque fonction
  - En-têtes de modules avec descriptions détaillées
  - Commentaires inline explicatifs et sections logiques
  - Messages d'aide CLI en français et plus détaillés
  - Documentation de l'architecture et du flux d'exécution
