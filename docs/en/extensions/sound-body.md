# Sound, body and imagery — FR / EN / Vaeltharyn construction guide

Edition **1.5.0**, 25 October 2026. Creator: **SheIsZoe**. [Français](../../fr/extensions/sound-body.md).

The [supplied list](../../../data/expressions/sound-body-1.5.0/references/source_utilisateur.txt) is handled in **111 contextual records**, adding **15 lexical entries: eight roots and seven compounds**. Current data: **65,041 entries**, **65,038 spellings**, **6,538 verbs**. All 65,026 earlier entries are preserved field for field. Additions remain unvalidated proposals; checks are written, with no claimed audio trial. This is a construction guide, not a new song.

## Construction and meaning

Search both editions before creating a term: **korthir** already denotes physical frequency, so `frekven` was rejected. Existing terms for loudspeaker, steering wheel, leather, traffic lane, fingers, lips and eyebrow are reused. The adapted technical loans are `synth`, `klavir`, `konsol`, `paed`, `transistor`, `kikoe`, `snaer`; `saevron` is an original anatomical root with no invented historical etymology. Compounds use modifier–head order and right-edge inflection.

Physical performance pads and sustained pad sounds are distinct. `Potul` means key ring, `gigik` sanitary pad, `detaes` tablecloth; ship bedroom and dwelling are not silently turned into truck cabins. Timbre is not loudness or just pitch. **Timber** is interpreted as the stated voice **timbre**. TR-606 and TR-808 retain their model names; a literal count of 606 transistors is not asserted as either device's component count.

Ordinary fantasy is not made pathological. Admiring “divine” is separated from actual divinity, romantic complicity from crime, and ingenuousness from guiltlessness. Unforgotten is not automatically unforgettable. A shared embrace is not one divided for distribution. Only is retained through a necessary-condition paraphrase rather than dropped or assigned an undefined focus rule.

Word and sentence construction keeps aspect, subject number, transitive passive formation and locative cases. Velvet air, thunder stampedes, dancing giants, a passing blurred world and frozen memory are explicitly figurative, not new scientific facts. Examples may choose a speaker or referent for illustration; the complete line must determine the actual actors. **Mine** needs its antecedent; the angle-bracket fields in exchange_mine are slots, not words. Waiting height, meant to be, plain and conditions retain context-sensitive alternatives in the notes.

## Finding a construction

From the repository root, search lemmas and context records with:

```text
python scripts/chercher_corpus.py --root . --lang en "keyboard pad" "harmonic frequency" "synthesizer"
python scripts/chercher_corpus.py --root . --lang vh "saevron"
```

Read `fichier_complement`, the back-reading and the notes. A record marked `schema_a_completer` is a template, not ready-to-sing text. Searches are read-only.

## Fifteen lexical additions

### synth

`n` · /synθ/ · synth

**FR :** Instrument ou dispositif électronique qui produit et façonne des sons par synthèse ; synthé est un renvoi au même lemme.

**EN:** An electronic instrument or device that generates and shapes sounds by synthesis; synth is an alias of the same lemma.

Formation (French annotation): emprunt technique adapté de synth, y prononcé /y/ et th /θ/.

### klavir

`n` · /ˈkla.vir/ · kla·vir

**FR :** Ensemble de touches permettant de jouer des notes ou de piloter un instrument musical. Ne désigne ni un porte-clefs ni tout clavier informatique.

**EN:** A set of keys used to play notes or control a musical instrument; neither a key ring nor every computer keyboard.

Formation (French annotation): emprunt adapté du français clavier ; le groupe consonantique kl et les voyelles restent canoniques.

### konsol

`n` · /ˈkɔn.sɔl/ · kon·sol

**FR :** Ensemble de commandes et de surfaces de contrôle d'un véhicule ou d'un appareil ; le complément précise console automobile ou musicale. Distinct du support architectural dharok.

**EN:** A control assembly for a vehicle or device; a complement specifies automotive or musical use. Distinct from an architectural bracket.

Formation (French annotation): emprunt adapté de console, c remplacé par k, sans lettre muette.

### paed

`n` · /pæːd/ · paed

**FR :** Son ou texture de synthèse tenu dans la durée, souvent utilisé comme fond harmonique. Ne désigne pas le coussinet physique qui déclenche une note.

**EN:** A sustained synthesized sound or texture, often used as a harmonic background; not the physical pad used to trigger a note.

Formation (French annotation): emprunt spécialisé adapté de pad ; ae est une seule voyelle longue.

### transistor

`n` · /ˈtran.sis.tɔr/ · tran·sis·tor

**FR :** Composant semi-conducteur utilisé notamment pour amplifier ou commuter des signaux électriques. Ne désigne pas par défaut un poste de radio.

**EN:** A semiconductor component used, among other purposes, to amplify or switch electrical signals; not by default a portable radio.

Formation (French annotation): emprunt international conservé, prononcé avec les valeurs vaeltharyn des lettres.

### kikoe

`n` · /ˈki.kœː/ · ki·koe

**FR :** Percussion de grosse caisse ; dans le contexte d'une boîte à rythmes, son électronique qui la représente. Ne désigne pas un coup de pied donné à une personne.

**EN:** The musical bass drum; in a drum-machine context, the electronic sound representing it. Not a kick delivered to a person.

Formation (French annotation): emprunt adapté de kick avec finale vocalique propre au vaeltharyn ; aucun suffixe productif oe n’est postulé.

### snaer

`n` · /snæːr/ · snaer

**FR :** Tambour à timbres de caisse claire ; en synthèse, son qui en représente le rôle. Ne désigne pas un piège ni le timbre d'une voix.

**EN:** A snare drum, or in synthesis a sound representing its role; not a trap or a voice's timbre.

Formation (French annotation): emprunt adapté de snare ; sn initial et ae long respectent la phonologie.

### saevron

`n` · /ˈsæː.vrɔn/ · sae·vron

**FR :** Partie du tronc située entre le bas des côtes et les hanches, notamment l'endroit où les mains peuvent entourer le corps. Ne désigne ni la stature ni une manière de couper.

**EN:** The part of the trunk between the lower ribs and hips, including where hands may encircle the body; neither stature nor a cutting method.

Formation (French annotation): racine originale indépendante, choisie pour deux syllabes chantables ; aucune fausse dérivation de saev n'est revendiquée.

### methuv-lymdhaev

`n` · /ˈmɛ.θuvˌlym.ðæːv/ · me·thuv-lym·dhaev

**FR :** Espace intérieur d'un véhicule destiné au conducteur et aux occupants, distinct de la zone de chargement. Le génitif dhalruthen précise un camion.

**EN:** The vehicle interior intended for the driver and occupants, distinct from cargo space; dhalruthen specifies a truck.

Formation (French annotation): composition nominale véhicule + intérieur, spécialisation explicitement définie.

### kaeneth-dolgik

`n` · /ˈkæː.nɛθˌdɔl.gik/ · kae·neth-dol·gik

**FR :** Surface de commande que l'on touche ou frappe pour déclencher ou contrôler un événement musical ; distinct d'une nappe sonore paed.

**EN:** A control surface touched or struck to trigger or control a musical event; distinct from a pad sound, paed.

Formation (French annotation): nom d'action kaeneth issu de kaenar + nom dolgik, toucher + surface.

### thrylkim-molpyv

`n` · /ˈθryl.kimˌmɔl.pyv/ · thryl·kim-mol·pyv

**FR :** Qualité perceptive qui aide à distinguer des sons de même hauteur et intensité, liée notamment à leur spectre et à leur évolution temporelle ; le génitif thaemen précise la voix.

**EN:** The perceptual quality helping distinguish sounds of the same pitch and intensity, related to spectrum and temporal development; thaemen specifies voice.

Formation (French annotation): composition son + qualité ; terme acoustique lexicalisé, non synonyme de volume ou de seule forme d'onde.

### thrylkim-braesyr

`n` · /ˈθryl.kimˌbræː.syr/ · thryl·kim-brae·syr

**FR :** Bande servant de support à un enregistrement sonore ; poemnaes précise une bande magnétique. Ne désigne pas un simple ruban textile.

**EN:** A strip serving as a medium for recorded sound; poemnaes specifies magnetic tape. Not simply a textile ribbon.

Formation (French annotation): composition son + bande, fonction d'enregistrement explicitement lexicalisée.

### maev-sityn

`n` · /ˈmæːvˌsi.tyn/ · maev-si·tyn

**FR :** Image, scène ou scénario construit dans l'imagination ; peut être érotique si l'adjectif braeltyner ou le contexte le précise. Aucun trouble perceptif n'est impliqué.

**EN:** An imagined image, scene or scenario; erotic only when braeltyner or the context specifies it. No perceptual disorder is implied.

Formation (French annotation): composition imagination + fiction ; sens non pathologique explicitement défini.

### rydhem-fythiv

`n` · /ˈry.ðɛmˌfy.θiv/ · ry·dhem-fy·thiv

**FR :** Action ou contrepartie convenue dans un jeu, notamment après une défaite ; ne désigne ni une sûreté de dette ni une peine légale. Une contrepartie affective doit être explicitée par le contexte.

**EN:** An agreed task or forfeit in a game, especially after losing; neither collateral for debt nor a legal penalty. Any affectionate exchange must be specified in context.

Formation (French annotation): composition jeu + prix, emploi ludique distinct du gage financier sanuk.

### graelven-thavrel

`n` · /ˈgræːl.vɛnˌθa.vrɛl/ · grael·ven-tha·vrel

**FR :** Seuil et espace d'entrée domestique protégés par un toit ; ne suppose ni temple ni palais, ni nécessairement un escalier extérieur.

**EN:** A roofed domestic threshold and entrance space; implies neither a temple nor a palace, nor necessarily an exterior staircase.

Formation (French annotation): composition toit + seuil, définition architecturale explicite.

## 1. Technology and sound

### truck_cabin

**Source:** truck cabin (vehicle interior)

**Vaeltharyn:** methuv-lymdhaev dhalruthen

**EN:** truck occupant compartment

**FR:** habitacle du camion

The genitive specifies the truck; not the ship bedroom vekath or cargo space.

### highway

**Source:** highway

**Vaeltharyn:** throelev

**EN:** motorway

**FR:** autoroute

Motorway reading; an ordinary road remains varethgrel.

### lane

**Source:** lane

**Vaeltharyn:** hodhok

**EN:** vehicle traffic lane

**FR:** voie de circulation automobile

The precise sense already exists; neither a footpath nor a dike.

### speaker

**Source:** speaker (audio)

**Vaeltharyn:** thaemgrael

**EN:** loudspeaker

**FR:** haut-parleur

Not a person speaking or piltyn, an architectural enclosure.

### wheel

**Source:** steering wheel

**Vaeltharyn:** tibon

**EN:** steering wheel

**FR:** volant de direction

The noun tibon, not skosaev, capable of flying.

### leather

**Source:** leather (as material of the wheel)

**Vaeltharyn:** tibon kaenkaren

**EN:** leather steering wheel

**FR:** volant en cuir

Material genitive; kaenkar names leather without a new acoustic property.

### console

**Source:** console (car dashboard/console)

**Vaeltharyn:** konsol methuven

**EN:** vehicle control console

**FR:** console du véhicule

Dharok remains an architectural bracket; context distinguishes a centre console from a dashboard.

### tr606

**Source:** TR-606

**Vaeltharyn:** TR-606

**EN:** TR-606 model name

**FR:** modèle TR-606

Preserve the model name; it does not mean six hundred and six transistors.

### tr808

**Source:** 808

**Vaeltharyn:** TR-808 ; kikoe TR-808-en

**EN:** TR-808; TR-808 bass drum

**FR:** TR-808 ; grosse caisse de la TR-808

808 can refer to the machine or its bass-drum sound: make the latter reading explicit.

### sub_bass

**Source:** sub-bass

**Vaeltharyn:** thrylkim ya korthir se-en vele sha dhorv

**EN:** sound whose frequency is very low

**FR:** son dont la fréquence est très basse

Not the seriousness of a situation or automatically a bass line. Dhorv describes a low value on a scale here.

### hihat

**Source:** hi-hat

**Vaeltharyn:** broedutun ; thrylkim broedutunen

**EN:** hi-hat; hi-hat sound

**FR:** charleston ; son de charleston

The genitive denotes the synthesized sound without silently redefining the physical instrument.

### kick

**Source:** kick

**Vaeltharyn:** kikoe

**EN:** musical bass drum or kick

**FR:** grosse caisse musicale

Explicitly musical; never a bodily kick in this record.

### snare

**Source:** snare

**Vaeltharyn:** snaer

**EN:** snare drum

**FR:** caisse claire musicale

Musical sense, not a trap; the machine sound can be thrylkim snaeren.

### synth

**Source:** synth / synthesizer

**Vaeltharyn:** synth

**EN:** synthesizer

**FR:** synthétiseur

Both English forms point to one entry.

### keyboard

**Source:** keyboard pads — musical keyboard reading

**Vaeltharyn:** klavir ; paedi klaviren

**EN:** musical keyboard; keyboard pad sounds

**FR:** clavier musical ; nappes du clavier

If pads means pad sounds, use paed; do not assume this reading for physical controls.

### keyboard_hardware

**Source:** keyboard pads — physical controls reading

**Vaeltharyn:** kaeneth-dolgiki klaviren

**EN:** physical keyboard pads

**FR:** pads physiques du clavier

A trigger surface, not a sustained sound; gigik retains its sanitary-pad sense.

### transistor

**Source:** transistor

**Vaeltharyn:** transistor

**EN:** electronic transistor

**FR:** transistor électronique

Component, not a portable radio.

### tape

**Source:** ribbon / tape (recording medium)

**Vaeltharyn:** thrylkim-braesyr poemnaes

**EN:** magnetic audio recording tape

**FR:** bande magnétique d'enregistrement sonore

Fraerkem denotes a textile ribbon; do not transfer all its uses automatically.

### resonance

**Source:** acoustic resonance

**Vaeltharyn:** tynoer kremlyk

**EN:** acoustic resonance

**FR:** résonance acoustique

Distinguish resonance, reverberation, simple echo and synthesis; do not duplicate tynoer.

### harmonic_frequency

**Source:** harmonic frequency

**Vaeltharyn:** korthir goesumen

**EN:** frequency of a harmonic

**FR:** fréquence d'une harmonique

Goesum already has the physical harmonic sense. Fikodhav alone, relating to harmony, does not impose an integer multiple.

### oscillate

**Source:** oscillate

**Vaeltharyn:** keposar ; dhoetinar

**EN:** oscillate; vibrate

**FR:** osciller ; vibrer

Keposar covers back-and-forth motion; dhoetinar vibration. Choose according to what oscillates.

### velvet_air

**Source:** velvet air (as sound-design metaphor)

**Vaeltharyn:** kimuk kragaevilen

**EN:** velvet air

**FR:** air de velours

Material genitive used as tactile and sonic imagery; neither an acoustic measure nor a new gas.

## 2. Actions and body

### grip

**Source:** grip (firm hand on the wheel)

**Vaeltharyn:** Thim bropaeke tibon.

**EN:** A hand firmly grips the wheel.

**FR:** Une main agrippe le volant.

Bropaekar already conveys a firm grip; not storing something away.

### wrap

**Source:** wrap around (the cabin wrapping us)

**Vaeltharyn:** Methuv-lymdhaev pedyse min.

**EN:** The cabin surrounds us.

**FR:** L'habitacle nous entoure.

Pedysar retains spatial surrounding; dulaelar would introduce a material wrapping.

### lift

**Source:** lift / lift me to the waiting height

**Vaeltharyn:** Haelkara mi to braepavath haelv ya mi vaenem.

**EN:** Lift me towards the high position I am waiting for.

**FR:** Soulève-moi vers la position haute que j'attends.

Waiting height is personifying and context dependent; here the person awaits the position, not a geographic altitude.

### secure

**Source:** secure (hands securing the waist)

**Vaeltharyn:** Thimi fraerfysen saevron.

**EN:** Hands hold the waist securely.

**FR:** Des mains maintiennent la taille.

Fraerfysar means hold firm and steady; no extra possession or intention is inferred.

### waist

**Source:** waist

**Vaeltharyn:** saevron

**EN:** anatomical waist

**FR:** taille anatomique

Distinct from doebyn, a cutting method, and from stature.

### suspended

**Source:** suspend / suspended high

**Vaeltharyn:** Mi velem toebivun e braepavath haelv.

**EN:** I am suspended in a high position.

**FR:** Je suis suspendu dans une position haute.

Passive of transitive toebivar. A lifted, supported person can be thritolun without an assumed attachment point.

### height

**Source:** height (waiting height)

**Vaeltharyn:** dhobov ; braepav haelv

**EN:** height; high position

**FR:** élévation ; position haute

Fakun is a base-to-top dimension; thynek an altitude above sea level. Neither automatically denotes a meeting height.

### porch_lights

**Source:** porch lights / shine (porch)

**Vaeltharyn:** Aeluni graelven-thavrelen aelunen.

**EN:** The porch lights shine.

**FR:** Les lumières de l'entrée couverte brillent.

A roofed domestic entrance; no required temple, palace or staircase.

### sleeve

**Source:** sleeve (touch the sleeve)

**Vaeltharyn:** Kaena gorrov.

**EN:** Touch the sleeve.

**FR:** Touche la manche du vêtement.

Gorrov is the garment noun; faemim is an insulting adjective.

### fingers

**Source:** finger(s)

**Vaeltharyn:** brakuk ; brakuki

**EN:** finger; fingers

**FR:** doigt ; doigts

Regular plural in i, not a new root.

### lips

**Source:** lip(s) (daring lips)

**Vaeltharyn:** vaemil ; vaemili dhoefyv

**EN:** lip; daring lips

**FR:** lèvre ; lèvres audacieuses

Postposed invariable adjective; daring is poetically attributed to lips.

### eyebrow

**Source:** eyebrow (raises)

**Vaeltharyn:** Se pulyne vrimyth si-en.

**EN:** They raise their eyebrow.

**FR:** Cette personne lève son sourcil.

Reflexive possession because the subject raises their own eyebrow; no grammatical gender added.

### smile

**Source:** smile / grin

**Vaeltharyn:** daefivan ; daefivan thar

**EN:** smile; broad grin

**FR:** sourire ; large sourire

A grin need not be a mocking sneer. Naemlar is the verb smile.

### crooked_smile

**Source:** crooked smile

**Vaeltharyn:** daefivan remnuhoer ; daefivan fraefaev

**EN:** asymmetric smile; knowing smirk

**FR:** sourire asymétrique ; sourire narquois

Physical asymmetry and a knowing expression remain distinct; do not impose the latter on the former.

### laughter

**Source:** laugh / laughter

**Vaeltharyn:** laethar ; pimuv

**EN:** laugh, verb; laughter, noun

**FR:** rire, verbe ; rire, nom

The action noun laetheth is also productive, without replacing pimuv.

### secret_laughter

**Source:** secret laughter / sparks

**Vaeltharyn:** pimuv kogur ; pyreli

**EN:** secret laughter; sparks

**FR:** rire secret ; étincelles

Sparks remain an image when describing laughter.

### gaze

**Source:** gaze / steady gaze

**Vaeltharyn:** throenen ; throenen kymoethyn

**EN:** gaze; steady gaze

**FR:** regard ; regard stable

Steadiness concerns gaze direction and bearing, not a fixed salary.

### voice_timbre

**Source:** timber (of the speaking tone) – as quality of voice

**Vaeltharyn:** thrylkim-molpyv thaemen

**EN:** voice timbre

**FR:** timbre de la voix

Timber is read as a typo for timbre, following the voice clarification; neither lumber nor the bell foelas.

### frozen_sugar

**Source:** freeze / frozen (sugar, memory) — sugar

**Vaeltharyn:** saevmar iskiv

**EN:** frozen sugar

**FR:** sucre gelé

Literal or figurative according to the line; not automatically crystallized sugar or hardened caramel.

### frozen_memory

**Source:** freeze / frozen (sugar, memory) — memory

**Vaeltharyn:** nael poekekun

**EN:** memory held still

**FR:** mémoire immobilisée

Passive participle of poekekar, immobilize; avoids claiming to chemically freeze a memory.

## 3. Nuance and imagery

### daydream

**Source:** daydream

**Vaeltharyn:** pofer

**EN:** daydream

**FR:** rêverie éveillée

The reverie sense exists; vrofoesar, restless sleep, is not every waking daydream.

### force

**Source:** force (undeniable force)

**Vaeltharyn:** fukel thrugak ; vael-fukel thrugak

**EN:** undeniable strength; undeniable force of desire

**FR:** force indéniable ; force indéniable du désir

Fukel primarily means vigour; the desire compound explicitly marks the emotional image rather than a measured physical force.

### yield

**Source:** yield (yields toward)

**Vaeltharyn:** Se kedhoeke to mi-ath.

**EN:** They lean towards me.

**FR:** Cette personne se penche vers moi.

Bodily reading of yields toward. Relinquishing resistance uses felhukar thranurer; the acts are distinct.

### surface

**Source:** surface (shadows surface)

**Vaeltharyn:** Thyri gynoeken.

**EN:** Shadows emerge into view.

**FR:** Les ombres apparaissent.

The become-visible verb fits; no rising from a liquid is added.

### crowded_room

**Source:** crowded room

**Vaeltharyn:** sitik brifuth

**EN:** crowded reception room

**FR:** salle bondée

Sitik is a room open to visitors; a private bedroom needs another noun. Not thimgov, a fulling workshop.

### unspoken_intentions

**Source:** unspoken intentions

**Vaeltharyn:** gegani trymdhael

**EN:** unspoken intentions

**FR:** intentions tacites

Tacit is not automatically deceptive or wholly unknowable.

### bloom

**Source:** bloom (intentions begin to bloom)

**Vaeltharyn:** Gegani inu naelraeren.

**EN:** Intentions begin to bloom.

**FR:** Les intentions commencent à fleurir.

Inu marks inception; the plural subject requires en. Egg hatching is not automatically substituted.

### teasing_line

**Source:** accidental teasing line

**Vaeltharyn:** krimsuk thrisav ya dhyhune min

**EN:** an accidental teasing remark

**FR:** énoncé involontaire qui nous fait badiner

Krimsuk means an utterance, while tharel is just a word. Dhyhunar preserves playful teasing without obligatory hostility.

### hidden_wishes

**Source:** unveil / hidden wishes

**Vaeltharyn:** Dhynmuna morhemi kaervil.

**EN:** Reveal the hidden wishes.

**FR:** Révèle les souhaits cachés.

Dhynmunar reveals a secret; budirar primarily removes a physical veil.

### divine_gaze

**Source:** divine (gaze divine)

**Vaeltharyn:** throenen vrelloen

**EN:** a wonderful gaze

**FR:** regard merveilleux

Admiring reading of divine; skaedhydaer is for an actual divine relation. Do not invent religious meaning.

### accomplices

**Source:** accomplice(s)

**Vaeltharyn:** toemul ; toemuli

**EN:** accomplice; accomplices

**FR:** comparse ; comparses

Do not impose thykel, linked to crime, on romantic complicity.

### dark

**Source:** dark (out into the dark)

**Vaeltharyn:** fra aelunath to duraenath

**EN:** out of the light into the dark

**FR:** hors de la lumière vers l'obscurité

The origin is light here; replace aelun with an actual source place when known. Duraen does not automatically mean night.

### restless_curiosity

**Source:** restless curiosity

**Vaeltharyn:** naivmael ya nu vaele momlaevar saerv

**EN:** curiosity that will not stay quiet

**FR:** curiosité qui ne veut pas rester calme

Refusal is personified in curiosity; not a diagnosis of agitation.

### world_noise

**Source:** worldly noise

**Vaeltharyn:** koemmas mithilaken

**EN:** worldly noise

**FR:** bruit du monde

High-society mondain is not imposed; the world's noise can be figurative.

### fantasies

**Source:** fantasy / fantasies (erotic/imaginative)

**Vaeltharyn:** maev-sityn ; maev-sityni braeltyner

**EN:** imagined fantasy; erotic fantasies

**FR:** fantaisie imaginée ; fantasmes érotiques

Eroticism must be specified; inherited fulan, a pathological vision, is not reused.

### trace_space

**Source:** trace the space

**Vaeltharyn:** Roevaera frysiv.

**EN:** Trace the space.

**FR:** Trace l'espace.

A drawn contour or path image; not digitally tracking a person.

### closer

**Source:** closer

**Vaeltharyn:** mer neir

**EN:** closer

**FR:** plus proche

Adjective phrase. An expressed comparison adds ta plus a direct-case noun or pronoun; do not invent the comparison term.

### boundaries

**Source:** boundaries

**Vaeltharyn:** slaeldomasi

**EN:** boundaries

**FR:** limites à ne pas franchir

Abstract boundaries already exist; hepoes is primarily a geographic border.

### longing

**Source:** longing

**Vaeltharyn:** vael naev

**EN:** deep longing

**FR:** désir profond

Specify waiting or absence when important; vaelnael is nostalgia, not every desire.

### thunder

**Source:** stampede(s) of thunder (metaphor)

**Vaeltharyn:** foembymi grumen

**EN:** stampedes of thunder

**FR:** ruées de tonnerre

Singular genitive of grum; no horses or festive procession added.

### hollow_chest

**Source:** hollow chest

**Vaeltharyn:** naevrel guraeraem

**EN:** hollow chest

**FR:** poitrine creuse

Guraeraem is the cavity adjective; do not use an adverb as an adjective.

### practiced_innocence

**Source:** practiced innocence

**Vaeltharyn:** taeroek nyvaenun

**EN:** practiced ingenuousness

**FR:** ingénuité apprise

A rehearsed manner; tralul is guiltlessness, not naïveté. Gemkuthun explicitly marks feigning if intended.

### test

**Source:** put to the test

**Vaeltharyn:** Se vele e vedalath.

**EN:** They are being put to the test.

**FR:** Cette personne est à l'épreuve.

A trial frame; kafoevar means make a will and is not used. Testing an object can use konovar.

### unanswered

**Source:** questions drift unanswered

**Vaeltharyn:** Madhysi thromnumen sen froefyl.

**EN:** Questions drift without an answer.

**FR:** Les questions flottent sans réponse.

Liquid floating is an explicit image, not a silent change to a nautical drifting verb.

### electric_space

**Source:** warm electric space

**Vaeltharyn:** frysiv nufaedhor an kraeliv

**EN:** warm electric space

**FR:** espace chaud et électrique

Temperature and electricity may image interpersonal tension; no measured physical field inferred.

### dissolve_hesitation

**Source:** dissolve hesitation

**Vaeltharyn:** Trukoem grypeke.

**EN:** Hesitation dissolves away.

**FR:** L'hésitation disparaît.

The organism-disbanding verb is not repurposed; disappearance preserves the emotional result.

### shared_embrace

**Source:** shared embrace

**Vaeltharyn:** kraevetol min-en

**EN:** our shared embrace

**FR:** notre étreinte

Shared possession in context; metothar, divide for distribution, would mislead.

### reluctant

**Source:** reluctant to surrender

**Vaeltharyn:** Mi nu vaelem felhukar thranurer si-en.

**EN:** I am reluctant to relinquish my resistance.

**FR:** Je ne veux pas abandonner ma résistance.

Person comes from this example; match the actual text's pronoun. Skimfaes is not every reluctance to act.

### already_divine

**Source:** already feels divine

**Vaeltharyn:** Mi gedaenem dhais dhe se vele vrelloen.

**EN:** It already feels wonderful to me.

**FR:** Je sens déjà que c'est merveilleux.

Emotional, admiring reading; not a claim of divinity. Dhais means already.

### captivated

**Source:** captivated

**Vaeltharyn:** Mi velem gokevun.

**EN:** I am captivated.

**FR:** Je suis captivé.

Passive of a transitive verb; not physically imprisoned.

### peculiar_comfort

**Source:** peculiar comfort

**Vaeltharyn:** graedoen gaebyk

**EN:** peculiar comfort

**FR:** réconfort singulier

Unusual comfort, with no diagnostic judgement.

### unknown_before

**Source:** never previously known

**Vaeltharyn:** Thirkaeris mi nu ranoelhikem ith graedoen.

**EN:** I had never known this comfort before.

**FR:** Auparavant, je n'avais pas connu ce réconfort.

Comfort comes from the neighbouring phrase; replace it according to the complete text.

### reckless_courage

**Source:** sudden reckless courage

**Vaeltharyn:** vaethun bohom an dhavil

**EN:** sudden reckless courage

**FR:** courage soudain et téméraire

Recklessness is retained, not replaced by uncomplicated heroic praise.

### sweep_uncertainty

**Source:** sweep uncertainty away

**Vaeltharyn:** Hirlum grypeke.

**EN:** Uncertainty is swept away.

**FR:** L'incertitude s'efface.

Disappearance preserves the result; inherited vryfaemar denotes broom sweeping. An explicit broom metaphor remains optional.

### bold_conditions

**Source:** bold conditions

**Vaeltharyn:** thrirdhithi dhoefyv

**EN:** bold requirements

**FR:** exigences audacieuses

Conditions read as negotiated requirements. A logical condition uses ir plus a clause; gribaefem means state or nature.

### daring_demand

**Source:** daring demand / demanding

**Vaeltharyn:** thrirdhith dhoefyv ; hythikar

**EN:** a daring demand; demand

**FR:** exigence audacieuse ; exiger

Hehon describes habitual demandingness, not just this scene's request.

### sweet_forfeit

**Source:** sweet forfeit

**Vaeltharyn:** rydhem-fythiv gytyr

**EN:** a sweet playful forfeit

**FR:** gage de jeu agréable

Sweet means pleasant here, not necessarily sugary or soft to touch.

### exchange_mine

**Source:** exchange for mine

**Vaeltharyn:** Ir ti vaeres ⟨objet reçu⟩ mi-or, mi vaerem ⟨objet donné⟩ ti-or.

**EN:** If you give me X, I give you Y.

**FR:** Si tu me donnes X, je te donne Y.

Mine needs its antecedent: repeat the noun plus mi-en. Angle brackets are slots, not Vaeltharyn words; do not invent a kiss as referent.

### amused_pause

**Source:** amused & calculating pause

**Vaeltharyn:** vroloek, ko thalen mumpikothun an pomul

**EN:** a pause, with someone amused and calculating

**FR:** pause, avec une personne amusée et calculatrice

Amusement and calculation belong to the person, not literally to a duration; no malice added.

### inspect_plea

**Source:** inspect the brazen plea

**Vaeltharyn:** Faenlatha nydem dipir.

**EN:** Inspect the brazen plea.

**FR:** Examine la requête effrontée.

Nydem can be an ordinary request; no religious prayer is imposed.

### grant_unmeant

**Source:** grant what was never meant to be

**Vaeltharyn:** Kihoma skoendhoem ya min nu ravaelom.

**EN:** Grant what we had not intended.

**FR:** Accorde ce que nous n'avions pas voulu.

Prior-intention reading, not cosmic destiny or a universal ban. If meant means expected or permitted, use trupukar or thrusirar in another clause.

### long_awaited

**Source:** long-awaited

**Vaeltharyn:** skoendhoem ya mi ravaenem thirvaris

**EN:** a long-awaited thing

**FR:** chose que j'ai attendue longtemps

Thirvaris is the recorded adverb for a long time; the relative specifies who waited.

### unexpected_peace

**Source:** unexpected peace

**Vaeltharyn:** saerun doeboes

**EN:** unexpected peace

**FR:** paix inattendue

No permanent personality trait or religious peace added.

### nothing_same

**Source:** nothing stays the same

**Vaeltharyn:** Nul skoendhoem momlaeve grygel.

**EN:** Nothing stays the same.

**FR:** Rien ne reste identique.

Nul quantifies the noun; nu is not placed before a noun phrase.

### ancient_boundaries

**Source:** ancient boundaries fall away

**Vaeltharyn:** Slaeldomasi vaenal grypeken.

**EN:** Ancient boundaries fall away.

**FR:** Les anciennes limites disparaissent.

Interpersonal boundaries, not automatically state borders. Literal falling can be chosen as an explicit image.

### no_innocence_return

**Source:** no return to innocence

**Vaeltharyn:** Nul thrudhun to taeroekath.

**EN:** No return to innocence.

**FR:** Aucun retour vers l'ingénuité.

Innocence read as ingenuousness; tralul fits actual guiltlessness.

### polite_truths

**Source:** polite truths

**Vaeltharyn:** thaevi maerunvaerva

**EN:** polite truths

**FR:** vérités de politesse

Maerunvaer plus va, relating to politeness; krekom means polished smooth, not socially polite.

### between_laughter_certainty

**Source:** suspended between laughter and the certainty untold

**Vaeltharyn:** Se vele toebivun bri pimuvath an runkusath ya min nu pipyrom.

**EN:** It is suspended between laughter and a certainty we leave unspoken.

**FR:** Cela est suspendu entre le rire et une certitude que nous n'avouons pas.

Both nouns after bri take the locative. The relative has a subject and finite verb; replace min with the actual subject when needed.

### chapter

**Source:** watch a new chapter gradually unfold

**Vaeltharyn:** Mira dhe kenur naiv gynoeke grihak.

**EN:** Watch a new chapter gradually unfold.

**FR:** Regarde un nouveau chapitre apparaître peu à peu.

A life chapter is an explicit image; emergence does not require physically unfolding a book.

### dancing_giants

**Source:** dancing giants (in the chest)

**Vaeltharyn:** Sykimi kaenraeren e naevrelath mi-en.

**EN:** Giants dance in my chest.

**FR:** Des géants dansent dans ma poitrine.

Imagined giants; plural subject requires en. The possessor follows the inflected noun.

### never_same

**Source:** never quite the same

**Vaeltharyn:** Nesoen, vethen gylgoesykath, se nu vivele sloehil grygel.

**EN:** Afterwards, it will never be quite the same.

**FR:** Ensuite, à chaque instant, cela ne sera pas tout à fait identique.

Vethen plus a locative moment retains never's scope; shorten this explicit model only when context already supplies that duration.

## 4. Further expressions

### family_gathering

**Source:** family gathering / polite discussions

**Vaeltharyn:** lyrven nayren ; roenaemi maerunvaerva

**EN:** family gathering; polite discussions

**FR:** rencontre familiale ; discussions de politesse

A family gathering, not rejoining separate pieces. Politeness is not surface polish.

### imagined_shadows

**Source:** weeks of imagined shadows

**Vaeltharyn:** saunreli, ko thyri skethithun

**EN:** weeks with imagined shadows

**FR:** des semaines, avec des ombres imaginées

Duration and the imagining agent depend on the line; the phrase is not declared a new compound.

### unhurried_grin

**Source:** unhurried grin appears

**Vaeltharyn:** Daefivan saerv gynoeke naevris.

**EN:** An unhurried grin appears.

**FR:** Un sourire calme apparaît lentement.

Slow calm without inferred negligence or apathy; satath is not imposed.

### guide_two

**Source:** guide two accomplices

**Vaeltharyn:** Skikyka dai toemuli.

**EN:** Guide two accomplices.

**FR:** Guide deux comparses.

Singular imperative; dai requires a plural noun, not a new dual number.

### soft_anthems

**Source:** melodic anthems playing softly

**Vaeltharyn:** Thrynaeki rymfuvov thaehynen faedhor.

**EN:** Melodic anthems play softly.

**FR:** Des hymnes mélodiques sonnent doucement.

Musical sounding, not role-playing or gambling. Softly need not mean slowly.

### quiet_poise

**Source:** plain quiet poise

**Vaeltharyn:** throldhuth saerel an saerv

**EN:** plain quiet poise

**FR:** assurance simple et calme

Emotional poise, not a plumb line; plain is not physical flatness or necessarily lack of beauty.

### replace_noise

**Source:** replace worldly noise

**Vaeltharyn:** Koemmas mithilaken grypeke; saerun gynoeke.

**EN:** Worldly noise gives way to peace.

**FR:** Le bruit du monde disparaît ; la paix apparaît.

Dhytelar, replacing someone in a job, is not repurposed. Peace is an example to replace with the line's actual subject.

### destination

**Source:** arriving at the destination

**Vaeltharyn:** Min tyterom.

**EN:** We arrive at the destination.

**FR:** Nous arrivons à destination.

The verb already means reaching a destination; davaem means intended assignment or use, not necessarily an arrival place.

### creating_conditions

**Source:** creating bold conditions

**Vaeltharyn:** Min thaelom thrirdhithi dhoefyv.

**EN:** We create bold requirements.

**FR:** Nous formulons des exigences audacieuses.

Same requirement reading as bold conditions; a logical condition uses ir, not an automatic new word.

### only_lips

**Source:** only daring lips can say

**Vaeltharyn:** Ir vaemili nu velen dhoefyv, sen nu kelen lyrar se.

**EN:** If lips are not daring, they cannot say it.

**FR:** Si des lèvres ne sont pas audacieuses, elles ne peuvent pas le dire.

Only is retained as a necessary condition. Skanoem exists, but no undefined focus scope is improvised; the referent of se comes from the line.

### firm_hands

**Source:** firm hands

**Vaeltharyn:** thimi filthyk

**EN:** firm hands

**FR:** mains fermes

Physical firmness; use bropaekar or fraerfysar for secure gripping as in the dedicated records.

### universe_blurs

**Source:** surrounding universe blurs past

**Vaeltharyn:** Fyndhok skemuse min; se rytaeme dhoevom.

**EN:** The surrounding universe blurs past us.

**FR:** L'univers nous dépasse ; il devient flou.

Viewpoint from a moving vehicle, not a cosmological claim; no material mixing implied.

### absolute_release

**Source:** in absolute release

**Vaeltharyn:** e vruvythath kromer

**EN:** in complete release of tension

**FR:** dans un relâchement entier

A release-of-tension reading; nypaek fits liberation. No extra bodily event added.

### six_hundred_six

**Source:** six hundred six transistors

**Vaeltharyn:** sul khar sul transistori

**EN:** six hundred and six transistors

**FR:** six cent six transistors

606 is sul khar sul. This literal count is not asserted as a technical description of the TR-606.

### sequence

**Source:** sequence

**Vaeltharyn:** thrufon

**EN:** ordered sequence

**FR:** séquence ordonnée

A sequence is not by definition a loop or repetition.

### no_repetition

**Source:** no repetition

**Vaeltharyn:** nul broedaek

**EN:** no repetition

**FR:** aucune répétition

Nul before the noun; not nu before a noun fragment.

### lingers

**Source:** lingers

**Vaeltharyn:** Se momlaeve.

**EN:** It lingers.

**FR:** Cela demeure.

Momlaevar allows remaining in a state; furrolar emphasizes persistence of resolve.

### memory_shape

**Source:** leaving the memory frozen in an unforgotten shape

**Vaeltharyn:** Nael momlaeve poekekun e remirath ya min nu rakutykom.

**EN:** Memory remains frozen in an unforgotten shape.

**FR:** La mémoire reste immobilisée dans une forme que nous n'avons pas oubliée.

Unforgotten means actually not forgotten; slolnodoel would mean impossible to forget and change the scope. Replace min with the actual subject when needed.

## References and audit

| Reference | Checked distinction |
|---|---|
| [Roland — TR-808 technical specifications](https://support.roland.com/hc/en-us/articles/201963539-TR-808-Technical-Specifications) | Instrument parts and model; no count of 606 transistors is inferred. |
| [Roland — T-8 sound sources including TR-606](https://support.roland.com/hc/en-us/articles/6145882578715-T-8-Can-I-change-the-sound-for-each-part) | Distinguishes snare, bass drum and hi-hat sounds. |
| [Roland S-1 — keyboard pads and envelope](https://static.roland.com/manuals/s-1_manual_v102/eng/87294693.html) | Physical keyboard pads and envelope control, distinct from a pad sound. |
| [Roland GAIA SH-01 guidebook](https://cdn.roland.com/assets/media/pdf/gaia_sh-01_guidebook.pdf) | Synth pad distinction; guide preview consulted, full PDF not ingested. |
| [OpenStax — Sound interference and resonance](https://openstax.org/books/physics/pages/14-4-sound-interference-and-resonance) | Natural frequency and resonance, not just an echo. |
| [OpenStax — Hearing](https://openstax.org/books/college-physics-2e/pages/17-6-hearing) | Distinguishes frequency/pitch, loudness and timbre. |
| [Texas Instruments — transistor amplifier and switch](https://www.ti.com/document-viewer/lit/html/SSZTAH9/GUID-9AFA0B17-038E-457B-8B5E-C7F89561163A) | Transistors used for amplification and switching, not a whole radio. |

[Consulted entries](../../../data/expressions/sound-body-1.5.0/references/lexique_consulte.json) · [Structured records](../../../data/expressions/sound-body-1.5.0/sens.json) · [Rejected choices](../../../data/expressions/sound-body-1.5.0/contre_exemples.json).
