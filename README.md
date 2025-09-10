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
- ✅ Ajout de nouvelles tâches
- ✅ Modification de tâches existantes
- ✅ Suppression de tâches
- ✅ Affichage de la liste des tâches

Chaque tâche possède :
- Un **identifiant unique** (ID numérique auto-incrémenté)
- Une **description** (texte libre sans retour chariot)

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

### Exemple d'utilisation complète

```bash
# Ajouter quelques tâches
python3 codes/task.py lestaches.txt add "Réviser pour l'examen"
python3 codes/task.py lestaches.txt add "Rendre le rapport de projet"
python3 codes/task.py lestaches.txt add "Préparer la présentation"

# Afficher la liste
python3 codes/task.py lestaches.txt show

# Modifier une tâche
python3 codes/task.py lestaches.txt modify 2 "Rendre le rapport de projet avant vendredi"

# Supprimer une tâche
python3 codes/task.py lestaches.txt rm 3

# Afficher le résultat final
python3 codes/task.py lestaches.txt show
```

## Format de Fichier

Les tâches sont stockées dans un fichier texte simple avec le format :
```
ID;Description
```

Exemple de contenu de fichier :
```
1;Réviser pour l'examen
2;Rendre le rapport de projet avant vendredi
```

## Fonctionnalités Implémentées

- [x] **Étape 1** : Commandes de base (add, modify, rm, show)
- [x] Gestion des erreurs (tâches non trouvées, fichiers inexistants)
- [x] IDs auto-incrémentés
- [x] Tri des tâches par ID lors de l'affichage
- [x] Interface CLI intuitive avec `argparse`
- [x] Format de fichier simple et lisible

## Avancée du Projet

**Phase 1 - Fonctionnalités de base** : ✅ **TERMINÉE**
- Toutes les commandes de base sont implémentées et fonctionnelles
- Tests manuels réussis
- Code respectant les spécifications du codecamp

**Phase 2 - Extensions futures** : 🔄 **À VENIR**
- Extensions à définir selon les tirages au sort des enseignants

## Problèmes Connus

Aucun problème critique identifié à ce jour. Le système fonctionne correctement selon les spécifications.

## Tests

Le projet a été testé manuellement avec :
- ✅ Ajout de tâches multiples
- ✅ Modification de tâches existantes  
- ✅ Suppression de tâches
- ✅ Affichage formaté des tâches
- ✅ Gestion d'erreurs (IDs inexistants)
- ✅ Création de nouveaux fichiers
- ✅ Fichiers vides ou inexistants

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
