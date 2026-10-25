# Grand dictionnaire Vaeltharyn — édition de travail 1.2.0

**65,000 graphies lexicales distinctes**, 65,001 entrées lemme/catégorie, dont **62,083 nouvelles propositions définies et sourcées**. Les 2 918 entrées de 1.1.0 sont conservées à l’identique. Les conjugaisons et les renvois français ne sont pas comptés comme des mots supplémentaires.

Cette édition atteint l’ordre de grandeur numérique d’un dictionnaire général de français. Elle n’en possède pas encore la même révision éditoriale : les nouvelles formes ont été attribuées par un procédé déterministe, et leur définition française provient d’un sens filtré du Wiktionnaire. **Contrôlé mécaniquement** ne signifie pas **validé mot par mot par le créateur**. Les sens sont proposés comme base de travail pour les chansons ; les formes et les identifiants enregistrés doivent rester stables.

## Accès

- [Vaeltharyn → français](16_Index_Vaeltharyn.md) : volumes de 400 entrées au maximum.
- [Français → Vaeltharyn](17_Index_francais.md) : volumes de 400 entrées au maximum.
- [Atelier d’écriture](19_Atelier_des_chansons.md) : palettes thématiques, distinctions et révision.
- [Conjuguer les nouveaux verbes](20_Conjuguer_le_grand_lexique.md) : exemples et tables complètes du supplément.
- [18_Sources_et_licences](18_Sources_et_licences.md) : définitions, attribution et modifications.
- [21_Bilan_grande_edition](21_Bilan_grande_edition.md) : contrôles effectués, décompte et limites.
- [Accueil de la langue](00_Accueil.md) : règles communes, dictionnaire initial et textes.

`lexique.csv` garde ses cinq colonnes. `lexique_detaille.csv` ajoute les définitions, l’API, la segmentation proposée, le registre, l’identifiant, la source et l’état de révision. Les API sont calculées depuis les règles écrites ; aucune prononciation n’est présentée comme testée dans Suno.

## Un sens défini par proposition nouvelle

Le mot français sert de repère de recherche ; la **définition complète** délimite la traduction. Le français « grave », par exemple, n’autorise pas à confondre registre sonore, danger et solennité. Aucun sens supplémentaire de la page source n’est importé implicitement. Un terme Vaeltharyn déjà présent conserve sa définition même si son renvoi français est polysémique.

Les flexions et variantes explicites, les noms propres, les entrées sans définition exploitable et les sens marqués vieillis, désuets ou rares ont été exclus de la sélection nouvelle. Les marques familières, figurées ou péjoratives restent visibles si le sens a été retenu. Cette sélection reste une sélection de travail, non une liste officielle du français contemporain.

## État éditorial

Les 2 918 entrées antérieures gardent leurs qualités et leurs limites. Les ajouts n’ont pas tous un exemple contextualisé, une famille morphologique révisée ou des collocations testées. Leur présence dans l’index ne suffit pas à en faire un choix naturel en poésie. Avant une chanson, relire les entrées utilisées, leur valence et les images produites ; enregistrer la version des sens effectivement retenus.

Il n’est pas nécessaire d’approuver une par une toutes les entrées pour écrire : on utilise le noyau et les propositions utiles, puis on consigne les décisions. Aucune génération aléatoire ne doit rebaptiser un mot déjà enregistré dans une chanson.


## Complément lexical du 24 octobre 2026 — royaume

[22_Complement_lexical_royaume](22_Complement_lexical_royaume.md) : 6 entrées supplémentaires (aquaponie, serre horticole, sauna, avoir besoin de, fichu intensif, tendre la main vers), avec définitions et index dans les deux sens. Les deux CSV sont actualisés ; les volumes 1.2.0 ci-dessus restent des instantanés historiques.


## Jurons, insultes et expressions — 25 octobre 2026

[Complément expressif bilingue](23_Jurons_insultes_expressions.md) : 10 entrées proposées, 79 expressions et leurs lectures littérales. Les CSV actuels contiennent 65 017 entrées ; les volumes historiques gardent leur périmètre.


## Extension documentée 1.4.0 — 25 octobre 2026

[Inventaire expressif FR/EN](24_Inventaire_expressif_FR_EN.md) : les 719 lignes fournies sont documentées, avec 226 fiches de sens et neuf ajouts lexicaux. Quatre lignes restent sans équivalent établi, explicitement signalées. CSV actuels : 65,026 entrées, 65,023 graphies, 6,538 verbes. Les chiffres antérieurs des volumes restent historiques. Les ajouts sont des propositions non validées.


## Extension 1.5.0 — son, corps et images

[Guide de construction FR/EN](25_Son_corps_et_images.md) : 111 fiches contextualisées, quinze entrées supplémentaires, huit racines et sept composés. Corpus courant : 65 041 entrées, 65 038 graphies, 6 538 verbes. Les comptes antérieurs restent historiques ; les ajouts restent des propositions vérifiées à l’écrit.
