# 🧠 AI Brief Series – Agents IA autonomes pour la veille en intelligence artificielle

Une série de **trois agents IA autonomes** développés avec **n8n**, permettant d’automatiser la veille sur l’intelligence artificielle, aussi bien dans l’actualité que dans la recherche scientifique.

## 🚀 Présentation

Chaque agent est capable de :
- 📥 Récupérer le contenu depuis une source dédiée
- 🧠 Filtrer les informations liées à l’IA
- ✍️ Générer un résumé synthétique (via Gemini ou DeepSeek)
- 🌍 Traduire en français
- 📧 Envoyer un rapport automatisé par email

---

## 🤖 Les agents

### 🔹 Reddit AI Brief – Powered by an Autonomous Agent
- **Source** : Reddit
- **Objectif** : Résumer chaque jour les discussions pertinentes sur l’IA dans les subreddits spécialisés

### 🔹 ArXiv AI Brief – Powered by an Autonomous Agent
- **Source** : Flux RSS d’ArXiv (catégorie IA)
- **Objectif** : Suivre chaque semaine les dernières publications scientifiques sur l’IA

### 🔹 AI Brief – Powered by an Autonomous Agent
- **Source** : Flux RSS de VentureBeat
- **Objectif** : Synthétiser l’actualité technologique de l’IA chaque semaine

---

## 🛠️ Technologies utilisées

- [n8n](https://n8n.io/) – Orchestration des workflows
- [Google Gemini](https://ai.google.dev/) – Résumés & traduction
- [DeepSeek](https://api-docs.deepseek.com/) – Résumés & traduction
- Reddit / flux RSS – Récupération des données
- Gmail – Envoi automatisé par email

---

## 📁 Structure du dépôt

- `reddit-ai-brief/` : contient le fichier `workflow.json` de l’agent Reddit
- `arxiv-ai-brief/` : contient le fichier `workflow.json` de l’agent ArXiv
- `venturebeat-ai-brief/` : contient le fichier `workflow.json` de l’agent VentureBeat

---

## ▶️ Comment utiliser ces agents

1. Cloner ce dépôt GitHub
2. Ouvrir [n8n](https://n8n.io/) (instance locale ou cloud)
3. Importer les fichiers `workflow.json` correspondants
4. Ajouter vos identifiants API : Gemini, DeepSeek, Reddit, Gmail…
5. Planifier les exécutions (quotidienne ou hebdomadaire)
6. Et c’est tout ! 🤖

---

## 💡 Vision

Ce projet constitue les premières briques d’un **assistant IA personnel** autonome, pensé pour faciliter la veille technologique et scientifique.

---

## 📬 Contact

📩 amessaoudi.am@gmail.com  
🌍 https://github.com/AdelMessaoudi-13
