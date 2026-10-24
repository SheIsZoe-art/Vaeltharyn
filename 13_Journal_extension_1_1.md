# Journal — extension lexicale 1.1.0

Date : 2026-10-24. Demande : développer un dictionnaire aussi complet que possible à partir de la base installée. Retour : [00_Accueil](00_Accueil.md).

## Résultat

- 2,918 entrées, contre 465 au départ ; 2,453 ajouts.
- 1073 nouveaux lemmes proposés, 1322 dérivés réguliers et 58 composés explicites.
- 256 verbes ; 13,824 formes finies présentées séparément.
- Chaque définition figure dans l’index français ; les renvois supplémentaires ne gonflent pas le nombre de lemmes.
- Les 465 lignes initiales, leurs catégories, sens et valences sont conservés à l’identique.

## Décisions rédactionnelles

Les ajouts sont étiquetés **extension proposée**, sans prétendre que le créateur a validé chaque entrée. La grammaire et la phonologie restent celles de 1.0.0. Les noms nouveaux enregistrés comme unités lexicales ne doivent pas recevoir d’étymologie improvisée. Les composés transparents sont marqués par le trait d’union ; les dérivés donnent leur base et leur règle.

Les homographies lexicales nouvelles sont refusées lors de la construction. Les homographies entre flexions et lemmes sont recensées, pas cachées : 105 couples forme/base dans le contrôle livré. 14 dérivations potentielles ont été écartées parce que la forme était déjà occupée. Aucune entrée préexistante n’a été remplacée pour faire de la place.

## Vérifications et limites

Le contrôle vérifie la préservation des entrées, l’unicité, la graphie des ajouts, les infinitifs, la reconstruction des dérivés, les composés, la couverture de l’index inverse et les liens. Il ne remplace pas une relecture linguistique exhaustive. Les exemples sont illustratifs ; la naturalité de chaque formulation, l’idiomatique et la perception au chant restent à développer. Aucun audio n’a été téléchargé ou généré.

Une copie de précaution des fichiers remplacés est conservée hors des notes actives. Ce n’est pas une archive de commentaires Suno.

Voir [11_Couverture_et_limites](11_Couverture_et_limites.md) pour les domaines encore ouverts et `controle_coherence.json` pour le détail des contrôles réellement exécutés.
