# 🛸 Guide de l'App Blueprint Generator

## Qu'est-ce que l'App Blueprint Generator ?

C'est un outil qui transforme votre **idée d'application** (décrite avec vos propres mots) en un **paquet professionnel** prêt pour qu'une Intelligence Artificielle construise l'application pour vous.

Vous n'avez pas besoin de savoir programmer. Vous avez juste besoin de savoir ce que vous voulez.

---

## Configuration requise

- **Python 3** installé sur votre ordinateur ([télécharger ici](https://www.python.org/))
- **Navigateur web** (Chrome, Firefox, Safari ou Edge)
- Ce dépôt complet téléchargé sur votre équipement

---

## Comment l'utiliser (Étape par étape)

### 1. Lancez le générateur

**Double-cliquez** sur le fichier correspondant à votre système d'exploitation :

| Système | Fichier |
|---------|---------|
| macOS | `CREAR_APP.command` |
| Windows | `CREAR_APP.bat` |
| Linux | `CREAR_APP.sh` |

Votre navigateur s'ouvrira automatiquement avec l'interface du générateur.

### 2. Décrivez votre idée (5 étapes simples)

1. **Vision** : Donnez un nom à votre application et décrivez ce qu'elle fait.
2. **Public** : Indiquez qui l'utilisera et dans quel secteur.
3. **Fonctions** : Sélectionnez les fonctionnalités dont vous avez besoin.
4. **Design** : Choisissez les couleurs et le style visuel.
5. **Générer** : Vérifiez le résumé et appuyez sur "Générer Mon Blueprint".

### 3. Téléchargez votre Blueprint

Le système générera un fichier ZIP qui sera automatiquement enregistré dans le dossier **`APPS-CREADAS`** au sein du dépôt.

### 4. Ouvrez votre IA et commencez à construire

1. Ouvrez votre outil d'IA préféré (Antigravity, Cursor, Claude, ChatGPT...)
2. Ouvrez le fichier `LEEME_PRIMERO.md` du ZIP téléchargé.
3. **Copiez tout le texte** et collez-le comme votre premier message.
4. L'IA commencera à construire votre application !

---

## Que contient le Blueprint (ZIP) ?

| Dossier | Contenu |
|---------|-----------|
| `LEEME_PRIMERO.md` | Guide d'utilisation rapide |
| `PROMPT_INICIAL.md`| Le premier message pour l'IA |
| `01_VISION/` | Projet, public et fonctionnalités |
| `02_AGENTES/` | Rôles de l'équipe IA |
| `03_SKILLS/` | Connaissances techniques spécialisées |
| `04_ARQUITECTURA/` | Recommandations technologiques |
| `05_REGLAS/` | Limites, normes et sécurité |
| `06_DISEÑO/` | Guide de style visuel |

---

## Questions Fréquemment Posées

### Ai-je besoin d'une connexion Internet ?
**Non.** Tout fonctionne en local. Vous avez besoin d'Internet uniquement pour charger les polices de l'interface (Google Fonts), mais cela fonctionne aussi sans elles.

### Puis-je créer plus d'un Blueprint ?
**Oui.** Vous pouvez en créer autant que vous le souhaitez. Chacun est enregistré avec son propre nom et sa propre date.

### Puis-je modifier le Blueprint après sa création ?
**Oui.** Les fichiers du ZIP sont des documents Markdown (.md) que vous pouvez ouvrir et éditer avec n'importe quel éditeur de texte.

---

## Dépannage

| Problème | Solution |
|----------|----------|
| "Serveur hors línea" | Fermez et rouvrez le fichier `CREAR_APP.*` |
| Le navigateur ne s'ouvre pas | Ouvrez manuellement `http://localhost:5500` |
| Erreur Python | Assurez-vous d'avoir Python 3 installé : `python3 --version` |
| Le ZIP est vide | Vérifiez que le fichier `INDEX.js` existe à la racine |

---

## Crédits

Conçu et développé par **Jesús García Fernández** | [jesusgarciafernandez.com](https://jesusgarciafernandez.com)

App Blueprint Generator v1.0 — Écosystème Antigravity
