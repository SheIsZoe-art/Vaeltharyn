# Précautions de traduction / Translation cautions

## Expressions, jurons et sens



Consulter `docs/fr/extensions/register.md`, `docs/fr/extensions/idioms.md` et les fiches `data/expressions/idioms-1.4.0/sens.json`. L’extension comprend 226 fiches de sens, 200 formulations supplémentaires et neuf lemmes. Le grand lexique contient 65 041 entrées et 65 038 graphies, dont beaucoup de propositions anciennes non relues individuellement : ces volumes ne garantissent pas leur qualité.



Les synonymes de la source sont des renvois, pas des racines distinctes. Choisir selon le contexte plutôt que remplacer mécaniquement chaque juron par `vrask`. Distinguer colère et ivresse pour `pissed`, admiration et menace pour `badass`, crédulité et folie pour `jobard`, mensonge et erreur pour « connerie », intensité et mauvaise qualité pour « putain de » et « de merde ». Préserver destinataire, sujet, force et intention ; ne pas transformer une phrase en « je » ou « il » en injonction à « tu ».



Neuf ajouts définis : `gydimar` échouer à une action (intr.), `slusoemar` se préoccuper de (tr.), `thenthosar` tourner une cible en ridicule (tr.), `gydim-thalen` raté (injure), `nathem-thaelor` fouteur de discorde, `vaermar-lodhom` vendu pour intérêt financier, `vareth-greth` difficulté pratique ou relationnelle, `fonul-brabon` composé sexuel descriptif ou injurieux, `traemtoer-dhokun` injure sexuelle objectivante. Lire leurs définitions complètes avant emploi. Ne pas détourner les anciens verbes de mise à feu, de navigation ou de souci causé à autrui pour ces sens.



Quatre lignes n’ont pas d’équivalent établi : « D jobi / jobi », « Gognand », `trailer trash`, `white trash`. Expliquer l’incertitude régionale ou culturelle, ou proposer une paraphrase contextualisée explicitement partielle. Ne pas inventer de population, de tradition, de diagnostic ou de fait sexuel pour transposer une injure. `contre_exemples.json` contient des erreurs documentées comme tests négatifs, jamais des modèles de traduction.



## Son, corps et images — extension 1.5.0



Lire `docs/fr/extensions/sound-body.md` et `data/expressions/sound-body-1.5.0/sens.json` dans le corpus choisi pour les technologies, gestes, nuances et images de la liste utilisateur. Les 111 fiches décrivent des lectures contextualisées, avec quinze ajouts (huit racines, sept composés) ; les anciens lemmes restent inchangés. La recherche charge aussi ces compléments, leurs alias et leurs notes, tout en conservant les anciens registres.



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



Conserver les attributions dans les exports, notamment `docs/fr/reference/sources-and-licenses.md`, `LICENSE.md` et les références de l’inventaire. Le moteur expérimental de PR #1 n’est pas un MCP distant et ne doit pas être présenté comme un outil accessible depuis le web.
