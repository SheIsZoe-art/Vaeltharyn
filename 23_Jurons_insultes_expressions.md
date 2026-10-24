# Jurons, insultes et expressions — Vaeltharyn / français / anglais

Version 1.3.0 · 2026-10-25. [English](en/23_Jurons_insultes_expressions.md) · [Accueil](README.md).

**10 entrées lexicales nouvelles, 79 expressions contextualisées et 20 renvois de recherche.** Un renvoi ou une conjugaison n’est pas compté comme nouveau mot. Statut : **PROPOSITIONS NON VALIDÉES**, enregistrées à la demande du créateur ; le complément ne vaut pas approbation individuelle par celui-ci. Les anciennes définitions ne changent pas.

## Analyse de l’existant

Les quatre CSV complets ont été parcourus : 65 007 entrées dans chaque édition, avec vérification des formes, catégories et identifiants entre français et anglais. Les définitions pertinentes ont ensuite été lues, avec phonologie, grammaire, conjugaison, formation des mots et complément « royaume ». L’audit ne prétend pas être une relecture humaine de toutes les définitions. Les volumes historiques restent des instantanés ; les CSV courants et ce complément font foi pour ces ajouts.

| Forme existante | Distinction à conserver |
|---|---|
| rymvos | chier : nom géologique, pas déféquer |
| bridhoem | couillon : élément de voile, pas une personne stupide |
| himvos | bordel : établissement, pas désordre ni juron |
| bradhaek | crétin : sens médical historique, pas injure générique |
| vroepaer | lâche : non tendu, pas une personne sans courage |
| fonul | pénis : anatomie, pas automatiquement une insulte |
| lodys | gueule : bouche animale ; ne pas lui attribuer toute la polysémie de gueule |
| thulsem | foutre : renforcement négatif, pas verbe sexuel |


Le corpus possède déjà `kofav`, `tronodaev`, `skithin`, `lodhom`, `moesyk`, ainsi que les adjectifs `fregos`, `nifen`, `skentav`, `slaroem`. Ils sont réemployés selon leur sens. Un terme descriptif neutre peut devenir une insulte en adresse ; cet emploi contextuel ne transforme pas automatiquement tous ses emplois en injures.

## Logique du registre

- `garuniv` demeure l’intensif familier antérieur, proche de « fichu / damn ».
- `vrask` est proposé comme intensif beaucoup plus vulgaire. L’adjectif suit son nom : `ith nyr vrask`, « cette putain de nuit / this fucking night ». Il n’est pas placé devant un adjectif comme si c’était un adverbe anglais.
- `grusk` distingue matière fécale vulgaire et juron interjectif, deux catégories explicitement enregistrées ; `gruskar` désigne uniquement l’action de déféquer.
- `skarn` vise une conduite méprisable ; `skarnar` décrit cette conduite. Aucun genre grammatical ni accusation sexuelle ou familiale n’est ajouté.
- `grusk-tharel` et `graeth-naelkaror` respectent la composition déterminant + noyau. Pluriels : `grusk-thareli`, `graeth-naelkarori`. Génitifs : `grusk-tharelen`, `graeth-naelkaroren`.
- Les interjections sont enregistrées comme `part`, mots invariables, pour conserver les catégories du corpus. Aucun suffixe injurieux universel ni règle de nominalisation d’adjectif n’est inventé : `thalen fregos` garde un nom explicite.

**Force indicative :** 0 neutre ; 1 contrariété légère ou limite ferme ; 2 familier/rude ; 3 vulgaire ou franchement injurieux ; 4 très vulgaire. Ce n’est pas une mesure acoustique ni une équivalence culturelle exacte. L’adresse, la relation et le ton changent la portée ; une limite ferme n’est pas intrinsèquement une insulte.

## Sonorité et diction

Les quatre nouvelles racines simples `sketh`, `grusk`, `vrask`, `skarn` respectent les groupes initiaux existants et la structure syllabique autorisée. Elles offrent des attaques consonantiques nettes et des finales brèves adaptées à une ponctuation scandée ; c’est une proposition d’écriture, pas une performance testée. Les verbes gardent l’accent sur la racine : **GRUSK-ar**, `SKARN-ar` ; aucune apostrophe ou lettre décorative.

Les composés prennent l’accent principal sur le premier élément et un secondaire sur le second. Les consonnes finales peuvent fermer une voyelle tenue ; ne pas transformer un mot court en plusieurs syllabes pour le faire paraître « mystique ». Les API ci-dessous sont déduites des règles écrites, sans validation audio.

## Fiches lexicales nouvelles

### VX-62ee27b1c1ae19f3

**sketh** · `part` · /skɛθ/ · force 1/4

**Français :** zut. **English:** darn.

Interjection invariable de contrariété légère ou de petite surprise désagréable. Ne désigne ni personne ni objet.

**Formation :** racine expressive proposée. Base : nouvelle racine proposée. **Valence :** sans flexion verbale.

**Exemple :** Sketh! — Zut ! — Darn!

**Statut :** PROPOSITION NON VALIDÉE — complément demandé par le créateur, 2026-10-25.

### VX-ac715a2646bc65cb

**grusk** · `n` · /grusk/ · force 3/4

**Français :** merde (matière). **English:** shit (substance).

Matière fécale, dans un registre vulgaire ; ne comprend pas automatiquement l’urine. Le sens clinique d’excrément reste distinct.

**Formation :** racine scatologique proposée. Base : nouvelle racine proposée. **Valence :** sans flexion verbale.

**Exemple :** Se vele grusk. — C’est de la merde. — It is shit.

**Statut :** PROPOSITION NON VALIDÉE — complément demandé par le créateur, 2026-10-25.

### VX-6b1d3a5384bc50ec

**grusk** · `part` · /grusk/ · force 3/4

**Français :** merde !. **English:** shit!.

Interjection scatologique exprimant contrariété, surprise ou enthousiasme selon le contexte. Ne constitue pas à elle seule une insulte adressée.

**Formation :** emploi interjectif explicitement enregistré, sans changement du sens nominal. Base : grusk (n). **Valence :** sans flexion verbale.

**Exemple :** Grusk, nau! — Merde, non ! — Shit, no!

**Statut :** PROPOSITION NON VALIDÉE — complément demandé par le créateur, 2026-10-25.

### VX-3a6e4d7c6b1b782e

**gruskar** · `v` · /ˈgrusk.ar/ · force 3/4

**Français :** chier (déféquer). **English:** shit (defecate).

Déféquer, dans un registre vulgaire. Intransitif ; ne signifie pas automatiquement importuner, rater, tromper ou avoir peur.

**Formation :** nom + ar ; sens verbal intransitif lexicalisé. Base : grusk. **Valence :** intr.

**Exemple :** Mi gruskem. — Je chie. — I shit.

**Statut :** PROPOSITION NON VALIDÉE — complément demandé par le créateur, 2026-10-25.

### VX-698513c5c68dc072

**vrask** · `adj` · /vrask/ · force 4/4

**Français :** foutu ; putain de (intensif). **English:** fucking (intensifier).

Adjectif expressif très vulgaire renforçant un nom, par colère, étonnement ou admiration. Placé après le nom selon la grammaire ; n’est pas une description d’acte sexuel.

**Formation :** racine expressive proposée, parallèle intensif fort de garuniv. Base : nouvelle racine proposée. **Valence :** sans flexion verbale.

**Exemple :** Ith nyr vrask! — Cette putain de nuit ! — This fucking night!

**Statut :** PROPOSITION NON VALIDÉE — complément demandé par le créateur, 2026-10-25.

### VX-bcc0895b083109ae

**vrask** · `part` · /vrask/ · force 4/4

**Français :** putain !. **English:** fuck!.

Interjection très vulgaire de réaction émotionnelle forte. Ne formule ni demande sexuelle, ni ordre sexuel, ni malédiction religieuse.

**Formation :** emploi interjectif explicitement enregistré dans la même famille expressive. Base : vrask (adj). **Valence :** sans flexion verbale.

**Exemple :** Vrask, ei! — Putain, oui ! — Fuck yes!

**Statut :** PROPOSITION NON VALIDÉE — complément demandé par le créateur, 2026-10-25.

### VX-71c873e47f68801b

**skarn** · `n` · /skarn/ · force 3/4

**Français :** salopard ; ordure (personne). **English:** asshole; bastard (contemptible person).

Personne insultée pour une conduite jugée délibérément méprisable, nuisible ou déloyale. Ne désigne ni anatomie, filiation, genre, ni état de santé.

**Formation :** racine injurieuse proposée. Base : nouvelle racine proposée. **Valence :** sans flexion verbale.

**Exemple :** Ti veles skarn. — Tu es une ordure. — You are an asshole.

**Statut :** PROPOSITION NON VALIDÉE — complément demandé par le créateur, 2026-10-25.

### VX-8986f6880509a476

**skarnar** · `v` · /ˈskarn.ar/ · force 3/4

**Français :** se comporter en salopard. **English:** act like an asshole.

Se conduire de manière délibérément méprisable ou nuisible. Intransitif ; ko + personne précise éventuellement la relation.

**Formation :** nom + ar ; manifester le comportement désigné, intransitif. Base : skarn. **Valence :** intr.

**Exemple :** Nu skarna ko mi! — Ne fais pas le connard avec moi ! — Do not be an asshole with me!

**Statut :** PROPOSITION NON VALIDÉE — complément demandé par le créateur, 2026-10-25.

### VX-6e1ca81d64ca4a10

**grusk-tharel** · `n` · /ˈgruskˌθarɛl/ · force 3/4

**Français :** connerie (propos). **English:** bullshit (utterance).

Propos rejeté comme absurde, trompeur ou sans valeur. Composé lexicalisé ; une discussion neutre de matières fécales n’est pas appelée ainsi.

**Formation :** nom déterminant + nom noyau ; flexion du dernier élément. Base : grusk + tharel. **Valence :** sans flexion verbale.

**Exemple :** Nu lyra grusk-thareli! — Ne raconte pas de conneries ! — Do not talk bullshit!

**Statut :** PROPOSITION NON VALIDÉE — complément demandé par le créateur, 2026-10-25.

### VX-91adcaa2a34ff809

**graeth-naelkaror** · `n` · /ˈgræːθˌnæːlkarɔr/ · force 2/4

**Français :** briseur de serment ; parjure (personne). **English:** oathbreaker.

Personne accusée de détruire volontairement un engagement solennel. Insulte de trahison dans un registre poétique ; aucun droit pénal ou tabou historique n’est inventé.

**Formation :** serment + destructeur, nom de participant déjà enregistré. Base : graeth + naelkaror. **Valence :** sans flexion verbale.

**Exemple :** Graeth-naelkaror! — Briseur de serment ! — Oathbreaker!

**Statut :** PROPOSITION NON VALIDÉE — complément demandé par le créateur, 2026-10-25.

## Expressions françaises et anglaises

Le littéral est conservé dans `registres/expressions.json` et le CSV pour distinguer sens et effet. Les formulations imagées sont des propositions nouvelles, pas des proverbes historiques attestés.

### EX-240c713c11cb

**Sketh!**

- FR : Zut !
- EN: Darn!
- Littéral : Interjection de contrariété légère.
- Literal: A mild expression of annoyance.
- Force : 1/4 · Fonction : juron · Équivalence : pragmatique.

### EX-c78ac8e1cf64

**Grusk!**

- FR : Merde !
- EN: Shit!
- Littéral : Interjection scatologique de contrariété.
- Literal: A scatological exclamation of frustration.
- Force : 3/4 · Fonction : juron · Équivalence : pragmatique.

### EX-04e8b39b4ecf

**Vrask!**

- FR : Putain !
- EN: Fuck!
- Littéral : Interjection d'émotion très forte, sans sens sexuel dans cet emploi.
- Literal: An exclamation of strong emotion, not a sexual proposition.
- Force : 4/4 · Fonction : juron · Équivalence : pragmatique.

### EX-1024537169ad

**Grusk, nau!**

- FR : Merde, non !
- EN: Shit, no!
- Littéral : Merde ; non.
- Literal: Shit; no.
- Force : 3/4 · Fonction : juron · Équivalence : pragmatique.

### EX-7dfae6d75fde

**Vrask, nau!**

- FR : Putain, non !
- EN: Fuck, no!
- Littéral : Juron fort ; non.
- Literal: Strong expletive; no.
- Force : 4/4 · Fonction : juron · Équivalence : pragmatique.

### EX-b5251a59fe3d

**Grusk, ei!**

- FR : Merde, oui !
- EN: Hell yes!
- Littéral : Merde ; oui, avec enthousiasme.
- Literal: Shit; yes, enthusiastically.
- Force : 3/4 · Fonction : juron positif · Équivalence : pragmatique.

### EX-8a549adc20e9

**Vrask, ei!**

- FR : Putain, oui !
- EN: Fuck yes!
- Littéral : Juron fort ; oui.
- Literal: Strong expletive; yes.
- Force : 4/4 · Fonction : juron positif · Équivalence : pragmatique.

### EX-5a276f294101

**Dhimmus!**

- FR : Foutaises !
- EN: Nonsense!
- Littéral : Une chose dénuée de sens ou d'intérêt.
- Literal: Something pointless or nonsensical.
- Force : 2/4 · Fonction : réplique · Équivalence : pragmatique.

### EX-fe45306c279e

**Grusk-thareli!**

- FR : Conneries !
- EN: Bullshit!
- Littéral : Mots de merde, au sens lexicalisé de propos rejetés.
- Literal: Shit-words, lexicalised as rejected claims or talk.
- Force : 3/4 · Fonction : réplique · Équivalence : pragmatique.

### EX-25948ef3b45e

**Ith saun garuniv!**

- FR : Cette fichue journée !
- EN: This damn day!
- Littéral : Ce jour fichu.
- Literal: This damn day.
- Force : 2/4 · Fonction : intensif · Équivalence : pragmatique.

### EX-b0ce083039ba

**Ith saun vrask!**

- FR : Cette putain de journée !
- EN: This fucking day!
- Littéral : Ce jour, intensif très vulgaire.
- Literal: This day with a strong vulgar intensifier.
- Force : 4/4 · Fonction : intensif · Équivalence : pragmatique.

### EX-5556eddd8e06

**Ith nyr garuniv!**

- FR : Cette fichue nuit !
- EN: This damn night!
- Littéral : Cette nuit fichue.
- Literal: This damn night.
- Force : 2/4 · Fonction : intensif · Équivalence : pragmatique.

### EX-fe025adcdd5e

**Ith nyr vrask!**

- FR : Cette putain de nuit !
- EN: This fucking night!
- Littéral : Cette nuit, intensif très vulgaire.
- Literal: This night with a strong vulgar intensifier.
- Force : 4/4 · Fonction : intensif · Équivalence : pragmatique.

### EX-c1ec9b1ec09d

**Ith kaerun vrask!**

- FR : Cette putain de porte !
- EN: This fucking door!
- Littéral : Cette porte, intensif très vulgaire.
- Literal: This door with a strong vulgar intensifier.
- Force : 4/4 · Fonction : intensif · Équivalence : pragmatique.

### EX-3bec2f1a6003

**Ith therval garuniv!**

- FR : Ce fichu boulot !
- EN: This damn job!
- Littéral : Ce travail fichu.
- Literal: This damn work.
- Force : 2/4 · Fonction : intensif · Équivalence : pragmatique.

### EX-b54344fbb09c

**Ith therval vrask!**

- FR : Ce putain de boulot !
- EN: This fucking job!
- Littéral : Ce travail, intensif très vulgaire.
- Literal: This work with a strong vulgar intensifier.
- Force : 4/4 · Fonction : intensif · Équivalence : pragmatique.

### EX-2644fb29f389

**Se vele grusk.**

- FR : C'est de la merde.
- EN: It's shit.
- Littéral : Cela est de la merde.
- Literal: It is shit.
- Force : 3/4 · Fonction : jugement · Équivalence : pragmatique.

### EX-78358e2801f7

**Ith thael vele grusk.**

- FR : Cette chanson, c'est de la merde.
- EN: This song is shit.
- Littéral : Cette chanson est de la merde.
- Literal: This song is shit.
- Force : 3/4 · Fonction : jugement · Équivalence : pragmatique.

### EX-c909579ba99e

**Ith therval vele grusk.**

- FR : Ce boulot, c'est de la merde.
- EN: This job is crap.
- Littéral : Ce travail est de la merde.
- Literal: This work is shit.
- Force : 3/4 · Fonction : jugement · Équivalence : pragmatique.

### EX-6ca8cb5b46a8

**Se vele grusk-tharel.**

- FR : C'est une connerie.
- EN: That's bullshit.
- Littéral : Cela est un propos rejeté comme absurde ou trompeur.
- Literal: That is an utterance dismissed as absurd or misleading.
- Force : 3/4 · Fonction : jugement · Équivalence : pragmatique.

### EX-95aa01f5e047

**Sava thareli ti-en velen grusk-thareli.**

- FR : Tout ce que tu racontes, c'est des conneries.
- EN: Everything you say is bullshit.
- Littéral : Tous tes mots sont des propos rejetés.
- Literal: All your words are rejected utterances.
- Force : 3/4 · Fonction : jugement · Équivalence : pragmatique.

### EX-be1f46fa865a

**Sava vugomi ti-en velen grusk-thareli.**

- FR : Tes promesses, c'est que des conneries.
- EN: All your promises are bullshit.
- Littéral : Toutes tes promesses sont des propos rejetés.
- Literal: All your promises are rejected utterances.
- Force : 3/4 · Fonction : jugement · Équivalence : pragmatique.

### EX-53ea4bdeaf3f

**Skarn!**

- FR : Salopard !
- EN: Asshole!
- Littéral : Personne jugée délibérément méprisable.
- Literal: A person condemned as deliberately vile.
- Force : 3/4 · Fonction : insulte · Équivalence : pragmatique.

### EX-3a80e8b3ae99

**Ti veles skarn.**

- FR : Tu es une ordure.
- EN: You're an asshole.
- Littéral : Tu es une personne délibérément méprisable.
- Literal: You are a deliberately vile person.
- Force : 3/4 · Fonction : insulte · Équivalence : pragmatique.

### EX-6cd6083ac860

**Thalen fregos!**

- FR : Connard !
- EN: Jerk!
- Littéral : Personne insupportable et méprisable.
- Literal: An insufferable, contemptible person.
- Force : 3/4 · Fonction : insulte · Équivalence : pragmatique.

### EX-4cdd3739b39f

**Ti veles fregos.**

- FR : Tu es vraiment con.
- EN: You're being a jerk.
- Littéral : Tu es insupportable et méprisable.
- Literal: You are insufferable and contemptible.
- Force : 3/4 · Fonction : insulte · Équivalence : pragmatique.

### EX-56004e61301a

**Ti veles skentav.**

- FR : Tu es un salaud.
- EN: You're a bastard.
- Littéral : Tu es contraire à la morale ou à la loyauté.
- Literal: You act against morality or loyalty.
- Force : 3/4 · Fonction : insulte · Équivalence : pragmatique.

### EX-8884fcddf258

**Ti veles moesyk.**

- FR : Tu es un pourri.
- EN: You're a corrupt bastard.
- Littéral : Tu es une personne corrompue.
- Literal: You are a corrupt person.
- Force : 3/4 · Fonction : insulte · Équivalence : pragmatique.

### EX-489a7bd4237c

**Skithin!**

- FR : Hypocrite !
- EN: Hypocrite!
- Littéral : Personne hypocrite.
- Literal: A hypocritical person.
- Force : 2/4 · Fonction : insulte · Équivalence : pragmatique.

### EX-109966f2f0e4

**Lodhom!**

- FR : Traître !
- EN: Traitor!
- Littéral : Personne qui trahit.
- Literal: A person who betrays.
- Force : 2/4 · Fonction : insulte · Équivalence : pragmatique.

### EX-c001c39dbac3

**Kofav!**

- FR : Imbécile !
- EN: Idiot!
- Littéral : Personne incapable d'agir judicieusement, selon l'insulte.
- Literal: A person insulted as lacking sound judgement.
- Force : 2/4 · Fonction : insulte · Équivalence : pragmatique.

### EX-8d47d9547de9

**Tronodaev!**

- FR : Idiot !
- EN: Fool!
- Littéral : Personne considérée comme sans idées ni intelligence.
- Literal: A person considered devoid of ideas or intelligence.
- Force : 2/4 · Fonction : insulte · Équivalence : pragmatique.

### EX-d2954c1ba25e

**Ti veles basoel.**

- FR : Tu es imbécile.
- EN: You're foolish.
- Littéral : Tu manques de jugement.
- Literal: You lack sound judgement.
- Force : 2/4 · Fonction : insulte · Équivalence : pragmatique.

### EX-b5f77a789e5b

**Ti veles nifen.**

- FR : Tu es stupide.
- EN: You're stupid.
- Littéral : Tu es stupide, emploi évaluatif insultant.
- Literal: You are stupid, as an insulting evaluation.
- Force : 2/4 · Fonction : insulte · Équivalence : pragmatique.

### EX-b290eed9b8ac

**Ti veles slaroem.**

- FR : Tu es hypocrite.
- EN: You're hypocritical.
- Littéral : Tu fais preuve d'hypocrisie.
- Literal: You display hypocrisy.
- Force : 2/4 · Fonction : accusation · Équivalence : pragmatique.

### EX-2af6f0f7c4a3

**Ti veles lifaen.**

- FR : Tu es déloyal.
- EN: You're treacherous.
- Littéral : Tu es capable de trahison.
- Literal: You are capable of betrayal.
- Force : 2/4 · Fonction : accusation · Équivalence : pragmatique.

### EX-396c44e315cb

**Ti skarnes.**

- FR : Tu te comportes en salopard.
- EN: You're acting like an asshole.
- Littéral : Tu manifestes la conduite d'un skarn.
- Literal: You exhibit the behaviour of a skarn.
- Force : 3/4 · Fonction : accusation · Équivalence : pragmatique.

### EX-ecd3f10bebb8

**Nu skarna!**

- FR : Ne fais pas le connard !
- EN: Don't be an asshole!
- Littéral : Ne te comporte pas en personne méprisable.
- Literal: Do not behave like a vile person.
- Force : 3/4 · Fonction : injonction · Équivalence : pragmatique.

### EX-ce803c82404b

**Graeth-naelkaror!**

- FR : Briseur de serment !
- EN: Oathbreaker!
- Littéral : Destructeur de serment.
- Literal: A destroyer of oaths.
- Force : 2/4 · Fonction : insulte poétique · Équivalence : pragmatique.

### EX-0353803e565b

**Ti naelkares graeth si-en.**

- FR : Tu piétines ta parole.
- EN: You break your own oath.
- Littéral : Tu détruis ton propre serment.
- Literal: You destroy your own oath.
- Force : 2/4 · Fonction : accusation · Équivalence : pragmatique.

### EX-50dea903c623

**Naethala!**

- FR : Casse-toi !
- EN: Get lost!
- Littéral : Pars.
- Literal: Leave.
- Force : 2/4 · Fonction : renvoi · Équivalence : pragmatique.

### EX-65b223ab09bd

**Naethala, vrask!**

- FR : Casse-toi, putain !
- EN: Fuck off!
- Littéral : Pars, suivi d'un juron fort.
- Literal: Leave, followed by a strong expletive.
- Force : 4/4 · Fonction : renvoi · Équivalence : pragmatique.

### EX-a1e68830ce44

**Naethala, skarn!**

- FR : Dégage, connard !
- EN: Get lost, asshole!
- Littéral : Pars, personne méprisable.
- Literal: Leave, vile person.
- Force : 3/4 · Fonction : renvoi · Équivalence : pragmatique.

### EX-8ab2aa73cf9d

**Kaerala vaem si-en!**

- FR : Ferme ta gueule !
- EN: Shut your mouth!
- Littéral : Ferme ta propre bouche.
- Literal: Close your own mouth.
- Force : 3/4 · Fonction : injonction · Équivalence : pragmatique.

### EX-7f121e9f6823

**Kaerala vaem si-en, skarn!**

- FR : Ferme ta gueule, salopard !
- EN: Shut your mouth, asshole!
- Littéral : Ferme ta propre bouche, personne méprisable.
- Literal: Close your own mouth, vile person.
- Force : 3/4 · Fonction : injonction · Équivalence : pragmatique.

### EX-accf503cde14

**Nu lyra!**

- FR : Tais-toi !
- EN: Shut up!
- Littéral : Ne parle pas.
- Literal: Do not speak.
- Force : 2/4 · Fonction : injonction · Équivalence : pragmatique.

### EX-5b0791c2faa9

**Nu lyra, vrask!**

- FR : Tais-toi, putain !
- EN: Shut the fuck up!
- Littéral : Ne parle pas, juron fort.
- Literal: Do not speak, strong expletive.
- Force : 4/4 · Fonction : injonction · Équivalence : pragmatique.

### EX-648dc4f93cfe

**Nu lyra grusk-thareli!**

- FR : Ne raconte pas de conneries !
- EN: Don't talk bullshit!
- Littéral : Ne prononce pas de propos rejetés.
- Literal: Do not speak rejected utterances.
- Force : 3/4 · Fonction : injonction · Équivalence : pragmatique.

### EX-cd5deae5bd08

**Nu vaera grusk-thareli mi-or!**

- FR : Ne me sers pas tes conneries !
- EN: Don't feed me bullshit!
- Littéral : Ne me donne pas des propos rejetés.
- Literal: Do not give me rejected utterances.
- Force : 3/4 · Fonction : injonction · Équivalence : pragmatique.

### EX-010c8cb18510

**Nu skarna ko mi!**

- FR : Ne fais pas le connard avec moi !
- EN: Don't be an asshole with me!
- Littéral : Ne te comporte pas en personne méprisable avec moi.
- Literal: Do not behave like a vile person with me.
- Force : 3/4 · Fonction : injonction · Équivalence : pragmatique.

### EX-0541e1733268

**Nu kaena mi!**

- FR : Ne me touche pas !
- EN: Don't touch me!
- Littéral : Ne me touche pas.
- Literal: Do not touch me.
- Force : 1/4 · Fonction : limite · Équivalence : pragmatique.

### EX-9f3a3792a43f

**Laera mi!**

- FR : Laisse-moi !
- EN: Leave me!
- Littéral : Laisse-moi.
- Literal: Leave me.
- Force : 1/4 · Fonction : limite · Équivalence : pragmatique.

### EX-4316e106a06a

**Laera mi e saerunath!**

- FR : Fous-moi la paix !
- EN: Leave me the hell alone!
- Littéral : Laisse-moi dans la paix.
- Literal: Leave me in peace.
- Force : 3/4 · Fonction : limite · Équivalence : pragmatique.

### EX-9069b36f53e5

**Mi nu dhaelem ti.**

- FR : Je ne te fais pas confiance.
- EN: I don't trust you.
- Littéral : Je ne te fais pas confiance.
- Literal: I do not trust you.
- Force : 1/4 · Fonction : limite · Équivalence : pragmatique.

### EX-eaca4a66ca2b

**Mi nu lisem ti.**

- FR : Je ne t'écoute pas.
- EN: I'm not listening to you.
- Littéral : Je ne t'écoute pas.
- Literal: I do not listen to you.
- Force : 1/4 · Fonction : limite · Équivalence : pragmatique.

### EX-e5087048085b

**Mi nu vaelem lisar ti.**

- FR : Je n'ai pas envie de t'écouter.
- EN: I don't want to listen to you.
- Littéral : Je ne veux pas t'écouter.
- Literal: I do not want to listen to you.
- Force : 1/4 · Fonction : limite · Équivalence : pragmatique.

### EX-c1e52ee7b32f

**Mi nu haedhoefovem ti.**

- FR : Je n'ai pas besoin de toi.
- EN: I don't need you.
- Littéral : Je n'ai pas besoin de toi.
- Literal: I do not need you.
- Force : 1/4 · Fonction : limite · Équivalence : pragmatique.

### EX-a76c4464ab2d

**Mi nu haedhoefovem thareli ti-en.**

- FR : Je n'ai pas besoin de tes discours.
- EN: I don't need your talk.
- Littéral : Je n'ai pas besoin de tes mots.
- Literal: I do not need your words.
- Force : 1/4 · Fonction : limite · Équivalence : pragmatique.

### EX-68690a42e04b

**Mi nu haedhoefovem graethkaevi ti-en.**

- FR : Je n'ai pas besoin de tes règles.
- EN: I don't need your rules.
- Littéral : Je n'ai pas besoin de tes règles.
- Literal: I do not need your rules.
- Force : 1/4 · Fonction : limite · Équivalence : pragmatique.

### EX-f4f8892a29b0

**Mi nu kaethem ti.**

- FR : Tu ne me fais pas peur.
- EN: I'm not afraid of you.
- Littéral : Je ne te crains pas.
- Literal: I do not fear you.
- Force : 1/4 · Fonction : défi · Équivalence : pragmatique.

### EX-8a8a66f09c1a

**Ti nu thaves mi.**

- FR : Tu n'as pas de prise sur moi.
- EN: You don't have a hold on me.
- Littéral : Tu ne me tiens pas.
- Literal: You do not hold me.
- Force : 1/4 · Fonction : défi · Équivalence : pragmatique.

### EX-bbd37e60c172

**Ti dhaves thaem; ti nu dhaves thaev.**

- FR : Tu as de la voix, pas la vérité.
- EN: You've got a voice, not the truth.
- Littéral : Tu as une voix ; tu n'as pas la vérité.
- Literal: You have a voice; you do not have the truth.
- Force : 2/4 · Fonction : pique · Équivalence : pragmatique.

### EX-c15c1772766a

**Thaem ti-en vele thar; thaev vele niv.**

- FR : Grande voix, petite vérité.
- EN: Big voice, little truth.
- Littéral : Ta voix est grande ; la vérité est petite.
- Literal: Your voice is big; the truth is small.
- Force : 2/4 · Fonction : pique poétique · Équivalence : pragmatique.

### EX-30168dd5003a

**Mi vaelem thaev; mi nu vaelem grusk-thareli.**

- FR : Je veux la vérité, pas tes conneries.
- EN: I want the truth, not bullshit.
- Littéral : Je veux la vérité ; je ne veux pas de propos rejetés.
- Literal: I want truth; I do not want rejected utterances.
- Force : 3/4 · Fonction : réplique · Équivalence : pragmatique.

### EX-69670a247144

**Thaem ti-en vele naur; thareli ti-en velen thask.**

- FR : Tu fais du feu, tu ne laisses que des cendres.
- EN: All that fire, and nothing but ashes.
- Littéral : Ta voix est du feu ; tes mots sont des cendres.
- Literal: Your voice is fire; your words are ashes.
- Force : 2/4 · Fonction : pique poétique · Équivalence : pragmatique.

### EX-29882cbce3f2

**Ti vaeres ulthaev; mi vaelem thaev.**

- FR : Tu me sers du mensonge ; je veux la vérité.
- EN: You give me lies; I want the truth.
- Littéral : Tu donnes du mensonge ; je veux la vérité.
- Literal: You give lies; I want truth.
- Force : 2/4 · Fonction : réplique · Équivalence : pragmatique.

### EX-215c8f465a31

**Mi mirem tra ulthaevath ti-en.**

- FR : Je vois à travers tes mensonges.
- EN: I see through your lies.
- Littéral : Je vois à travers ton mensonge.
- Literal: I see through your lie.
- Force : 2/4 · Fonction : réplique · Équivalence : pragmatique.

### EX-90527dbd8f06

**Graeth ti-en vele thask.**

- FR : Ta parole ne vaut plus que de la cendre.
- EN: Your word is nothing but ash.
- Littéral : Ton serment est de la cendre.
- Literal: Your oath is ash.
- Force : 2/4 · Fonction : pique poétique · Équivalence : pragmatique.

### EX-dc4a1455cc09

**Mi nu laevrem si.**

- FR : Je ne plie pas.
- EN: I won't bend.
- Littéral : Je ne me plie pas.
- Literal: I do not fold myself.
- Force : 1/4 · Fonction : défi · Équivalence : pragmatique.

### EX-6e545ea05e43

**Mi nu bregysem si.**

- FR : Je ne m'efface pas.
- EN: I won't erase myself.
- Littéral : Je ne m'efface pas.
- Literal: I do not erase myself.
- Force : 1/4 · Fonction : défi · Équivalence : pragmatique.

### EX-bbee6a2d7d18

**Ti nu vidhaves tharel taesoen.**

- FR : Tu n'auras pas le dernier mot.
- EN: You won't have the last word.
- Littéral : Tu n'auras pas le mot dernier.
- Literal: You will not have the final word.
- Force : 1/4 · Fonction : défi · Équivalence : pragmatique.

### EX-96534402c331

**Ti nu veles en vaur.**

- FR : Tu n'es pas le centre du monde.
- EN: The world doesn't revolve around you.
- Littéral : Tu n'es pas le soleil.
- Literal: You are not the sun.
- Force : 2/4 · Fonction : pique poétique · Équivalence : pragmatique.

### EX-4f82a73d465c

**Thareli ti-en velen maur.**

- FR : Tu parles pour brouiller les pistes.
- EN: Your words are a smokescreen.
- Littéral : Tes mots sont de la brume.
- Literal: Your words are mist.
- Force : 2/4 · Fonction : pique poétique · Équivalence : pragmatique.

### EX-0030492f1a2c

**Vrask, mi velem raev!**

- FR : Putain, je suis libre !
- EN: Fuck, I'm free!
- Littéral : Juron fort ; je suis libre.
- Literal: Strong expletive; I am free.
- Force : 4/4 · Fonction : juron positif · Équivalence : pragmatique.

### EX-f421e11d41d1

**Vrask, ti thaeres saevis!**

- FR : Putain, que tu chantes magnifiquement !
- EN: Fuck, you sing beautifully!
- Littéral : Juron fort ; tu chantes de belle manière.
- Literal: Strong expletive; you sing beautifully.
- Force : 4/4 · Fonction : juron positif · Équivalence : pragmatique.

### EX-c9dc862e544c

**Ith thael garuniv vele saev.**

- FR : Elle est belle, cette fichue chanson.
- EN: This damn song is beautiful.
- Littéral : Cette chanson fichue est belle.
- Literal: This damn song is beautiful.
- Force : 2/4 · Fonction : intensif positif · Équivalence : pragmatique.

### EX-2ab76fd2aafc

**Ith thael vrask vele saev.**

- FR : Elle est belle, cette putain de chanson.
- EN: This fucking song is beautiful.
- Littéral : Cette chanson, intensif vulgaire, est belle.
- Literal: This song, with a vulgar intensifier, is beautiful.
- Force : 4/4 · Fonction : intensif positif · Équivalence : pragmatique.

### EX-59b37e87434e

**Se vele sha saev, vrask!**

- FR : C'est vraiment beau, putain !
- EN: It's so beautiful, fuck!
- Littéral : Cela est très beau, juron fort.
- Literal: It is very beautiful, strong expletive.
- Force : 4/4 · Fonction : juron positif · Équivalence : pragmatique.

### EX-4d88e40cc392

**Skarn vrask!**

- FR : Putain de salopard !
- EN: Fucking asshole!
- Littéral : Personne méprisable, renforcée par un intensif très vulgaire.
- Literal: Vile person with a strong vulgar intensifier.
- Force : 4/4 · Fonction : insulte · Équivalence : pragmatique.

## Renvois et faux amis

| Langue | Recherche | Formulation | Limite du renvoi |
|---|---|---|---|
| fr | va te faire foutre | Naethala, vrask! | renvoi très vulgaire, pas acte sexuel |
| fr | va te faire voir | Naethala! | renvoi familier |
| fr | salope | Ti veles skarn. | mépris d’une conduite, sans inférence sexuelle ; pas une traduction de tous les emplois |
| fr | connasse | Thalen fregos! | injure de mépris ; le nom vaeltharyn ne code pas le genre |
| fr | sale con | Skarn vrask! | injure forte, sans sens hygiénique |
| fr | bordel ! | Grusk! | juron de réaction, pas établissement ni désordre |
| fr | merde alors | Grusk! | surprise contrariée |
| fr | n’importe quoi | Dhimmus! | rejet de propos, pas quantificateur universel |
| fr | ne me raconte pas de salades | Nu vaera grusk-thareli mi-or! | réplique impérative ; aucune salade alimentaire |
| en | motherfucker | Skarn vrask! | strong generic invective; not a statement about family or sex |
| en | son of a bitch | Skarn vrask! | generic invective; not parentage |
| en | bitch | Ti veles skarn. | contempt for behaviour only; not every gendered or sexual use |
| en | dick | Ti veles skarn. | a contemptible person, not anatomy |
| en | prick | Ti veles skarn. | a contemptible person, not anatomy |
| en | bollocks | Grusk-thareli! | dismissal of claims, not anatomy |
| en | bloody hell | Grusk! | approximate frustrated exclamation; strength varies by speaker |
| en | for fuck’s sake | Vrask! | standalone frustration; no automatic causal meaning |
| en | damn it | Grusk! | frustrated exclamation, approximate force |
| en | fuck you | Naethala, vrask! | hostile dismissal, not a sexual instruction |
| en | give me a break | Laera mi e saerunath! | leave-me-alone reading only, not a request for a timed rest |

## Ce que ce complément ne change pas

Les définitions antérieures, les textes de chansons, les licences et les identifiants existants sont préservés. `fuck`, `shit`, `bitch`, `con`, `putain` ou `bordel` ne reçoivent pas une traduction unique pour tous leurs emplois. L’acte sexuel, l’anatomie et les liens familiaux demandent leurs propres lemmes et ne se déduisent pas de ces équivalences pragmatiques. Aucun passé culturel, tabou religieux ou attestation orale n’est inventé pour justifier les jurons.

Les intensifs émotionnels positifs sont distingués des agressions : `vrask, mi velem raev!` n’insulte personne. Les noms de personnes restent sans genre grammatical ; les équivalents genrés des renvois n’ajoutent pas de suffixe masculin ou féminin au Vaeltharyn.

### Conjugaisons utiles

`gruskar` : **mi gruskem**, **ti gruskes**, **se gruske**, **min gruskom**, **tin gruskos**, **sen grusken** ; passé 1SG **mi ragruskem**, futur **mi vigruskem**. Impératifs **gruska / gruskai**. Pas de participe passif proposé : intransitif.

`skarnar` : **mi skarnem**, **ti skarnes**, **se skarne**, **min skarnom**, **tin skarnos**, **sen skarnen** ; passé 1SG **mi raskarnem**, futur **mi viskarnem**. Impératifs **skarna / skarnai**. Pas de participe passif proposé : intransitif.

Contrôle reproductible : `python scripts/verifier_registres.py`. Données : `registres/`. Les règles de grammaire et de phonologie existantes priment ; aucune validation audio n’est déclarée.
