# Sons et chant

## Alphabet canonique

Écriture latine : `a á ae b d dh e é f g h i í k l m n ng o ó oe p r s t th u ú v y ý`. Les digrammes constituent chacun un son. Pas de lettres muettes, de nasalisation française, de mutation initiale ni de changement historique obligatoire.

| Graphie | API | Indication française |
|---|---|---|
| a / á | /a aː/ | a / a tenu |
| e / é | /ɛ ɛː/ | è / è tenu |
| i / í | /i iː/ | i / i tenu |
| o / ó | /ɔ ɔː/ | o ouvert / o tenu |
| u / ú | /u uː/ | ou / ou tenu |
| y / ý | /y yː/ | u français / u tenu |
| ae | /æː/ | voyelle longue entre a et è |
| oe | /œː/ | eu ouvert tenu, comme dans cœur |
| ai | /ai̯/ | a puis i dans une même syllabe |
| ei | /ɛi̯/ | è puis i dans une même syllabe |
| au | /au̯/ | a puis ou dans une même syllabe |
| oi | /ɔi̯/ | o puis i, jamais « oua » |
| th / dh | /θ ð/ | th anglais sourd / sonore |
| ng | /ŋ/ | fin de parking, un seul son |
| r | /r/ | r roulé ou battu, jamais obligatoire en gorge |
| g | /g/ | toujours dur, comme gare |
| s | /s/ | toujours sourd, même entre voyelles |
| h | /h/ | souffle léger articulé |
| autres consonnes | /b d f k l m n p t v/ | valeur API usuelle |

Deux voyelles différentes non listées comme digramme se prononcent en hiatus : `ia` = /i.a/. Deux voyelles identiques en contact morphologique restent deux syllabes, séparables par un point dans une annotation. Une voyelle ne devient longue que par l'accent écrit ou par `ae/oe` ; la mélodie peut l'étirer sans changer le mot.

## Accent et syllabes

L'accent lexical tombe sur la première syllabe de la racine et ne bouge jamais après suffixation. Les préfixes de temps `ra-`, `vi-`, `ru-` restent inaccentués. Un composé reçoit l'accent principal sur sa première racine et un accent secondaire sur la seconde. Les particules ne prennent normalement pas l'accent de phrase.

Exemples : `THAER-ar`, `ra-THAER-em`, `SAEL-i-ath`, `SAEL-aelun`. `ae` compte pour un seul noyau syllabique, même long. Ainsi `thaerem` a deux syllabes : `thae-rem`.

Structure usuelle : (C)(C)V(C)(C). Les racines privilégient une ou deux syllabes ; les dérivés peuvent être plus longs. Groupes initiaux autorisés : consonne obstruante + l/r/v, ou s + p/t/k/m/n/l/v. `th+r` est autorisé. Une suite morphologique plus difficile reste prononcée distinctement ; on peut ajouter un très bref schwa **phonétique**, sans le noter ni le compter comme syllabe métrique canonique.

## Chant

- Tenir la voyelle, puis fermer la consonne : `thaaaer-m`, et non multiplier les r.
- Préférer des fins de vers en `á, ae, ó, ú, l, n, r, m`.
- En chœur, synchroniser les consonnes finales après la tenue.
- Les accents graves/symboles de stress dans une aide de lecture ne font pas partie du texte canonique.
- Ne pas ajouter d'apostrophes décoratives : elles ne codent aucun phénomène.
- Le texte chanté conserve les mêmes règles de grammaire que le texte parlé.

## Deux transcriptions de travail

**ASCII fidèle** : á=aa, é=ee, í=ii, ó=oo, ú=uu, ý=yy ; garder ae/oe/th/dh/ng. Elle est pratique pour saisir les paroles mais les doublons de voyelles ne constituent pas l'orthographe canonique.

**Aide francophone** : u→ou, y→u, ae→aèè, oe→eu, th→th, dh→dh, r→r roulé. Ce n'est pas un alphabet alternatif ni une promesse de prononciation exacte par un moteur musical.

Dans Suno, commencer par l'orthographe canonique. Si un mot résiste, tester une transcription sur ce seul mot. Conserver séparément texte canonique et version de performance. La réalisation de /θ ð æː œː y/ peut varier selon le moteur et la voix.
