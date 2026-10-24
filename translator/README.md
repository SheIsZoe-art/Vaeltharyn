# Traducteur Vaeltharyn

## Plugin ChatGPT privé

Un plugin personnel **Traducteur Vaeltharyn** (v0.1.0) a été créé pour exploiter le canon linguistique de ce dépôt :

https://chatgpt.com/plugins/plugins_6add0cf9ee008191ba29f15c78e89513

Le plugin fournit un workflow de traduction assistée français ↔ Vaeltharyn avec vérification des règles de flexion, conjugaison et syntaxe, notes de traduction, registre poétique et prononciation pour le chant. Les données du dépôt `main` sont la source de référence; les propositions lexicales de l'édition 1.2.0 restent à distinguer des entrées validées.

### Limites de v0.1.0

- Le plugin repose sur un skill et sur l'accès au dépôt quand la connexion GitHub est disponible ; il ne fournit **pas** d'API de traduction ni de serveur MCP autonome.
- Il ne charge pas automatiquement tout le corpus de plus de 65 000 entrées en mémoire. Une grande traduction exige une recherche contextuelle dans les index ou les CSV accessibles.
- Une traduction poétique demande une validation humaine, particulièrement pour les définitions générées et les néologismes.

### Tests linguistiques attendus

| Français | Vaeltharyn |
|---|---|
| Je chante. | Mi thaerem. |
| Tu as chanté. | Ti rathaeres. |
| Les âmes chanteront. | En saeli vithaeren. |
| Chantes-tu ? | Ti thaeres ma ? |
| La lumière est dans mon âme. | Aelun vele e mi-en saelath. |

Pour une API ou interface web indépendante, construire une couche de lecture de `lexique_detaille.csv`, un moteur morphologique et une désambiguïsation des sens, avec des tests et la gestion des licences décrites dans `18_Sources_et_licences.md`.
