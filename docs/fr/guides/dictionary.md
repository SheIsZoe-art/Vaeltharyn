# Guide du dictionnaire Vaeltharyn

Version 1.1.0 — 2026-10-24. Retour : [00_Accueil](../start.md).

## Ce que contient une entrée

Le **lemme** est la forme de citation : nom singulier au direct, adjectif invariable, verbe à l’infinitif en `-ar`. Le **sens** délimite l’emploi. La **valence** indique si le verbe accepte un objet ; un bénéficiaire se place au datif selon [02_Grammaire](../reference/grammar.md). Pour une nouvelle construction complexe non fixée, écrire une proposition explicative plutôt que calquer les prépositions françaises.

`data/lexicon/fr/summary.csv` conserve les cinq colonnes initiales pour les outils existants. `data/lexicon/fr/entries.csv` ajoute nature, base, règle, statut, construction illustrative, traduction et note d’usage. Les tableaux restent des notes Markdown consultables sans extension Obsidian.

## Racines, dérivés, composés

- **Héritage 1.0.0** : entrée de départ préservée ; cette étiquette ne prétend pas que chaque mot hérité soit une racine simple.
- **Racine proposée** : nouveau lemme enregistré avec une définition stable. Certaines formes possèdent des échos d’autres mots ; aucune décomposition ni règle nouvelle ne s’en déduit. Ces unités lexicales proposées ne doivent pas être confondues avec les composés transparents à trait d’union. Leur éventuelle resegmentation demandera une décision versionnée.
- **Dérivé** : application d’une règle existante, avec base et suffixe indiqués. La définition reste compositionnelle.
- **Composé** : deux noms indépendants, déterminant puis noyau, reliés par un trait d’union. Seul le dernier élément reçoit le nombre et le cas.

Pour les ajouts suivants, préférer la dérivation ou un composé transparent avant d’inventer un lemme. Une entrée lexicalisée enregistrée conserve son sens même si une décomposition séduisante semble possible après coup.

## Flexions : système complet, index limité aux lemmes

Les noms donnent dix formes régulières (deux nombres, cinq cas) : `sael`, `saelen`, `saelor`, `saelath`, `saelul` ; `saeli`, `saelien`, `saelior`, `saeliath`, `saeliul`. Les pronoms gardent leurs traits d’union. Les noms propres suivent leur règle particulière.

Chaque verbe donne 54 formes finies dans [09_Paradigmes_des_verbes](../reference/verb-paradigms.md). Les impératifs et participes sont indiqués à part. Les aspects restent des mots indépendants, donc ne sont pas multipliés artificiellement dans le décompte lexical. Un participe passif exige une valence transitive ; un verbe intransitif ne reçoit pas un objet par simple suffixation.

## Dérivations et limites de sens

`-eth` sur un radical verbal désigne un processus, pas systématiquement son produit : l’action de créer n’est pas l’œuvre créée. `-or` nomme un participant à une action, pas nécessairement une profession. `-va` signifie « relatif à », sans transformer le nom en qualité évaluative. `-is` exprime la manière, sans ajouter de sens spatial ou temporel. Le préfixe `ul-` ne remplace jamais la négation verbale `nu`.

Les collisions entre formes nouvelles et lemmes existants sont signalées dans `archives/audits/control-before-refactor.json`. Une forme déjà occupée n’est ni écrasée ni redéfinie automatiquement. Une homographie avec une flexion demeure possible : le lecteur utilise le contexte ou reformule ; le rapport en fournit un relevé.

## Registre, genre, technique

Les noms de personnes ne marquent pas le genre grammatical. `nayrvan` peut désigner un frère ou une sœur ; une précision de genre ou de parenté se formule si elle est utile. Les rôles d’agent ne constituent pas des titres réservés.

Les mots scientifiques désignent les notions explicitement définies, sans devenir des recommandations médicales, juridiques ou techniques. Les mots magiques décrivent un univers fictif, sans affirmer de phénomène réel. Le vocabulaire nordique et celtique est une évocation artistique, jamais une attestation historique.

## Écrire un texte

1. Chercher le sens précis dans [06_Dictionnaire_FR_Vaeltharyn](../../../archives/core-dictionary-1.0.0/fr/06_Dictionnaire_FR_Vaeltharyn.md).
2. Vérifier la définition et la catégorie dans [05_Dictionnaire_Vaeltharyn_FR](../../../archives/core-dictionary-1.0.0/fr/05_Dictionnaire_Vaeltharyn_FR.md).
3. Vérifier valence, cas, conjugaison et ordre des mots.
4. Si le sens manque, essayer une périphrase ou proposer un composé avec définition.
5. Conserver la traduction française, puis distinguer texte canonique et transcription de chant.
6. Noter toute nouvelle décision dans [08_Canon_et_controles](../reference/canon-and-controls.md).

L’extension 1.1.0 ne vaut pas validation individuelle de toutes les propositions. La demande de développement autorise leur rédaction, sans attribuer au créateur des décisions lexicales qu’il n’a pas encore prises.

## Grande édition 1.2.0

Le noyau de 1.1.0 reste consultable ci-dessus. Le grand dictionnaire est dans [15_Grand_dictionnaire](dictionary-editions.md). Ses ajouts disposent d’un sens sourcé, d’une catégorie, d’une prononciation calculée et d’un état de révision ; ils ne disposent pas tous d’une phrase naturelle révisée. Les API et la segmentation du radical sont des propositions écrites. Conserver les définitions et l’attribution lors du partage.
