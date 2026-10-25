> Archive historique : périmètre et comptes de son édition. Pour le corpus courant, utiliser le manifeste `corpus.json` à la racine et la recherche indexée.

# Bilan de la grande édition 1.2.0

Retour : [15_Grand_dictionnaire](../../../docs/fr/guides/dictionary-editions.md). Date : 2026-10-24.

## Décompte vérifié

| Mesure | Total |
|---|---:|
| Graphies lexicales distinctes | 65,000 |
| Entrées lemme/catégorie | 65,001 |
| Entrées antérieures conservées | 2 918 |
| Propositions nouvelles avec définition sourcée | 62,083 |
| Verbes | 6,531 |
| Formes finies régulières, comptées à part | 352,674 |
| Volumes directs / inverses | 163 / 163 |

La différence d’une unité entre graphies et entrées vient de `thar`, homographe initial adjectif/particule. Aucune nouvelle homographie lexicale n’a été ajoutée. Les différentes catégories d’un dictionnaire français ne se comparent pas toujours terme pour terme à celles d’une langue construite ; le repère de 65 000 est un objectif de volume, pas une équivalence éditoriale.

## Catégories

| Catégorie | Entrées |
|---|---|
| adj | 14628 |
| adv | 2058 |
| n | 41711 |
| num | 11 |
| part | 62 |
| v | 6531 |

## Domaines

| Domaine | Entrées |
|---|---|
| Actions corporelles | 18 |
| Actions nominalisées | 246 |
| Actions quotidiennes | 26 |
| Agents et activités | 180 |
| Agriculture | 320 |
| Animaux | 449 |
| Arts et images | 328 |
| Arts et récits | 25 |
| Biologie | 229 |
| Bois et menuiserie | 111 |
| Boissons | 34 |
| Chant et imaginaire — composés | 36 |
| Chasse | 174 |
| Chimie | 996 |
| Ciel et astronomie | 131 |
| Climat et météo | 52 |
| Commerce | 136 |
| Communication | 54 |
| Construction | 137 |
| Corps et anatomie | 724 |
| Corps et intimité | 56 |
| Corps et sensations | 30 |
| Création et outils numériques | 32 |
| Croyances et rites | 793 |
| Cuisine et alimentation | 423 |
| Danse et mouvement | 46 |
| Droit | 535 |
| Économie et organisation | 20 |
| Économie et travail | 30 |
| Éducation | 73 |
| Éducation et savoir | 25 |
| Électricité | 248 |
| Émotions et cognition | 30 |
| Émotions et psychologie | 137 |
| Espace et formes | 25 |
| Esprit et liens | 30 |
| Famille et relations sociales | 28 |
| Faune et élevage | 40 |
| Finance | 102 |
| Flore et agriculture | 30 |
| Forêts | 56 |
| Géographie et environnement | 34 |
| Géographie et paysages | 261 |
| Géométrie | 198 |
| Grammaire et relations | 62 |
| Guerre et armes | 258 |
| Habitat et architecture | 356 |
| Héraldique | 137 |
| Histoire | 611 |
| Informatique | 165 |
| Informatique et communication | 35 |
| Insectes | 127 |
| Interactions et communication | 29 |
| Internet | 6 |
| Jeux | 53 |
| Jeux et activité physique | 20 |
| Langue et écriture | 30 |
| Langue et linguistique | 694 |
| Lexicographie | 3 |
| Littérature et récit | 70 |
| Manière et repères | 35 |
| Manières dérivées | 143 |
| Mathématiques | 136 |
| Mathématiques et mesure | 25 |
| Mer et navigation | 632 |
| Mesure | 405 |
| Monde et ciel | 27 |
| Musique et production sonore | 52 |
| Musique et voix | 542 |
| Mythes et imaginaire | 71 |
| Nature et matière | 28 |
| Nombres | 11 |
| Objets, art et rituel | 40 |
| Oiseaux | 326 |
| Pêche | 165 |
| Pensée et apprentissage | 20 |
| Pensée et philosophie | 236 |
| Plantes et milieux | 1715 |
| Poésie et récit | 50 |
| Poissons | 155 |
| Politique et institutions | 200 |
| Psychiatrie | 40 |
| Qualités | 61 |
| Qualités complémentaires | 98 |
| Qualités nominalisées | 154 |
| Relations et domaines | 599 |
| Relations et société | 30 |
| Rituel et imaginaire | 20 |
| Santé | 1254 |
| Santé et soins | 25 |
| Sciences de la matière | 31 |
| Société droit et politique | 32 |
| Sports | 152 |
| Statistiques | 9 |
| Techniques et outils | 198 |
| Technologie et énergie | 29 |
| Temps et calendrier | 20 |
| Temps et monde humain | 31 |
| Temps, lieu et manière | 26 |
| Terre et eau | 36 |
| Terre et géologie | 419 |
| Textiles | 146 |
| Transports | 98 |
| Usages quotidiens — composés | 22 |
| Ustensiles et maison | 40 |
| Verbes | 83 |
| Vêtements | 187 |
| Vêtements et matières | 33 |
| Vie et animaux | 28 |
| Vocabulaire général | 45716 |
| Voyage et transports | 26 |

## Travail réalisé

Le supplément ajoute 62,083 propositions, chacune associée à **un sens français défini**, une catégorie, un domaine, un registre source, une forme stable, une segmentation syllabique de travail et une API calculée. Il ne multiplie ni les pluriels ni les conjugaisons pour atteindre le total. Les 2 918 entrées antérieures et leurs colonnes d’origine sont préservées.

Les formes nouvelles ont été attribuées automatiquement selon un inventaire de syllabes compatible avec la phonologie. Le système réserve les lemmes, leurs flexions régulières et plusieurs dérivations simples ; 5,423 candidats ont été rejetés lors de l’allocation pour éviter des collisions. Cette vérification ne résout pas toutes les ambiguïtés syntaxiques héritées ni les dérivations de profondeur arbitraire.

Les dictionnaires direct et inverse donnent accès aux mêmes entrées. Les liens et ancres du lot ont été vérifiés. Le supplément fournit tous les paradigmes réguliers des nouveaux verbes ; les anciens tableaux restent en place. Les mots français déjà reliés à une entrée connue sont des renvois de recherche, sans changement du sens Vaeltharyn existant.

## Travail éditorial restant

**Les 62,083 nouvelles propositions n’ont pas été relues individuellement comme le seraient les articles d’un dictionnaire publié.** Les filtres de la source peuvent laisser passer des définitions discutables, des doublons de sens ou des mots peu pertinents. Les formes sont phonologiquement contrôlées, mais leur qualité esthétique et leur facilité réelle de chant ne sont pas démontrées.

Les familles étymologiques et morphologiques de tous les nouveaux radicaux ne sont pas reconstruites. Une racine attribuée automatiquement ne prétend pas provenir d’un mot ancien. Les nouvelles unités restent à rapprocher ou à différencier lors de la révision des domaines utilisés. Le français ne détermine ni la culture ni les métaphores obligatoires du Vaeltharyn.

Un groupe nominal défini ou une forme de première personne est un **exemple morphologique**, pas un exemple d’usage naturel. Les nouvelles entrées n’ont pas toutes des phrases contextualisées, des synonymes révisés, des antonymes ou des collocations. L’atelier fournit des points de départ pour les chansons ; les formes retenues dans chaque morceau doivent être relues avec leur traduction.

Aucun test audio, téléchargement de musique ou changement des chansons existantes n’a été effectué. Ce bilan ne revendique pas une exhaustivité absolue du français, de la terminologie scientifique ou des expressions possibles.

## Versionnement

L’édition est une extension compatible 1.2.0 : aucune règle de grammaire n’est modifiée et aucune forme antérieure n’est retirée. Toute correction ultérieure doit garder l’identifiant, noter les anciennes et nouvelles formes, expliquer le changement et rechercher les occurrences dans les chansons avant migration.

Contrôle détaillé : `Grand dictionnaire/controle_grande_edition.json`. Sources et attribution : [18_Sources_et_licences](../../../docs/fr/reference/sources-and-licenses.md). Les anciennes limites de 1.1.0 restent conservées dans [11_Couverture_et_limites](../../../docs/fr/guides/coverage-and-limits.md).
