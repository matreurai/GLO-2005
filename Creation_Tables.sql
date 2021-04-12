/* --Creation de la base de donnees GLO-2005 -- */
CREATE DATABASE `GLO-2005-Projet`;
USE `GLO-2005`;
-------------------------------------------------

/* --Creation de la table Projet-- */
CREATE TABLE IF NOT EXISTS `t_projet`
(
    `projet_ticker` VARCHAR(9) NOT NULL,
    `projet_logo` FLOAT,
    `projet_nom_du_coin` BIGINT,
    `projet_secteur_activite` BIGINT,
    `projet_description` BIGINT,
    `projet_start_date` DATE,
    `projet_forage_possible` BOOLEAN,

    PRIMARY KEY(`symbole_statistique`)
);

ALTER TABLE `t_statistique` ENGINE InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
--CREATE INDEX `idx_statistique` ON `t_statistique`(`symbole_statistique`);
-------------------------------------------------------------------------------------------------------------------------

/* --Creation de la table Cryptomonnaie-- */
CREATE TABLE IF NOT EXISTS `t_cryptomonnaie`
(
    `cryptomonnaie_id` VARCHAR(20) NOT NULL,
    `cryptomonnaie_ticker` VARCHAR(9) NOT NULL,
    `cryptomonnaie_nom_du_coin` VARCHAR(20),
    `cryptomonnaie_prix_actuel` DATE NOT NULL,
    `cryptomonnaie_prix_haut` VARCHAR(200),
    `cryptomonnaie_prix_bas` INT,
    `cryptomonnaie_Valeur_cad` INT,
    `cryptomonnaie_market_cap` INT,
    `cryptomonnaie_max_supply` INT,
    `cryptomonnaie_qte_circulation` INT,
    `cryptomonnaie_volume_24h` INT,
    `cryptomonnaie_logo` INT,

    PRIMARY KEY (`nom_information`),
    FOREIGN KEY (`information_symbole`) REFERENCES `t_statistique`(`symbole_statistique`)
);

ALTER TABLE `t_information` ENGINE InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
------------------------------------------------------------------------------------------------------------------------

/* --Creation de la table Titre-- */
CREATE TABLE IF NOT EXISTS `t_titre`
(
    `titre_ticker` SMALLINT NOT NULL AUTO_INCREMENT,
    `titre_qte` VARCHAR(9) NOT NULL,
    `titre_prix_paye` INT,
    `titre_valeur_courante` FLOAT,
    `titre_profits` SMALLINT,
    `titre_ratio_%` FLOAT,

    PRIMARY KEY(`ID_portefeuille`),
    FOREIGN KEY(`portefeuille_symbole`) REFERENCES `t_statistique`(`symbole_statistique`)
);

ALTER TABLE `t_portefeuille` ENGINE InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
---------------------------------------------------------------------------------------------------------------------

/* --Creation de la table Portfolio-- */
CREATE TABLE IF NOT EXISTS `t_portfolio`
(
    `portfolio_id` SMALLINT NOT NULL,
    `portfolio_balance` VARCHAR(9) NOT NULL,
    `portfolio_profit_total` VARCHAR(20) NOT NULL,
    `portfolio_cout_total` FLOAT NOT NULL,
    `portfolio_qte_coin_diff` FLOAT NOT NULL,
    `portfolio_ratio_%` FLOAT NOT NULL,

    FOREIGN KEY(`ID_apercu`) REFERENCES `t_portefeuille`(`ID_portefeuille`),
    FOREIGN KEY(`apercu_symbole`) REFERENCES `t_statistique`(`symbole_statistique`),
    FOREIGN KEY(`apercu_nom`) REFERENCES `t_information`(`nom_information`)
);

ALTER TABLE `t_apercu` ENGINE InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
-------------------------------------------------------------------------------------------------------------------------

/* --Creation de la table Alerte-- */
CREATE TABLE IF NOT EXISTS `t_alerte`
(
    `alerte_id` TINYINT NOT NULL AUTO_INCREMENT,
    `alerte_ticker` VARCHAR(25) NOT NULL,
    `alerte_below_price` VARCHAR(20) NOT NULL,
    `alerte_above_price` VARCHAR(7) NOT NULL,
    `alerte_end_date` VARCHAR(7) NOT NULL,

    PRIMARY KEY(`ID_theme`)
);

ALTER TABLE `t_theme` ENGINE InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
-------------------------------------------------------------------------------------------------------------------------

/* --Creation de la table Utilisateur-- */
CREATE TABLE IF NOT EXISTS `t_utilisateur`
(
    `utilisateur_id` SMALLINT NOT NULL AUTO_INCREMENT,
    `utilisateur_username` VARCHAR(20) NOT NULL,
    `utilisateur_password` VARCHAR(20) NOT NULL,
    `utilisateur_email` VARCHAR(40) NOT NULL,
    `utilisateur_phone` VARCHAR(40) NOT NULL,
    `utilisateur_prenom` VARCHAR(30) NOT NULL,
    `utilisateur_nom` VARCHAR(40) NOT NULL,
    `utilisateur_age` TINYINT NOT NULL,
    `utilisateur_sexe` ENUM('H', 'F', 'NB', 'NA') NOT NULL,
    `utilisateur_privilege` BOOLEAN DEFAULT 0,
    `utilisateur_date_creation` DATE NOT NULL,

    PRIMARY KEY(`ID_utilisateur`),
    FOREIGN KEY(`utilisateur_theme`) REFERENCES `t_theme`(`ID_theme`),
    UNIQUE(`utilisateur_nom_utilisateur`),
    UNIQUE(`utilisateur_courriel`)
);

ALTER TABLE `t_utilisateur` ENGINE InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
----------------------------------------------------------------------------------------------------------------------

/* --------------------------------------------------------------------------------------------------------------------------
                -- EXEMPLE --
 --Peuplement de la table NOMDELATABLE--

INSERT INTO `t_NOMDELATABLE`(attribut1, attribut2, attribut3, etc) VALUES
(valeur1, valeur2, valeur3, etc),
(valeur1, valeur2, valeur3, etc),
(valeur1, valeur2, valeur3, etc),
(valeur1, valeur2, valeur3, etc),
(valeur1, valeur2, valeur3, etc),
(valeur1, valeur2, valeur3, etc),
(valeur1, valeur2, valeur3, etc);

 -------------------------------------------------------------------------------------------------------------------------- */

/* --Peuplement de la table Statistique-- */
INSERT INTO `t_statistique`(symbole_statistique, statistique_capitalisation_boursiere, statistique_volume_max, statistique_quantite_circulation, statistique_volume_24h) VALUES
(),
();
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
/* --Peuplement de la table Statistique-- */
INSERT INTO `t_information`(nom_information, information_symbole, information_secteur_activite, information_date_entree_marche, information_description, information_minee) VALUES
(),
();
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
/* --Peuplement de la table Statistique-- */
INSERT INTO `t_portefeuille`(ID_portefeuille, portefeuille_symbole, portefeuille_quantite_possedee, portefeuille_prix_achat, portefeuille_gains, portefeuille_diff_achat_courant) VALUES
(),
();
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
/* --Peuplement de la table Statistique-- */
INSERT INTO `t_apercu`(ID_apercu, apercu_symbole, apercu_nom, apercu_prix_reel, apercu_prix_haut, apercu_prix_bas, apercu_valeur_cad, apercu_valeur_us) VALUES
(),
();
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
/* --Peuplement de la table Statistique-- */
INSERT INTO `t_theme`(ID_theme, theme_nom, theme_police, theme_couleur_arriere_plan, theme_couleur_texte) VALUES
(0, Clair),
(1, Sombre);
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
/* --Peuplement de la table Statistique-- */
INSERT INTO `t_utilisateur`(ID_utilisateur, utilisateur_nom_utilisateur, utilisateur_mdp, utilisateur_courriel, utilisateur_prenom, utilisateur_nom, utilisateur_age, utilisateur_sexe, utilisateur_theme, utilisateur_privilege, utilisateur_date_creation) VALUES
(0, "matreurai", "123456", "saaub15@ulaval.ca", "Samuel", "Aubert", 27, 'H', 0, 1, now()),
(1, "cactusman", "123456", "chgod54@ulaval.ca", "Christopher", "Godin", 22, 'H', 0, 1, now()),
(2, "jarvis", "123456", "dabol66@ulaval.ca", "David", "Bolduc", 28, 'H', 0, 1, now());
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------