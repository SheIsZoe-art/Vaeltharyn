# Extension de l’inventaire expressif — français / anglais / Vaeltharyn

Version 1.4.0 · 2026-10-25. [English](../../en/extensions/idioms.md) · [Premier complément](register.md).

Les **719 lignes tabulées** de la pièce jointe sont conservées et traitées : 370 françaises et 349 anglaises. Elles renvoient à **226 fiches de sens**, **222 formulations distinctes utilisées**, et **9 nouveaux lemmes** dérivés ou composés sur des bases existantes. Les flexions, répétitions, variantes de genre et synonymes ne sont pas comptés comme mots nouveaux.

Statut : propositions non validées par le créateur. Les anciennes entrées sont préservées à l’identique. Les sens du grand lexique réemployés ont été lus pour cette tâche ; leur réemploi n’équivaut pas à valider tous les mots du corpus. Les constructions ont été vérifiées à l’écrit, sans test audio.

## Méthode et couverture

Le document original est [reproduit exactement](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt), avec [empreinte et provenance](../../../data/expressions/idioms-1.4.0/references/provenance.json). Les corrections ne modifient pas cette pièce. Le [tableau complet de couverture](../../../data/expressions/idioms-1.4.0/couverture.csv) conserve chaque ligne, sa langue, ses correspondances fournies, les sens proposés et les limites. Les formulations ne sont pas attribuées aléatoirement : le [routage par lignes](../../../data/expressions/idioms-1.4.0/couverture-redigee.txt) et les [fiches rédigées](../../../data/expressions/idioms-1.4.0/sens-rediges.tsv) sont conservés.

Les emplois ordinaires, injurieux, sexuels, figurés, régionaux, archaïques, ironiques et admiratifs ne sont pas fusionnés. Une seule expression source peut renvoyer à plusieurs lectures ; le contexte choisit. « Je m’en fiche » et « j’en ai rien à foutre » ont le même contenu possible mais des degrés distincts. « C’est de la merde » et « ce putain de… » ne confondent pas mauvaise qualité et intensité.

`jobard` est orienté vers la crédulité, non la folie ; `knucklehead` vers sottise ou maladresse, non obstination obligatoire. `pissed` américain ne remplace pas `ivre` britannique. `badass` et `kick-ass` peuvent être admiratifs. Les mots `rater` (mise à feu), `échouer` (navigation), `bâcler` (arrêt de navigation), `problème` (question scientifique), `moquer` (intransitif) et `soucier` (causer du souci) de l’ancien lexique ne sont pas détournés pour obtenir une traduction commode.

## Cas sans équivalent établi

Les deux formes régionales « D jobi / jobi » et « Gognand » restent à confirmer. Les deux injures sociales américaines `trailer trash` et `white trash` sont documentées avec leurs connotations, sans inventer une population vaeltharyn correspondante. Ces quatre lignes ne sont pas présentées comme traduites exactement. Les autres approximations culturelles ou de registre sont indiquées dans les fiches.

Les injures sexuelles et genrées sont documentées comme emplois de locuteurs ; elles ne prouvent ni conduite réelle, ni orientation, ni consentement. Le Vaeltharyn n’impose pas de genre grammatical, mais les noms `sorkev` et `bidim` permettent de conserver un référent explicitement femme ou homme lorsque le sens le demande. Une activité sexuelle, la prostitution, la faiblesse ou un célibat ne sont pas automatiquement synonymes de méchanceté, crime ou misogynie. Les diagnostics ne se déduisent pas des invectives.

## Cohérence et sonorité écrite

Aucune racine nouvelle n’est allouée au hasard. Les neuf ajouts sont des dénominaux ou des composés définis ci-dessous. L’accent des verbes reste sur la racine ; les composés gardent accent principal et secondaire. Les verbes en -ar ne perdent aucune lettre à la flexion. Les groupes consonantiques issus d’une frontière morphologique sont articulés sans apostrophe décorative ni élision inventée. Les composés longs sont des choix expressifs possibles, pas une obligation dans un refrain rapide : une paraphrase courte existante reste disponible.

Les contrôles recherchent collisions avec les anciens lemmes et les formes fléchies, ainsi que les doublons d’identifiants. Les phrases conservent les agents, cibles et nombres : « il se moque de moi » ne devient pas une question adressée à « tu » ; peur et colère ont deux routes pour « ça me fout les boules ». Les contre-exemples « chanter une querelle », `sha` devant un nom et `ko` pour le comparatif sont exclus des traductions publiées et conservés seulement comme tests négatifs.

## Neuf entrées lexicales

### VX-f2322cff4e11153c

**gydimar** · `v` · /ˈgy.dim.ar/

**FR :** Ne pas réussir une action ou un projet. Intransitif ; ne signifie pas seulement un raté de mise à feu ni un échouage maritime.

**EN:** To fail at an action or project. Intransitive; not merely a gun misfiring or a vessel running aground.

Formation : gydim ; nom + ar ; manifestation du ratage, lecture intransitive enregistrée. Valence : intr.

Mi ragydimem. — J’ai échoué. — I failed.

### VX-97008f247782429b

**slusoemar** · `v` · /ˈslu.sœːm.ar/

**FR :** Accorder de l’importance à quelque chose ou quelqu’un dans son soin, son intérêt ou son inquiétude. Objet direct ; ne signifie pas causer de l’inquiétude à autrui.

**EN:** To care about a person or matter through attention, interest or concern. Takes a direct object; does not mean to cause someone else concern.

Formation : slusoem ; nom + ar ; valence transitive explicitement lexicalisée, non générale pour les dénominaux. Valence : tr.

Mi nu slusoemem se. — Je ne m’en préoccupe pas. — I do not care about it.

### VX-7639c72e87540506

**thenthosar** · `v` · /ˈθɛn.θɔs.ar/

**FR :** Tourner une personne ou une chose en ridicule. Objet direct pour la cible ; distinct du verbe intransitif dynbothar, se railler.

**EN:** To mock or ridicule a person or thing. The target is a direct object; distinct from intransitive dynbothar.

Formation : thenthos ; nom + ar ; sens transitif explicitement lexicalisé. Valence : tr.

Se thenthose mi. — Il ou elle se moque de moi. — They are mocking me.

### VX-562c9cc095617dab

**gydim-thalen** · `n` · /ˈgy.dimˌθa.lɛn/

**FR :** Personne méprisée par un locuteur pour des échecs qu’il lui attribue. Désignation injurieuse, non mesure de la valeur d’une vie.

**EN:** A person disparaged by a speaker for attributed failures. An insulting label, not a measure of the value of a life.

Formation : gydim + thalen ; composition nominale ratage + personne ; emploi injurieux explicitement proposé. Valence : nom.

Gydim-thalen! — Raté ! — Loser!

### VX-784f5431e53b89e0

**nathem-thaelor** · `n` · /ˈna.θɛmˌθæː.lɔr/

**FR :** Personne accusée de provoquer des querelles. L’intention de discorde distingue cet emploi d’un simple ratage involontaire.

**EN:** A person accused of provoking quarrels. Stirring discord is distinct from merely making an accidental mistake.

Formation : nathem + thaelor ; composition nominale querelle + créateur ; registre de l’expression fixé par le contexte. Valence : nom.

Nathem-thaelor! — Fouteur de discorde ! — Shit-stirrer!

### VX-5568b94aa9f465ec

**vaermar-lodhom** · `n` · /ˈvæːr.marˌlɔ.ðɔm/

**FR :** Personne accusée de trahir ses engagements pour un gain financier. Les autres motivations de la trahison restent à contextualiser.

**EN:** A person accused of betraying commitments for financial gain. Other motives for betrayal need separate context.

Formation : vaermar + lodhom ; composition nominale monnaie + traître. Valence : nom.

Vaermar-lodhom! — Vendu ! — Sellout!

### VX-b551a8a8a6c1aff0

**vareth-greth** · `n` · /ˈva.rɛθˌgrɛθ/

**FR :** Difficulté ou obstacle à dénouer dans une action ou une relation ; métaphore d’un nœud sur le chemin. Distinct d’une question scientifique à résoudre.

**EN:** A practical or interpersonal difficulty to untangle, using the image of a knot in a path. Distinct from a scientific question or exercise.

Formation : vareth + greth ; composition nominale chemin + nœud ; métaphore explicitement lexicalisée. Valence : nom.

Mi dhavem vareth-greth. — J’ai une difficulté. — I have a problem.

### VX-066c896124f55161

**fonul-brabon** · `n` · /ˈfɔ.nulˌbra.bɔn/

**FR :** Composé décrivant une personne qui suce un pénis. En adresse injurieuse, l’acte est allégué sans être établi. L’orientation sexuelle n’est pas encodée ; le calque ne garantit pas une force culturelle identique.

**EN:** A compound describing someone sucking a penis. In insulting address, the act is alleged rather than established. Sexual orientation is not encoded; the calque does not guarantee identical cultural force.

Formation : fonul + brabon ; composition nominale pénis + personne qui suce ; portée descriptive et injurieuse distinguée. Valence : nom.

Fonul-brabon! — Suceur de pénis ! — Cocksucker!

### VX-904333cb297e9843

**traemtoer-dhokun** · `n` · /ˈtræːm.tœːrˌðɔ.kun/

**FR :** Injure extrêmement dégradante comparant une personne à un récipient de sperme. La comparaison n’établit ni activité sexuelle réelle ni consentement.

**EN:** An extremely degrading insult comparing a person to a receptacle for semen. It establishes neither real sexual activity nor consent.

Formation : traemtoer + dhokun ; composition nominale sperme + sac ; métaphore objectivante explicitement citée. Valence : nom.

Traemtoer-dhokun! — Sac à sperme ! — Cum dumpster!

## Références vérifiées

| Référence | Source | Note |
|---|---|---|
| REF-INPUT | [Inventaire fourni par le créateur](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt) | 719 lignes tabulées ; correspondances à examiner, pas autorité lexicographique indépendante. |
| REF-PISSED | [Collins — pissed](https://www.collinsdictionary.com/us/dictionary/english/pissed) | Distingue colère américaine et ivresse britannique. |
| REF-BADASS | [Cambridge — badass](https://dictionary.cambridge.org/us/dictionary/english/badass) | Distingue la lecture menaçante de la lecture admirative. |
| REF-CUNT | [Cambridge — cunt](https://dictionary.cambridge.org/us/dictionary/english/cunt) | Marque l’offense et distingue insulte personnelle et sens anatomique. |
| REF-JOBARD | [Académie française — jobard](https://www.dictionnaire-academie.fr/article/A9J0220) | Le sens retenu vise une crédulité excessive ; la correspondance nutcase du document est corrigée. |
| REF-CUISTRE | [Académie française — cuistre](https://www.dictionnaire-academie.fr/article/A9C5228) | Pédanterie vaniteuse ; le terme hérité dafyv est réutilisé. |
| REF-KNUCKLEHEAD | [Dictionary.com — knucklehead](https://www.dictionary.com/browse/knucklehead) | L’idiotie ou la maladresse, plutôt que l’obstination, est retenue. |
| REF-SNITCH | [Cambridge — snitch](https://dictionary.cambridge.org/dictionary/english/snitch) | Dénonciation secrète à une autorité ; ne pas déduire le sens voler. |
| REF-SHITFACED | [Oxford Learner’s — shit-faced](https://www.oxfordlearnersdictionaries.com/definition/english/shit-faced) | Le terme adjectival signifie très ivre ; ne pas l’appliquer automatiquement au nom injurieux shitface fourni. |
| REF-PEUCHERE | [Académie française — peuchère](https://www.dictionnaire-academie.fr/article/A9P1862) | Peut exprimer compassion, étonnement ou admiration ; le mot n’est pas toujours un juron. |
| REF-TRAILER | [Cambridge — trailer trash](https://dictionary.cambridge.org/dictionary/english/trailer-trash) | Marque sociale et racialisée documentée ; aucun groupe équivalent dans la fiction n’est inventé. |

## Fiches de sens et formulations

### S-idiot

**Vaeltharyn :** Kofav!

**FR :** Imbécile ! **EN:** Idiot!

Jugement injurieux, pas diagnostic médical

Force indicative : 2/4. Sources : L6, L7, L8, L9, L10, L437, L438, L439, L440, L441, L443, L444, L445, L446, L447, L448, L449, L451, L452, L455, L456, L461, L463, L464, L465, L483, L484, L485.

### S-idiot_strong

**Vaeltharyn :** Kofav vrask!

**FR :** Putain d'imbécile ! **EN:** Fucking idiot!

L'intensif porte sur le nom

Force indicative : 4/4. Sources : L439, L440, L465, L58, L458.

### S-fool

**Vaeltharyn :** Tronodaev!

**FR :** Idiot ! **EN:** Fool!

Manque de jugement attribué

Force indicative : 2/4. Sources : L15, L16, L17, L18, L19, L20, L21, L22, L23, L39, L64, L65, L457, L459, L460, L442, L450.

### S-silly

**Vaeltharyn :** Thalen basoel!

**FR :** Personne sotte ! **EN:** Silly person!

Peut être taquin, sans équivalence affectueuse automatique

Force indicative : 1/4. Sources : L445, L446, L447, L448, L449, L15, L16, L11, L12, L13, L14.

### S-gullible

**Vaeltharyn :** Thalen loemkyk!

**FR :** Personne trop crédule ! **EN:** Gullible fool!

Crédulité, non folie

Force indicative : 1/4. Sources : L375, L481, L482.

### S-old_fool

**Vaeltharyn :** Kofav mamysem!

**FR :** Vieil imbécile ! **EN:** Old fool!

L'âge est conservé quand la source le vise

Force indicative : 2/4. Sources : L24, L389.

### S-scatterbrain

**Vaeltharyn :** Laelbek!

**FR :** Distrait ! **EN:** Scatterbrain!

Inattention, pas forcément manque d'intelligence

Force indicative : 1/4. Sources : L26, L27.

### S-airhead

**Vaeltharyn :** Brosol!

**FR :** Écervelé ! **EN:** Airhead!

Peu de jugement, sans genre grammatical

Force indicative : 2/4. Sources : L183, L184, L185, L186, L453, L630.

### S-burden

**Vaeltharyn :** Ti veles mersik min-or.

**FR :** Tu es un fardeau pour nous. **EN:** You're a burden to us.

Métaphore de charge, pas un poids physique réel

Force indicative : 2/4. Sources : L28.

### S-loser

**Vaeltharyn :** Gydim-thalen!

**FR :** Raté ! **EN:** Loser!

Désignation méprisante liée aux échecs; pas un constat de valeur humaine

Force indicative : 2/4. Sources : L39, L29, L30, L38, L40, L41, L44, L476, L477, L480, L515, L785.

### S-inept

**Vaeltharyn :** Thalen slyllum!

**FR :** Incapable ! **EN:** Incompetent person!

Capacité dans le contexte, non inutilité générale

Force indicative : 2/4. Sources : L477, L37, L380.

### S-clown

**Vaeltharyn :** Thalen thryrsom!

**FR :** Guignol ! **EN:** Ridiculous fool!

Ridicule, pas métier du cirque

Force indicative : 2/4. Sources : L461, L30, L31, L32, L34, L35, L43, L462, L474, L475, L478, L479.

### S-puppet

**Vaeltharyn :** Ti veles porvogok.

**FR :** Tu es un pantin. **EN:** You're a puppet.

Métaphore explicite de manipulation, pas extension silencieuse du jouet

Force indicative : 2/4. Sources : L475, L33, L607, L608.

### S-useless

**Vaeltharyn :** Thalen ulhaevvaer!

**FR :** Bon à rien ! **EN:** Good-for-nothing!

Jugement de locuteur, non définition d'une personne

Force indicative : 2/4. Sources : L515, L36, L42, L90, L378, L379, L516, L586, L163.

### S-lout

**Vaeltharyn :** Goelvaek!

**FR :** Malotru ! **EN:** Lout!

Manque de savoir-vivre

Force indicative : 2/4. Sources : L381, L47, L48, L52, L383, L384, L385, L386.

### S-boor

**Vaeltharyn :** Luthom!

**FR :** Rustre ! **EN:** Boor!

N'implique pas une origine rurale

Force indicative : 2/4. Sources : L382, L50.

### S-cad

**Vaeltharyn :** Boenrev!

**FR :** Goujat ! **EN:** Cad!

Conduite grossière, particulièrement envers les femmes dans le sens hérité

Force indicative : 2/4. Sources : L49, L51.

### S-clumsy

**Vaeltharyn :** Slaehoen!

**FR :** Maladroit ! **EN:** Clumsy fool!

Maladresse, pas stupidité générale

Force indicative : 1/4. Sources : .

### S-boor_clumsy

**Vaeltharyn :** Skaedhal!

**FR :** Balourd ! **EN:** Bumbling lout!

Grossièreté et maladresse

Force indicative : 2/4. Sources : L454.

### S-country_sneer

**Vaeltharyn :** Thalen thriroes!

**FR :** Personne rustre ! **EN:** Uncouth person!

Équivalence partielle: ne conserve pas le mépris d'origine sociale ou rurale

Force indicative : 2/4. Sources : L45, L46.

### S-vile

**Vaeltharyn :** Skarn!

**FR :** Salopard ! **EN:** Asshole!

Mépris d'une conduite; pas anatomie ni filiation

Force indicative : 3/4. Sources : L483, L484, L64, L65, L57, L62, L63, L66, L67, L68, L69, L70, L71, L72, L73, L74, L75, L76, L80, L81, L82, L83, L84, L85, L86, L87, L92, L93, L95, L96, L99, L100, L101, L102, L177, L178, L179, L180, L181, L182, L187, L193, L194, L195, L200, L201, L466, L467, L468, L469, L470, L471, L472, L473, L497, L498, L499, L500, L501, L502, L505, L506, L507, L508, L509, L510, L511, L512, L517, L518, L519, L583, L617, L618, L619, L635.

### S-vile_strong

**Vaeltharyn :** Skarn vrask!

**FR :** Putain de salopard ! **EN:** Fucking asshole!

Équivalent de force pour invectives fortes, non récit sexuel ou familial

Force indicative : 4/4. Sources : L58, L100, L101, L102, L499, L509, L510, L60, L98, L103, L492, L522, L523, L634, L637.

### S-small_vile

**Vaeltharyn :** Skarnil!

**FR :** Petit merdeux ! **EN:** Little shit!

Diminutif péjoratif contextuel, pas âge déduit

Force indicative : 3/4. Sources : L59, L77, L78, L91, L405, L487, L488, L489.

### S-old_vile

**Vaeltharyn :** Skarn mamysem!

**FR :** Vieux con ! **EN:** Old asshole!

Âge explicite de l'insulte source

Force indicative : 3/4. Sources : L61.

### S-worthless_vile

**Vaeltharyn :** Skarn ulhaevvaer!

**FR :** Ordure jugée bonne à rien ! **EN:** Worthless bastard!

Pragmatique; ne reproduit pas une image de fausse couche ou d'objet sexuel

Force indicative : 4/4. Sources : L515, L516, L95, L96, L510, L511, L79, L94, L503, L504.

### S-corrupt

**Vaeltharyn :** Moesyk!

**FR :** Pourri ! **EN:** Corrupt bastard!

Corruption, pas toute forme de méchanceté

Force indicative : 3/4. Sources : .

### S-fregos

**Vaeltharyn :** Thalen fregos!

**FR :** Connard ! **EN:** Jerk!

Nom explicite avec adjectif; pas nominalisation arbitraire

Force indicative : 3/4. Sources : L458, L64, L65, L457, L459, L460, L57, L62, L63, L82, L83, L84, L85, L86, L182, L98.

### S-small_fool

**Vaeltharyn :** Kofavil!

**FR :** Petit idiot ! **EN:** Little fool!

Diminutif régulier de kofav

Force indicative : 2/4. Sources : .

### S-lazy

**Vaeltharyn :** Tasil!

**FR :** Paresseux ! **EN:** Slacker!

Paresse, non masturbation

Force indicative : 2/4. Sources : L379, L87, L467, L88, L585.

### S-lazy_strong

**Vaeltharyn :** Tasil vrask!

**FR :** Putain de feignasse ! **EN:** Lazy bastard!

Intensif de paresse, pas acte sexuel

Force indicative : 4/4. Sources : L89, L584.

### S-pedant

**Vaeltharyn :** Paemevus!

**FR :** Pédant ! **EN:** Pedant!

Étalage de savoir; ne signifie pas exactitude utile

Force indicative : 2/4. Sources : L99, L388, L559.

### S-cuistre

**Vaeltharyn :** Dafyv!

**FR :** Cuistre ! **EN:** Pompous pseudo-scholar!

Savoir affiché de façon vaniteuse et mal maîtrisée

Force indicative : 2/4. Sources : L387.

### S-nuisance

**Vaeltharyn :** Thalen ya horsahime mi!

**FR :** Emmerdeur ! **EN:** Pain in the ass!

Personne qui m'importune; pas personne qui défèque

Force indicative : 3/4. Sources : L110, L111, L112, L114, L135, L572.

### S-nuisance_mild

**Vaeltharyn :** Thalen ya horsahime mi, sketh!

**FR :** Casse-pieds ! **EN:** Pain in the neck!

Version atténuée, destinataire implicite contextualisé

Force indicative : 2/4. Sources : L113, L573, L574.

### S-troublemaker

**Vaeltharyn :** Nathem-thaelor!

**FR :** Fouteur de discorde ! **EN:** Shit-stirrer!

Production de querelles, distincte d'une erreur involontaire

Force indicative : 3/4. Sources : L115, L167, L551, L552.

### S-nosy

**Vaeltharyn :** Slakal!

**FR :** Fouineur ! **EN:** Nosy meddler!

Ne présume pas une enquête journalistique illégitime

Force indicative : 2/4. Sources : L116, L117, L570, L571.

### S-bootlicker

**Vaeltharyn :** Toenvapam!

**FR :** Lèche-bottes ! **EN:** Bootlicker!

Servilité envers les puissants, pas action de lécher

Force indicative : 3/4. Sources : L118, L119, L545, L546, L547, L548, L550.

### S-hypocrite

**Vaeltharyn :** Skithin!

**FR :** Hypocrite ! **EN:** Hypocrite!

Deux attitudes opposées selon l'interlocuteur, pas deux visages anatomiques

Force indicative : 2/4. Sources : L120, L121, L122, L536, L538.

### S-liar

**Vaeltharyn :** Vraegom!

**FR :** Menteur ! **EN:** Liar!

Accusation de mensonge sans diagnostic

Force indicative : 2/4. Sources : L123, L124, L534, L535.

### S-liar_habit

**Vaeltharyn :** Vraegom ya ara ulthaeve!

**FR :** Menteur invétéré ! **EN:** Habitual liar!

Habitude, pas diagnostic de mythomanie

Force indicative : 2/4. Sources : L124, L535.

### S-bullshitter

**Vaeltharyn :** Mulroem!

**FR :** Baratineur ! **EN:** Bullshitter!

Baratin; n'implique pas un mensonge pathologique

Force indicative : 2/4. Sources : L125, L126, L533.

### S-loudmouth

**Vaeltharyn :** Thalen thaemraeliv!

**FR :** Grande gueule ! **EN:** Loudmouth!

Personne bruyante; pas révélation de secret déduite

Force indicative : 2/4. Sources : L127, L128, L129, L555, L556.

### S-braggart

**Vaeltharyn :** Foeden!

**FR :** Vantard ! **EN:** Braggart!

Celui qui se vante

Force indicative : 2/4. Sources : L563.

### S-showoff

**Vaeltharyn :** Frobim!

**FR :** Frimeur ! **EN:** Show-off!

Frime, pas pose d'objets

Force indicative : 2/4. Sources : L130, L132, L562.

### S-poser

**Vaeltharyn :** Thalen nygaek!

**FR :** Poseur ! **EN:** Poser!

Adjectif d'affectation, pas le nom du poseur d'objets

Force indicative : 2/4. Sources : L131, L564.

### S-arrogant

**Vaeltharyn :** Memkor!

**FR :** Arrogant ! **EN:** Arrogant person!

Attitude hautaine

Force indicative : 2/4. Sources : L473, L133.

### S-bossy

**Vaeltharyn :** Slilyk!

**FR :** Petit chef ! **EN:** Bossy control freak!

Volonté de dominer l'entourage

Force indicative : 2/4. Sources : L134.

### S-grouch

**Vaeltharyn :** Baroth!

**FR :** Pisse-vinaigre ! **EN:** Sourpuss!

Humeur revêche; aucune urine dans le sens

Force indicative : 2/4. Sources : L136, L137, L190, L191, L192.

### S-killjoy

**Vaeltharyn :** Loefoeton!

**FR :** Rabat-joie ! **EN:** Killjoy!

Hostilité à la joie des autres

Force indicative : 2/4. Sources : L138, L577, L578, L581.

### S-prude

**Vaeltharyn :** Thalen troedhel!

**FR :** Personne coincée ! **EN:** Prude!

Pruderie dans cette lecture, pas radinerie

Force indicative : 2/4. Sources : L139, L580.

### S-rigid

**Vaeltharyn :** Thalen koriv!

**FR :** Personne rigide ! **EN:** Rigid person!

Métaphore corporelle; pudibonderie et avarice restent distinctes

Force indicative : 2/4. Sources : L140, L579.

### S-coward

**Vaeltharyn :** Thalen sen vaethun!

**FR :** Lâche ! **EN:** Coward!

Absence de courage attribuée; distincte d'une corde lâche

Force indicative : 2/4. Sources : L30, L492, L143, L146, L600, L601, L602, L605, L606, L643.

### S-timid

**Vaeltharyn :** Tanek!

**FR :** Trouillard ! **EN:** Scaredy-cat!

Disposition craintive; pas inférence de lâcheté morale

Force indicative : 2/4. Sources : L601, L602, L141, L142, L145.

### S-weakling

**Vaeltharyn :** Thalen getor!

**FR :** Mauviette ! **EN:** Weakling!

Faiblesse attribuée; pas identité de genre

Force indicative : 2/4. Sources : L605, L144, L603, L604, L612, L642.

### S-whiner

**Vaeltharyn :** Gaegylym!

**FR :** Pleurnichard ! **EN:** Crybaby!

Manière larmoyante, pas pathologie ni enfant réel

Force indicative : 2/4. Sources : L147, L148, L575, L576.

### S-snitch

**Vaeltharyn :** Pupak!

**FR :** Mouchard ! **EN:** Informer!

Le sens hérité porte sur la police; lecture scolaire séparée

Force indicative : 2/4. Sources : L149, L150, L151, L541, L542.

### S-tattletale

**Vaeltharyn :** Thalen ya vaere kaer thaliror!

**FR :** Rapporteur ! **EN:** Tattletale!

Donne un secret au parent, au datif; contexte enfantin, pas accusation criminelle

Force indicative : 2/4. Sources : L149, L543, L549.

### S-traitor

**Vaeltharyn :** Lodhom!

**FR :** Traître ! **EN:** Traitor!

Trahison, pas morsure animale

Force indicative : 2/4. Sources : L541, L152, L539, L540.

### S-sellout

**Vaeltharyn :** Vaermar-lodhom!

**FR :** Vendu ! **EN:** Sellout!

Traître par intérêt financier dans cette lecture

Force indicative : 3/4. Sources : L153, L544.

### S-freeloader

**Vaeltharyn :** Brimvav!

**FR :** Pique-assiette ! **EN:** Freeloader!

Profite sans contribuer, non animal parasite

Force indicative : 2/4. Sources : L518, L154, L155, L156, L157, L588, L589, L590.

### S-exploiter

**Vaeltharyn :** Saehoemoem!

**FR :** Exploiteur ! **EN:** Exploiter!

Profit abusif d'une personne ou situation

Force indicative : 2/4. Sources : .

### S-profiteer

**Vaeltharyn :** Graloes!

**FR :** Profiteur ! **EN:** Dishonest opportunist!

Avantage obtenu malhonnêtement

Force indicative : 2/4. Sources : L154, L588.

### S-greedy

**Vaeltharyn :** Thalen dhepegor!

**FR :** Rapace d'argent ! **EN:** Greedy person!

Avidité, non espèce d'oiseau

Force indicative : 2/4. Sources : L158.

### S-cheapskate

**Vaeltharyn :** Nulyk!

**FR :** Radin ! **EN:** Cheapskate!

Avare, pas rat animal

Force indicative : 2/4. Sources : L579, L159, L160, L591, L592, L593.

### S-penny_pincher

**Vaeltharyn :** Vrasik!

**FR :** Grippe-sou ! **EN:** Penny-pincher!

Attachement aux petits gains

Force indicative : 2/4. Sources : L592, L161.

### S-crook

**Vaeltharyn :** Tridum!

**FR :** Escroc ! **EN:** Scammer!

Accusation d'escroquerie, à distinguer d'incompétence

Force indicative : 2/4. Sources : L162, L164, L537, L594, L595.

### S-thug

**Vaeltharyn :** Lavum!

**FR :** Malfaiteur ! **EN:** Thug!

Conduite criminelle alléguée

Force indicative : 2/4. Sources : L165, L166, L486.

### S-filthy

**Vaeltharyn :** Thalen thrutos!

**FR :** Crasseux ! **EN:** Filthy slob!

Saleté, pas sexualité

Force indicative : 2/4. Sources : L519, L583, L390, L391, L392, L393, L394, L395, L582.

### S-drunkard

**Vaeltharyn :** Freloek!

**FR :** Poivrot ! **EN:** Drunkard!

Consommation habituelle excessive, pas simple ivresse ponctuelle

Force indicative : 2/4. Sources : L396, L397, L398, L399, L400.

### S-barfly

**Vaeltharyn :** Thalen ya ara vathune vaurmeth!

**FR :** Habitué qui boit sans cesse ! **EN:** Habitual drinker!

Périphrase: boit habituellement du vin; lieu du comptoir non codé

Force indicative : 2/4. Sources : .

### S-brat

**Vaeltharyn :** Maelin vrothok!

**FR :** Sale gosse ! **EN:** Brat!

Enfant impertinent, pas n'importe quel enfant

Force indicative : 2/4. Sources : L568, L403, L404, L490, L491.

### S-rascal

**Vaeltharyn :** Maelin throefuth!

**FR :** Petit chenapan ! **EN:** Little rascal!

Insolence légère dans cet emploi

Force indicative : 1/4. Sources : L401, L402, L708.

### S-old_vile_woman

**Vaeltharyn :** Sorkev mamysem koebok!

**FR :** Vieille femme méprisée ! **EN:** Contemptuously labelled old woman!

Équivalence descriptive: conserve âge et femme, pas chèvre ni peau comme fait

Force indicative : 3/4. Sources : L188, L189.

### S-bitch

**Vaeltharyn :** Sorkev skentav!

**FR :** Garce ! **EN:** Bitch!

Personne adulte féminine visée pour sa conduite; pas sexualité implicite

Force indicative : 3/4. Sources : L69, L177, L178, L179, L180, L181, L182, L187, L201, L617, L618, L619, L175, L176.

### S-sexual_slur

**Vaeltharyn :** Sorkev borbaem!

**FR :** Femme accusée de débauche ! **EN:** Woman accused of sexual depravity!

Accusation du locuteur, pas description vraie ni défaut de consentement

Force indicative : 4/4. Sources : L178, L179, L180, L181, L187, L173, L174, L175, L202, L203, L204, L623, L624, L625, L626, L627, L628.

### S-sexwork_slur

**Vaeltharyn :** Trosen!

**FR :** Pute ! **EN:** Whore!

Le mot hérité est descriptif; l'adresse injurieuse impute une prostitution sans l'établir

Force indicative : 4/4. Sources : L173, L174, L202, L624, L625.

### S-bimbo

**Vaeltharyn :** Sorkev supyk!

**FR :** Femme jugée écervelée ! **EN:** Woman called an airhead!

Équivalence partielle; ne code pas apparence ni intelligence réelle

Force indicative : 2/4. Sources : L183, L184, L185, L186, L630, L178, L179, L180, L629.

### S-sexual_creep

**Vaeltharyn :** Thalen graefyhael!

**FR :** Personne lubrique ! **EN:** Lewd person!

Désir affiché, non prédateur ou criminel déduit

Force indicative : 3/4. Sources : L200, L196, L199, L639, L640, L645, L646.

### S-creep

**Vaeltharyn :** Kaelydhyk!

**FR :** Personne répugnante ! **EN:** Disgusting creep!

Jugement de dégoût dans le sens hérité; ne vaut pas preuve de crime sexuel

Force indicative : 3/4. Sources : L520.

### S-pervert

**Vaeltharyn :** Thalen borbaem!

**FR :** Personne jugée dépravée ! **EN:** Person called depraved!

Jugement moral de locuteur; contexte sexuel à préciser

Force indicative : 3/4. Sources : L198, L644.

### S-disgusting

**Vaeltharyn :** Thalen loror!

**FR :** Personne dégoûtante ! **EN:** Disgusting person!

Dégoût, sans diagnostic

Force indicative : 3/4. Sources : L522, L523, L197.

### S-cuckold

**Vaeltharyn :** Barryv!

**FR :** Cocu ! **EN:** Cuckold!

Partenaire infidèle dans le sens hérité; pas « faible soumis » automatique

Force indicative : 2/4. Sources : L206, L610.

### S-flirt_accusation

**Vaeltharyn :** Sorkev ya vaere dhirum!

**FR :** Femme accusée d'attiser l'attirance ! **EN:** Woman accused of provoking attraction!

Équivalence partielle; n'implique aucune obligation sexuelle

Force indicative : 3/4. Sources : L205, L632, L633.

### S-sexist_boor

**Vaeltharyn :** Goelvaek ya ulmaerune sorkevi!

**FR :** Goujat qui méprise les femmes ! **EN:** Boor who despises women!

Comportement explicite, pas tout sens social de beauf

Force indicative : 3/4. Sources : L207.

### S-scat

**Vaeltharyn :** Grusk!

**FR :** Merde ! **EN:** Shit!

Juron indépendant

Force indicative : 3/4. Sources : L212, L213, L214, L217, L225, L226, L257, L262, L663, L664, L665, L668, L669, L684, L321.

### S-strong_expletive

**Vaeltharyn :** Vrask!

**FR :** Putain ! **EN:** Fuck!

Juron, sans acte sexuel ni destinataire nécessaire

Force indicative : 4/4. Sources : L217, L215, L238, L652, L653, L654, L658, L659, L678, L681, L682, L259.

### S-double_expletive

**Vaeltharyn :** Vrask, grusk!

**FR :** Putain de merde ! **EN:** Fucking hell!

Accumulation expressive, pas opération génitale

Force indicative : 4/4. Sources : L658, L659, L678, L216, L218, L219, L220, L655, L666, L675.

### S-mild_expletive

**Vaeltharyn :** Sketh!

**FR :** Zut ! **EN:** Darn!

Atténuation; pas traduction d'une plante ou d'un aliment

Force indicative : 1/4. Sources : L704, L709, L246, L247, L248, L249, L250, L251, L252, L253, L667, L692, L693, L694, L695, L697, L698, L699, L700, L701.

### S-theatrical

**Vaeltharyn :** Sketh, en hael!

**FR :** Grand ciel ! **EN:** Good heavens!

Proposition théâtrale; ne devient pas un archaïsme vaeltharyn attesté

Force indicative : 1/4. Sources : L227, L228, L230, L231, L232, L233, L239, L258, L676, L680, L702, L703, L704, L705, L706, L707, L709, L373.

### S-god_expletive

**Vaeltharyn :** Lemkun, vrask!

**FR :** Dieu, putain ! **EN:** God, damn it!

Invocation expressive; aucun tabou autochtone inventé

Force indicative : 4/4. Sources : L675, L221, L222, L223, L224, L229, L670, L671, L672, L673, L674, L677, L679.

### S-by_god

**Vaeltharyn :** Lemkun!

**FR :** Par Dieu ! **EN:** By God!

Invocation libre proposée; pas traduction syntaxique de « par » instrumental

Force indicative : 2/4. Sources : L222, L673, L674, L234, L235, L236, L237.

### S-devil_expletive

**Vaeltharyn :** Dyfel!

**FR :** Diable ! **EN:** What the devil!

Nom employé en exclamation

Force indicative : 2/4. Sources : L241, L242.

### S-curses

**Vaeltharyn :** Saelnyr!

**FR :** Malédiction ! **EN:** Curses!

Nom de malédiction fictive du lexique, pas mal réel revendiqué

Force indicative : 2/4. Sources : L244, L245.

### S-surprise

**Vaeltharyn :** Sketh, se vele thaevl ma?

**FR :** Ce n'est pas vrai ?! **EN:** Is that really true?!

Question de surprise, pas demande de silence

Force indicative : 1/4. Sources : L705, L698, L254, L256, L661, L662, L696, L710.

### S-strong_surprise

**Vaeltharyn :** Vrask, se vele thaevl ma?

**FR :** Putain, c'est vrai ?! **EN:** Holy shit, is that true?!

Surprise; la polarité interrogative est explicite

Force indicative : 4/4. Sources : L659, L255, L660.

### S-what

**Vaeltharyn :** Ven, vrask?!

**FR :** Quoi, putain ?! **EN:** What the fuck?!

Fragment interrogatif; pas une scène sexuelle

Force indicative : 4/4. Sources : L242, L656, L657, L683.

### S-hell_no

**Vaeltharyn :** Vrask, nau!

**FR :** Putain, non ! **EN:** Hell no!

Refus renforcé

Force indicative : 4/4. Sources : L685.

### S-hell_yes

**Vaeltharyn :** Vrask, ei!

**FR :** Putain, oui ! **EN:** Hell yeah!

Accord enthousiaste

Force indicative : 4/4. Sources : L686, L687.

### S-dismiss_mild

**Vaeltharyn :** Naethala!

**FR :** Dégage ! **EN:** Get lost!

Renvoi, pas obligation d'un itinéraire concret

Force indicative : 2/4. Sources : L271, L272, L289, L290, L291, L292, L728, L729, L730, L731.

### S-dismiss_strong

**Vaeltharyn :** Naethala, vrask!

**FR :** Va te faire foutre ! **EN:** Fuck off!

Équivalence pragmatique; ne reproduit pas sexe, famille ou origine

Force indicative : 4/4. Sources : L271, L272, L289, L290, L291, L292, L728, L729, L731, L243, L267, L268, L269, L270, L273, L274, L275, L276, L277, L278, L279, L280, L293, L295, L715, L716, L717, L718, L719, L720, L721, L722, L723, L727, L732, L733.

### S-dismiss_plural

**Vaeltharyn :** Tin naethalai, vrask!

**FR :** Allez vous faire foutre ! **EN:** Fuck off, all of you!

Impératif pluriel; pas un singulier de politesse non défini

Force indicative : 4/4. Sources : L277.

### S-shut_mild

**Vaeltharyn :** Nu lyra!

**FR :** Tais-toi ! **EN:** Shut up!

Négation de l'impératif parler

Force indicative : 2/4. Sources : L281, L283, L284, L285, L286, L738, L740, L743.

### S-shut_strong

**Vaeltharyn :** Nu lyra, vrask!

**FR :** Ferme ta gueule ! **EN:** Shut the fuck up!

Renforcement vulgaire, pas vérité anatomique

Force indicative : 4/4. Sources : L281, L282, L288, L739.

### S-mouth_shut

**Vaeltharyn :** Kaerala vaem si-en!

**FR :** Ferme ton clapet ! **EN:** Shut your trap!

Bouche réflexive du destinataire

Force indicative : 3/4. Sources : L740, L287, L741, L742.

### S-leave_alone

**Vaeltharyn :** Laera mi e saerunath!

**FR :** Fous-moi la paix ! **EN:** Leave me the hell alone!

Domaine figuré de la paix au locatif

Force indicative : 3/4. Sources : L296, L297, L736, L737.

### S-leave_alone_strong

**Vaeltharyn :** Laera mi e saerunath, vrask!

**FR :** Fous-moi la paix, putain ! **EN:** Leave me the fuck alone!

Renforcement explicite; distinct du degré plus faible antérieur

Force indicative : 4/4. Sources : L736, L294, L734.

### S-back_off

**Vaeltharyn :** Nu kaena mi, vrask!

**FR :** Ne me touche pas, putain ! **EN:** Back off, don't touch me!

Limite physique, pas ordre de reculer d'une distance donnée

Force indicative : 4/4. Sources : L735.

### S-stop_nuisance

**Vaeltharyn :** Nu horsahima mi!

**FR :** Arrête de me faire chier ! **EN:** Stop being a pain in the ass!

Importune, sans scatologie littérale

Force indicative : 3/4. Sources : L299, L300, L301, L748.

### S-annoyed

**Vaeltharyn :** Ti horsahimes mi, vrask!

**FR :** Tu me fais chier ! **EN:** You're pissing me off!

Irritation causée par l'autre

Force indicative : 4/4. Sources : L302, L303, L800, L803.

### S-annoyed_thing

**Vaeltharyn :** Se horsahime mi, vrask!

**FR :** Ça me fait chier ! **EN:** This pisses me off!

Objet non personnel conservé

Force indicative : 4/4. Sources : L260, L261, L356, L357, L358, L359.

### S-cut_bullshit

**Vaeltharyn :** Nu lyra grusk-thareli!

**FR :** Arrête tes conneries ! **EN:** Cut the bullshit!

Lecture de propos, pas erreur matérielle

Force indicative : 3/4. Sources : L298, L744, L745.

### S-stop_behaviour

**Vaeltharyn :** Nu skarna!

**FR :** Arrête de faire le connard ! **EN:** Stop being an asshole!

Conduite, non identité permanente

Force indicative : 3/4. Sources : L747.

### S-mock_question

**Vaeltharyn :** Ti thenthoses mi ma, vrask?

**FR :** Tu te fous de ma gueule ? **EN:** Are you fucking kidding me?

Verbe transitif explicitement créé pour conserver la cible

Force indicative : 4/4. Sources : L309, L752, L753, L808, L320.

### S-take_for_fool

**Vaeltharyn :** Ti hapeves dhe mi velem kofav ma, vrask?

**FR :** Tu me prends pour un con ? **EN:** Do you think I'm a fucking idiot?

Complétive complète avec première personne

Force indicative : 4/4. Sources : L310.

### S-who_are_you

**Vaeltharyn :** Ti loebemes dhe ti veles var, vrask?

**FR :** Tu te prends pour qui, putain ? **EN:** Who the fuck do you think you are?

Interrogatif porte sur l'identité prétendue

Force indicative : 4/4. Sources : L751.

### S-your_problem

**Vaeltharyn :** Ven vele en kaer ti-en, vrask?

**FR :** C'est quoi ton secret, putain ? **EN:** What's your secret, fuck?!

NE PAS utiliser pour « problème »; entrée conservée comme contrôle de faux ami

Force indicative : 4/4. Sources : .

### S-bullshit

**Vaeltharyn :** Grusk-thareli!

**FR :** Des conneries ! **EN:** Bullshit!

Propos rejetés, pas toute erreur

Force indicative : 3/4. Sources : L306, L308, L316, L325, L326, L760, L761, L762, L763, L767, L768.

### S-mistake

**Vaeltharyn :** Gydim basoel!

**FR :** Une erreur stupide ! **EN:** A stupid mistake!

Ratage ponctuel, distinct de propos mensongers

Force indicative : 2/4. Sources : L315, L786.

### S-mean_stunt

**Vaeltharyn :** Therval skentav!

**FR :** Une saloperie de manœuvre ! **EN:** A nasty stunt!

Travail/action moralement déloyale en contexte

Force indicative : 3/4. Sources : L317, L318, L319.

### S-bad_quality

**Vaeltharyn :** Se vele ulmaeriv, vrask!

**FR :** C'est vraiment de la merde ! **EN:** It's fucking awful!

Mauvaise qualité, pas nécessairement tromperie

Force indicative : 4/4. Sources : L261, L322, L323, L324, L778, L779.

### S-bogus

**Vaeltharyn :** Se vele ulthaevl.

**FR :** C'est faux. **EN:** It's bogus.

Fausseté, pas mauvais goût

Force indicative : 2/4. Sources : L325.

### S-mess

**Vaeltharyn :** Se vele dhidhys vrask.

**FR :** C'est un putain de bordel. **EN:** It's a fucking mess.

Désordre, pas établissement

Force indicative : 4/4. Sources : L327, L328, L329, L788.

### S-huge_mess

**Vaeltharyn :** Se vele dhidhysaun vrask.

**FR :** C'est un bordel monstre. **EN:** It's a complete fucking mess.

Augmentatif nominal régulier, non conjugaison

Force indicative : 4/4. Sources : L328, L329, L788, L330, L787, L789.

### S-failure

**Vaeltharyn :** Taempaer vrask!

**FR :** Un putain de fiasco ! **EN:** A fucking fiasco!

Échec complet; dumpster fire ne contient ici aucun conteneur en feu

Force indicative : 4/4. Sources : L329, L788, L330, L787, L789.

### S-crap_job

**Vaeltharyn :** Therval grusken!

**FR :** Un boulot de merde ! **EN:** A shitty job!

Génitif métaphorique, pas travail sur une matière fécale

Force indicative : 3/4. Sources : L332.

### S-crap_weather

**Vaeltharyn :** Saunrael grusken!

**FR :** Un temps de merde ! **EN:** Shitty weather!

Météo, pas durée

Force indicative : 3/4. Sources : L333.

### S-crap_day

**Vaeltharyn :** Saun grusken!

**FR :** Une journée de merde ! **EN:** A shitty day!

Qualité négative métaphorique, pas intensif neutre

Force indicative : 3/4. Sources : L334.

### S-crap_life

**Vaeltharyn :** Thaleth grusken!

**FR :** Vie de merde ! **EN:** Fuck my life!

Qualité de vie jugée mauvaise; pas souhait de mort

Force indicative : 3/4. Sources : L335, L773.

### S-intensifier_strong

**Vaeltharyn :** Ith skoendhoem vrask!

**FR :** Ce putain de truc ! **EN:** This fucking thing!

Gabarit nominal, remplacer le nom en conservant l'ordre

Force indicative : 4/4. Sources : L336, L337, L338, L344, L345.

### S-intensifier_mild

**Vaeltharyn :** Ith skoendhoem garuniv!

**FR :** Ce fichu truc ! **EN:** This damn thing!

Intensité, pas qualité négative automatique

Force indicative : 2/4. Sources : L701, L338, L339, L340.

### S-half_assed

**Vaeltharyn :** Therval hudhuthun ulmaeriv!

**FR :** Travail mal fait et négligé ! **EN:** Shoddy, half-assed work!

Participe passif de négliger, pas raccourci illégal du verbe

Force indicative : 2/4. Sources : L343, L347, L815.

### S-cheap

**Vaeltharyn :** Skoendhoem ulmaeriv garuniv!

**FR :** Un fichu truc de piètre qualité ! **EN:** A damn lousy thing!

Qualité médiocre; bas prix non garanti

Force indicative : 2/4. Sources : L342, L346.

### S-dont_care

**Vaeltharyn :** Mi nu slusoemem se.

**FR :** Je m'en fiche. **EN:** I don't care about it.

Verbe nouveau de préoccupation, pas « ne pas savoir »

Force indicative : 1/4. Sources : L348, L349.

### S-dont_care_strong

**Vaeltharyn :** Mi nu slusoemem se, vrask.

**FR :** J'en ai rien à foutre. **EN:** I don't give a fuck.

Même contenu, degré explicite plus fort

Force indicative : 4/4. Sources : L350, L351, L352, L795, L796, L797.

### S-fed_up

**Vaeltharyn :** Mi dhavem foegaek, vrask.

**FR :** J'en ai marre, putain. **EN:** I'm fucking fed up.

Exaspération, pas simple fatigue physique

Force indicative : 4/4. Sources : L353, L354, L355, L799.

### S-fed_up_this

**Vaeltharyn :** Mi dhavem foegaek fra se-ath, vrask.

**FR :** J'en ai marre de ça, putain. **EN:** I'm fucking sick of this.

Origine figurée au locatif, pas maladie

Force indicative : 4/4. Sources : L354, L770, L801.

### S-angry

**Vaeltharyn :** Mi velem vyrv.

**FR :** Je suis en rogne. **EN:** I'm pissed off.

Colère, distinct de l'ivresse

Force indicative : 2/4. Sources : L799, L798.

### S-drunk

**Vaeltharyn :** Mi velem brehum.

**FR :** Je suis ivre. **EN:** I'm drunk.

Pissed britannique possible, pas pissed américain colérique

Force indicative : 1/4. Sources : .

### S-bored

**Vaeltharyn :** Mi dhavem nyrmael, vrask.

**FR :** Je me fais chier. **EN:** I'm bored shitless.

Ennui, pas action de déféquer

Force indicative : 4/4. Sources : L363.

### S-hassled

**Vaeltharyn :** Mi velem brytoekun.

**FR :** Je me fais harceler. **EN:** I'm getting hassled.

Passif d'un verbe transitif, pas participe employé comme verbe personnel

Force indicative : 2/4. Sources : L364.

### S-manage

**Vaeltharyn :** Mi kelem thaelar se.

**FR :** Je peux y arriver. **EN:** I can manage it.

Périphrase d'accomplissement; autonomie complète non garantie

Force indicative : 1/4. Sources : L365.

### S-fuck_up

**Vaeltharyn :** Mi ragydimem, vrask.

**FR :** J'ai merdé. **EN:** I fucked up.

Échec d'action, pas rapport sexuel

Force indicative : 4/4. Sources : L366, L783.

### S-you_fuck_up

**Vaeltharyn :** Ti ragydimes, vrask.

**FR :** T'as merdé. **EN:** You fucked up.

Accord deuxième personne

Force indicative : 4/4. Sources : L784.

### S-stir_discord

**Vaeltharyn :** Ti thaeles nathem, vrask.

**FR :** Tu fous la merde. **EN:** You're stirring shit up.

Créer une querelle; pas toute erreur accidentelle

Force indicative : 4/4. Sources : L367.

### S-hard_work

**Vaeltharyn :** Mi thaelem velu tidom, vrask.

**FR :** Je me casse le cul. **EN:** I'm busting my ass.

Effort explicite, aucune blessure anatomique

Force indicative : 4/4. Sources : L802.

### S-know_nothing

**Vaeltharyn :** Ti sendes nul skoendhoem, vrask.

**FR :** Tu n'y connais que dalle. **EN:** You don't know shit.

Quantificateur nominal nul, pas double négation improvisée

Force indicative : 4/4. Sources : L794.

### S-no_value

**Vaeltharyn :** Se pykikove nul vaermar.

**FR :** Ça ne vaut pas un sou. **EN:** It's not worth a penny.

Valeur monétaire; autre valeur à contextualiser

Force indicative : 2/4. Sources : .

### S-huge_amount

**Vaeltharyn :** Setoesaun vrask!

**FR :** Une putain de quantité ! **EN:** A fuckton!

Augmentatif nominal, pas une unité de mesure

Force indicative : 4/4. Sources : L791, L792.

### S-nothing

**Vaeltharyn :** Nul skoendhoem, vrask.

**FR :** Rien, putain. **EN:** Jack shit.

Aucune chose avec juron explicite

Force indicative : 4/4. Sources : L817, L818.

### S-same_crap

**Vaeltharyn :** Grusk grygel; saun maenusoek.

**FR :** Même merde, autre jour. **EN:** Same shit, different day.

Accord invariable des adjectifs

Force indicative : 3/4. Sources : L774.

### S-shit_happens

**Vaeltharyn :** Gydimi vynen.

**FR :** Les ratages arrivent. **EN:** Shit happens.

Arrivée figurée d'événements

Force indicative : 2/4. Sources : L775.

### S-tough_luck

**Vaeltharyn :** Slaefiv ti-en.

**FR :** Pas de bol pour toi. **EN:** Tough luck.

Constate la malchance; sarcasme dépend du ton

Force indicative : 1/4. Sources : L777.

### S-not_my_problem

**Vaeltharyn :** Se vele skoendhoem ti-en; mi nu slusoemem se.

**FR :** C'est ton affaire; je m'en fiche. **EN:** That's your business; I don't care.

Deux propositions complètes, nuance moins empathique explicite

Force indicative : 2/4. Sources : L776.

### S-fuck_it

**Vaeltharyn :** Mi laerem se, vrask.

**FR :** Et puis merde, je laisse tomber. **EN:** Fuck it, I'm dropping it.

Abandon de la chose, pas renvoi d'une personne

Force indicative : 4/4. Sources : L771, L772.

### S-reject_this

**Vaeltharyn :** Mi nu vaelem se, vrask.

**FR :** Ah non, j'en veux pas, putain. **EN:** Fuck that.

Refus, pas indifférence automatique

Force indicative : 4/4. Sources : L769.

### S-sarcastic_truth

**Vaeltharyn :** Se vele thaevl, vrask!

**FR :** Sans déconner ! **EN:** No shit!

Affirmation sarcastique ou surprise: le ton doit trancher

Force indicative : 3/4. Sources : L764.

### S-swear_true

**Vaeltharyn :** Mi graethem dhe se vele thaevl.

**FR :** Je te jure que c'est vrai. **EN:** I swear it's true.

Serment affirmatif, non sarcasme

Force indicative : 2/4. Sources : L809.

### S-scared

**Vaeltharyn :** Se radityle mi, vrask.

**FR :** Ça m'a foutu une de ces trouilles. **EN:** That scared the shit out of me.

Verbe causal de peur, pas perte corporelle

Force indicative : 4/4. Sources : L810.

### S-mind_blown

**Vaeltharyn :** Se vele vrelloen, vrask!

**FR :** Ça me stupéfie, putain ! **EN:** That blows my fucking mind!

Littéralement c'est merveilleux; lecture admirative seulement

Force indicative : 4/4. Sources : .

### S-excellent

**Vaeltharyn :** Se vele mynoes, vrask!

**FR :** Ça déchire, putain ! **EN:** It's fucking excellent!

Qualité positive; pas être sexuellement dépravé

Force indicative : 4/4. Sources : L814.

### S-badass

**Vaeltharyn :** Thalen vaethv an vyral!

**FR :** Personne courageuse et puissante ! **EN:** A brave, formidable person!

Lecture admirative; le sens menaçant reste distinct

Force indicative : 2/4. Sources : L812.

### S-threatening

**Vaeltharyn :** Thalen slibelaev!

**FR :** Personne redoutable ! **EN:** An intimidating person!

Crainte inspirée, pas admiration obligatoire

Force indicative : 2/4. Sources : .

### S-smartass

**Vaeltharyn :** Kraeboer bremvyv!

**FR :** Insolent pédant ! **EN:** Pedantic wiseass!

Habileté réelle non garantie

Force indicative : 2/4. Sources : L560, L561, L813.

### S-foul_mouthed

**Vaeltharyn :** Thalen ya ara lyre grusk-thareli!

**FR :** Personne qui débite des conneries ! **EN:** Someone who habitually talks bullshit!

Pas forcément toute personne qui jure

Force indicative : 3/4. Sources : .

### S-wrong_way

**Vaeltharyn :** Se vele ulthaeviv, vrask.

**FR :** C'est fait de travers, putain. **EN:** It's fucking wrong.

Non-conformité, pas orientation spatiale précise

Force indicative : 4/4. Sources : L816.

### S-fake

**Vaeltharyn :** Thalen noekath!

**FR :** Imposteur ! **EN:** Phony!

Adjectif d'imposture, pas doctrine religieuse déduite

Force indicative : 2/4. Sources : L121, L536.

### S-imitator

**Vaeltharyn :** Thalen nygaek an slyllum!

**FR :** Poseur qui n'y arrive pas ! **EN:** Inept poser!

Ne couvre pas tout désir d'apprendre

Force indicative : 2/4. Sources : L565, L566.

### S-conformist_woman

**Vaeltharyn :** Sorkev noefor!

**FR :** Femme jugée conformiste ! **EN:** Woman called conformist!

Stéréotype basic bitch seulement partiellement transposé

Force indicative : 2/4. Sources : L620.

### S-empowered_woman

**Vaeltharyn :** Sorkev raev an garim!

**FR :** Femme libre et autonome ! **EN:** A free, self-directed woman!

Lecture valorisante de bad bitch, sans insulte native

Force indicative : 1/4. Sources : L621.

### S-leader_woman

**Vaeltharyn :** Sorkev ya dhave hynloel!

**FR :** Femme qui a du pouvoir ! **EN:** A woman with power!

Lecture valorisante de boss bitch; pas domination abusive déduite

Force indicative : 1/4. Sources : L622.

### S-attention_seeker

**Vaeltharyn :** Thalen ya vaele haelthim!

**FR :** Personne qui recherche l'attention ! **EN:** Attention-seeker!

Aucune prostitution ni genre déduit

Force indicative : 2/4. Sources : L554.

### S-dramatic

**Vaeltharyn :** Thalen ya thaele lapael!

**FR :** Personne qui en fait des tonnes ! **EN:** Someone who exaggerates everything!

Exagération, pas genre théâtral ni genre féminin

Force indicative : 2/4. Sources : L553.

### S-entitled

**Vaeltharyn :** Maelin ya vaele sava skoendhoemi!

**FR :** Gosse qui veut tout ! **EN:** A brat who wants everything!

Lecture d'exigence; le sentiment de droit est une approximation

Force indicative : 2/4. Sources : L568.

### S-bossy_complainer

**Vaeltharyn :** Thalen dhimor an doedas!

**FR :** Personne arrogante et râleuse ! **EN:** An arrogant complainer!

Karen descriptif seulement; nom propre et stéréotype non lexicalisés

Force indicative : 2/4. Sources : L569.

### S-lazy_parent

**Vaeltharyn :** Thalir ya hudhuthe maelin si-en!

**FR :** Parent qui néglige son enfant ! **EN:** A parent who neglects their child!

Le parent masculin peut être précisé par darun; responsabilité financière à contextualiser

Force indicative : 2/4. Sources : L587.

### S-submissive

**Vaeltharyn :** Thalen nypuhyl!

**FR :** Personne qui se laisse diriger ! **EN:** An easily led person!

Docilité, pas stupidité ni identité sexuelle

Force indicative : 1/4. Sources : L607, L608, L610, L609.

### S-sycophant_coward

**Vaeltharyn :** Toenvapam sen vaethun!

**FR :** Lèche-bottes sans courage ! **EN:** A cowardly bootlicker!

Deux reproches, pas un trait racial

Force indicative : 2/4. Sources : L611.

### S-childish_man

**Vaeltharyn :** Bidim basoel!

**FR :** Homme jugé sot ! **EN:** Man called foolish!

Approximation pour immaturité; ne prétend pas encoder l'âge mental

Force indicative : 2/4. Sources : L641.

### S-attracted_to_money

**Vaeltharyn :** Thalen ya vaele vaermar e lyrenath!

**FR :** Personne qui recherche l'argent dans une relation ! **EN:** Person seeking money in a relationship!

Gold digger contextuel; pas toute dépendance financière

Force indicative : 2/4. Sources : L631.

### S-sexual_harasser

**Vaeltharyn :** Thalen ya thaele brytoeketh braeltyner!

**FR :** Personne qui commet du harcèlement sexuel ! **EN:** A person engaging in sexual harassment!

Conduite spécifique; non synonyme de toute lubricité

Force indicative : 3/4. Sources : L521.

### S-involuntary_celibate

**Vaeltharyn :** Thalen sen maelnayrun!

**FR :** Personne sans partenaire ! **EN:** Person without a partner!

Lecture partielle: involontaire et idéologie incel non déduites

Force indicative : 0/4. Sources : L647.

### S-spiteful_misogynist

**Vaeltharyn :** Thalen ya ulmaerune sorkevi!

**FR :** Personne qui méprise les femmes ! **EN:** Someone who despises women!

Lecture injurieuse contextuelle d'incel; pas tous les célibataires

Force indicative : 3/4. Sources : L647.

### S-idiot_mildintense

**Vaeltharyn :** Kofav garuniv!

**FR :** Fichu imbécile ! **EN:** Bloody idiot!

Renforcement modéré, pas force de fucking idiot

Force indicative : 2/4. Sources : L25.

### S-adj_intensifier

**Vaeltharyn :** Se vele sha maeriv, sketh!

**FR :** C'est fichtrement bon ! **EN:** It's damn good!

Sha modifie l'adjectif, pas un nom ni un verbe

Force indicative : 2/4. Sources : L240.

### S-bad_situation

**Vaeltharyn :** Vareth-greth grusken!

**FR :** Une difficulté de merde ! **EN:** A shitty predicament!

Difficulté pratique, pas exercice scientifique

Force indicative : 3/4. Sources : L331.

### S-stupid_modifier

**Vaeltharyn :** Skoendhoem basoel!

**FR :** Un truc à la con ! **EN:** A dumb thing!

Jugement figuré, pas suffixe péjoratif universel

Force indicative : 2/4. Sources : L341.

### S-disgust

**Vaeltharyn :** Se vele dhaethoth, vrask!

**FR :** Ça me dégoûte, putain ! **EN:** It's fucking disgusting!

Lecture figurée; ne décrit pas nécessairement vomissement

Force indicative : 4/4. Sources : L360, L780.

### S-sympathy

**Vaeltharyn :** Mi dhavem maelnaev ti-or.

**FR :** J'éprouve de la compassion pour toi. **EN:** I feel for you.

Peuchère dans sa lecture compatissante, pas une insulte

Force indicative : 0/4. Sources : L372.

### S-unverified_regional

**Vaeltharyn :** Équivalent non établi.

**FR :** Forme régionale à confirmer **EN:** Regional form needing confirmation

Aucune forme vaeltharyn inventée sur une attestation insuffisante

Force indicative : 0/4. Sources : L376, L377.

### S-documented_social

**Vaeltharyn :** Équivalent non établi.

**FR :** Injure sociale ou racialisée documentée **EN:** Documented class-based or racialised insult

Référence source conservée; aucun groupe social vaeltharyn équivalent présumé

Force indicative : 4/4. Sources : L513, L514.

### S-weird_warning

**Vaeltharyn :** Thalen moelom!

**FR :** Personne jugée extravagante ! **EN:** Someone called eccentric!

Équivalent pragmatique partiel: ne transpose pas un diagnostic ni un spectacle de foire

Force indicative : 2/4. Sources : L374, L524, L525, L526, L527.

### S-snob

**Vaeltharyn :** Keltas!

**FR :** Snob ! **EN:** Snob!

Prétention à la haute société dans le sens existant

Force indicative : 2/4. Sources : L567.

### S-stop_whining

**Vaeltharyn :** Nu gimtaela!

**FR :** Arrête de pleurnicher ! **EN:** Quit whining!

Impératif négatif d'un verbe intransitif

Force indicative : 2/4. Sources : L746.

### S-dont_bullshit_me

**Vaeltharyn :** Nu vaera grusk-thareli mi-or!

**FR :** Ne me raconte pas de conneries ! **EN:** Don't bullshit me!

Donner des propos au datif destinataire

Force indicative : 3/4. Sources : L749, L750.

### S-screwed_you

**Vaeltharyn :** Ti dhaves vareth-greth thar, vrask.

**FR :** T'es dans une grosse merde. **EN:** You're in deep shit.

Difficulté majeure, pas rapport sexuel ni désespoir irréversible

Force indicative : 4/4. Sources : L781.

### S-screwed_us

**Vaeltharyn :** Min dhavom vareth-greth thar, vrask.

**FR :** On est dans une grosse merde. **EN:** We're in deep shit.

Première personne plurielle conservée

Force indicative : 4/4. Sources : L782.

### S-he_bullshit

**Vaeltharyn :** Se lyre grusk-thareli.

**FR :** Il raconte des conneries. **EN:** He's talking bullshit.

Se ne fixe pas le genre; le contexte anglais fourni le fixe

Force indicative : 3/4. Sources : L804.

### S-he_ignorant_talk

**Vaeltharyn :** Se lyre; se nu sende.

**FR :** Il parle sans savoir. **EN:** He's talking out of his ass.

Équivalence pragmatique, aucune anatomie supposée

Force indicative : 3/4. Sources : L805.

### S-he_ass

**Vaeltharyn :** Se vele skarn.

**FR :** C'est un connard. **EN:** He's an asshole.

Sujet source préservé, pas passage à tu

Force indicative : 3/4. Sources : L806.

### S-he_behaving

**Vaeltharyn :** Se skarne.

**FR :** Il se comporte en connard. **EN:** He's being an asshole.

Comportement plutôt qu'identité

Force indicative : 3/4. Sources : L807.

### S-windbag

**Vaeltharyn :** Hifun bremvyv!

**FR :** Bavard pédant ! **EN:** Pompous windbag!

Bavardage et pédanterie, pas seulement volume sonore

Force indicative : 2/4. Sources : L557, L558.

### S-bigmouth_secret

**Vaeltharyn :** Thalen ya nu kaere kaer!

**FR :** Personne incapable de garder un secret ! **EN:** Someone who cannot keep a secret!

Lecture particulière de bigmouth

Force indicative : 2/4. Sources : L556.

### S-family_fragment

**Vaeltharyn :** Melun ti-en!

**FR :** Ta mère ! **EN:** Your mother!

Fragment familial; intention injurieuse dépend du contexte, aucun fait affirmé

Force indicative : 3/4. Sources : L104.

### S-literal_shit_on

**Vaeltharyn :** Mi gruskem nar ti-ath.

**FR :** Je te chie dessus. **EN:** I shit on you.

Lecture littérale disponible; en situation le renvoi pragmatique reste distinct

Force indicative : 4/4. Sources : L278.

### S-eat_shit_die

**Vaeltharyn :** Maelvela grusk an nytha!

**FR :** Mange de la merde et crève ! **EN:** Eat shit and die!

Formule hostile citée lexicalement, pas une consigne au lecteur

Force indicative : 4/4. Sources : L724.

### S-suck_dick

**Vaeltharyn :** Sloelika fonul mi-en!

**FR :** Suce mon pénis ! **EN:** Suck my dick!

Formulation anatomique littérale; provocation et acte réel ne sont pas confondus

Force indicative : 4/4. Sources : L725.

### S-suck_balls

**Vaeltharyn :** Sloelika daeboroeki mi-en!

**FR :** Suce mes testicules ! **EN:** Suck my balls!

Pluriel explicite, lecture littérale

Force indicative : 4/4. Sources : L726.

### S-shove_ass

**Vaeltharyn :** Ti keles mesithar se e foenroeminath si-en!

**FR :** Tu peux te le mettre dans l'anus ! **EN:** You can shove it up your ass!

Orifice anatomique, pas simple fesse; usage injurieux contextuel

Force indicative : 4/4. Sources : L304.

### S-up_yours

**Vaeltharyn :** E foenroeminath ti-en!

**FR :** Dans ton cul ! **EN:** Up your ass!

Fragment locatif injurieux, pas une phrase verbale ni une suggestion pratique

Force indicative : 4/4. Sources : L720, L305, L307.

### S-sarcastic_known

**Vaeltharyn :** Mi sendem se, Sherlock.

**FR :** Je le sais, Sherlock. **EN:** No shit, Sherlock.

Sherlock reste un nom propre reconnaissable, sarcasme dépend du ton

Force indicative : 3/4. Sources : L765.

### S-your_issue

**Vaeltharyn :** Ven vele vareth-greth ti-en, vrask?

**FR :** C'est quoi ton putain de problème ? **EN:** What's your fucking problem?

Difficulté pratique ou relationnelle; pas un exercice scientifique

Force indicative : 4/4. Sources : L754.

### S-mess_and_find

**Vaeltharyn :** Ir ti horsahimes mi, ti vimires.

**FR :** Si tu me cherches, tu verras. **EN:** Mess with me and you'll find out.

Menace elliptique conservée sans inventer de violence précise

Force indicative : 3/4. Sources : L755.

### S-profound_surprise

**Vaeltharyn :** Se rathaele naivkaethaun e mi-ath, vrask!

**FR :** Ça m'a complètement stupéfié, putain ! **EN:** That blew my fucking mind!

Grande surprise créée en moi; valence émotionnelle non imposée

Force indicative : 4/4. Sources : L361, L811.

### S-sexual_sucker

**Vaeltharyn :** Fonul-brabon!

**FR :** Suceur de pénis ! **EN:** Cocksucker!

Composé descriptif cité comme injure sexuelle; aucune orientation déduite

Force indicative : 4/4. Sources : L637, L636.

### S-sexual_object

**Vaeltharyn :** Traemtoer-dhokun!

**FR :** Sac à sperme ! **EN:** Cum dumpster!

Métaphore dégradante objectivante, explicitement citée comme telle

Force indicative : 4/4. Sources : L97, L638.

### S-sex_manipulator

**Vaeltharyn :** Bidim ya krekoke thaleni vo vroefinar!

**FR :** Homme qui trompe des personnes pour coucher ! **EN:** Man who deceives people to get sex!

Manipulation sexuelle intentionnelle, pas simple désir

Force indicative : 3/4. Sources : L639.

### S-unfaithful_partner

**Vaeltharyn :** Thalen ya boebave maelnayrun si-en!

**FR :** Personne qui trahit son partenaire ! **EN:** Person who betrays their partner!

Trahison relationnelle; le nombre de partenaires ne suffit pas

Force indicative : 2/4. Sources : .

### S-old_creep

**Vaeltharyn :** Bidim mamysem graefyhael!

**FR :** Vieux homme lubrique ! **EN:** Dirty old man!

Âge et homme conservés, aucune déficience médicale déduite

Force indicative : 3/4. Sources : L645.

### S-unusual

**Vaeltharyn :** Thalen moelom!

**FR :** Personne extravagante ! **EN:** Eccentric person!

Équivalent partiel de weirdo; pas diagnostic psychiatrique

Force indicative : 1/4. Sources : L374, L525, L526.

### S-hard_to_intimidate

**Vaeltharyn :** Thalen vaethv!

**FR :** Personne courageuse ! **EN:** Brave person!

Ne confond pas bravoure, force physique et soumission

Force indicative : 1/4. Sources : .

### S-misery

**Vaeltharyn :** Mi dhavem lonbem, vrask.

**FR :** J'ai la poisse, putain. **EN:** Fuck, my luck is awful.

Malchance, pas souhait de mort

Force indicative : 4/4. Sources : .

### S-appreciation

**Vaeltharyn :** Se vele mynoes, vrask!

**FR :** Putain, c'est excellent ! **EN:** Holy shit, that's good!

Appréciation positive

Force indicative : 4/4. Sources : L766.

### S-not_worth

**Vaeltharyn :** Se pykikove nul vaermar, vrask.

**FR :** Ça ne vaut pas un sou, putain. **EN:** It's not worth shit.

Valeur monétaire dans le littéral, dépréciation contextuelle

Force indicative : 4/4. Sources : L793.

### S-he_mocks

**Vaeltharyn :** Se thenthose mi.

**FR :** Il se moque de moi. **EN:** He is making fun of me.

Troisième personne et cible moi conservées

Force indicative : 2/4. Sources : L362.

### S-causes_fear

**Vaeltharyn :** Se dityle mi, vrask.

**FR :** Ça me fout la trouille. **EN:** It scares the hell out of me.

Lecture peur, distincte de colère

Force indicative : 4/4. Sources : L359.

### S-controversy

**Vaeltharyn :** Nathemaun vrask!

**FR :** Une putain de querelle énorme ! **EN:** A fucking storm of controversy!

Grande querelle, pas météo littérale ni tout fiasco

Force indicative : 4/4. Sources : L790.

## Inventaire complet de la pièce jointe

Chaque ligne originale renvoie à ses fiches ; les variantes fournies ne deviennent pas des racines distinctes.

### Entrées source FR

| Ligne | Texte original | Correspondance fournie | Sens proposés | Traitement |
|---|---|---|---|---|
| [6](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L6) | Idiot / idiote | Idiot | [idiot](#s-idiot) | renvois contextualisés |
| [7](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L7) | Imbécile | Idiot, fool | [idiot](#s-idiot) | renvois contextualisés |
| [8](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L8) | Abruti / abrutie | Moron, idiot | [idiot](#s-idiot) | renvois contextualisés |
| [9](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L9) | Crétin / crétine | Moron, idiot | [idiot](#s-idiot) | renvois contextualisés |
| [10](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L10) | Débile | Idiot, moron | [idiot](#s-idiot) | renvois contextualisés |
| [11](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L11) | Andouille | Idiot, goof | [silly](#s-silly) | renvois contextualisés |
| [12](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L12) | Andouillette | Silly fool | [silly](#s-silly) | renvois contextualisés |
| [13](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L13) | Nouille | Silly fool, dummy | [silly](#s-silly) | renvois contextualisés |
| [14](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L14) | Patate | Dummy, idiot | [silly](#s-silly) | renvois contextualisés |
| [15](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L15) | Cornichon | Fool, dummy | [fool](#s-fool), [silly](#s-silly) | sens alternatifs à désambiguïser |
| [16](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L16) | Bêta | Silly, dummy | [fool](#s-fool), [silly](#s-silly) | sens alternatifs à désambiguïser |
| [17](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L17) | Nigaud / nigaude | Fool, simpleton | [fool](#s-fool) | renvois contextualisés |
| [18](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L18) | Niais / niaise | Simpleton, fool | [fool](#s-fool) | renvois contextualisés |
| [19](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L19) | Benêt | Simpleton, dimwit | [fool](#s-fool) | renvois contextualisés |
| [20](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L20) | Simplet / simplette | Simpleton, dimwit | [fool](#s-fool) | renvois contextualisés |
| [21](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L21) | Sot / sotte | Fool | [fool](#s-fool) | renvois contextualisés |
| [22](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L22) | Triple buse | Complete idiot | [fool](#s-fool) | renvois contextualisés |
| [23](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L23) | Buse | Idiot, dunce | [fool](#s-fool) | renvois contextualisés |
| [24](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L24) | Baderne | Old fool, old windbag | [old_fool](#s-old_fool) | renvois contextualisés |
| [25](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L25) | Bougre d’idiot | You bloody idiot | [idiot_mildintense](#s-idiot_mildintense) | renvois contextualisés |
| [26](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L26) | Tête de linotte | Scatterbrain | [scatterbrain](#s-scatterbrain) | renvois contextualisés |
| [27](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L27) | Tête en l’air | Scatterbrain — souvent affectueux | [scatterbrain](#s-scatterbrain) | renvois contextualisés |
| [28](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L28) | Boulet | Dead weight, liability | [burden](#s-burden) | renvois contextualisés |
| [29](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L29) | Blaireau | Loser, idiot | [loser](#s-loser) | renvois contextualisés |
| [30](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L30) | Baltringue | Loser, clown, coward — selon le contexte | [loser](#s-loser), [clown](#s-clown), [coward](#s-coward) | sens alternatifs à désambiguïser |
| [31](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L31) | Charlot | Clown, incompetent fool | [clown](#s-clown) | renvois contextualisés |
| [32](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L32) | Guignol | Clown, joker | [clown](#s-clown) | renvois contextualisés |
| [33](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L33) | Pantin | Puppet | [puppet](#s-puppet) | renvois contextualisés |
| [34](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L34) | Clown | Clown | [clown](#s-clown) | renvois contextualisés |
| [35](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L35) | Rigolo | Joker, clown — dans un emploi méprisant | [clown](#s-clown) | renvois contextualisés |
| [36](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L36) | Bon à rien | Good-for-nothing | [useless](#s-useless) | renvois contextualisés |
| [37](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L37) | Incapable | Incompetent fool | [inept](#s-inept) | renvois contextualisés |
| [38](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L38) | Minable | Loser, pathetic little man/woman | [loser](#s-loser) | renvois contextualisés |
| [39](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L39) | Nullard / nullarde | Loser, dunce | [fool](#s-fool), [loser](#s-loser) | sens alternatifs à désambiguïser |
| [40](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L40) | Raté / ratée | Loser, failure | [loser](#s-loser) | renvois contextualisés |
| [41](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L41) | Pauvre type / pauvre fille | Pathetic loser | [loser](#s-loser) | renvois contextualisés |
| [42](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L42) | Pauvre tâche / tache | Useless idiot, loser | [useless](#s-useless) | renvois contextualisés |
| [43](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L43) | Bouffon / bouffonne | Clown, fool, loser | [clown](#s-clown) | renvois contextualisés |
| [44](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L44) | Toccard / tocard | Loser, useless idiot | [loser](#s-loser) | renvois contextualisés |
| [45](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L45) | Plouc | Hick, country bumpkin | [country_sneer](#s-country_sneer) | renvois contextualisés |
| [46](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L46) | Péquenaud / péquenot | Hick, country bumpkin | [country_sneer](#s-country_sneer) | renvois contextualisés |
| [47](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L47) | Pignouf | Lout, rude idiot | [lout](#s-lout) | renvois contextualisés |
| [48](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L48) | Malotru | Lout, boor | [lout](#s-lout) | renvois contextualisés |
| [49](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L49) | Goujat | Jerk, cad | [cad](#s-cad) | renvois contextualisés |
| [50](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L50) | Rustre | Boor, lout | [boor](#s-boor) | renvois contextualisés |
| [51](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L51) | Mufle | Boor, insensitive jerk | [cad](#s-cad) | renvois contextualisés |
| [52](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L52) | Grossier personnage | Rude jerk, boor | [lout](#s-lout) | renvois contextualisés |
| [57](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L57) | Con / conne | Idiot, asshole ; UK : prat, twat | [vile](#s-vile), [fregos](#s-fregos) | sens alternatifs à désambiguïser |
| [58](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L58) | Gros con / grosse conne | Fucking idiot, total asshole | [idiot_strong](#s-idiot_strong), [vile_strong](#s-vile_strong) | sens alternatifs à désambiguïser |
| [59](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L59) | Petit con / petite conne | Little shit, little prick | [small_vile](#s-small_vile) | renvois contextualisés |
| [60](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L60) | Sale con / sale conne | Fucking asshole | [vile_strong](#s-vile_strong) | renvois contextualisés |
| [61](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L61) | Vieux con / vieille conne | Old fart, old asshole | [old_vile](#s-old_vile) | renvois contextualisés |
| [62](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L62) | Connard / connasse | Asshole, prick ; UK : wanker | [vile](#s-vile), [fregos](#s-fregos) | sens alternatifs à désambiguïser |
| [63](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L63) | Conard | Variante orthographique de connard | [vile](#s-vile), [fregos](#s-fregos) | sens alternatifs à désambiguïser |
| [64](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L64) | Ducon | Dumbass, asshole | [fool](#s-fool), [vile](#s-vile), [fregos](#s-fregos) | sens alternatifs à désambiguïser |
| [65](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L65) | Conneau | Idiot, dumbass | [fool](#s-fool), [vile](#s-vile), [fregos](#s-fregos) | sens alternatifs à désambiguïser |
| [66](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L66) | Trou du cul | Asshole | [vile](#s-vile) | renvois contextualisés |
| [67](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L67) | Trouduc | Asshole | [vile](#s-vile) | renvois contextualisés |
| [68](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L68) | Enfoiré / enfoirée | Bastard, asshole | [vile](#s-vile) | renvois contextualisés |
| [69](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L69) | Salaud / salope | Bastard / bitch — selon l’emploi | [vile](#s-vile), [bitch](#s-bitch) | sens alternatifs à désambiguïser |
| [70](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L70) | Salopard | Bastard, scumbag | [vile](#s-vile) | renvois contextualisés |
| [71](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L71) | Ordure | Scumbag, piece of shit | [vile](#s-vile) | renvois contextualisés |
| [72](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L72) | Pourriture | Scumbag, rotten bastard | [vile](#s-vile) | renvois contextualisés |
| [73](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L73) | Fumier | Bastard, scumbag | [vile](#s-vile) | renvois contextualisés |
| [74](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L74) | Racaille | Scum, lowlife | [vile](#s-vile) | renvois contextualisés |
| [75](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L75) | Charogne | Vile bastard, scumbag | [vile](#s-vile) | renvois contextualisés |
| [76](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L76) | Sac à merde | Piece of shit | [vile](#s-vile) | renvois contextualisés |
| [77](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L77) | Merdeux / merdeuse | Little shit, brat | [small_vile](#s-small_vile) | renvois contextualisés |
| [78](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L78) | Petite merde | Little shit | [small_vile](#s-small_vile) | renvois contextualisés |
| [79](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L79) | Sous-merde | Worthless piece of shit | [worthless_vile](#s-worthless_vile) | renvois contextualisés |
| [80](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L80) | Étron | Turd, piece of shit | [vile](#s-vile) | renvois contextualisés |
| [81](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L81) | Chiure | Little piece of shit | [vile](#s-vile) | renvois contextualisés |
| [82](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L82) | Tête de con | Dickhead, dumbass | [vile](#s-vile), [fregos](#s-fregos) | sens alternatifs à désambiguïser |
| [83](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L83) | Tête de nœud | Dickhead | [vile](#s-vile), [fregos](#s-fregos) | sens alternatifs à désambiguïser |
| [84](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L84) | Tête de bite | Dickhead | [vile](#s-vile), [fregos](#s-fregos) | sens alternatifs à désambiguïser |
| [85](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L85) | Tête de gland | Dickhead, knobhead | [vile](#s-vile), [fregos](#s-fregos) | sens alternatifs à désambiguïser |
| [86](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L86) | Gland | Dickhead, idiot | [vile](#s-vile), [fregos](#s-fregos) | sens alternatifs à désambiguïser |
| [87](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L87) | Branleur / branleuse | Wanker ; slacker si l’on vise la paresse | [vile](#s-vile), [lazy](#s-lazy) | sens alternatifs à désambiguïser |
| [88](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L88) | Glandeur / glandeuse | Slacker, lazy bastard | [lazy](#s-lazy) | renvois contextualisés |
| [89](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L89) | Fainéant / feignasse | Lazy bum, lazy bastard | [lazy_strong](#s-lazy_strong) | renvois contextualisés |
| [90](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L90) | Jean-foutre | Good-for-nothing, worthless bastard | [useless](#s-useless) | renvois contextualisés |
| [91](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L91) | Foutriquet | Pipsqueak, little nobody | [small_vile](#s-small_vile) | renvois contextualisés |
| [92](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L92) | Raclure | Scumbag | [vile](#s-vile) | renvois contextualisés |
| [93](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L93) | Raclure de bidet | Scumbag, piece of filth | [vile](#s-vile) | renvois contextualisés |
| [94](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L94) | Résidu de fausse couche | Worthless piece of shit — pas d’équivalent idiomatique exact | [worthless_vile](#s-worthless_vile) | renvois contextualisés |
| [95](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L95) | Déchet | Human garbage, waste of space | [vile](#s-vile), [worthless_vile](#s-worthless_vile) | sens alternatifs à désambiguïser |
| [96](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L96) | Déchet humain | Human garbage, waste of skin | [vile](#s-vile), [worthless_vile](#s-worthless_vile) | sens alternatifs à désambiguïser |
| [97](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L97) | Sac à foutre | Cum dumpster — très dégradant, sens parfois différent | [sexual_object](#s-sexual_object) | renvois contextualisés |
| [98](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L98) | Enculé / enculée | Fucking asshole, motherfucker — traduction pragmatique | [vile_strong](#s-vile_strong), [fregos](#s-fregos) | sens alternatifs à désambiguïser |
| [99](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L99) | Enculeur de mouches | Nitpicking asshole, pedantic bastard | [vile](#s-vile), [pedant](#s-pedant) | sens alternatifs à désambiguïser |
| [100](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L100) | Fils de pute | Son of a bitch | [vile](#s-vile), [vile_strong](#s-vile_strong) | sens alternatifs à désambiguïser |
| [101](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L101) | Fils de chienne | Son of a bitch | [vile](#s-vile), [vile_strong](#s-vile_strong) | sens alternatifs à désambiguïser |
| [102](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L102) | Bâtard / bâtarde | Bastard | [vile](#s-vile), [vile_strong](#s-vile_strong) | sens alternatifs à désambiguïser |
| [103](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L103) | Nique ta mère | Fuck your mother — littéral ; souvent fuck you en situation | [vile_strong](#s-vile_strong) | renvois contextualisés |
| [104](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L104) | Ta mère ! | Your mom! — fonction et intensité variables | [family_fragment](#s-family_fragment) | renvois contextualisés |
| [110](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L110) | Emmerdeur / emmerdeuse | Pain in the ass, annoying bastard | [nuisance](#s-nuisance) | renvois contextualisés |
| [111](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L111) | Casse-couilles | Pain in the ass ; UK : pain in the arse | [nuisance](#s-nuisance) | renvois contextualisés |
| [112](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L112) | Casse-burnes | Pain in the ass | [nuisance](#s-nuisance) | renvois contextualisés |
| [113](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L113) | Casse-pieds | Pain in the neck | [nuisance_mild](#s-nuisance_mild) | renvois contextualisés |
| [114](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L114) | Chieur / chieuse | Pain in the ass, annoying little shit | [nuisance](#s-nuisance) | renvois contextualisés |
| [115](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L115) | Fouteur / fouteuse de merde | Shit-stirrer, troublemaker | [troublemaker](#s-troublemaker) | renvois contextualisés |
| [116](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L116) | Fouille-merde | Muckraker, nosy bastard | [nosy](#s-nosy) | renvois contextualisés |
| [117](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L117) | Fouille-au-merde | Nosy bastard, muckraker | [nosy](#s-nosy) | renvois contextualisés |
| [118](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L118) | Lèche-cul | Ass-kisser ; UK : arse-licker | [bootlicker](#s-bootlicker) | renvois contextualisés |
| [119](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L119) | Lèche-bottes | Bootlicker, suck-up | [bootlicker](#s-bootlicker) | renvois contextualisés |
| [120](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L120) | Faux-cul | Two-faced bastard, hypocrite | [hypocrite](#s-hypocrite) | renvois contextualisés |
| [121](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L121) | Faux jeton | Phony, two-faced bastard | [hypocrite](#s-hypocrite), [fake](#s-fake) | sens alternatifs à désambiguïser |
| [122](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L122) | Hypocrite | Hypocrite | [hypocrite](#s-hypocrite) | renvois contextualisés |
| [123](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L123) | Menteur / menteuse | Liar | [liar](#s-liar) | renvois contextualisés |
| [124](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L124) | Mythomane / mytho | Compulsive liar ; liar dans l’usage courant | [liar](#s-liar), [liar_habit](#s-liar_habit) | sens alternatifs à désambiguïser |
| [125](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L125) | Baratineur / baratineuse | Bullshitter, smooth talker | [bullshitter](#s-bullshitter) | renvois contextualisés |
| [126](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L126) | Beau parleur | All talk, smooth talker | [bullshitter](#s-bullshitter) | renvois contextualisés |
| [127](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L127) | Grande gueule | Loudmouth, bigmouth | [loudmouth](#s-loudmouth) | renvois contextualisés |
| [128](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L128) | Gueulard / gueularde | Loudmouth | [loudmouth](#s-loudmouth) | renvois contextualisés |
| [129](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L129) | Braillard / braillarde | Loudmouth, loud obnoxious person | [loudmouth](#s-loudmouth) | renvois contextualisés |
| [130](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L130) | Frimeur / frimeuse | Show-off, poser | [showoff](#s-showoff) | renvois contextualisés |
| [131](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L131) | Poseur / poseuse | Poser | [poser](#s-poser) | renvois contextualisés |
| [132](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L132) | M’as-tu-vu | Show-off | [showoff](#s-showoff) | renvois contextualisés |
| [133](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L133) | Prétentieux / prétentieuse | Pompous ass, arrogant jerk | [arrogant](#s-arrogant) | renvois contextualisés |
| [134](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L134) | Pète-sec | Bossy jerk | [bossy](#s-bossy) | renvois contextualisés |
| [135](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L135) | Pète-couilles | Pain in the ass | [nuisance](#s-nuisance) | renvois contextualisés |
| [136](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L136) | Pisse-froid | Joyless bore, sourpuss | [grouch](#s-grouch) | renvois contextualisés |
| [137](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L137) | Pisse-vinaigre | Sourpuss, miserable old grouch | [grouch](#s-grouch) | renvois contextualisés |
| [138](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L138) | Rabat-joie | Killjoy, spoilsport | [killjoy](#s-killjoy) | renvois contextualisés |
| [139](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L139) | Coincé / coincée | Uptight person, prude | [prude](#s-prude) | renvois contextualisés |
| [140](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L140) | Balai dans le cul | Stick up one’s ass — expression plutôt qu’un nom | [rigid](#s-rigid) | renvois contextualisés |
| [141](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L141) | Trouillard / trouillarde | Chicken, coward | [timid](#s-timid) | renvois contextualisés |
| [142](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L142) | Froussard / froussarde | Chicken, coward | [timid](#s-timid) | renvois contextualisés |
| [143](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L143) | Dégonflé / dégonflée | Chicken, coward | [coward](#s-coward) | renvois contextualisés |
| [144](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L144) | Mauviette | Wimp, weakling | [weakling](#s-weakling) | renvois contextualisés |
| [145](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L145) | Poule mouillée | Chicken | [timid](#s-timid) | renvois contextualisés |
| [146](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L146) | Lâche | Coward | [coward](#s-coward) | renvois contextualisés |
| [147](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L147) | Pleurnichard / pleurnicharde | Crybaby, whiner | [whiner](#s-whiner) | renvois contextualisés |
| [148](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L148) | Chouineur / chouineuse | Whiner, crybaby | [whiner](#s-whiner) | renvois contextualisés |
| [149](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L149) | Cafteur / cafteuse | Snitch, tattletale | [snitch](#s-snitch), [tattletale](#s-tattletale) | sens alternatifs à désambiguïser |
| [150](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L150) | Balance | Snitch, rat | [snitch](#s-snitch) | renvois contextualisés |
| [151](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L151) | Mouchard | Snitch, informer | [snitch](#s-snitch) | renvois contextualisés |
| [152](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L152) | Traître / traîtresse | Traitor, backstabber | [traitor](#s-traitor) | renvois contextualisés |
| [153](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L153) | Vendue / vendu | Sellout | [sellout](#s-sellout) | renvois contextualisés |
| [154](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L154) | Profiteur / profiteuse | Freeloader, user | [freeloader](#s-freeloader), [profiteer](#s-profiteer) | sens alternatifs à désambiguïser |
| [155](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L155) | Pique-assiette | Freeloader, moocher | [freeloader](#s-freeloader) | renvois contextualisés |
| [156](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L156) | Parasite | Parasite, freeloader | [freeloader](#s-freeloader) | renvois contextualisés |
| [157](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L157) | Sangsue | Leech | [freeloader](#s-freeloader) | renvois contextualisés |
| [158](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L158) | Rapace | Vulture, greedy bastard | [greedy](#s-greedy) | renvois contextualisés |
| [159](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L159) | Rat | Cheapskate, tightwad — lorsqu’on vise l’avarice | [cheapskate](#s-cheapskate) | renvois contextualisés |
| [160](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L160) | Crevard / crevarde | Cheap bastard, scumbag — selon le contexte | [cheapskate](#s-cheapskate) | renvois contextualisés |
| [161](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L161) | Grippe-sou | Penny-pincher, cheapskate | [penny_pincher](#s-penny_pincher) | renvois contextualisés |
| [162](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L162) | Escroc | Crook, scammer | [crook](#s-crook) | renvois contextualisés |
| [163](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L163) | Vaurien | Good-for-nothing, scoundrel | [useless](#s-useless) | renvois contextualisés |
| [164](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L164) | Crapule | Scoundrel, crook, scumbag | [crook](#s-crook) | renvois contextualisés |
| [165](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L165) | Voyou | Thug, hoodlum | [thug](#s-thug) | renvois contextualisés |
| [166](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L166) | Petite frappe | Small-time thug, punk | [thug](#s-thug) | renvois contextualisés |
| [167](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L167) | Fauteur de troubles | Troublemaker | [troublemaker](#s-troublemaker) | renvois contextualisés |
| [173](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L173) | Pute | Whore | [sexual_slur](#s-sexual_slur), [sexwork_slur](#s-sexwork_slur) | sens alternatifs à désambiguïser |
| [174](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L174) | Putain — visant une personne | Whore | [sexual_slur](#s-sexual_slur), [sexwork_slur](#s-sexwork_slur) | sens alternatifs à désambiguïser |
| [175](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L175) | Salope | Bitch ; slut lorsqu’on vise la sexualité | [sexual_slur](#s-sexual_slur), [bitch](#s-bitch) | sens alternatifs à désambiguïser |
| [176](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L176) | Salopette — emploi insultant rare | Little bitch — selon le contexte | [bitch](#s-bitch) | renvois contextualisés |
| [177](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L177) | Garce | Bitch | [vile](#s-vile), [bitch](#s-bitch) | sens alternatifs à désambiguïser |
| [178](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L178) | Pouffiasse | Bitch, trashy woman | [vile](#s-vile), [sexual_slur](#s-sexual_slur), [bitch](#s-bitch), [bimbo](#s-bimbo) | sens alternatifs à désambiguïser |
| [179](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L179) | Pouffe | Bimbo, bitch — selon le contexte | [vile](#s-vile), [sexual_slur](#s-sexual_slur), [bitch](#s-bitch), [bimbo](#s-bimbo) | sens alternatifs à désambiguïser |
| [180](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L180) | Pétasse | Bitch, bimbo | [vile](#s-vile), [sexual_slur](#s-sexual_slur), [bitch](#s-bitch), [bimbo](#s-bimbo) | sens alternatifs à désambiguïser |
| [181](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L181) | Grognasse | Bitch, unpleasant woman | [vile](#s-vile), [sexual_slur](#s-sexual_slur), [bitch](#s-bitch) | sens alternatifs à désambiguïser |
| [182](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L182) | Connasse | Bitch, asshole | [vile](#s-vile), [fregos](#s-fregos), [bitch](#s-bitch) | sens alternatifs à désambiguïser |
| [183](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L183) | Grel u che / greluche | Bimbo, silly woman | [airhead](#s-airhead), [bimbo](#s-bimbo) | sens alternatifs à désambiguïser |
| [184](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L184) | Dinde | Silly woman, airhead | [airhead](#s-airhead), [bimbo](#s-bimbo) | sens alternatifs à désambiguïser |
| [185](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L185) | Bécasse | Silly woman, dimwit | [airhead](#s-airhead), [bimbo](#s-bimbo) | sens alternatifs à désambiguïser |
| [186](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L186) | Cruche | Airhead, dimwit | [airhead](#s-airhead), [bimbo](#s-bimbo) | sens alternatifs à désambiguïser |
| [187](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L187) | Morue | Bitch, old cow — emploi insultant | [vile](#s-vile), [sexual_slur](#s-sexual_slur), [bitch](#s-bitch) | sens alternatifs à désambiguïser |
| [188](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L188) | Vieille peau | Old bag, old hag | [old_vile_woman](#s-old_vile_woman) | renvois contextualisés |
| [189](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L189) | Vieille bique | Old goat, old cow | [old_vile_woman](#s-old_vile_woman) | renvois contextualisés |
| [190](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L190) | Mégère | Shrew, harridan | [grouch](#s-grouch) | renvois contextualisés |
| [191](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L191) | Harpie | Harpy, shrew | [grouch](#s-grouch) | renvois contextualisés |
| [192](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L192) | Sorcière | Witch, hag — emploi insultant | [grouch](#s-grouch) | renvois contextualisés |
| [193](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L193) | Truie | Pig, sow | [vile](#s-vile) | renvois contextualisés |
| [194](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L194) | Porc | Pig, filthy pig | [vile](#s-vile) | renvois contextualisés |
| [195](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L195) | Cochon / cochonne | Pig, dirty pig ; parfois affectueux ou sexuel | [vile](#s-vile) | renvois contextualisés |
| [196](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L196) | Obsédé / obsédée | Creep, sex maniac | [sexual_creep](#s-sexual_creep) | renvois contextualisés |
| [197](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L197) | Gros dégueulasse | Dirty bastard, disgusting pig | [disgusting](#s-disgusting) | renvois contextualisés |
| [198](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L198) | Pervers | Pervert | [pervert](#s-pervert) | renvois contextualisés |
| [199](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L199) | Queutard | Horndog, womanizer | [sexual_creep](#s-sexual_creep) | renvois contextualisés |
| [200](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L200) | Chien de la casse | Scumbag ; horndog dans certains contextes | [vile](#s-vile), [sexual_creep](#s-sexual_creep) | sens alternatifs à désambiguïser |
| [201](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L201) | Chienne | Bitch — le sens sexuel dépend du contexte | [vile](#s-vile), [bitch](#s-bitch) | sens alternatifs à désambiguïser |
| [202](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L202) | Catin | Whore, harlot — vieilli | [sexual_slur](#s-sexual_slur), [sexwork_slur](#s-sexwork_slur) | sens alternatifs à désambiguïser |
| [203](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L203) | Traînée | Slut | [sexual_slur](#s-sexual_slur) | renvois contextualisés |
| [204](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L204) | Marie-couche-toi-là | Slut, easy lay | [sexual_slur](#s-sexual_slur) | renvois contextualisés |
| [205](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L205) | Allumeuse | Tease | [flirt_accusation](#s-flirt_accusation) | renvois contextualisés |
| [206](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L206) | Cocu | Cuckold ; cuck dans certains usages injurieux | [cuckold](#s-cuckold) | renvois contextualisés |
| [207](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L207) | Beauf | Boor, vulgar sexist guy — pas d’équivalent unique | [sexist_boor](#s-sexist_boor) | renvois contextualisés |
| [212](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L212) | Merde ! | Shit! | [scat](#s-scat) | renvois contextualisés |
| [213](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L213) | Oh merde ! | Oh shit! | [scat](#s-scat) | renvois contextualisés |
| [214](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L214) | Et merde ! | Shit! / Damn it! | [scat](#s-scat) | renvois contextualisés |
| [215](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L215) | Putain ! | Fuck! / Fucking hell! | [strong_expletive](#s-strong_expletive) | renvois contextualisés |
| [216](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L216) | Putain de merde ! | Fucking hell! / Holy shit! | [double_expletive](#s-double_expletive) | renvois contextualisés |
| [217](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L217) | Bordel ! | Fuck! / Damn it! | [scat](#s-scat), [strong_expletive](#s-strong_expletive) | sens alternatifs à désambiguïser |
| [218](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L218) | Bordel de merde ! | Fucking hell! | [double_expletive](#s-double_expletive) | renvois contextualisés |
| [219](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L219) | Bordel à cul ! | Fucking hell! | [double_expletive](#s-double_expletive) | renvois contextualisés |
| [220](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L220) | Bordel de cul ! | Fucking hell! | [double_expletive](#s-double_expletive) | renvois contextualisés |
| [221](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L221) | Nom de Dieu ! | Goddamn it! | [god_expletive](#s-god_expletive) | renvois contextualisés |
| [222](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L222) | Bon Dieu ! | Good God! / Goddamn it! | [god_expletive](#s-god_expletive), [by_god](#s-by_god) | sens alternatifs à désambiguïser |
| [223](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L223) | Putain de Dieu ! | God fucking damn it! | [god_expletive](#s-god_expletive) | renvois contextualisés |
| [224](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L224) | Bordel de Dieu ! | Goddamn it! / Fucking hell! | [god_expletive](#s-god_expletive) | renvois contextualisés |
| [225](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L225) | Nom de nom ! | Damn it! | [scat](#s-scat) | renvois contextualisés |
| [226](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L226) | Nom d’un chien ! | Damn it! / For heaven’s sake! | [scat](#s-scat) | renvois contextualisés |
| [227](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L227) | Nom d’une pipe ! | For crying out loud! | [theatrical](#s-theatrical) | renvois contextualisés |
| [228](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L228) | Nom d’une pipe en bois ! | For crying out loud! | [theatrical](#s-theatrical) | renvois contextualisés |
| [229](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L229) | Sacré nom de Dieu ! | God fucking damn it! | [god_expletive](#s-god_expletive) | renvois contextualisés |
| [230](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L230) | Sacrebleu ! | Good heavens! — vieilli et théâtral | [theatrical](#s-theatrical) | renvois contextualisés |
| [231](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L231) | Sapristi ! | Good heavens! / Gosh! | [theatrical](#s-theatrical) | renvois contextualisés |
| [232](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L232) | Saperlipopette ! | Goodness gracious! | [theatrical](#s-theatrical) | renvois contextualisés |
| [233](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L233) | Saperlotte ! | Good heavens! | [theatrical](#s-theatrical) | renvois contextualisés |
| [234](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L234) | Morbleu ! | By God! — archaïque | [by_god](#s-by_god) | renvois contextualisés |
| [235](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L235) | Palsambleu ! | By God! — archaïque | [by_god](#s-by_god) | renvois contextualisés |
| [236](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L236) | Parbleu ! | By God! / Of course! — selon l’emploi | [by_god](#s-by_god) | renvois contextualisés |
| [237](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L237) | Tudieu ! | Good God! — archaïque | [by_god](#s-by_god) | renvois contextualisés |
| [238](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L238) | Foutre ! | Damn! / Fuck! — vieilli comme juron | [strong_expletive](#s-strong_expletive) | renvois contextualisés |
| [239](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L239) | Fichtre ! | Good heavens! / Damn! | [theatrical](#s-theatrical) | renvois contextualisés |
| [240](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L240) | Fichtrement | Damn, bloody — comme intensif | [adj_intensifier](#s-adj_intensifier) | renvois contextualisés |
| [241](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L241) | Diable ! | Damn! / Well, I’ll be damned! | [devil_expletive](#s-devil_expletive) | renvois contextualisés |
| [242](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L242) | Que diable ! | What the devil! / What the hell! | [devil_expletive](#s-devil_expletive), [what](#s-what) | sens alternatifs à désambiguïser |
| [243](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L243) | Au diable ! | To hell with it! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [244](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L244) | Enfer et damnation ! | Hell and damnation! | [curses](#s-curses) | renvois contextualisés |
| [245](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L245) | Malédiction ! | Damn it! / Curses! | [curses](#s-curses) | renvois contextualisés |
| [246](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L246) | Mince ! | Darn! / Shoot! | [mild_expletive](#s-mild_expletive) | renvois contextualisés |
| [247](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L247) | Zut ! | Darn! / Shoot! | [mild_expletive](#s-mild_expletive) | renvois contextualisés |
| [248](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L248) | Zut alors ! | Darn it! | [mild_expletive](#s-mild_expletive) | renvois contextualisés |
| [249](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L249) | Flûte ! | Darn! | [mild_expletive](#s-mild_expletive) | renvois contextualisés |
| [250](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L250) | Crotte ! | Poop! / Darn! | [mild_expletive](#s-mild_expletive) | renvois contextualisés |
| [251](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L251) | Purée ! | Jeez! / Dang! | [mild_expletive](#s-mild_expletive) | renvois contextualisés |
| [252](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L252) | Punaise ! | Jeez! / Dang! | [mild_expletive](#s-mild_expletive) | renvois contextualisés |
| [253](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L253) | Pétard ! | Damn! / Jeez! | [mild_expletive](#s-mild_expletive) | renvois contextualisés |
| [254](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L254) | La vache ! | Holy cow! | [surprise](#s-surprise) | renvois contextualisés |
| [255](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L255) | Oh la vache ! | Holy cow! / Holy shit! | [strong_surprise](#s-strong_surprise) | renvois contextualisés |
| [256](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L256) | Ça alors ! | Well, damn! / Good grief! | [surprise](#s-surprise) | renvois contextualisés |
| [257](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L257) | Bon sang ! | Damn it! / For heaven’s sake! | [scat](#s-scat) | renvois contextualisés |
| [258](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L258) | Bon sang de bonsoir ! | For crying out loud! | [theatrical](#s-theatrical) | renvois contextualisés |
| [259](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L259) | Fait chier ! | Fuck! / What a pain in the ass! | [strong_expletive](#s-strong_expletive) | renvois contextualisés |
| [260](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L260) | Ça me fait chier ! | This pisses me off! | [annoyed_thing](#s-annoyed_thing) | renvois contextualisés |
| [261](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L261) | Ça fait chier ! | This fucking sucks! | [annoyed_thing](#s-annoyed_thing), [bad_quality](#s-bad_quality) | sens alternatifs à désambiguïser |
| [262](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L262) | Merde alors ! | Bloody hell! / Well, shit! | [scat](#s-scat) | renvois contextualisés |
| [267](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L267) | Va te faire foutre ! | Go fuck yourself! / Fuck off! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [268](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L268) | Va te faire mettre ! | Go fuck yourself! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [269](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L269) | Va te faire enculer ! | Go fuck yourself! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [270](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L270) | Va chier ! | Fuck off! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [271](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L271) | Va te faire voir ! | Get lost! / Screw you! | [dismiss_mild](#s-dismiss_mild), [dismiss_strong](#s-dismiss_strong) | sens alternatifs à désambiguïser |
| [272](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L272) | Va te faire cuire un œuf ! | Go take a hike! / Get lost! | [dismiss_mild](#s-dismiss_mild), [dismiss_strong](#s-dismiss_strong) | sens alternatifs à désambiguïser |
| [273](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L273) | Va au diable ! | Go to hell! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [274](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L274) | Va te faire pendre ailleurs ! | Get lost! / Go to hell! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [275](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L275) | Va te faire voir chez les Grecs ! | Get lost! / Fuck off! — expression à sous-entendu homophobe | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [276](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L276) | Je t’emmerde ! | Fuck you! / Screw you! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [277](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L277) | Je vous emmerde ! | Fuck you! / Fuck you all! | [dismiss_strong](#s-dismiss_strong), [dismiss_plural](#s-dismiss_plural) | sens alternatifs à désambiguïser |
| [278](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L278) | Je te chie dessus ! | Fuck you! — littéralement I shit on you | [dismiss_strong](#s-dismiss_strong), [literal_shit_on](#s-literal_shit_on) | sens alternatifs à désambiguïser |
| [279](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L279) | Nique-toi ! | Go fuck yourself! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [280](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L280) | Nique ta race ! | Fuck you! — pas d’équivalent idiomatique exact | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [281](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L281) | Ta gueule ! | Shut the fuck up! / Shut up! | [shut_mild](#s-shut_mild), [shut_strong](#s-shut_strong) | sens alternatifs à désambiguïser |
| [282](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L282) | Ferme ta gueule ! | Shut the fuck up! | [shut_strong](#s-shut_strong) | renvois contextualisés |
| [283](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L283) | Ferme-la ! | Shut up! | [shut_mild](#s-shut_mild) | renvois contextualisés |
| [284](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L284) | Boucle-la ! | Shut it! / Shut your mouth! | [shut_mild](#s-shut_mild) | renvois contextualisés |
| [285](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L285) | Écrase ! | Shut it! | [shut_mild](#s-shut_mild) | renvois contextualisés |
| [286](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L286) | La ferme ! | Shut up! | [shut_mild](#s-shut_mild) | renvois contextualisés |
| [287](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L287) | Ferme ton clapet ! | Shut your trap! | [mouth_shut](#s-mouth_shut) | renvois contextualisés |
| [288](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L288) | Ferme ton claque-merde ! | Shut your fucking mouth! | [shut_strong](#s-shut_strong) | renvois contextualisés |
| [289](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L289) | Dégage ! | Get lost! / Get out! | [dismiss_mild](#s-dismiss_mild), [dismiss_strong](#s-dismiss_strong) | sens alternatifs à désambiguïser |
| [290](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L290) | Barre-toi ! | Get lost! / Piss off! | [dismiss_mild](#s-dismiss_mild), [dismiss_strong](#s-dismiss_strong) | sens alternatifs à désambiguïser |
| [291](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L291) | Casse-toi ! | Piss off! / Fuck off! | [dismiss_mild](#s-dismiss_mild), [dismiss_strong](#s-dismiss_strong) | sens alternatifs à désambiguïser |
| [292](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L292) | Tire-toi ! | Get out! / Get lost! | [dismiss_mild](#s-dismiss_mild), [dismiss_strong](#s-dismiss_strong) | sens alternatifs à désambiguïser |
| [293](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L293) | Fous le camp ! | Get the hell out! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [294](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L294) | Fous-moi la paix ! | Leave me the fuck alone! | [leave_alone_strong](#s-leave_alone_strong) | renvois contextualisés |
| [295](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L295) | Fous-moi le camp ! | Get the hell out of here! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [296](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L296) | Lâche-moi la grappe ! | Get off my back! | [leave_alone](#s-leave_alone) | renvois contextualisés |
| [297](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L297) | Lâche-moi les baskets ! | Get off my back! / Leave me alone! | [leave_alone](#s-leave_alone) | renvois contextualisés |
| [298](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L298) | Arrête tes conneries ! | Cut the bullshit! | [cut_bullshit](#s-cut_bullshit) | renvois contextualisés |
| [299](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L299) | Arrête de faire chier ! | Stop being a pain in the ass! | [stop_nuisance](#s-stop_nuisance) | renvois contextualisés |
| [300](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L300) | Fais pas chier ! | Don’t piss me off! / Stop fucking around! | [stop_nuisance](#s-stop_nuisance) | renvois contextualisés |
| [301](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L301) | Me casse pas les couilles ! | Get off my fucking back! / Don’t bust my balls! | [stop_nuisance](#s-stop_nuisance) | renvois contextualisés |
| [302](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L302) | Tu me fais chier ! | You’re pissing me off! | [annoyed](#s-annoyed) | renvois contextualisés |
| [303](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L303) | Tu me casses les couilles ! | You’re a fucking pain in the ass! | [annoyed](#s-annoyed) | renvois contextualisés |
| [304](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L304) | Tu peux te le mettre au cul ! | You can shove it up your ass! | [shove_ass](#s-shove_ass) | renvois contextualisés |
| [305](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L305) | Dans ton cul ! | Up your ass! | [up_yours](#s-up_yours) | renvois contextualisés |
| [306](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L306) | Mon cul ! | My ass! / Bullshit! | [bullshit](#s-bullshit) | renvois contextualisés |
| [307](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L307) | Ton cul ! | Your ass! — emploi variable | [up_yours](#s-up_yours) | renvois contextualisés |
| [308](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L308) | Mes couilles ! | Bullshit! / My ass! | [bullshit](#s-bullshit) | renvois contextualisés |
| [309](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L309) | Tu te fous de ma gueule ? | Are you fucking kidding me? | [mock_question](#s-mock_question) | renvois contextualisés |
| [310](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L310) | Tu me prends pour un con ? | Do you think I’m a fucking idiot? | [take_for_fool](#s-take_for_fool) | renvois contextualisés |
| [315](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L315) | Une connerie | Something stupid, a stupid mistake ; bullshit selon le contexte | [mistake](#s-mistake) | renvois contextualisés |
| [316](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L316) | Des conneries | Bullshit, stupid shit | [bullshit](#s-bullshit) | renvois contextualisés |
| [317](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L317) | Une saloperie | A nasty thing, a piece of shit | [mean_stunt](#s-mean_stunt) | renvois contextualisés |
| [318](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L318) | Une vacherie | A nasty trick, a shitty thing to do | [mean_stunt](#s-mean_stunt) | renvois contextualisés |
| [319](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L319) | Une putasserie | A shitty stunt, a sleazy move | [mean_stunt](#s-mean_stunt) | renvois contextualisés |
| [320](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L320) | Du foutage de gueule | A fucking joke, a piss-take UK | [mock_question](#s-mock_question) | renvois contextualisés |
| [321](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L321) | C’est de la merde | It’s shit | [scat](#s-scat) | renvois contextualisés |
| [322](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L322) | C’est à chier | It’s fucking awful / It sucks | [bad_quality](#s-bad_quality) | renvois contextualisés |
| [323](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L323) | C’est pourri | It sucks / It’s crap | [bad_quality](#s-bad_quality) | renvois contextualisés |
| [324](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L324) | C’est naze | It sucks / It’s lame | [bad_quality](#s-bad_quality) | renvois contextualisés |
| [325](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L325) | C’est bidon | It’s bogus / It’s bullshit | [bullshit](#s-bullshit), [bogus](#s-bogus) | sens alternatifs à désambiguïser |
| [326](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L326) | C’est des conneries | That’s bullshit | [bullshit](#s-bullshit) | renvois contextualisés |
| [327](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L327) | C’est le bordel | It’s a fucking mess | [mess](#s-mess) | renvois contextualisés |
| [328](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L328) | Un bordel monstre | A complete fucking mess | [mess](#s-mess), [huge_mess](#s-huge_mess) | sens alternatifs à désambiguïser |
| [329](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L329) | Un merdier | A shitshow, a fucking mess | [mess](#s-mess), [huge_mess](#s-huge_mess), [failure](#s-failure) | sens alternatifs à désambiguïser |
| [330](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L330) | Un sacré merdier | A real shitshow | [huge_mess](#s-huge_mess), [failure](#s-failure) | sens alternatifs à désambiguïser |
| [331](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L331) | Une situation de merde | A shitty situation | [bad_situation](#s-bad_situation) | renvois contextualisés |
| [332](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L332) | Un boulot de merde | A shitty job | [crap_job](#s-crap_job) | renvois contextualisés |
| [333](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L333) | Un temps de merde | Shitty weather | [crap_weather](#s-crap_weather) | renvois contextualisés |
| [334](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L334) | Une journée de merde | A shitty day | [crap_day](#s-crap_day) | renvois contextualisés |
| [335](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L335) | Une vie de merde | A shitty life | [crap_life](#s-crap_life) | renvois contextualisés |
| [336](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L336) | Une putain de journée | A fucking day — préciser : a fucking awful/amazing day selon le sens | [intensifier_strong](#s-intensifier_strong) | renvois contextualisés |
| [337](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L337) | Ce putain de… | This fucking… | [intensifier_strong](#s-intensifier_strong) | renvois contextualisés |
| [338](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L338) | Ce foutu… | This damn… / This fucking… | [intensifier_strong](#s-intensifier_strong), [intensifier_mild](#s-intensifier_mild) | sens alternatifs à désambiguïser |
| [339](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L339) | Ce satané… | This damn… / This blasted… | [intensifier_mild](#s-intensifier_mild) | renvois contextualisés |
| [340](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L340) | Ce fichu… | This darn… / This damn… | [intensifier_mild](#s-intensifier_mild) | renvois contextualisés |
| [341](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L341) | À la con | Stupid, dumb, shitty | [stupid_modifier](#s-stupid_modifier) | renvois contextualisés |
| [342](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L342) | À la noix | Stupid, lame, lousy | [cheap](#s-cheap) | renvois contextualisés |
| [343](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L343) | À la mord-moi-le-nœud | Half-assed, crappy | [half_assed](#s-half_assed) | renvois contextualisés |
| [344](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L344) | De mes deux | Fucking useless, lousy — selon la construction | [intensifier_strong](#s-intensifier_strong) | renvois contextualisés |
| [345](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L345) | De mes couilles | Fucking…, my ass — selon la construction | [intensifier_strong](#s-intensifier_strong) | renvois contextualisés |
| [346](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L346) | À deux balles | Cheap, crappy, two-bit | [cheap](#s-cheap) | renvois contextualisés |
| [347](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L347) | À la mords-moi le jonc | Half-assed, crappy | [half_assed](#s-half_assed) | renvois contextualisés |
| [348](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L348) | Je m’en fous | I don’t care / I don’t give a damn | [dont_care](#s-dont_care) | renvois contextualisés |
| [349](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L349) | Je m’en fiche | I don’t care | [dont_care](#s-dont_care) | renvois contextualisés |
| [350](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L350) | Je m’en branle | I don’t give a fuck | [dont_care_strong](#s-dont_care_strong) | renvois contextualisés |
| [351](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L351) | Je m’en bats les couilles | I don’t give a fuck | [dont_care_strong](#s-dont_care_strong) | renvois contextualisés |
| [352](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L352) | J’en ai rien à foutre | I don’t give a fuck | [dont_care_strong](#s-dont_care_strong) | renvois contextualisés |
| [353](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L353) | J’en ai ras le cul | I’m fucking fed up | [fed_up](#s-fed_up) | renvois contextualisés |
| [354](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L354) | J’en ai plein le cul | I’m fucking sick of it | [fed_up](#s-fed_up), [fed_up_this](#s-fed_up_this) | sens alternatifs à désambiguïser |
| [355](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L355) | J’en ai ras les couilles | I’m fucking fed up | [fed_up](#s-fed_up) | renvois contextualisés |
| [356](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L356) | Ça me casse les couilles | It’s a fucking pain in the ass | [annoyed_thing](#s-annoyed_thing) | renvois contextualisés |
| [357](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L357) | Ça me casse les pieds | It’s getting on my nerves | [annoyed_thing](#s-annoyed_thing) | renvois contextualisés |
| [358](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L358) | Ça me prend la tête | It’s doing my head in UK / It’s driving me nuts | [annoyed_thing](#s-annoyed_thing) | renvois contextualisés |
| [359](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L359) | Ça me fout les boules | It pisses me off / It freaks me out — selon le contexte | [annoyed_thing](#s-annoyed_thing), [causes_fear](#s-causes_fear) | sens alternatifs à désambiguïser |
| [360](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L360) | Ça me fout la gerbe | It makes me fucking sick | [disgust](#s-disgust) | renvois contextualisés |
| [361](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L361) | Ça me troue le cul | That fucking blows my mind | [profound_surprise](#s-profound_surprise) | renvois contextualisés |
| [362](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L362) | Il se fout de moi | He’s taking the piss UK / He’s fucking with me | [he_mocks](#s-he_mocks) | renvois contextualisés |
| [363](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L363) | Se faire chier | To be bored shitless | [bored](#s-bored) | renvois contextualisés |
| [364](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L364) | Se faire emmerder | To get hassled | [hassled](#s-hassled) | renvois contextualisés |
| [365](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L365) | Se démerder | To figure it out, to manage — registre plus vulgaire en français | [manage](#s-manage) | renvois contextualisés |
| [366](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L366) | Faire de la merde | To fuck things up / To do a shitty job | [fuck_up](#s-fuck_up) | renvois contextualisés |
| [367](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L367) | Foutre la merde | To stir shit up / To fuck things up | [stir_discord](#s-stir_discord) | renvois contextualisés |
| [372](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L372) | Peuchère ! | Good grief! / You poor thing! — pas toujours un juron | [sympathy](#s-sympathy) | renvois contextualisés |
| [373](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L373) | Fan de chichourle ! | Good grief! / Bloody hell! — méridional | [theatrical](#s-theatrical) | renvois contextualisés |
| [374](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L374) | Fada | Nutcase, crazy fool — méridional, parfois affectueux | [weird_warning](#s-weird_warning), [unusual](#s-unusual) | sens alternatifs à désambiguïser |
| [375](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L375) | Jobard | Nutcase, fool | [gullible](#s-gullible) | renvois contextualisés |
| [376](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L376) | D jobi / jobi | Fool — régional, graphies variables | [unverified_regional](#s-unverified_regional) | documenté sans équivalent établi |
| [377](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L377) | Gognand | Fool, simpleton — régional | [unverified_regional](#s-unverified_regional) | documenté sans équivalent établi |
| [378](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L378) | Glandu | Idiot, useless guy | [useless](#s-useless) | renvois contextualisés |
| [379](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L379) | Glandouille | Idiot, slacker | [useless](#s-useless), [lazy](#s-lazy) | sens alternatifs à désambiguïser |
| [380](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L380) | Branquignol | Clown, incompetent fool | [inept](#s-inept) | renvois contextualisés |
| [381](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L381) | Bachi-bouzouk | Ruffian, savage — surtout littéraire ou humoristique | [lout](#s-lout) | renvois contextualisés |
| [382](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L382) | Ostrogoth | Barbarian, uncouth person | [boor](#s-boor) | renvois contextualisés |
| [383](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L383) | Paltoquet | Impudent little fool, lout | [lout](#s-lout) | renvois contextualisés |
| [384](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L384) | Faquin | Scoundrel, insolent fellow | [lout](#s-lout) | renvois contextualisés |
| [385](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L385) | Maraud | Scoundrel, rogue | [lout](#s-lout) | renvois contextualisés |
| [386](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L386) | Bélître | Scoundrel, good-for-nothing | [lout](#s-lout) | renvois contextualisés |
| [387](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L387) | Cuistre | Pompous pedant | [cuistre](#s-cuistre) | renvois contextualisés |
| [388](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L388) | Pédant | Pedant, know-it-all | [pedant](#s-pedant) | renvois contextualisés |
| [389](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L389) | Ganache | Old fool | [old_fool](#s-old_fool) | renvois contextualisés |
| [390](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L390) | Sagouin | Filthy pig, slob | [filthy](#s-filthy) | renvois contextualisés |
| [391](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L391) | Goret | Pig, slob | [filthy](#s-filthy) | renvois contextualisés |
| [392](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L392) | Crasseux / crasseuse | Filthy slob | [filthy](#s-filthy) | renvois contextualisés |
| [393](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L393) | Crado | Slob, filthy person | [filthy](#s-filthy) | renvois contextualisés |
| [394](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L394) | Cradingue | Filthy slob | [filthy](#s-filthy) | renvois contextualisés |
| [395](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L395) | Souillon | Slob, slovenly person | [filthy](#s-filthy) | renvois contextualisés |
| [396](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L396) | Sac à vin | Drunkard, boozehound | [drunkard](#s-drunkard) | renvois contextualisés |
| [397](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L397) | Poivrot / poivrote | Drunk, pisshead UK | [drunkard](#s-drunkard) | renvois contextualisés |
| [398](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L398) | Pochtron / pochtronne | Drunk, pisshead UK | [drunkard](#s-drunkard) | renvois contextualisés |
| [399](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L399) | Pilier de comptoir | Barfly | [drunkard](#s-drunkard) | renvois contextualisés |
| [400](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L400) | Arsouille | Rogue, drunkard — selon l’usage | [drunkard](#s-drunkard) | renvois contextualisés |
| [401](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L401) | Chenapan | Rascal, little brat — souvent léger | [rascal](#s-rascal) | renvois contextualisés |
| [402](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L402) | Garnement | Brat, rascal | [rascal](#s-rascal) | renvois contextualisés |
| [403](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L403) | Morveux / morveuse | Snot-nosed brat | [brat](#s-brat) | renvois contextualisés |
| [404](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L404) | Sale gosse | Little brat | [brat](#s-brat) | renvois contextualisés |
| [405](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L405) | Petit merdeux | Little shit | [small_vile](#s-small_vile) | renvois contextualisés |

### Entrées source EN

| Ligne | Texte original | Correspondance fournie | Sens proposés | Traitement |
|---|---|---|---|---|
| [437](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L437) | Idiot | Idiot, imbécile | [idiot](#s-idiot) | renvois contextualisés |
| [438](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L438) | Moron | Abruti, crétin | [idiot](#s-idiot) | renvois contextualisés |
| [439](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L439) | Dumbass | Abruti, gros con | [idiot](#s-idiot), [idiot_strong](#s-idiot_strong) | sens alternatifs à désambiguïser |
| [440](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L440) | Dumbfuck | Putain d’abruti, gros con | [idiot](#s-idiot), [idiot_strong](#s-idiot_strong) | sens alternatifs à désambiguïser |
| [441](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L441) | Fuckwit | Abruti, débile — davantage britannique | [idiot](#s-idiot) | renvois contextualisés |
| [442](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L442) | Dimwit | Simplet, abruti | [fool](#s-fool) | renvois contextualisés |
| [443](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L443) | Nitwit | Nigaud, imbécile | [idiot](#s-idiot) | renvois contextualisés |
| [444](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L444) | Halfwit | Crétin, abruti | [idiot](#s-idiot) | renvois contextualisés |
| [445](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L445) | Dumbbell | Andouille, abruti | [idiot](#s-idiot), [silly](#s-silly) | sens alternatifs à désambiguïser |
| [446](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L446) | Dummy | Andouille, idiot — parfois affectueux | [idiot](#s-idiot), [silly](#s-silly) | sens alternatifs à désambiguïser |
| [447](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L447) | Doofus | Andouille, grand benêt | [idiot](#s-idiot), [silly](#s-silly) | sens alternatifs à désambiguïser |
| [448](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L448) | Dork | Nigaud, ringard, empoté — parfois affectueux | [idiot](#s-idiot), [silly](#s-silly) | sens alternatifs à désambiguïser |
| [449](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L449) | Dingus | Andouille, idiot — souvent humoristique | [idiot](#s-idiot), [silly](#s-silly) | sens alternatifs à désambiguïser |
| [450](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L450) | Knucklehead | Tête de mule, abruti | [fool](#s-fool) | renvois contextualisés |
| [451](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L451) | Bonehead | Abruti, tête de pioche | [idiot](#s-idiot) | renvois contextualisés |
| [452](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L452) | Blockhead | Imbécile, tête de pioche | [idiot](#s-idiot) | renvois contextualisés |
| [453](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L453) | Airhead | Écervelé, tête vide | [airhead](#s-airhead) | renvois contextualisés |
| [454](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L454) | Meathead | Gros bourrin, brute sans cervelle | [boor_clumsy](#s-boor_clumsy) | renvois contextualisés |
| [455](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L455) | Dipshit | Abruti, petit con | [idiot](#s-idiot) | renvois contextualisés |
| [456](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L456) | Dipstick | Andouille, abruti | [idiot](#s-idiot) | renvois contextualisés |
| [457](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L457) | Shithead | Tête de con, connard | [fool](#s-fool), [fregos](#s-fregos) | sens alternatifs à désambiguïser |
| [458](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L458) | Fuckhead | Tête de con, gros connard | [idiot_strong](#s-idiot_strong), [fregos](#s-fregos) | sens alternatifs à désambiguïser |
| [459](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L459) | Dickhead | Tête de bite, connard | [fool](#s-fool), [fregos](#s-fregos) | sens alternatifs à désambiguïser |
| [460](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L460) | Butthead | Tête de con — généralement moins vulgaire | [fool](#s-fool), [fregos](#s-fregos) | sens alternatifs à désambiguïser |
| [461](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L461) | Asshat | Abruti, bouffon | [idiot](#s-idiot), [clown](#s-clown) | sens alternatifs à désambiguïser |
| [462](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L462) | Assclown | Bouffon, guignol | [clown](#s-clown) | renvois contextualisés |
| [463](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L463) | Jackass | Abruti, gros con | [idiot](#s-idiot) | renvois contextualisés |
| [464](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L464) | Ass | Con, imbécile | [idiot](#s-idiot) | renvois contextualisés |
| [465](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L465) | Horse’s ass | Gros con, parfait imbécile | [idiot](#s-idiot), [idiot_strong](#s-idiot_strong) | sens alternatifs à désambiguïser |
| [466](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L466) | Jerk | Connard, sale type | [vile](#s-vile) | renvois contextualisés |
| [467](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L467) | Jerk-off | Branleur, connard | [vile](#s-vile), [lazy](#s-lazy) | sens alternatifs à désambiguïser |
| [468](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L468) | Jagoff | Connard, abruti — régional, notamment Pittsburgh | [vile](#s-vile) | renvois contextualisés |
| [469](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L469) | Asshole | Connard, trou du cul | [vile](#s-vile) | renvois contextualisés |
| [470](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L470) | Prick | Connard, enfoiré | [vile](#s-vile) | renvois contextualisés |
| [471](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L471) | Dick | Connard, sale con | [vile](#s-vile) | renvois contextualisés |
| [472](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L472) | Douche | Connard, blaireau | [vile](#s-vile) | renvois contextualisés |
| [473](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L473) | Douchebag | Gros connard, blaireau prétentieux | [vile](#s-vile), [arrogant](#s-arrogant) | sens alternatifs à désambiguïser |
| [474](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L474) | Douchecanoe | Connard, bouffon — variante humoristique | [clown](#s-clown) | renvois contextualisés |
| [475](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L475) | Tool | Blaireau, bouffon ; parfois pantin | [clown](#s-clown), [puppet](#s-puppet) | sens alternatifs à désambiguïser |
| [476](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L476) | Loser | Raté, minable | [loser](#s-loser) | renvois contextualisés |
| [477](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L477) | Failure | Raté, incapable | [loser](#s-loser), [inept](#s-inept) | sens alternatifs à désambiguïser |
| [478](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L478) | Clown | Guignol, bouffon | [clown](#s-clown) | renvois contextualisés |
| [479](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L479) | Joke — You’re a joke | Guignol, personne ridicule | [clown](#s-clown) | renvois contextualisés |
| [480](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L480) | Scrub | Minable, bon à rien — argot | [loser](#s-loser) | renvois contextualisés |
| [481](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L481) | Chump | Pigeon, pauvre con | [gullible](#s-gullible) | renvois contextualisés |
| [482](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L482) | Sucker | Pigeon, poire | [gullible](#s-gullible) | renvois contextualisés |
| [483](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L483) | Schmuck | Pauvre con, imbécile | [idiot](#s-idiot), [vile](#s-vile) | sens alternatifs à désambiguïser |
| [484](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L484) | Putz | Abruti, pauvre type | [idiot](#s-idiot), [vile](#s-vile) | sens alternatifs à désambiguïser |
| [485](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L485) | Fool | Idiot, imbécile | [idiot](#s-idiot) | renvois contextualisés |
| [486](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L486) | Punk | Petite frappe, petit con | [thug](#s-thug) | renvois contextualisés |
| [487](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L487) | Little shit | Petit merdeux, petite merde | [small_vile](#s-small_vile) | renvois contextualisés |
| [488](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L488) | Little prick | Petit con | [small_vile](#s-small_vile) | renvois contextualisés |
| [489](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L489) | Little bastard | Petit salaud | [small_vile](#s-small_vile) | renvois contextualisés |
| [490](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L490) | Brat | Sale gosse, enfant gâté | [brat](#s-brat) | renvois contextualisés |
| [491](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L491) | Snot-nosed brat | Petit morveux | [brat](#s-brat) | renvois contextualisés |
| [492](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L492) | Punk-ass bitch | Petite merde, pauvre lâche — très méprisant | [vile_strong](#s-vile_strong), [coward](#s-coward) | sens alternatifs à désambiguïser |
| [497](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L497) | Bastard | Salaud, enfoiré | [vile](#s-vile) | renvois contextualisés |
| [498](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L498) | Son of a bitch | Fils de pute, salaud | [vile](#s-vile) | renvois contextualisés |
| [499](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L499) | Motherfucker | Enculé, gros enfoiré | [vile](#s-vile), [vile_strong](#s-vile_strong) | sens alternatifs à désambiguïser |
| [500](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L500) | Fucker | Enfoiré, connard | [vile](#s-vile) | renvois contextualisés |
| [501](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L501) | Fuckface | Tête de con, sale gueule | [vile](#s-vile) | renvois contextualisés |
| [502](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L502) | Shitface | Tête de merde, connard | [vile](#s-vile) | renvois contextualisés |
| [503](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L503) | Asswipe | Torche-cul, sous-merde | [worthless_vile](#s-worthless_vile) | renvois contextualisés |
| [504](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L504) | Shitbag | Sac à merde, ordure | [worthless_vile](#s-worthless_vile) | renvois contextualisés |
| [505](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L505) | Dirtbag | Ordure, sale type | [vile](#s-vile) | renvois contextualisés |
| [506](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L506) | Scumbag | Ordure, raclure | [vile](#s-vile) | renvois contextualisés |
| [507](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L507) | Sleazebag | Sale type, ordure, pervers — selon le contexte | [vile](#s-vile) | renvois contextualisés |
| [508](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L508) | Scum | Pourriture, racaille | [vile](#s-vile) | renvois contextualisés |
| [509](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L509) | Piece of shit | Merde, ordure | [vile](#s-vile), [vile_strong](#s-vile_strong) | sens alternatifs à désambiguïser |
| [510](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L510) | Worthless piece of shit | Sous-merde, déchet humain | [vile](#s-vile), [vile_strong](#s-vile_strong), [worthless_vile](#s-worthless_vile) | sens alternatifs à désambiguïser |
| [511](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L511) | Human garbage | Déchet humain, ordure | [vile](#s-vile), [worthless_vile](#s-worthless_vile) | sens alternatifs à désambiguïser |
| [512](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L512) | Trash — visant une personne | Déchet, racaille | [vile](#s-vile) | renvois contextualisés |
| [513](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L513) | Trailer trash | Cassos — insulte sociale visant les habitants de mobil-homes | [documented_social](#s-documented_social) | documenté sans équivalent établi |
| [514](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L514) | White trash | Cassos blanc, « petit Blanc » méprisé — insulte sociale et racialisée | [documented_social](#s-documented_social) | documenté sans équivalent établi |
| [515](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L515) | Waste of space | Bon à rien, déchet | [loser](#s-loser), [useless](#s-useless), [worthless_vile](#s-worthless_vile) | sens alternatifs à désambiguïser |
| [516](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L516) | Waste of skin | Déchet humain, sous-merde | [useless](#s-useless), [worthless_vile](#s-worthless_vile) | sens alternatifs à désambiguïser |
| [517](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L517) | Low life / lowlife | Crapule, raclure | [vile](#s-vile) | renvois contextualisés |
| [518](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L518) | Bottom-feeder | Raclure, parasite | [vile](#s-vile), [freeloader](#s-freeloader) | sens alternatifs à désambiguïser |
| [519](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L519) | Dirtball | Crasseux, sale type | [vile](#s-vile), [filthy](#s-filthy) | sens alternatifs à désambiguïser |
| [520](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L520) | Creep | Sale type, type malsain ou inquiétant | [creep](#s-creep) | renvois contextualisés |
| [521](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L521) | Creeper | Type louche, pervers qui met mal à l’aise | [sexual_harasser](#s-sexual_harasser) | renvois contextualisés |
| [522](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L522) | Sick fuck | Grand malade, pervers dégueulasse | [vile_strong](#s-vile_strong), [disgusting](#s-disgusting) | sens alternatifs à désambiguïser |
| [523](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L523) | Sick bastard | Sale pervers, grand malade | [vile_strong](#s-vile_strong), [disgusting](#s-disgusting) | sens alternatifs à désambiguïser |
| [524](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L524) | Psycho | Psychopathe, grand malade — emploi injurieux | [weird_warning](#s-weird_warning) | renvois contextualisés |
| [525](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L525) | Freak | Monstre, taré, personne bizarre — selon le contexte | [weird_warning](#s-weird_warning), [unusual](#s-unusual) | sens alternatifs à désambiguïser |
| [526](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L526) | Weirdo | Type bizarre, énergumène, taré | [weird_warning](#s-weird_warning), [unusual](#s-unusual) | sens alternatifs à désambiguïser |
| [527](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L527) | Freakshow | Phénomène de foire, personne jugée monstrueuse ou ridicule | [weird_warning](#s-weird_warning) | renvois contextualisés |
| [533](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L533) | Bullshitter | Baratineur, mytho | [bullshitter](#s-bullshitter) | renvois contextualisés |
| [534](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L534) | Liar | Menteur | [liar](#s-liar) | renvois contextualisés |
| [535](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L535) | Pathological liar | Menteur pathologique, gros mytho | [liar](#s-liar), [liar_habit](#s-liar_habit) | sens alternatifs à désambiguïser |
| [536](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L536) | Phony | Faux jeton, imposteur | [hypocrite](#s-hypocrite), [fake](#s-fake) | sens alternatifs à désambiguïser |
| [537](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L537) | Fraud | Imposteur, escroc | [crook](#s-crook) | renvois contextualisés |
| [538](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L538) | Two-faced asshole | Faux-cul, connard hypocrite | [hypocrite](#s-hypocrite) | renvois contextualisés |
| [539](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L539) | Backstabber | Traître, personne qui poignarde dans le dos | [traitor](#s-traitor) | renvois contextualisés |
| [540](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L540) | Snake | Vipère, traître | [traitor](#s-traitor) | renvois contextualisés |
| [541](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L541) | Rat | Balance, traître | [snitch](#s-snitch), [traitor](#s-traitor) | sens alternatifs à désambiguïser |
| [542](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L542) | Snitch | Balance, cafteur | [snitch](#s-snitch) | renvois contextualisés |
| [543](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L543) | Tattletale | Rapporteur, cafteur — souvent enfantin | [tattletale](#s-tattletale) | renvois contextualisés |
| [544](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L544) | Sellout | Vendu | [sellout](#s-sellout) | renvois contextualisés |
| [545](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L545) | Ass-kisser | Lèche-cul | [bootlicker](#s-bootlicker) | renvois contextualisés |
| [546](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L546) | Brown-noser | Lèche-cul, fayot | [bootlicker](#s-bootlicker) | renvois contextualisés |
| [547](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L547) | Suck-up | Fayot, lèche-bottes | [bootlicker](#s-bootlicker) | renvois contextualisés |
| [548](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L548) | Bootlicker | Lèche-bottes | [bootlicker](#s-bootlicker) | renvois contextualisés |
| [549](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L549) | Teacher’s pet | Chouchou du prof, fayot | [tattletale](#s-tattletale) | renvois contextualisés |
| [550](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L550) | Kiss-ass | Lèche-cul | [bootlicker](#s-bootlicker) | renvois contextualisés |
| [551](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L551) | Shit-stirrer | Fouteur de merde | [troublemaker](#s-troublemaker) | renvois contextualisés |
| [552](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L552) | Troublemaker | Fauteur de troubles, fouteur de merde | [troublemaker](#s-troublemaker) | renvois contextualisés |
| [553](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L553) | Drama queen | Personne qui fait des histoires ou en fait des tonnes | [dramatic](#s-dramatic) | renvois contextualisés |
| [554](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L554) | Attention whore | Personne prête à tout pour attirer l’attention | [attention_seeker](#s-attention_seeker) | renvois contextualisés |
| [555](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L555) | Loudmouth | Grande gueule | [loudmouth](#s-loudmouth) | renvois contextualisés |
| [556](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L556) | Bigmouth | Grande gueule ; personne incapable de garder un secret | [loudmouth](#s-loudmouth), [bigmouth_secret](#s-bigmouth_secret) | sens alternatifs à désambiguïser |
| [557](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L557) | Blowhard | Grande gueule, vantard | [windbag](#s-windbag) | renvois contextualisés |
| [558](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L558) | Windbag | Bavard pompeux, moulin à paroles | [windbag](#s-windbag) | renvois contextualisés |
| [559](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L559) | Know-it-all | Monsieur/Madame je-sais-tout | [pedant](#s-pedant) | renvois contextualisés |
| [560](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L560) | Smart-ass | Petit malin, petit con | [smartass](#s-smartass) | renvois contextualisés |
| [561](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L561) | Wiseass | Petit malin, insolent | [smartass](#s-smartass) | renvois contextualisés |
| [562](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L562) | Show-off | Frimeur | [showoff](#s-showoff) | renvois contextualisés |
| [563](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L563) | Braggart | Vantard | [braggart](#s-braggart) | renvois contextualisés |
| [564](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L564) | Poser | Frimeur, poseur | [poser](#s-poser) | renvois contextualisés |
| [565](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L565) | Wannabe | Apprenti…, personne qui se donne un genre | [imitator](#s-imitator) | renvois contextualisés |
| [566](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L566) | Try-hard | Personne qui en fait trop pour impressionner | [imitator](#s-imitator) | renvois contextualisés |
| [567](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L567) | Snob | Snob | [snob](#s-snob) | renvois contextualisés |
| [568](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L568) | Entitled brat | Sale gosse qui se croit tout permis | [entitled](#s-entitled), [brat](#s-brat) | sens alternatifs à désambiguïser |
| [569](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L569) | Karen | Personne autoritaire qui multiplie les réclamations abusives — stéréotype genré | [bossy_complainer](#s-bossy_complainer) | renvois contextualisés |
| [570](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L570) | Busybody | Fouineur, personne qui se mêle de tout | [nosy](#s-nosy) | renvois contextualisés |
| [571](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L571) | Nosy bastard | Fouineur, fouille-merde | [nosy](#s-nosy) | renvois contextualisés |
| [572](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L572) | Pain in the ass | Casse-couilles, emmerdeur | [nuisance](#s-nuisance) | renvois contextualisés |
| [573](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L573) | Pain in the neck | Casse-pieds | [nuisance_mild](#s-nuisance_mild) | renvois contextualisés |
| [574](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L574) | Nag | Casse-pieds, personne qui rabâche | [nuisance_mild](#s-nuisance_mild) | renvois contextualisés |
| [575](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L575) | Whiner | Chouineur, râleur | [whiner](#s-whiner) | renvois contextualisés |
| [576](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L576) | Crybaby | Pleurnichard | [whiner](#s-whiner) | renvois contextualisés |
| [577](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L577) | Spoilsport | Rabat-joie | [killjoy](#s-killjoy) | renvois contextualisés |
| [578](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L578) | Killjoy | Rabat-joie | [killjoy](#s-killjoy) | renvois contextualisés |
| [579](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L579) | Tight-ass | Coincé, pisse-froid ; parfois radin | [rigid](#s-rigid), [cheapskate](#s-cheapskate) | sens alternatifs à désambiguïser |
| [580](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L580) | Prude | Prude, coincé | [prude](#s-prude) | renvois contextualisés |
| [581](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L581) | Stick-in-the-mud | Vieux jeu, rabat-joie | [killjoy](#s-killjoy) | renvois contextualisés |
| [582](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L582) | Slob | Crado, souillon | [filthy](#s-filthy) | renvois contextualisés |
| [583](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L583) | Pig | Porc, dégueulasse | [vile](#s-vile), [filthy](#s-filthy) | sens alternatifs à désambiguïser |
| [584](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L584) | Lazy ass | Grosse feignasse | [lazy_strong](#s-lazy_strong) | renvois contextualisés |
| [585](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L585) | Slacker | Glandeur | [lazy](#s-lazy) | renvois contextualisés |
| [586](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L586) | Deadbeat | Bon à rien, personne qui fuit ses obligations | [useless](#s-useless) | renvois contextualisés |
| [587](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L587) | Deadbeat dad | Père qui n’assume pas ses enfants, notamment financièrement | [lazy_parent](#s-lazy_parent) | renvois contextualisés |
| [588](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L588) | Freeloader | Profiteur, parasite | [freeloader](#s-freeloader), [profiteer](#s-profiteer) | sens alternatifs à désambiguïser |
| [589](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L589) | Moocher | Profiteur, pique-assiette | [freeloader](#s-freeloader) | renvois contextualisés |
| [590](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L590) | Leech | Sangsue, parasite | [freeloader](#s-freeloader) | renvois contextualisés |
| [591](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L591) | Cheapskate | Radin, pince | [cheapskate](#s-cheapskate) | renvois contextualisés |
| [592](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L592) | Tightwad | Radin, grippe-sou | [cheapskate](#s-cheapskate), [penny_pincher](#s-penny_pincher) | sens alternatifs à désambiguïser |
| [593](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L593) | Cheap bastard | Sale radin | [cheapskate](#s-cheapskate) | renvois contextualisés |
| [594](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L594) | Grifter | Escroc, arnaqueur | [crook](#s-crook) | renvois contextualisés |
| [595](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L595) | Con artist | Escroc, arnaqueur | [crook](#s-crook) | renvois contextualisés |
| [600](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L600) | Coward | Lâche | [coward](#s-coward) | renvois contextualisés |
| [601](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L601) | Chicken | Poule mouillée | [coward](#s-coward), [timid](#s-timid) | sens alternatifs à désambiguïser |
| [602](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L602) | Chicken-shit / chickenshit | Trouillard, dégonflé ; aussi « minable » selon l’emploi | [coward](#s-coward), [timid](#s-timid) | sens alternatifs à désambiguïser |
| [603](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L603) | Wimp | Mauviette | [weakling](#s-weakling) | renvois contextualisés |
| [604](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L604) | Wuss | Mauviette, dégonflé | [weakling](#s-weakling) | renvois contextualisés |
| [605](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L605) | Pussy | Mauviette, couille molle — emploi injurieux sexiste | [coward](#s-coward), [weakling](#s-weakling) | sens alternatifs à désambiguïser |
| [606](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L606) | Spineless bastard | Enfoiré sans courage, lâche | [coward](#s-coward) | renvois contextualisés |
| [607](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L607) | Doormat | Paillasson, personne qui se laisse marcher dessus | [puppet](#s-puppet), [submissive](#s-submissive) | sens alternatifs à désambiguïser |
| [608](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L608) | Pushover | Personne facile à intimider ou à convaincre | [puppet](#s-puppet), [submissive](#s-submissive) | sens alternatifs à désambiguïser |
| [609](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L609) | Simp | Personne qui s’écrase pour plaire à quelqu’un, souvent dans un contexte amoureux | [submissive](#s-submissive) | renvois contextualisés |
| [610](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L610) | Cuck | Cocu ; par extension, homme jugé faible ou soumis dans certains discours | [cuckold](#s-cuckold), [submissive](#s-submissive) | sens alternatifs à désambiguïser |
| [611](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L611) | Bootlicking coward | Lâche et lèche-bottes | [sycophant_coward](#s-sycophant_coward) | renvois contextualisés |
| [612](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L612) | Sissy | Mauviette, femmelette — insulte sexiste, parfois homophobe | [weakling](#s-weakling) | renvois contextualisés |
| [617](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L617) | Bitch | Salope, garce | [vile](#s-vile), [bitch](#s-bitch) | sens alternatifs à désambiguïser |
| [618](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L618) | Mean bitch | Sale garce | [vile](#s-vile), [bitch](#s-bitch) | sens alternatifs à désambiguïser |
| [619](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L619) | Crazy bitch | Folle furieuse, sale folle | [vile](#s-vile), [bitch](#s-bitch) | sens alternatifs à désambiguïser |
| [620](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L620) | Basic bitch | Fille jugée banale et conformiste — pas d’équivalent exact | [conformist_woman](#s-conformist_woman) | renvois contextualisés |
| [621](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L621) | Bad bitch | Femme sûre d’elle, indépendante — souvent valorisant | [empowered_woman](#s-empowered_woman) | renvois contextualisés |
| [622](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L622) | Boss bitch | Femme qui s’impose et dirige — souvent valorisant | [leader_woman](#s-leader_woman) | renvois contextualisés |
| [623](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L623) | Slut | Salope, traînée | [sexual_slur](#s-sexual_slur) | renvois contextualisés |
| [624](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L624) | Whore | Pute | [sexual_slur](#s-sexual_slur), [sexwork_slur](#s-sexwork_slur) | sens alternatifs à désambiguïser |
| [625](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L625) | Ho / hoe | Pute, traînée — argot | [sexual_slur](#s-sexual_slur), [sexwork_slur](#s-sexwork_slur) | sens alternatifs à désambiguïser |
| [626](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L626) | Skank | Pouffiasse, traînée, fille jugée sale | [sexual_slur](#s-sexual_slur) | renvois contextualisés |
| [627](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L627) | Tramp | Traînée — dans cet emploi | [sexual_slur](#s-sexual_slur) | renvois contextualisés |
| [628](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L628) | Hussy | Dévergondée, traînée — vieilli | [sexual_slur](#s-sexual_slur) | renvois contextualisés |
| [629](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L629) | Bimbo | Bimbo, greluche | [bimbo](#s-bimbo) | renvois contextualisés |
| [630](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L630) | Airhead | Écervelée, cruche — peut aussi viser un homme | [airhead](#s-airhead), [bimbo](#s-bimbo) | sens alternatifs à désambiguïser |
| [631](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L631) | Gold digger | Personne qui recherche une relation pour l’argent | [attracted_to_money](#s-attracted_to_money) | renvois contextualisés |
| [632](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L632) | Tease | Allumeuse, personne qui aguiche sans vouloir aller plus loin | [flirt_accusation](#s-flirt_accusation) | renvois contextualisés |
| [633](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L633) | Cocktease | Allumeuse — plus vulgaire | [flirt_accusation](#s-flirt_accusation) | renvois contextualisés |
| [634](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L634) | Cunt | Salope, connasse — généralement extrêmement violent aux États-Unis | [vile_strong](#s-vile_strong) | renvois contextualisés |
| [635](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L635) | Twat | Connasse, con — davantage britannique | [vile](#s-vile) | renvois contextualisés |
| [636](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L636) | Cocksucker | Suceur de bites, enculé — injure sexuelle, souvent homophobe | [sexual_sucker](#s-sexual_sucker) | renvois contextualisés |
| [637](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L637) | Motherfucking cocksucker | Putain d’enculé — équivalence de force approximative | [vile_strong](#s-vile_strong), [sexual_sucker](#s-sexual_sucker) | sens alternatifs à désambiguïser |
| [638](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L638) | Cum dumpster | Sac à foutre — extrêmement dégradant | [sexual_object](#s-sexual_object) | renvois contextualisés |
| [639](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L639) | Fuckboy / fuckboi | Queutard immature, mec qui manipule pour coucher | [sexual_creep](#s-sexual_creep), [sex_manipulator](#s-sex_manipulator) | sens alternatifs à désambiguïser |
| [640](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L640) | Manwhore | Queutard, homme qui multiplie les partenaires | [sexual_creep](#s-sexual_creep) | renvois contextualisés |
| [641](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L641) | Man-child | Gamin dans un corps d’adulte, homme immature | [childish_man](#s-childish_man) | renvois contextualisés |
| [642](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L642) | Limp dick | Impuissant, couille molle — selon le contexte | [weakling](#s-weakling) | renvois contextualisés |
| [643](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L643) | Dickless | Sans couilles, lâche | [coward](#s-coward) | renvois contextualisés |
| [644](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L644) | Pervert | Pervers | [pervert](#s-pervert) | renvois contextualisés |
| [645](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L645) | Dirty old man | Vieux pervers | [sexual_creep](#s-sexual_creep), [old_creep](#s-old_creep) | sens alternatifs à désambiguïser |
| [646](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L646) | Horny bastard | Obsédé, sacré queutard — parfois plaisant | [sexual_creep](#s-sexual_creep) | renvois contextualisés |
| [647](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L647) | Incel | Célibataire involontaire ; comme insulte, homme jugé misogyne et aigri | [involuntary_celibate](#s-involuntary_celibate), [spiteful_misogynist](#s-spiteful_misogynist) | sens alternatifs à désambiguïser |
| [652](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L652) | Fuck! | Putain ! | [strong_expletive](#s-strong_expletive) | renvois contextualisés |
| [653](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L653) | Oh, fuck! | Oh putain ! | [strong_expletive](#s-strong_expletive) | renvois contextualisés |
| [654](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L654) | Fuck me! | Putain ! / Ça alors ! — hors emploi littéral | [strong_expletive](#s-strong_expletive) | renvois contextualisés |
| [655](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L655) | Fucking hell! | Putain de merde ! / Bordel ! | [double_expletive](#s-double_expletive) | renvois contextualisés |
| [656](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L656) | What the fuck?! | C’est quoi ce bordel ?! / Mais putain, quoi ?! | [what](#s-what) | renvois contextualisés |
| [657](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L657) | The fuck?! | Quoi, putain ?! | [what](#s-what) | renvois contextualisés |
| [658](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L658) | Holy fuck! | Oh putain ! / Putain de merde ! | [strong_expletive](#s-strong_expletive), [double_expletive](#s-double_expletive) | sens alternatifs à désambiguïser |
| [659](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L659) | Holy shit! | Oh putain ! / La vache ! | [strong_expletive](#s-strong_expletive), [double_expletive](#s-double_expletive), [strong_surprise](#s-strong_surprise) | sens alternatifs à désambiguïser |
| [660](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L660) | Holy crap! | La vache ! / Oh merde ! | [strong_surprise](#s-strong_surprise) | renvois contextualisés |
| [661](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L661) | Holy cow! | La vache ! | [surprise](#s-surprise) | renvois contextualisés |
| [662](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L662) | Holy smokes! | La vache ! / Bon sang ! | [surprise](#s-surprise) | renvois contextualisés |
| [663](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L663) | Shit! | Merde ! | [scat](#s-scat) | renvois contextualisés |
| [664](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L664) | Oh, shit! | Oh merde ! | [scat](#s-scat) | renvois contextualisés |
| [665](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L665) | Well, shit | Bon, merde. / Eh ben, putain. | [scat](#s-scat) | renvois contextualisés |
| [666](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L666) | Shitballs! | Merde ! / Bordel ! — humoristique | [double_expletive](#s-double_expletive) | renvois contextualisés |
| [667](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L667) | Crap! | Merde ! / Mince ! — moins fort que shit | [mild_expletive](#s-mild_expletive) | renvois contextualisés |
| [668](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L668) | Damn! | Merde ! / Bon sang ! / Putain ! — selon le contexte | [scat](#s-scat) | renvois contextualisés |
| [669](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L669) | Damn it! | Et merde ! / Bon sang ! | [scat](#s-scat) | renvois contextualisés |
| [670](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L670) | Goddamn it! | Nom de Dieu ! / Bordel ! | [god_expletive](#s-god_expletive) | renvois contextualisés |
| [671](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L671) | God damn! | Nom de Dieu ! / Putain ! | [god_expletive](#s-god_expletive) | renvois contextualisés |
| [672](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L672) | God fucking damn it! | Putain de bordel de merde ! | [god_expletive](#s-god_expletive) | renvois contextualisés |
| [673](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L673) | Jesus! | Bon Dieu ! / Putain ! | [god_expletive](#s-god_expletive), [by_god](#s-by_god) | sens alternatifs à désambiguïser |
| [674](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L674) | Jesus Christ! | Bon Dieu ! / Nom de Dieu ! | [god_expletive](#s-god_expletive), [by_god](#s-by_god) | sens alternatifs à désambiguïser |
| [675](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L675) | Jesus fucking Christ! | Putain de merde ! / Nom de Dieu ! | [double_expletive](#s-double_expletive), [god_expletive](#s-god_expletive) | sens alternatifs à désambiguïser |
| [676](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L676) | Christ on a cracker! | Bon sang de bonsoir ! — humoristique | [theatrical](#s-theatrical) | renvois contextualisés |
| [677](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L677) | For Christ’s sake! | Bon Dieu ! / Mais enfin ! | [god_expletive](#s-god_expletive) | renvois contextualisés |
| [678](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L678) | For fuck’s sake! | Putain, fais chier ! / Bordel ! | [strong_expletive](#s-strong_expletive), [double_expletive](#s-double_expletive) | sens alternatifs à désambiguïser |
| [679](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L679) | For God’s sake! | Bon sang ! / Par pitié ! | [god_expletive](#s-god_expletive) | renvois contextualisés |
| [680](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L680) | For crying out loud! | Bon sang ! / Non mais c’est pas vrai ! | [theatrical](#s-theatrical) | renvois contextualisés |
| [681](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L681) | Son of a bitch! | Putain ! / Bordel ! — sans destinataire précis | [strong_expletive](#s-strong_expletive) | renvois contextualisés |
| [682](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L682) | Motherfucker! | Putain ! / Enculé ! — selon le destinataire | [strong_expletive](#s-strong_expletive) | renvois contextualisés |
| [683](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L683) | What the hell?! | C’est quoi ce bordel ?! / Mais qu’est-ce que… ?! | [what](#s-what) | renvois contextualisés |
| [684](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L684) | Bloody hell! | Bordel ! — surtout britannique | [scat](#s-scat) | renvois contextualisés |
| [685](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L685) | Hell no! | Sûrement pas ! / Ah ça, putain, non ! | [hell_no](#s-hell_no) | renvois contextualisés |
| [686](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L686) | Hell yeah! | Oh que oui ! / Putain, ouais ! | [hell_yes](#s-hell_yes) | renvois contextualisés |
| [687](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L687) | Damn right! | Carrément ! / Putain, oui ! | [hell_yes](#s-hell_yes) | renvois contextualisés |
| [692](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L692) | Darn! | Zut ! / Mince ! | [mild_expletive](#s-mild_expletive) | renvois contextualisés |
| [693](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L693) | Darn it! | Zut alors ! | [mild_expletive](#s-mild_expletive) | renvois contextualisés |
| [694](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L694) | Dang! | Mince ! / Purée ! | [mild_expletive](#s-mild_expletive) | renvois contextualisés |
| [695](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L695) | Heck! | Mince ! — selon la construction | [mild_expletive](#s-mild_expletive) | renvois contextualisés |
| [696](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L696) | What the heck? | Mais qu’est-ce que… ? / C’est quoi ce truc ? | [surprise](#s-surprise) | renvois contextualisés |
| [697](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L697) | Shoot! | Zut ! / Flûte ! | [mild_expletive](#s-mild_expletive) | renvois contextualisés |
| [698](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L698) | Shucks! | Zut ! / Oh, voyons ! — selon le contexte | [mild_expletive](#s-mild_expletive), [surprise](#s-surprise) | sens alternatifs à désambiguïser |
| [699](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L699) | Fudge! | Flûte ! / Purée ! | [mild_expletive](#s-mild_expletive) | renvois contextualisés |
| [700](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L700) | Frick! / Frig! | Purée ! / Punaise ! | [mild_expletive](#s-mild_expletive) | renvois contextualisés |
| [701](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L701) | Freaking / Frigging | Fichu, foutu, sacrément | [mild_expletive](#s-mild_expletive), [intensifier_mild](#s-intensifier_mild) | sens alternatifs à désambiguïser |
| [702](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L702) | Gosh! | Mon Dieu ! / Mince ! | [theatrical](#s-theatrical) | renvois contextualisés |
| [703](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L703) | Gee! | Mince ! / Eh ben ! | [theatrical](#s-theatrical) | renvois contextualisés |
| [704](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L704) | Jeez! / Geez! | Bon sang ! / Punaise ! | [theatrical](#s-theatrical), [mild_expletive](#s-mild_expletive) | sens alternatifs à désambiguïser |
| [705](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L705) | Good grief! | Bon sang ! / C’est pas vrai ! | [theatrical](#s-theatrical), [surprise](#s-surprise) | sens alternatifs à désambiguïser |
| [706](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L706) | Good lord! | Mon Dieu ! / Seigneur ! | [theatrical](#s-theatrical) | renvois contextualisés |
| [707](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L707) | Goodness gracious! | Grand Dieu ! / Mon Dieu ! | [theatrical](#s-theatrical) | renvois contextualisés |
| [708](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L708) | Son of a gun! | Petit filou ! / Sacré numéro ! — parfois simple exclamation | [rascal](#s-rascal) | renvois contextualisés |
| [709](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L709) | Son of a biscuit! | Purée ! / Nom d’un chien ! — humoristique | [theatrical](#s-theatrical), [mild_expletive](#s-mild_expletive) | sens alternatifs à désambiguïser |
| [710](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L710) | Shut the front door! | Non, c’est pas vrai ! — surprise ; détournement de shut the fuck up | [surprise](#s-surprise) | renvois contextualisés |
| [715](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L715) | Fuck you! | Va te faire foutre ! / Je t’emmerde ! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [716](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L716) | Fuck off! | Va te faire foutre ! / Casse-toi ! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [717](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L717) | Go fuck yourself! | Va te faire foutre ! / Va te faire enculer ! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [718](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L718) | Go screw yourself! | Va te faire foutre ! — généralement moins fort | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [719](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L719) | Screw you! | Je t’emmerde ! / Va te faire voir ! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [720](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L720) | Up yours! | Dans ton cul ! / Va te faire foutre ! | [dismiss_strong](#s-dismiss_strong), [up_yours](#s-up_yours) | sens alternatifs à désambiguïser |
| [721](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L721) | Kiss my ass! | Va te faire foutre ! / Tu peux toujours courir ! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [722](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L722) | Bite me! | Va te faire voir ! / Tu peux te brosser ! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [723](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L723) | Eat shit! | Va chier ! / Va te faire foutre ! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [724](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L724) | Eat shit and die! | Va crever, sale merde ! | [eat_shit_die](#s-eat_shit_die) | renvois contextualisés |
| [725](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L725) | Suck my dick! | Suce-moi la bite ! — provocation vulgaire | [suck_dick](#s-suck_dick) | renvois contextualisés |
| [726](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L726) | Suck my balls! | Suce-moi les couilles ! — provocation vulgaire | [suck_balls](#s-suck_balls) | renvois contextualisés |
| [727](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L727) | Go to hell! | Va au diable ! / Va te faire foutre ! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [728](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L728) | Get lost! | Dégage ! / Va te faire voir ! | [dismiss_mild](#s-dismiss_mild), [dismiss_strong](#s-dismiss_strong) | sens alternatifs à désambiguïser |
| [729](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L729) | Get bent! | Va te faire voir ! / Va te faire foutre ! | [dismiss_mild](#s-dismiss_mild), [dismiss_strong](#s-dismiss_strong) | sens alternatifs à désambiguïser |
| [730](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L730) | Take a hike! | Dégage ! / Va voir ailleurs ! | [dismiss_mild](#s-dismiss_mild) | renvois contextualisés |
| [731](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L731) | Get out of my face! | Dégage de devant moi ! / Lâche-moi ! | [dismiss_mild](#s-dismiss_mild), [dismiss_strong](#s-dismiss_strong) | sens alternatifs à désambiguïser |
| [732](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L732) | Get the fuck out! | Dégage, putain ! | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [733](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L733) | Get the fuck outta here! | Dégage ! ; aussi « Arrête tes conneries ! » par incrédulité | [dismiss_strong](#s-dismiss_strong) | renvois contextualisés |
| [734](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L734) | Leave me the fuck alone! | Fous-moi la paix ! | [leave_alone_strong](#s-leave_alone_strong) | renvois contextualisés |
| [735](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L735) | Back the fuck off! | Recule, putain ! / Lâche-moi ! | [back_off](#s-back_off) | renvois contextualisés |
| [736](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L736) | Get off my ass! | Lâche-moi la grappe ! / Arrête de me faire chier ! | [leave_alone](#s-leave_alone), [leave_alone_strong](#s-leave_alone_strong) | sens alternatifs à désambiguïser |
| [737](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L737) | Get off my back! | Lâche-moi les baskets ! | [leave_alone](#s-leave_alone) | renvois contextualisés |
| [738](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L738) | Shut up! | Tais-toi ! / Ferme-la ! | [shut_mild](#s-shut_mild) | renvois contextualisés |
| [739](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L739) | Shut the fuck up! | Ferme ta gueule ! | [shut_strong](#s-shut_strong) | renvois contextualisés |
| [740](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L740) | Shut your mouth! | Ferme-la ! | [shut_mild](#s-shut_mild), [mouth_shut](#s-mouth_shut) | sens alternatifs à désambiguïser |
| [741](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L741) | Shut your trap! | Ferme ton clapet ! | [mouth_shut](#s-mouth_shut) | renvois contextualisés |
| [742](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L742) | Shut your pie hole! | Ferme ton clapet ! — moqueur | [mouth_shut](#s-mouth_shut) | renvois contextualisés |
| [743](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L743) | Can it! | La ferme ! | [shut_mild](#s-shut_mild) | renvois contextualisés |
| [744](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L744) | Cut the crap! | Arrête tes conneries ! | [cut_bullshit](#s-cut_bullshit) | renvois contextualisés |
| [745](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L745) | Cut the bullshit! | Arrête tes conneries ! / Arrête ton baratin ! | [cut_bullshit](#s-cut_bullshit) | renvois contextualisés |
| [746](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L746) | Quit your bitching! | Arrête de chouiner ! / Arrête de râler ! | [stop_whining](#s-stop_whining) | renvois contextualisés |
| [747](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L747) | Stop being an asshole! | Arrête de faire ton connard ! | [stop_behaviour](#s-stop_behaviour) | renvois contextualisés |
| [748](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L748) | Don’t fuck with me! | Me cherche pas ! / Me fais pas chier ! | [stop_nuisance](#s-stop_nuisance) | renvois contextualisés |
| [749](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L749) | Don’t bullshit me! | Me raconte pas de conneries ! | [dont_bullshit_me](#s-dont_bullshit_me) | renvois contextualisés |
| [750](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L750) | Don’t give me that shit! | Me sors pas ces conneries ! | [dont_bullshit_me](#s-dont_bullshit_me) | renvois contextualisés |
| [751](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L751) | Who the fuck do you think you are? | Tu te prends pour qui, putain ? | [who_are_you](#s-who_are_you) | renvois contextualisés |
| [752](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L752) | Are you fucking kidding me? | Tu te fous de ma gueule ? | [mock_question](#s-mock_question) | renvois contextualisés |
| [753](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L753) | You’ve got to be shitting me! | C’est une blague, putain ! / Tu te fous de moi ! | [mock_question](#s-mock_question) | renvois contextualisés |
| [754](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L754) | What’s your fucking problem? | C’est quoi ton putain de problème ? | [your_issue](#s-your_issue) | renvois contextualisés |
| [755](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L755) | Fuck around and find out | Fais le malin, tu vas voir ce qui t’attend | [mess_and_find](#s-mess_and_find) | renvois contextualisés |
| [760](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L760) | Bullshit | Conneries, baratin | [bullshit](#s-bullshit) | renvois contextualisés |
| [761](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L761) | That’s bullshit | C’est des conneries | [bullshit](#s-bullshit) | renvois contextualisés |
| [762](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L762) | Horseshit | Conneries, foutaises | [bullshit](#s-bullshit) | renvois contextualisés |
| [763](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L763) | A load of crap | Un tas de conneries | [bullshit](#s-bullshit) | renvois contextualisés |
| [764](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L764) | No shit! | Sans déconner ! — surprise ou sarcasme | [sarcastic_truth](#s-sarcastic_truth) | renvois contextualisés |
| [765](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L765) | No shit, Sherlock! | Sans déconner, Sherlock ! / Merci, on avait compris ! | [sarcastic_known](#s-sarcastic_known) | renvois contextualisés |
| [766](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L766) | Holy shit, that’s good! | Putain, c’est bon ! | [appreciation](#s-appreciation) | renvois contextualisés |
| [767](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L767) | My ass! | Mon cul ! | [bullshit](#s-bullshit) | renvois contextualisés |
| [768](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L768) | Like hell! | Mon cul ! / Sûrement pas ! | [bullshit](#s-bullshit) | renvois contextualisés |
| [769](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L769) | Fuck that | Rien à foutre de ça / Ah non, merde ! — selon le contexte | [reject_this](#s-reject_this) | renvois contextualisés |
| [770](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L770) | Fuck this | J’en ai marre de ces conneries / Merde à ça | [fed_up_this](#s-fed_up_this) | renvois contextualisés |
| [771](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L771) | Fuck it | Et puis merde | [fuck_it](#s-fuck_it) | renvois contextualisés |
| [772](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L772) | Screw it | Et puis zut / Et puis merde | [fuck_it](#s-fuck_it) | renvois contextualisés |
| [773](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L773) | Fuck my life / FML | Vie de merde / VDM | [crap_life](#s-crap_life) | renvois contextualisés |
| [774](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L774) | Same shit, different day | Toujours la même merde | [same_crap](#s-same_crap) | renvois contextualisés |
| [775](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L775) | Shit happens | C’est des choses qui arrivent / Les emmerdes, ça arrive | [shit_happens](#s-shit_happens) | renvois contextualisés |
| [776](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L776) | Tough shit | Tant pis pour toi / C’est ton problème | [not_my_problem](#s-not_my_problem) | renvois contextualisés |
| [777](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L777) | Tough luck | Pas de bol — parfois sarcastique | [tough_luck](#s-tough_luck) | renvois contextualisés |
| [778](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L778) | That sucks | Ça craint / C’est nul / Ça fait chier | [bad_quality](#s-bad_quality) | renvois contextualisés |
| [779](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L779) | That blows | Ça craint / C’est de la merde | [bad_quality](#s-bad_quality) | renvois contextualisés |
| [780](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L780) | That’s fucked up | C’est tordu / C’est dégueulasse / Ça craint vraiment | [disgust](#s-disgust) | renvois contextualisés |
| [781](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L781) | You’re fucked | T’es foutu / T’es dans la merde | [screwed_you](#s-screwed_you) | renvois contextualisés |
| [782](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L782) | We’re screwed | On est foutus | [screwed_us](#s-screwed_us) | renvois contextualisés |
| [783](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L783) | I fucked up | J’ai merdé | [fuck_up](#s-fuck_up) | renvois contextualisés |
| [784](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L784) | You screwed up | T’as merdé / T’as déconné | [you_fuck_up](#s-you_fuck_up) | renvois contextualisés |
| [785](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L785) | Fuck-up — une personne | Bon à rien, personne qui foire tout | [loser](#s-loser) | renvois contextualisés |
| [786](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L786) | A fuck-up — un événement | Une grosse connerie, un ratage | [mistake](#s-mistake) | renvois contextualisés |
| [787](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L787) | A clusterfuck | Un bordel monstre, une catastrophe | [huge_mess](#s-huge_mess), [failure](#s-failure) | sens alternatifs à désambiguïser |
| [788](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L788) | A shitshow | Un merdier, un fiasco | [mess](#s-mess), [huge_mess](#s-huge_mess), [failure](#s-failure) | sens alternatifs à désambiguïser |
| [789](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L789) | A dumpster fire | Une catastrophe, un désastre complet | [huge_mess](#s-huge_mess), [failure](#s-failure) | sens alternatifs à désambiguïser |
| [790](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L790) | A shitstorm | Une déferlante d’emmerdes, une énorme polémique | [controversy](#s-controversy) | renvois contextualisés |
| [791](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L791) | A shitload | Une chiée, un putain de paquet | [huge_amount](#s-huge_amount) | renvois contextualisés |
| [792](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L792) | A fuckton | Une quantité énorme, une chiée | [huge_amount](#s-huge_amount) | renvois contextualisés |
| [793](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L793) | Not worth shit | Qui ne vaut rien, qui ne vaut pas un clou | [not_worth](#s-not_worth) | renvois contextualisés |
| [794](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L794) | You don’t know shit | Tu n’y connais que dalle | [know_nothing](#s-know_nothing) | renvois contextualisés |
| [795](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L795) | I don’t give a shit | J’en ai rien à foutre | [dont_care_strong](#s-dont_care_strong) | renvois contextualisés |
| [796](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L796) | I don’t give a fuck | Je m’en branle / J’en ai rien à foutre | [dont_care_strong](#s-dont_care_strong) | renvois contextualisés |
| [797](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L797) | I couldn’t give two shits | J’en ai strictement rien à foutre | [dont_care_strong](#s-dont_care_strong) | renvois contextualisés |
| [798](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L798) | I’m pissed | Je suis vénère / Je suis en rogne — aux États-Unis | [angry](#s-angry) | renvois contextualisés |
| [799](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L799) | I’m pissed off | J’en ai marre / Je suis furieux | [fed_up](#s-fed_up), [angry](#s-angry) | sens alternatifs à désambiguïser |
| [800](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L800) | You piss me off | Tu me fais chier / Tu m’énerves | [annoyed](#s-annoyed) | renvois contextualisés |
| [801](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L801) | I’m sick of this shit | J’en ai marre de ces conneries | [fed_up_this](#s-fed_up_this) | renvois contextualisés |
| [802](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L802) | I’m busting my ass | Je me casse le cul | [hard_work](#s-hard_work) | renvois contextualisés |
| [803](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L803) | You’re busting my balls | Tu me casses les couilles | [annoyed](#s-annoyed) | renvois contextualisés |
| [804](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L804) | He’s full of shit | Il raconte des conneries / C’est un baratineur | [he_bullshit](#s-he_bullshit) | renvois contextualisés |
| [805](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L805) | He’s talking out of his ass | Il raconte n’importe quoi sans savoir | [he_ignorant_talk](#s-he_ignorant_talk) | renvois contextualisés |
| [806](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L806) | He’s an ass | C’est un con | [he_ass](#s-he_ass) | renvois contextualisés |
| [807](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L807) | He’s being an ass | Il fait le con / Il se comporte comme un connard | [he_behaving](#s-he_behaving) | renvois contextualisés |
| [808](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L808) | You’re shitting me | Tu déconnes / Tu te fous de moi | [mock_question](#s-mock_question) | renvois contextualisés |
| [809](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L809) | I shit you not | Sans déconner / Je te jure que c’est vrai | [swear_true](#s-swear_true) | renvois contextualisés |
| [810](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L810) | That scared the shit out of me | Ça m’a foutu une de ces trouilles | [scared](#s-scared) | renvois contextualisés |
| [811](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L811) | That blew my fucking mind | Ça m’a complètement troué le cul | [profound_surprise](#s-profound_surprise) | renvois contextualisés |
| [812](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L812) | Badass | Une vraie pointure, quelqu’un de redoutable — souvent admiratif | [badass](#s-badass) | renvois contextualisés |
| [813](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L813) | Smartass | Petit malin, petit con — généralement critique | [smartass](#s-smartass) | renvois contextualisés |
| [814](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L814) | Kick-ass | Excellent, qui déchire | [excellent](#s-excellent) | renvois contextualisés |
| [815](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L815) | Half-assed | Bâclé, fait à l’arrache | [half_assed](#s-half_assed) | renvois contextualisés |
| [816](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L816) | Ass-backwards | Complètement à l’envers, fait en dépit du bon sens | [wrong_way](#s-wrong_way) | renvois contextualisés |
| [817](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L817) | Fuck all | Que dalle — davantage britannique | [nothing](#s-nothing) | renvois contextualisés |
| [818](../../../data/expressions/idioms-1.4.0/references/inventaire-fourni.txt#L818) | Jack shit | Que dalle, absolument rien | [nothing](#s-nothing) | renvois contextualisés |
