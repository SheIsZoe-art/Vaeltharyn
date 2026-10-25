---
name: translate-vaeltharyn
description: Traduire entre français, anglais et Vaeltharyn avec le corpus 1.5.0, ses définitions, sa grammaire et ses expressions contextualisées. Utiliser aussi pour vérifier ou expliquer une traduction et préparer des paroles.
---

# Traducteur Vaeltharyn — corpus 1.5.0

Créateur du plugin : **SheIsZoe**.

Traduire entre français, anglais et Vaeltharyn en préservant le sens, le registre et les rôles grammaticaux. Les recherches ne modifient jamais le corpus.

## Corpus et recherche

Le corpus local actualisé est `C:/Users/user/Documents/ChatGPT/Vaeltharyn/publication-github`. Il remplace l’ancien chemin Obsidian pour cette installation. La copie autonome `references/corpus/` permet la consultation si ce dossier est absent. `VAELTHARYN_ROOT` ou `--root` sélectionne explicitement un autre corpus ; un corpus absent ou incomplet est signalé, sans retour silencieux vers une ancienne édition.

Révision embarquée : `d30199ad5a2595aea63688881f301cb6988be21b`, édition 1.5.0 du 25 octobre 2026. Source : https://github.com/SheIsZoe-art/Vaeltharyn/tree/feat/jurons-insultes-fr-en ; demande https://github.com/SheIsZoe-art/Vaeltharyn/pull/2 . Ces derniers ajouts sont publiés sur cette branche, pas encore intégrés à `main`. Ils sont utilisables pour les traductions demandées tout en conservant leur statut de propositions non validées. Ne pas les présenter comme définitivement approuvés. Vérifier la révision réellement consultée avant d’affirmer qu’elle est la plus récente ; ne pas changer de branche ni mettre à jour des fichiers pour une simple traduction.

Lire `references/corpus/02_Grammaire.md` et `03_Conjugaison.md` avant une traduction non triviale ; consulter `04_Formation_des_mots.md`, `01_Sons_et_chant.md`, `12_Exemples_et_distinctions.md` et `08_Canon_et_controles.md` selon le besoin. Quand le corpus vivant est utilisé, lire ces mêmes fichiers à sa racine.

Rechercher les entrées avec leur définition, valence, registre et statut, sans charger le grand CSV en contexte :

```text
python <skill>/scripts/chercher.py --lang fr "échouer (action)"
python <skill>/scripts/chercher.py --lang en "I'm pissed off" "badass"
python <skill>/scripts/chercher.py --lang vh "grusk" "thenthosar"
python <skill>/scripts/chercher.py --lang fr --contains "j'en ai rien à foutre"
```

`--contains` aide à trouver un candidat ; il ne prouve pas une équivalence. La recherche interroge directement les colonnes anglaises pour l’anglais, les 79 expressions initiales et les 719 lignes de l’inventaire rattachées à leurs fiches. Lire les notes de portée et les alternatives ; la correspondance fournie dans la pièce jointe n’est pas une traduction validée. Une forme fléchie demande de reconstruire ses analyses possibles à partir des lemmes.

## Expressions, jurons et sens

Consulter `23_Jurons_insultes_expressions.md`, `24_Inventaire_expressif_FR_EN.md` et les fiches `registres/inventaire-2026-10-25/sens.json`. L’extension comprend 226 fiches de sens, 200 formulations supplémentaires et neuf lemmes. Le grand lexique contient 65 041 entrées et 65 038 graphies, dont beaucoup de propositions anciennes non relues individuellement : ces volumes ne garantissent pas leur qualité.

Les synonymes de la source sont des renvois, pas des racines distinctes. Choisir selon le contexte plutôt que remplacer mécaniquement chaque juron par `vrask`. Distinguer colère et ivresse pour `pissed`, admiration et menace pour `badass`, crédulité et folie pour `jobard`, mensonge et erreur pour « connerie », intensité et mauvaise qualité pour « putain de » et « de merde ». Préserver destinataire, sujet, force et intention ; ne pas transformer une phrase en « je » ou « il » en injonction à « tu ».

Neuf ajouts définis : `gydimar` échouer à une action (intr.), `slusoemar` se préoccuper de (tr.), `thenthosar` tourner une cible en ridicule (tr.), `gydim-thalen` raté (injure), `nathem-thaelor` fouteur de discorde, `vaermar-lodhom` vendu pour intérêt financier, `vareth-greth` difficulté pratique ou relationnelle, `fonul-brabon` composé sexuel descriptif ou injurieux, `traemtoer-dhokun` injure sexuelle objectivante. Lire leurs définitions complètes avant emploi. Ne pas détourner les anciens verbes de mise à feu, de navigation ou de souci causé à autrui pour ces sens.

Quatre lignes n’ont pas d’équivalent établi : « D jobi / jobi », « Gognand », `trailer trash`, `white trash`. Expliquer l’incertitude régionale ou culturelle, ou proposer une paraphrase contextualisée explicitement partielle. Ne pas inventer de population, de tradition, de diagnostic ou de fait sexuel pour transposer une injure. `contre_exemples.json` contient des erreurs documentées comme tests négatifs, jamais des modèles de traduction.

## Son, corps et images — extension 1.5.0

Lire `25_Son_corps_et_images.md` et `complements/son-corps-images-1.5.0/sens.json` dans le corpus choisi pour les technologies, gestes, nuances et images de la liste utilisateur. Les 111 fiches décrivent des lectures contextualisées, avec quinze ajouts (huit racines, sept composés) ; les anciens lemmes restent inchangés. La recherche charge aussi ces compléments, leurs alias et leurs notes, tout en conservant les anciens registres.

Réutiliser `korthir` pour la fréquence physique, `tibon` pour le volant, `kaenkar` pour le cuir, `thaemgrael` pour le haut-parleur. Distinguer `klavir` clavier musical de `potul` porte-clefs ; `paed` nappe sonore de `kaeneth-dolgik` pad physique ; `saevron` taille anatomique de `doebyn` découpe. `Thrylkim-molpyv` désigne le timbre, pas le bois de timber ni le volume. `Maev-sityn` est une fantaisie imaginée, sans diagnostic ; préciser l'érotisme seulement quand le texte le demande. `Kikoe` a été préféré à kik pour éviter des collisions de cas avec kiken et kikor.

Conserver `TR-606` et `TR-808` comme modèles reconnaissables. Six cent six se construit `sul khar sul`, suivi du nom pluriel ; ce nombre littéral ne décrit pas automatiquement les composants de la machine. Only ne doit pas être effacé ; les notes proposent une condition nécessaire sans inventer une nouvelle portée de focus. Unforgotten n'est pas forcément unforgettable. Les métaphores sont indiquées comme telles et ne changent pas silencieusement les définitions physiques.

Un résultat `schema_a_completer` contient des emplacements entre chevrons : retrouver l'antécédent, notamment pour mine, et remplir les emplacements avant de livrer une traduction. Lire les hypothèses de waiting height, meant to be, plain et conditions ; demander le vers complet seulement si le contexte disponible ne permet pas de choisir. Adapter les pronoms et les acteurs des exemples au texte réel.

## Construction et restitution

- Ordre SVO ; VSO seulement après `ke` rituel. Pas de genre grammatical automatique ; noms de référent homme/femme seulement si nécessaires au sens.
- Pluriel `-i` avant cas `-en`, `-or`, `-ath`, `-ul`. Adjectifs postposés, invariables. Pronoms fléchis avec trait d’union. Prépositions spatiales avec locatif ; `ko` signifie avec, pas le comparatif comme.
- Retirer exactement `ar` de l’infinitif, puis temps + radical + mode + personne, sans élision. Présent `em/es/e/om/os/en`, passé `ra-`, futur `vi-`, modes `ir/el`. Deuxième personne : `Ti veles`, jamais `Ti vele`. Modal + infinitif à sujet commun ; participes distincts des verbes personnels ; passif seulement si valence transitive autorisée.
- `nu` nie le verbe ; `nul` quantifie le nom. `sha` intensifie l’adjectif, pas le nom, le verbe ou l’adverbe. Vérifier les possessifs réfléchis et les sujets des relatives/complétives.
- Vérifier en sens inverse négation, temps, agents, cibles et images. Préférer une périphrase attestée à une racine improvisée. Distinguer formation productive et entrée enregistrée ; marquer toute néologie supplémentaire comme proposition, sans modifier le canon pour une simple traduction.

Donner directement la traduction et respecter les balises, couplets et format demandés. Pour des paroles, adapter rime ou métrique seulement si cela conserve le sens ou si l’arbitrage est explicite. Donner les traductions sous chaque ligne quand demandé ; ne pas imposer systématiquement une glose. Séparer aide phonétique de performance et orthographe canonique. La sonorité écrite suit les règles ; ne pas prétendre avoir testé l’audio.

Conserver les attributions dans les exports, notamment `18_Sources_et_licences.md`, `LICENSE.md` et les références de l’inventaire. Le moteur expérimental de PR #1 n’est pas un MCP distant et ne doit pas être présenté comme un outil accessible depuis le web.
