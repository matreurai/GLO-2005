/* --Creation de la base de donnees GLO-2005 -- */
CREATE DATABASE `GLO-2005-Projet`;
USE `GLO-2005`;
-------------------------------------------------

/* --Creation de la table Projet-- */
CREATE TABLE IF NOT EXISTS `t_projet`
(
    `projet_ticker` VARCHAR(9) NOT NULL,
    `projet_logo` VARCHAR(50),
    `projet_nom_du_coin` VARCHAR(20) NOT NULL,
    `projet_secteur_activite` VARCHAR(20),
    `projet_description` VARCHAR(300),
    `projet_start_date` DATE,
    `projet_forage_possible` BOOLEAN,

    PRIMARY KEY(`projet_ticker`)
);

ALTER TABLE `t_projet` ENGINE InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
CREATE INDEX `idx_projet` ON `t_projet`(`projet_ticker`);
-------------------------------------------------------------------------------------------------------------------------

/* --Creation de la table Cryptomonnaie-- */
CREATE TABLE IF NOT EXISTS `t_cryptomonnaie`
(
    `cryptomonnaie_id` SMALLINT NOT NULL AUTO_INCREMENT,
    `cryptomonnaie_ticker` VARCHAR(9) NOT NULL,
    `cryptomonnaie_nom_du_coin` VARCHAR(20),
    `cryptomonnaie_prix_actuel` FLOAT NOT NULL,
    `cryptomonnaie_prix_haut` FLOAT,
    `cryptomonnaie_prix_bas` FLOAT,
    `cryptomonnaie_Valeur_cad` FLOAT,
    `cryptomonnaie_market_cap` BIGINT,
    `cryptomonnaie_max_supply` BIGINT,
    `cryptomonnaie_qte_circulation` BIGINT,
    `cryptomonnaie_volume_24h` BIGINT,
    `cryptomonnaie_logo` VARCHAR(50),

    PRIMARY KEY (`cryptomonnaie_id`),
    FOREIGN KEY (`cryptomonnaie_ticker`) REFERENCES `t_projet`(`projet_ticker`)
);

ALTER TABLE `t_cryptomonnaie` ENGINE InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
CREATE INDEX `idx_projet` ON `t_cryptomonnaie`(`cryptomonnaie_id`);
------------------------------------------------------------------------------------------------------------------------

/* --Creation de la table Titre-- */
CREATE TABLE IF NOT EXISTS `t_titre`
(
    `titre_ticker` VARCHAR(9) NOT NULL,
    `titre_qte` INT,
    `titre_prix_paye` FLOAT,
    `titre_valeur_courante` FLOAT,
    `titre_profits` FLOAT,
    `titre_ratio_%` FLOAT,

    FOREIGN KEY(`titre_ticker`) REFERENCES `t_projet`(`projet_ticker`)
);

ALTER TABLE `t_titre` ENGINE InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
---------------------------------------------------------------------------------------------------------------------

/* --Creation de la table Portfolio-- */
CREATE TABLE IF NOT EXISTS `t_portfolio`
(
    `portfolio_id` SMALLINT NOT NULL,
    `portfolio_balance` FLOAT,
    `portfolio_profit_total` FLOAT,
    `portfolio_cout_total` FLOAT,
    `portfolio_qte_coin_diff` SMALLINT,
    `portfolio_ratio_%` FLOAT,

    PRIMARY KEY(`portfolio_id`)
);

ALTER TABLE `t_portfolio` ENGINE InnoDB
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

    PRIMARY KEY(`alerte_id`),
    FOREIGN KEY(`alerte_ticker`) REFERENCES `t_projet`(projet_ticker)
);

ALTER TABLE `t_alerte` ENGINE InnoDB
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
    `utilisateur_phone` VARCHAR(20),
    `utilisateur_prenom` VARCHAR(30),
    `utilisateur_nom` VARCHAR(40),
    `utilisateur_age` TINYINT,
    `utilisateur_sexe` VARCHAR(15),
    `utilisateur_date_creation` DATE NOT NULL,

    PRIMARY KEY(`utilisateur_id`),
    UNIQUE(`utilisateur_username`),
    UNIQUE(`utilisateur_email`),
    UNIQUE(`utilisateur_phone`)
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

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
/* --Peuplement de la table Statistique-- */
INSERT INTO `t_utilisateur`(ID_utilisateur, utilisateur_nom_utilisateur, utilisateur_mdp, utilisateur_courriel, utilisateur_prenom, utilisateur_nom, utilisateur_age, utilisateur_sexe, utilisateur_theme, utilisateur_privilege, utilisateur_date_creation) VALUES
(0, "matreurai", "123456", "saaub15@ulaval.ca", "Samuel", "Aubert", 27, 'H', 0, 1, now()),
(1, "cactusman", "123456", "chgod54@ulaval.ca", "Christopher", "Godin", 22, 'H', 0, 1, now()),
(2, "jarvis", "123456", "dabol66@ulaval.ca", "David", "Bolduc", 28, 'H', 0, 1, now());
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
