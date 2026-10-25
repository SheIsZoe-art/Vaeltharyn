# Son, corps et images — guide de construction FR / EN / Vaeltharyn

Édition **1.5.0**, 25 octobre 2026. Créateur : **SheIsZoe**. [English](en/25_Son_corps_et_images.md).

Cette extension traite la [liste fournie](complements/son-corps-images-1.5.0/references/source_utilisateur.txt) en **111 fiches contextualisées**, avec **15 entrées lexicales supplémentaires : huit racines et sept composés**. Le corpus courant atteint **65 041 entrées**, **65 038 graphies** et **6 538 verbes**. Les 65 026 entrées antérieures sont conservées dans tous leurs champs.

Les propositions sont utilisables dans les traductions demandées mais ne sont pas présentées comme validées individuellement par le créateur. Les contrôles portent sur l'écrit ; aucune écoute chantée n'est revendiquée. Ce guide fournit des constructions, pas une nouvelle chanson.

## Construire avant de créer

Un mot absent d'une recherche ne prouve pas une lacune : **korthir**, retrouvé dans les deux éditions, signifie déjà fréquence physique. Le candidat `frekven` a donc été rejeté. `Thaemgrael`, `tibon`, `kaenkar`, `hodhok`, `brakuk`, `vaemil` et `vrimyth` sont également réutilisés.

Les nouvelles racines techniques sont des adaptations déclarées : `synth`, `klavir`, `konsol`, `paed`, `transistor`, `kikoe`, `snaer`. La racine anatomique `saevron` est originale, sans étymologie fictive. Les composés utilisent l'ordre déterminant–noyau, avec trait d'union obligatoire et flexion seulement à droite. `Kaeneth-dolgik` emploie le nom d'action régulier de `kaenar` comme premier élément.

Les emprunts ne suivent pas la prononciation anglaise par défaut : `synth` /synθ/, `paed` /pæːd/, `snaer` /snæːr/. `Saevron` /ˈsæː.vrɔn/ et `klavir` /ˈkla.vir/ ont deux syllabes. L'accent des racines reste initial ; les composés portent un accent secondaire sur leur second élément. Les formes longues servent les passages descriptifs ; une relative claire vaut mieux qu'un composé artificiel accumulant quatre racines.

## Distinctions de sens à préserver

- `potul` est un porte-clefs, pas un clavier musical ; `gigik` une protection hygiénique, pas un pad de musique ; `detaes` une nappe de table.
- `vekath` est une chambre de bateau, `themin` une demeure. L'habitacle automobile reçoit une définition précise, sans changer ces mots.
- `korthir` est la fréquence physique ; `fanun` la répétition régulière. Le timbre n'est ni le volume ni une seule fréquence ; `foelas` est une cloche. L'anglais **timber** est ici corrigé en **timbre**, suivant la précision sur la voix.
- Un `pad` physique déclenche ; une `nappe` sonore dure. Un `808` peut être une machine ou un son de grosse caisse : expliciter le second sens. **TR-606 reste un nom de modèle ; “six hundred six transistors” est un nombre littéral, pas sa fiche technique.**
- `fulan` n'est pas réemployé pour une imagination érotique ordinaire. `Maev-sityn` ne porte aucun diagnostic ; `braeltyner` précise l'érotisme lorsque nécessaire.
- `divine` admiratif peut être merveilleux ; `skaedhydaer` implique une divinité. `Complice` ne devient pas automatiquement criminel. `Innocence` comme ingénuité et absence de culpabilité restent distinctes.
- `unforgotten` décrit ce qui n'a pas été oublié ; `slolnodoel` décrit ce qu'on ne peut oublier. `Shared embrace` ne signifie pas une étreinte divisée pour distribution. `Only` ne disparaît pas : une condition nécessaire permet de conserver sa restriction sans nouvelle règle de focus improvisée.

## Grammaire et métaphores

`Gegani inu naelraeren` conserve le commencement et le sujet pluriel ; `sul khar sul transistori` conserve 606 et le pluriel. Les deux termes après `bri` portent le locatif. Les participes passifs proviennent de verbes transitifs et ne remplacent jamais un verbe personnel dans une relative.

Les images de velours, de tonnerre, de géants, d'un monde flou ou d'une mémoire figée restent des **métaphores déclarées**. Elles n'ajoutent pas une propriété physique, un diagnostic ou une histoire culturelle à la définition d'un lemme. Une reformulation par disparition est proposée quand “sweep away” ou “dissolve” emploierait un verbe matériel inadéquat.

Les fiches sont des modèles, pas des remplacements aveugles. Les pronoms `mi`, `min` ou `se` d'un exemple doivent suivre les acteurs du texte réel. Pour **mine**, il faut retrouver le nom possédé : nom + `mi-en`. Le schéma entre chevrons de la fiche exchange_mine est à compléter ; ses emplacements ne sont pas des mots vaeltharyn. “Waiting height”, “grant what was never meant to be”, “plain” et “conditions” demandent le vers complet pour fixer exactement leur lecture. Les notes indiquent les hypothèses choisies.

## Retrouver une construction

Depuis la racine du dépôt, la recherche commune retrouve les entrées et les fiches de toutes les extensions disponibles :

```text
python scripts/chercher_corpus.py --root . --lang en "keyboard pad" "harmonic frequency" "synthesizer"
python scripts/chercher_corpus.py --root . --lang fr --contains "taille"
python scripts/chercher_corpus.py --root . --lang vh "saevron"
```

Lire le champ `fichier_complement`, la rétrotraduction et les notes avant de choisir une formulation. Un schéma marqué `schema_a_completer` n'est pas une traduction prête à chanter. Les recherches restent en lecture seule.

## Quinze entrées lexicales

### synth

`n` · /synθ/ · synth

**FR :** Instrument ou dispositif électronique qui produit et façonne des sons par synthèse ; synthé est un renvoi au même lemme.

**EN:** An electronic instrument or device that generates and shapes sounds by synthesis; synth is an alias of the same lemma.

Formation : emprunt technique adapté de synth, y prononcé /y/ et th /θ/.

### klavir

`n` · /ˈkla.vir/ · kla·vir

**FR :** Ensemble de touches permettant de jouer des notes ou de piloter un instrument musical. Ne désigne ni un porte-clefs ni tout clavier informatique.

**EN:** A set of keys used to play notes or control a musical instrument; neither a key ring nor every computer keyboard.

Formation : emprunt adapté du français clavier ; le groupe consonantique kl et les voyelles restent canoniques.

### konsol

`n` · /ˈkɔn.sɔl/ · kon·sol

**FR :** Ensemble de commandes et de surfaces de contrôle d'un véhicule ou d'un appareil ; le complément précise console automobile ou musicale. Distinct du support architectural dharok.

**EN:** A control assembly for a vehicle or device; a complement specifies automotive or musical use. Distinct from an architectural bracket.

Formation : emprunt adapté de console, c remplacé par k, sans lettre muette.

### paed

`n` · /pæːd/ · paed

**FR :** Son ou texture de synthèse tenu dans la durée, souvent utilisé comme fond harmonique. Ne désigne pas le coussinet physique qui déclenche une note.

**EN:** A sustained synthesized sound or texture, often used as a harmonic background; not the physical pad used to trigger a note.

Formation : emprunt spécialisé adapté de pad ; ae est une seule voyelle longue.

### transistor

`n` · /ˈtran.sis.tɔr/ · tran·sis·tor

**FR :** Composant semi-conducteur utilisé notamment pour amplifier ou commuter des signaux électriques. Ne désigne pas par défaut un poste de radio.

**EN:** A semiconductor component used, among other purposes, to amplify or switch electrical signals; not by default a portable radio.

Formation : emprunt international conservé, prononcé avec les valeurs vaeltharyn des lettres.

### kikoe

`n` · /ˈki.kœː/ · ki·koe

**FR :** Percussion de grosse caisse ; dans le contexte d'une boîte à rythmes, son électronique qui la représente. Ne désigne pas un coup de pied donné à une personne.

**EN:** The musical bass drum; in a drum-machine context, the electronic sound representing it. Not a kick delivered to a person.

Formation : emprunt adapté de kick avec finale vocalique propre au vaeltharyn ; aucun suffixe productif oe n’est postulé.

### snaer

`n` · /snæːr/ · snaer

**FR :** Tambour à timbres de caisse claire ; en synthèse, son qui en représente le rôle. Ne désigne pas un piège ni le timbre d'une voix.

**EN:** A snare drum, or in synthesis a sound representing its role; not a trap or a voice's timbre.

Formation : emprunt adapté de snare ; sn initial et ae long respectent la phonologie.

### saevron

`n` · /ˈsæː.vrɔn/ · sae·vron

**FR :** Partie du tronc située entre le bas des côtes et les hanches, notamment l'endroit où les mains peuvent entourer le corps. Ne désigne ni la stature ni une manière de couper.

**EN:** The part of the trunk between the lower ribs and hips, including where hands may encircle the body; neither stature nor a cutting method.

Formation : racine originale indépendante, choisie pour deux syllabes chantables ; aucune fausse dérivation de saev n'est revendiquée.

### methuv-lymdhaev

`n` · /ˈmɛ.θuvˌlym.ðæːv/ · me·thuv-lym·dhaev

**FR :** Espace intérieur d'un véhicule destiné au conducteur et aux occupants, distinct de la zone de chargement. Le génitif dhalruthen précise un camion.

**EN:** The vehicle interior intended for the driver and occupants, distinct from cargo space; dhalruthen specifies a truck.

Formation : composition nominale véhicule + intérieur, spécialisation explicitement définie.

### kaeneth-dolgik

`n` · /ˈkæː.nɛθˌdɔl.gik/ · kae·neth-dol·gik

**FR :** Surface de commande que l'on touche ou frappe pour déclencher ou contrôler un événement musical ; distinct d'une nappe sonore paed.

**EN:** A control surface touched or struck to trigger or control a musical event; distinct from a pad sound, paed.

Formation : nom d'action kaeneth issu de kaenar + nom dolgik, toucher + surface.

### thrylkim-molpyv

`n` · /ˈθryl.kimˌmɔl.pyv/ · thryl·kim-mol·pyv

**FR :** Qualité perceptive qui aide à distinguer des sons de même hauteur et intensité, liée notamment à leur spectre et à leur évolution temporelle ; le génitif thaemen précise la voix.

**EN:** The perceptual quality helping distinguish sounds of the same pitch and intensity, related to spectrum and temporal development; thaemen specifies voice.

Formation : composition son + qualité ; terme acoustique lexicalisé, non synonyme de volume ou de seule forme d'onde.

### thrylkim-braesyr

`n` · /ˈθryl.kimˌbræː.syr/ · thryl·kim-brae·syr

**FR :** Bande servant de support à un enregistrement sonore ; poemnaes précise une bande magnétique. Ne désigne pas un simple ruban textile.

**EN:** A strip serving as a medium for recorded sound; poemnaes specifies magnetic tape. Not simply a textile ribbon.

Formation : composition son + bande, fonction d'enregistrement explicitement lexicalisée.

### maev-sityn

`n` · /ˈmæːvˌsi.tyn/ · maev-si·tyn

**FR :** Image, scène ou scénario construit dans l'imagination ; peut être érotique si l'adjectif braeltyner ou le contexte le précise. Aucun trouble perceptif n'est impliqué.

**EN:** An imagined image, scene or scenario; erotic only when braeltyner or the context specifies it. No perceptual disorder is implied.

Formation : composition imagination + fiction ; sens non pathologique explicitement défini.

### rydhem-fythiv

`n` · /ˈry.ðɛmˌfy.θiv/ · ry·dhem-fy·thiv

**FR :** Action ou contrepartie convenue dans un jeu, notamment après une défaite ; ne désigne ni une sûreté de dette ni une peine légale. Une contrepartie affective doit être explicitée par le contexte.

**EN:** An agreed task or forfeit in a game, especially after losing; neither collateral for debt nor a legal penalty. Any affectionate exchange must be specified in context.

Formation : composition jeu + prix, emploi ludique distinct du gage financier sanuk.

### graelven-thavrel

`n` · /ˈgræːl.vɛnˌθa.vrɛl/ · grael·ven-tha·vrel

**FR :** Seuil et espace d'entrée domestique protégés par un toit ; ne suppose ni temple ni palais, ni nécessairement un escalier extérieur.

**EN:** A roofed domestic threshold and entrance space; implies neither a temple nor a palace, nor necessarily an exterior staircase.

Formation : composition toit + seuil, définition architecturale explicite.

## 1. Technologies et son

### truck_cabin

**Source :** truck cabin (vehicle interior)

**Vaeltharyn :** methuv-lymdhaev dhalruthen

**FR :** habitacle du camion

**EN :** truck occupant compartment

Le génitif précise le camion ; pas la chambre de bateau vekath ni la cargaison.

### highway

**Source :** highway

**Vaeltharyn :** throelev

**FR :** autoroute

**EN :** motorway

Lecture autoroutière ; une route ordinaire reste varethgrel.

### lane

**Source :** lane

**Vaeltharyn :** hodhok

**FR :** voie de circulation automobile

**EN :** vehicle traffic lane

Sens précis déjà présent, pas un sentier ni une digue.

### speaker

**Source :** speaker (audio)

**Vaeltharyn :** thaemgrael

**FR :** haut-parleur

**EN :** loudspeaker

Ne pas employer un nom de personne qui parle ni piltyn, enceinte architecturale.

### wheel

**Source :** steering wheel

**Vaeltharyn :** tibon

**FR :** volant de direction

**EN :** steering wheel

Le nom tibon, pas skosaev qui signifie capable de voler.

### leather

**Source :** leather (as material of the wheel)

**Vaeltharyn :** tibon kaenkaren

**FR :** volant en cuir

**EN :** leather steering wheel

Génitif de matière ; kaenkar nomme le cuir, sans propriété sonore nouvelle.

### console

**Source :** console (car dashboard/console)

**Vaeltharyn :** konsol methuven

**FR :** console du véhicule

**EN :** vehicle control console

Dharok reste un support architectural ; le contexte distingue console centrale et tableau de bord.

### tr606

**Source :** TR-606

**Vaeltharyn :** TR-606

**FR :** modèle TR-606

**EN :** TR-606 model name

Conserver le modèle ; le nom ne signifie pas six cent six transistors.

### tr808

**Source :** 808

**Vaeltharyn :** TR-808 ; kikoe TR-808-en

**FR :** TR-808 ; grosse caisse de la TR-808

**EN :** TR-808; TR-808 bass drum

808 peut désigner la machine ou son son de grosse caisse : expliciter la seconde lecture.

### sub_bass

**Source :** sub-bass

**Vaeltharyn :** thrylkim ya korthir se-en vele sha dhorv

**FR :** son dont la fréquence est très basse

**EN :** sound whose frequency is very low

Pas la gravité d'une situation ni automatiquement une ligne de basse. Dhorv qualifie ici une grandeur basse sur une échelle.

### hihat

**Source :** hi-hat

**Vaeltharyn :** broedutun ; thrylkim broedutunen

**FR :** charleston ; son de charleston

**EN :** hi-hat; hi-hat sound

Le génitif permet le son synthétisé sans redéfinir silencieusement l'instrument physique.

### kick

**Source :** kick

**Vaeltharyn :** kikoe

**FR :** grosse caisse musicale

**EN :** musical bass drum or kick

Sens musical explicite ; jamais un coup de pied dans cette fiche.

### snare

**Source :** snare

**Vaeltharyn :** snaer

**FR :** caisse claire musicale

**EN :** snare drum

Sens musical, pas piège ; le son de machine peut être thrylkim snaeren.

### synth

**Source :** synth / synthesizer

**Vaeltharyn :** synth

**FR :** synthétiseur

**EN :** synthesizer

Les deux formes anglaises renvoient à une seule entrée.

### keyboard

**Source :** keyboard pads — musical keyboard reading

**Vaeltharyn :** klavir ; paedi klaviren

**FR :** clavier musical ; nappes du clavier

**EN :** musical keyboard; keyboard pad sounds

Si pads signifie nappes sonores, employer paed ; ne pas supposer cette lecture pour des touches physiques.

### keyboard_hardware

**Source :** keyboard pads — physical controls reading

**Vaeltharyn :** kaeneth-dolgiki klaviren

**FR :** pads physiques du clavier

**EN :** physical keyboard pads

Surface de déclenchement, pas son tenu ; gigik garde son sens de protection hygiénique.

### transistor

**Source :** transistor

**Vaeltharyn :** transistor

**FR :** transistor électronique

**EN :** electronic transistor

Composant, pas poste de radio.

### tape

**Source :** ribbon / tape (recording medium)

**Vaeltharyn :** thrylkim-braesyr poemnaes

**FR :** bande magnétique d'enregistrement sonore

**EN :** magnetic audio recording tape

Fraerkem désigne un ruban textile ; ne pas transférer automatiquement tous ses emplois.

### resonance

**Source :** acoustic resonance

**Vaeltharyn :** tynoer kremlyk

**FR :** résonance acoustique

**EN :** acoustic resonance

Distinguer résonance, réverbération, simple écho et synthèse ; ne pas créer un doublon de tynoer.

### harmonic_frequency

**Source :** harmonic frequency

**Vaeltharyn :** korthir goesumen

**FR :** fréquence d'une harmonique

**EN :** frequency of a harmonic

Goesum a déjà le sens physique d'harmonique. Fikodhav seul, relatif à l'harmonie, n'impose pas un multiple entier.

### oscillate

**Source :** oscillate

**Vaeltharyn :** keposar ; dhoetinar

**FR :** osciller ; vibrer

**EN :** oscillate; vibrate

Keposar couvre l'aller-retour ; dhoetinar la vibration. Le choix dépend de ce qui oscille.

### velvet_air

**Source :** velvet air (as sound-design metaphor)

**Vaeltharyn :** kimuk kragaevilen

**FR :** air de velours

**EN :** velvet air

Génitif de matière employé comme image tactile et sonore ; pas une mesure acoustique ni un gaz nouveau.

## 2. Gestes et corps

### grip

**Source :** grip (firm hand on the wheel)

**Vaeltharyn :** Thim bropaeke tibon.

**FR :** Une main agrippe le volant.

**EN :** A hand firmly grips the wheel.

Bropaekar porte déjà la fermeté de la prise ; ne pas confondre avec serrer au sens ranger.

### wrap

**Source :** wrap around (the cabin wrapping us)

**Vaeltharyn :** Methuv-lymdhaev pedyse min.

**FR :** L'habitacle nous entoure.

**EN :** The cabin surrounds us.

Pedysar conserve l'enveloppement spatial ; dulaelar ferait intervenir une enveloppe matérielle.

### lift

**Source :** lift / lift me to the waiting height

**Vaeltharyn :** Haelkara mi to braepavath haelv ya mi vaenem.

**FR :** Soulève-moi vers la position haute que j'attends.

**EN :** Lift me towards the high position I am waiting for.

Waiting height est personnifiant et incomplet hors du vers ; ici c'est la personne qui attend la position, pas une altitude géographique.

### secure

**Source :** secure (hands securing the waist)

**Vaeltharyn :** Thimi fraerfysen saevron.

**FR :** Des mains maintiennent la taille.

**EN :** Hands hold the waist securely.

Fraerfysar signifie tenir ferme et fixe ; aucune possession ni intention supplémentaire n'est déduite.

### waist

**Source :** waist

**Vaeltharyn :** saevron

**FR :** taille anatomique

**EN :** anatomical waist

Distinct de doebyn, manière de couper, et de la stature.

### suspended

**Source :** suspend / suspended high

**Vaeltharyn :** Mi velem toebivun e braepavath haelv.

**FR :** Je suis suspendu dans une position haute.

**EN :** I am suspended in a high position.

Passif du transitif toebivar. Une personne simplement soulevée et soutenue peut être thritolun, sans point d'attache supposé.

### height

**Source :** height (waiting height)

**Vaeltharyn :** dhobov ; braepav haelv

**FR :** élévation ; position haute

**EN :** height; high position

Fakun est une dimension de base à sommet ; thynek une altitude par rapport à la mer. Aucun des deux n'est automatiquement une hauteur de rencontre.

### porch_lights

**Source :** porch lights / shine (porch)

**Vaeltharyn :** Aeluni graelven-thavrelen aelunen.

**FR :** Les lumières de l'entrée couverte brillent.

**EN :** The porch lights shine.

Entrée domestique couverte par un toit ; pas obligation de temple, palais ou escalier.

### sleeve

**Source :** sleeve (touch the sleeve)

**Vaeltharyn :** Kaena gorrov.

**FR :** Touche la manche du vêtement.

**EN :** Touch the sleeve.

Gorrov est le nom de vêtement ; faemim est un adjectif d'insulte.

### fingers

**Source :** finger(s)

**Vaeltharyn :** brakuk ; brakuki

**FR :** doigt ; doigts

**EN :** finger; fingers

Pluriel régulier en i, pas nouvelle racine.

### lips

**Source :** lip(s) (daring lips)

**Vaeltharyn :** vaemil ; vaemili dhoefyv

**FR :** lèvre ; lèvres audacieuses

**EN :** lip; daring lips

Adjectif postposé invariable ; l'audace est attribuée poétiquement aux lèvres.

### eyebrow

**Source :** eyebrow (raises)

**Vaeltharyn :** Se pulyne vrimyth si-en.

**FR :** Cette personne lève son sourcil.

**EN :** They raise their eyebrow.

Possessif réfléchi car le sujet lève son propre sourcil ; nul genre grammatical ajouté.

### smile

**Source :** smile / grin

**Vaeltharyn :** daefivan ; daefivan thar

**FR :** sourire ; large sourire

**EN :** smile; broad grin

Un grin n'est pas nécessairement un ricanement moqueur. Naemlar est le verbe sourire.

### crooked_smile

**Source :** crooked smile

**Vaeltharyn :** daefivan remnuhoer ; daefivan fraefaev

**FR :** sourire asymétrique ; sourire narquois

**EN :** asymmetric smile; knowing smirk

La forme physique et l'intention narquoise restent deux lectures distinctes ; ne pas imposer la seconde à la première.

### laughter

**Source :** laugh / laughter

**Vaeltharyn :** laethar ; pimuv

**FR :** rire, verbe ; rire, nom

**EN :** laugh, verb; laughter, noun

Le nom d'action laetheth est également productif, sans remplacer pimuv.

### secret_laughter

**Source :** secret laughter / sparks

**Vaeltharyn :** pimuv kogur ; pyreli

**FR :** rire secret ; étincelles

**EN :** secret laughter; sparks

Une image d'étincelles doit rester marquée comme image quand elle décrit le rire.

### gaze

**Source :** gaze / steady gaze

**Vaeltharyn :** throenen ; throenen kymoethyn

**FR :** regard ; regard stable

**EN :** gaze; steady gaze

La stabilité est celle de la direction et de la tenue du regard, pas un salaire fixe.

### voice_timbre

**Source :** timber (of the speaking tone) – as quality of voice

**Vaeltharyn :** thrylkim-molpyv thaemen

**FR :** timbre de la voix

**EN :** voice timbre

Timber est interprété ici comme la coquille de timbre, conformément à la précision sur la voix ; pas du bois ni la cloche foelas.

### frozen_sugar

**Source :** freeze / frozen (sugar, memory) — sugar

**Vaeltharyn :** saevmar iskiv

**FR :** sucre gelé

**EN :** frozen sugar

Lecture littérale ou image selon le vers ; ne signifie pas automatiquement sucre cristallisé ou caramel durci.

### frozen_memory

**Source :** freeze / frozen (sugar, memory) — memory

**Vaeltharyn :** nael poekekun

**FR :** mémoire immobilisée

**EN :** memory held still

Participe passif de poekekar, immobiliser ; évite de prétendre congeler chimiquement un souvenir.

## 3. Nuances et images

### daydream

**Source :** daydream

**Vaeltharyn :** pofer

**FR :** rêverie éveillée

**EN :** daydream

L'état de rêverie existe ; ne pas employer vrofoesar, sommeil inquiet, pour toute rêverie éveillée.

### force

**Source :** force (undeniable force)

**Vaeltharyn :** fukel thrugak ; vael-fukel thrugak

**FR :** force indéniable ; force indéniable du désir

**EN :** undeniable strength; undeniable force of desire

Fukel a d'abord le sens de vigueur ; le composé de désir explicite l'image affective sans force physique mesurée.

### yield

**Source :** yield (yields toward)

**Vaeltharyn :** Se kedhoeke to mi-ath.

**FR :** Cette personne se penche vers moi.

**EN :** They lean towards me.

Lecture corporelle de yields toward. Si le sens est abandonner une résistance, employer felhukar thranurer ; les deux actes ne sont pas identiques.

### surface

**Source :** surface (shadows surface)

**Vaeltharyn :** Thyri gynoeken.

**FR :** Les ombres apparaissent.

**EN :** Shadows emerge into view.

Le verbe devenir visible convient ; ne pas ajouter une montée depuis un liquide.

### crowded_room

**Source :** crowded room

**Vaeltharyn :** sitik brifuth

**FR :** salle bondée

**EN :** crowded reception room

Sitik est une pièce ouverte aux visiteurs ; une chambre privée demande un autre nom. Pas thimgov, atelier de foulage.

### unspoken_intentions

**Source :** unspoken intentions

**Vaeltharyn :** gegani trymdhael

**FR :** intentions tacites

**EN :** unspoken intentions

Tacite n'est pas automatiquement mensonger ni inaccessible à toute compréhension.

### bloom

**Source :** bloom (intentions begin to bloom)

**Vaeltharyn :** Gegani inu naelraeren.

**FR :** Les intentions commencent à fleurir.

**EN :** Intentions begin to bloom.

Inu marque le commencement ; le sujet pluriel impose en. Éclore d'un œuf n'est pas substitué automatiquement.

### teasing_line

**Source :** accidental teasing line

**Vaeltharyn :** krimsuk thrisav ya dhyhune min

**FR :** énoncé involontaire qui nous fait badiner

**EN :** an accidental teasing remark

Krimsuk signifie ce qui est énoncé ; tharel serait seulement un mot. Dhyhunar garde le badinage sans agressivité obligatoire.

### hidden_wishes

**Source :** unveil / hidden wishes

**Vaeltharyn :** Dhynmuna morhemi kaervil.

**FR :** Révèle les souhaits cachés.

**EN :** Reveal the hidden wishes.

Dhynmunar signifie révéler une chose secrète ; budirar vise d'abord le retrait d'un voile physique.

### divine_gaze

**Source :** divine (gaze divine)

**Vaeltharyn :** throenen vrelloen

**FR :** regard merveilleux

**EN :** a wonderful gaze

Lecture admirative de divine ; skaedhydaer est réservé au lien réel avec une divinité. Ne pas sacraliser sans contexte.

### accomplices

**Source :** accomplice(s)

**Vaeltharyn :** toemul ; toemuli

**FR :** comparse ; comparses

**EN :** accomplice; accomplices

Ne pas imposer thykel, adjectif lié à un crime, à une connivence romantique.

### dark

**Source :** dark (out into the dark)

**Vaeltharyn :** fra aelunath to duraenath

**FR :** hors de la lumière vers l'obscurité

**EN :** out of the light into the dark

Le départ est ici la lumière ; un lieu réel de départ peut remplacer aelun. Duraen ne signifie pas automatiquement nuit.

### restless_curiosity

**Source :** restless curiosity

**Vaeltharyn :** naivmael ya nu vaele momlaevar saerv

**FR :** curiosité qui ne veut pas rester calme

**EN :** curiosity that will not stay quiet

Le refus est attribué à la curiosité comme image ; ne pas transformer cela en diagnostic d'agitation.

### world_noise

**Source :** worldly noise

**Vaeltharyn :** koemmas mithilaken

**FR :** bruit du monde

**EN :** worldly noise

Mondain au sens haute société n'est pas imposé ; le bruit du monde peut être figuré.

### fantasies

**Source :** fantasy / fantasies (erotic/imaginative)

**Vaeltharyn :** maev-sityn ; maev-sityni braeltyner

**FR :** fantaisie imaginée ; fantasmes érotiques

**EN :** imagined fantasy; erotic fantasies

L'érotisme doit être précisé ; fulan, vision pathologique héritée, n'est pas réemployé.

### trace_space

**Source :** trace the space

**Vaeltharyn :** Roevaera frysiv.

**FR :** Trace l'espace.

**EN :** Trace the space.

Image d'un contour ou d'un trajet dessiné ; ne signifie pas localiser informatiquement une personne.

### closer

**Source :** closer

**Vaeltharyn :** mer neir

**FR :** plus proche

**EN :** closer

Groupe adjectival. Si le comparant est exprimé, ajouter ta + nom ou pronom au direct ; ne pas inventer ce comparant.

### boundaries

**Source :** boundaries

**Vaeltharyn :** slaeldomasi

**FR :** limites à ne pas franchir

**EN :** boundaries

Limites abstraites déjà disponibles ; hepoes est d'abord une frontière géographique.

### longing

**Source :** longing

**Vaeltharyn :** vael naev

**FR :** désir profond

**EN :** deep longing

L'attente et l'absence doivent être précisées si elles comptent ; vaelnael signifie nostalgie, pas tout désir.

### thunder

**Source :** stampede(s) of thunder (metaphor)

**Vaeltharyn :** foembymi grumen

**FR :** ruées de tonnerre

**EN :** stampedes of thunder

Génitif singulier de grum ; pas de chevaux ajoutés ni de défilé festif.

### hollow_chest

**Source :** hollow chest

**Vaeltharyn :** naevrel guraeraem

**FR :** poitrine creuse

**EN :** hollow chest

Guraeraem est l'adjectif de cavité ; ne pas employer un adverbe comme adjectif.

### practiced_innocence

**Source :** practiced innocence

**Vaeltharyn :** taeroek nyvaenun

**FR :** ingénuité apprise

**EN :** practiced ingenuousness

Lecture d'une manière travaillée ; tralul parle de non-culpabilité, pas de naïveté. Si l'innocence est feinte, gemkuthun l'explicite.

### test

**Source :** put to the test

**Vaeltharyn :** Se vele e vedalath.

**FR :** Cette personne est à l'épreuve.

**EN :** They are being put to the test.

Cadre d'épreuve ; le verbe kafoevar signifie tester par testament et n'est pas employé. Le test d'un objet peut être konovar.

### unanswered

**Source :** questions drift unanswered

**Vaeltharyn :** Madhysi thromnumen sen froefyl.

**FR :** Les questions flottent sans réponse.

**EN :** Questions drift without an answer.

Le flottement de liquide est une image déclarée, pas une modification du verbe nautique dériver.

### electric_space

**Source :** warm electric space

**Vaeltharyn :** frysiv nufaedhor an kraeliv

**FR :** espace chaud et électrique

**EN :** warm electric space

Température et électricité peuvent être images de tension relationnelle ; ne pas déduire un champ physique mesuré.

### dissolve_hesitation

**Source :** dissolve hesitation

**Vaeltharyn :** Trukoem grypeke.

**FR :** L'hésitation disparaît.

**EN :** Hesitation dissolves away.

Le verbe dissoudre un organisme n'est pas détourné ; la disparition conserve ici le résultat affectif.

### shared_embrace

**Source :** shared embrace

**Vaeltharyn :** kraevetol min-en

**FR :** notre étreinte

**EN :** our shared embrace

Possession commune en contexte ; metothar, diviser pour distribuer, ferait un contresens.

### reluctant

**Source :** reluctant to surrender

**Vaeltharyn :** Mi nu vaelem felhukar thranurer si-en.

**FR :** Je ne veux pas abandonner ma résistance.

**EN :** I am reluctant to relinquish my resistance.

La personne grammaticale vient de l'exemple ; le pronom doit suivre le texte réel. Ne pas employer skimfaes pour toute réticence à agir.

### already_divine

**Source :** already feels divine

**Vaeltharyn :** Mi gedaenem dhais dhe se vele vrelloen.

**FR :** Je sens déjà que c'est merveilleux.

**EN :** It already feels wonderful to me.

Lecture affective et admirative ; pas une affirmation de divinité. Dhais est l'adverbe déjà.

### captivated

**Source :** captivated

**Vaeltharyn :** Mi velem gokevun.

**FR :** Je suis captivé.

**EN :** I am captivated.

Participe passif d'un transitif ; ne signifie pas retenu physiquement prisonnier.

### peculiar_comfort

**Source :** peculiar comfort

**Vaeltharyn :** graedoen gaebyk

**FR :** réconfort singulier

**EN :** peculiar comfort

Réconfort qui ne ressemble pas aux autres ; aucun jugement pathologique.

### unknown_before

**Source :** never previously known

**Vaeltharyn :** Thirkaeris mi nu ranoelhikem ith graedoen.

**FR :** Auparavant, je n'avais pas connu ce réconfort.

**EN :** I had never known this comfort before.

Le référent réconfort est fourni par le voisinage de la liste ; le remplacer selon le texte complet.

### reckless_courage

**Source :** sudden reckless courage

**Vaeltharyn :** vaethun bohom an dhavil

**FR :** courage soudain et téméraire

**EN :** sudden reckless courage

L'imprudence est conservée, pas remplacée par un simple compliment héroïque.

### sweep_uncertainty

**Source :** sweep uncertainty away

**Vaeltharyn :** Hirlum grypeke.

**FR :** L'incertitude s'efface.

**EN :** Uncertainty is swept away.

La disparition conserve le résultat ; vryfaemar exige le nettoyage au balai dans son sens hérité. Une image littérale de balayage peut être explicitement choisie.

### bold_conditions

**Source :** bold conditions

**Vaeltharyn :** thrirdhithi dhoefyv

**FR :** exigences audacieuses

**EN :** bold requirements

Conditions prises comme exigences négociées. Pour une condition logique, construire ir + proposition ; gribaefem signifie état ou nature.

### daring_demand

**Source :** daring demand / demanding

**Vaeltharyn :** thrirdhith dhoefyv ; hythikar

**FR :** exigence audacieuse ; exiger

**EN :** a daring demand; demand

Hehon vise une habitude d'exiger beaucoup, pas la simple demande de cette scène.

### sweet_forfeit

**Source :** sweet forfeit

**Vaeltharyn :** rydhem-fythiv gytyr

**FR :** gage de jeu agréable

**EN :** a sweet playful forfeit

Sweet exprime ici l'agrément, pas obligatoirement du sucre ou une matière douce au toucher.

### exchange_mine

**Source :** exchange for mine

**Vaeltharyn :** Ir ti vaeres ⟨objet reçu⟩ mi-or, mi vaerem ⟨objet donné⟩ ti-or.

**FR :** Si tu me donnes X, je te donne Y.

**EN :** If you give me X, I give you Y.

Mine exige son antécédent : reprendre le nom + mi-en. Les chevrons sont des emplacements, pas des mots vaeltharyn ; ne pas inventer un baiser comme référent.

### amused_pause

**Source :** amused & calculating pause

**Vaeltharyn :** vroloek, ko thalen mumpikothun an pomul

**FR :** pause, avec une personne amusée et calculatrice

**EN :** a pause, with someone amused and calculating

Le plaisir et le calcul portent sur la personne, pas littéralement sur une durée ; aucune intention malveillante ajoutée.

### inspect_plea

**Source :** inspect the brazen plea

**Vaeltharyn :** Faenlatha nydem dipir.

**FR :** Examine la requête effrontée.

**EN :** Inspect the brazen plea.

Nydem peut être une demande ordinaire ; saelith n'impose pas une prière religieuse ici.

### grant_unmeant

**Source :** grant what was never meant to be

**Vaeltharyn :** Kihoma skoendhoem ya min nu ravaelom.

**FR :** Accorde ce que nous n'avions pas voulu.

**EN :** Grant what we had not intended.

Lecture d'intention antérieure, pas destin cosmique ni interdiction universelle. Si meant signifie prévu ou permis, choisir trupukar ou thrusirar dans une autre proposition.

### long_awaited

**Source :** long-awaited

**Vaeltharyn :** skoendhoem ya mi ravaenem thirvaris

**FR :** chose que j'ai attendue longtemps

**EN :** a long-awaited thing

Thirvaris est l'adverbe longtemps déjà enregistré ; la relative précise l'agent de l'attente.

### unexpected_peace

**Source :** unexpected peace

**Vaeltharyn :** saerun doeboes

**FR :** paix inattendue

**EN :** unexpected peace

Pas une propriété permanente de la personne ni une paix religieuse ajoutée.

### nothing_same

**Source :** nothing stays the same

**Vaeltharyn :** Nul skoendhoem momlaeve grygel.

**FR :** Rien ne reste identique.

**EN :** Nothing stays the same.

Nul quantifie le nom ; la négation n'est pas posée devant un groupe nominal avec nu.

### ancient_boundaries

**Source :** ancient boundaries fall away

**Vaeltharyn :** Slaeldomasi vaenal grypeken.

**FR :** Les anciennes limites disparaissent.

**EN :** Ancient boundaries fall away.

Des limites relationnelles, pas automatiquement des frontières d'État. L'idée de chute physique peut être ajoutée comme image explicite.

### no_innocence_return

**Source :** no return to innocence

**Vaeltharyn :** Nul thrudhun to taeroekath.

**FR :** Aucun retour vers l'ingénuité.

**EN :** No return to innocence.

Innocence lue comme ingénuité ; tralul convient si le texte parle réellement de culpabilité.

### polite_truths

**Source :** polite truths

**Vaeltharyn :** thaevi maerunvaerva

**FR :** vérités de politesse

**EN :** polite truths

Maerunvaer + va, adjectif relatif à la politesse ; krekom veut dire lisse, pas poli socialement.

### between_laughter_certainty

**Source :** suspended between laughter and the certainty untold

**Vaeltharyn :** Se vele toebivun bri pimuvath an runkusath ya min nu pipyrom.

**FR :** Cela est suspendu entre le rire et une certitude que nous n'avouons pas.

**EN :** It is suspended between laughter and a certainty we leave unspoken.

Les deux noms après bri prennent le locatif. La relative a un sujet et un verbe personnel ; le sujet réel doit remplacer min si nécessaire.

### chapter

**Source :** watch a new chapter gradually unfold

**Vaeltharyn :** Mira dhe kenur naiv gynoeke grihak.

**FR :** Regarde un nouveau chapitre apparaître peu à peu.

**EN :** Watch a new chapter gradually unfold.

Chapitre de vie explicite comme image ; l'apparition ne force pas à déplier matériellement un livre.

### dancing_giants

**Source :** dancing giants (in the chest)

**Vaeltharyn :** Sykimi kaenraeren e naevrelath mi-en.

**FR :** Des géants dansent dans ma poitrine.

**EN :** Giants dance in my chest.

Géants imaginés ; le pluriel impose en au verbe. Le possesseur suit le nom fléchi.

### never_same

**Source :** never quite the same

**Vaeltharyn :** Nesoen, vethen gylgoesykath, se nu vivele sloehil grygel.

**FR :** Ensuite, à chaque instant, cela ne sera pas tout à fait identique.

**EN :** Afterwards, it will never be quite the same.

Vethen + moment au locatif conserve la portée de never ; la phrase est un modèle explicite, à raccourcir seulement si le contexte porte déjà cette durée.

## 4. Expressions complémentaires

### family_gathering

**Source :** family gathering / polite discussions

**Vaeltharyn :** lyrven nayren ; roenaemi maerunvaerva

**FR :** rencontre familiale ; discussions de politesse

**EN :** family gathering; polite discussions

Une rencontre de famille, pas une réunion de morceaux séparés. La politesse n'est pas le poli d'une surface.

### imagined_shadows

**Source :** weeks of imagined shadows

**Vaeltharyn :** saunreli, ko thyri skethithun

**FR :** des semaines, avec des ombres imaginées

**EN :** weeks with imagined shadows

La durée relationnelle et l'agent imaginant dépendent du vers ; le groupe n'est pas déclaré comme un composé nouveau.

### unhurried_grin

**Source :** unhurried grin appears

**Vaeltharyn :** Daefivan saerv gynoeke naevris.

**FR :** Un sourire calme apparaît lentement.

**EN :** An unhurried grin appears.

Lenteur et calme sans négligence ni apathie déduites ; satath n'est pas imposé.

### guide_two

**Source :** guide two accomplices

**Vaeltharyn :** Skikyka dai toemuli.

**FR :** Guide deux comparses.

**EN :** Guide two accomplices.

Impératif à une personne ; dai demande un nom pluriel, sans créer un duel.

### soft_anthems

**Source :** melodic anthems playing softly

**Vaeltharyn :** Thrynaeki rymfuvov thaehynen faedhor.

**FR :** Des hymnes mélodiques sonnent doucement.

**EN :** Melodic anthems play softly.

Sonner musical, pas jouer un rôle ni parier. Doucement n'est pas nécessairement une vitesse lente.

### quiet_poise

**Source :** plain quiet poise

**Vaeltharyn :** throldhuth saerel an saerv

**FR :** assurance simple et calme

**EN :** plain quiet poise

Aplomb émotionnel, pas fil à plomb ; plain n'est pas la platitude physique ni nécessairement l'absence de beauté.

### replace_noise

**Source :** replace worldly noise

**Vaeltharyn :** Koemmas mithilaken grypeke; saerun gynoeke.

**FR :** Le bruit du monde disparaît ; la paix apparaît.

**EN :** Worldly noise gives way to peace.

Le remplacement d'une personne dans un emploi dhytelar n'est pas détourné. La paix est un exemple à remplacer par le vrai sujet du vers.

### destination

**Source :** arriving at the destination

**Vaeltharyn :** Min tyterom.

**FR :** Nous arrivons à destination.

**EN :** We arrive at the destination.

Le verbe porte déjà l'arrivée à destination ; davaem signifie affectation ou usage prévu, pas forcément lieu d'arrivée.

### creating_conditions

**Source :** creating bold conditions

**Vaeltharyn :** Min thaelom thrirdhithi dhoefyv.

**FR :** Nous formulons des exigences audacieuses.

**EN :** We create bold requirements.

Même lecture d'exigences que bold conditions ; une condition logique se construit par ir, sans nouveau mot automatique.

### only_lips

**Source :** only daring lips can say

**Vaeltharyn :** Ir vaemili nu velen dhoefyv, sen nu kelen lyrar se.

**FR :** Si des lèvres ne sont pas audacieuses, elles ne peuvent pas le dire.

**EN :** If lips are not daring, they cannot say it.

La restriction de only est conservée par sa condition nécessaire. Skanoem existe mais une portée de focus non définie n'est pas improvisée ; le référent de se vient du vers.

### firm_hands

**Source :** firm hands

**Vaeltharyn :** thimi filthyk

**FR :** mains fermes

**EN :** firm hands

Fermeté physique ; pour une prise ferme, employer bropaekar ou fraerfysar comme dans les fiches dédiées.

### universe_blurs

**Source :** surrounding universe blurs past

**Vaeltharyn :** Fyndhok skemuse min; se rytaeme dhoevom.

**FR :** L'univers nous dépasse ; il devient flou.

**EN :** The surrounding universe blurs past us.

Point de vue d'un véhicule en mouvement, pas une affirmation cosmologique ; aucun mélange matériel n'est impliqué.

### absolute_release

**Source :** in absolute release

**Vaeltharyn :** e vruvythath kromer

**FR :** dans un relâchement entier

**EN :** in complete release of tension

Lecture de tension qui se relâche ; nypaek convient si release signifie libération. Aucun événement corporel supplémentaire ajouté.

### six_hundred_six

**Source :** six hundred six transistors

**Vaeltharyn :** sul khar sul transistori

**FR :** six cent six transistors

**EN :** six hundred and six transistors

606 = sul khar sul. Ce compte littéral ne constitue pas une description technique de la TR-606.

### sequence

**Source :** sequence

**Vaeltharyn :** thrufon

**FR :** séquence ordonnée

**EN :** ordered sequence

Une séquence n'est pas par définition une boucle ni une répétition.

### no_repetition

**Source :** no repetition

**Vaeltharyn :** nul broedaek

**FR :** aucune répétition

**EN :** no repetition

Nul devant le nom ; pas nu devant un fragment nominal.

### lingers

**Source :** lingers

**Vaeltharyn :** Se momlaeve.

**FR :** Cela demeure.

**EN :** It lingers.

Momlaevar permet le maintien dans un état ; furrolar privilégie une persistance de volonté.

### memory_shape

**Source :** leaving the memory frozen in an unforgotten shape

**Vaeltharyn :** Nael momlaeve poekekun e remirath ya min nu rakutykom.

**FR :** La mémoire reste immobilisée dans une forme que nous n'avons pas oubliée.

**EN :** Memory remains frozen in an unforgotten shape.

Unforgotten = non oublié en fait ; slolnodoel signifierait impossible à oublier et changerait la portée. Le sujet réel doit remplacer min si nécessaire.

## Références et audit

| Référence | Point vérifié |
|---|---|
| [Roland — TR-808 technical specifications](https://support.roland.com/hc/en-us/articles/201963539-TR-808-Technical-Specifications) | Noms des parties et modèle ; aucun compte de 606 transistors n’en est déduit. |
| [Roland — T-8 sound sources including TR-606](https://support.roland.com/hc/en-us/articles/6145882578715-T-8-Can-I-change-the-sound-for-each-part) | Distinction sons de caisse claire, grosse caisse et charlestons. |
| [Roland S-1 — keyboard pads and envelope](https://static.roland.com/manuals/s-1_manual_v102/eng/87294693.html) | Pads physiques de clavier et commande de l’enveloppe, distincts d’une nappe sonore. |
| [Roland GAIA SH-01 guidebook](https://cdn.roland.com/assets/media/pdf/gaia_sh-01_guidebook.pdf) | Distinction de la nappe de synthèse ; aperçu du guide consulté, téléchargement intégral non exploité. |
| [OpenStax — Sound interference and resonance](https://openstax.org/books/physics/pages/14-4-sound-interference-and-resonance) | Fréquence propre et résonance ; ne pas confondre avec un simple écho. |
| [OpenStax — Hearing](https://openstax.org/books/college-physics-2e/pages/17-6-hearing) | Distinction entre fréquence/hauteur, niveau sonore et timbre. |
| [Texas Instruments — transistor amplifier and switch](https://www.ti.com/document-viewer/lit/html/SSZTAH9/GUID-9AFA0B17-038E-457B-8B5E-C7F89561163A) | Usages des transistors pour amplification et commutation ; pas une radio complète. |

[Entrées consultées](complements/son-corps-images-1.5.0/references/lexique_consulte.json) · [Fiches structurées](complements/son-corps-images-1.5.0/sens.json) · [Choix rejetés](complements/son-corps-images-1.5.0/contre_exemples.json) · [Bilan](complements/son-corps-images-1.5.0/bilan.json).
