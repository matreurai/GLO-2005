/* --Creation de la base de donnees GLO-2005 -- */
CREATE DATABASE `GLO-2005-Projet`;
USE `GLO-2005`;
-------------------------------------------------

/* --Creation de la table Statistique-- */
CREATE TABLE IF NOT EXISTS `t_statistique`
(
    `symbole_statistique` VARCHAR(9) NOT NULL,
    `statistique_capitalisation_boursiere` FLOAT,
    `statistique_volume_max` BIGINT,
    `statistique_quantite_circulation` BIGINT,
    `statistique_volume_24h` BIGINT,

    PRIMARY KEY(`symbole_statistique`)
);

ALTER TABLE `t_statistique` ENGINE InnoDB 
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
--CREATE INDEX `idx_statistique` ON `t_statistique`(`symbole_statistique`);
-------------------------------------------------------------------------------------------------------------------------

/* --Creation de la table Information-- */
CREATE TABLE IF NOT EXISTS `t_information`
(
    `nom_information` VARCHAR(20) NOT NULL,
    `information_symbole` VARCHAR(9) NOT NULL,
    `information_secteur_activite` VARCHAR(20),
    `information_date_entree_marche` DATE NOT NULL,
    `information_description` VARCHAR(200),
    `information_minee` ENUM('Oui','Non')  NOT NULL,
   
    PRIMARY KEY (`nom_information`),
    FOREIGN KEY (`information_symbole`) REFERENCES `t_statistique`(`symbole_statistique`)
);

ALTER TABLE `t_information` ENGINE InnoDB 
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
------------------------------------------------------------------------------------------------------------------------

/* --Creation de la table Portefeuille-- */
CREATE TABLE IF NOT EXISTS `t_portefeuille`
(
    `ID_portefeuille` SMALLINT NOT NULL AUTO_INCREMENT,
    `portefeuille_symbole` VARCHAR(9) NOT NULL,
    `portefeuille_quantite_possedee` INT,
    `portefeuille_prix_achat` FLOAT,
    `portefeuille_gains` SMALLINT,
    `portefeuille_diff_achat_courant` FLOAT,
   
    PRIMARY KEY(`ID_portefeuille`),
    FOREIGN KEY(`portefeuille_symbole`) REFERENCES `t_statistique`(`symbole_statistique`)
);

ALTER TABLE `t_portefeuille` ENGINE InnoDB 
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
---------------------------------------------------------------------------------------------------------------------

/* --Creation de la table Apercu-- */
CREATE TABLE IF NOT EXISTS `t_apercu`
(
    `ID_apercu` SMALLINT NOT NULL,
    `apercu_symbole` VARCHAR(9) NOT NULL,
    `apercu_nom` VARCHAR(20) NOT NULL,
    `apercu_prix_reel` FLOAT NOT NULL,
    `apercu_prix_haut` FLOAT NOT NULL,
    `apercu_prix_bas` FLOAT NOT NULL,
    `apercu_valeur_cad` FLOAT NOT NULL,
    `apercu_valeur_us` FLOAT NOT NULL,
   
    FOREIGN KEY(`ID_apercu`) REFERENCES `t_portefeuille`(`ID_portefeuille`),
    FOREIGN KEY(`apercu_symbole`) REFERENCES `t_statistique`(`symbole_statistique`),
    FOREIGN KEY(`apercu_nom`) REFERENCES `t_information`(`nom_information`)
);

ALTER TABLE `t_apercu` ENGINE InnoDB 
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
-------------------------------------------------------------------------------------------------------------------------

/* --Creation de la table Theme-- */
CREATE TABLE IF NOT EXISTS `t_theme`
(
    `ID_theme` TINYINT NOT NULL AUTO_INCREMENT,
    `theme_nom` VARCHAR(25) NOT NULL,
    `theme_police` VARCHAR(20) NOT NULL,
    `theme_couleur_arriere_plan` VARCHAR(7) NOT NULL,
    `theme_couleur_texte` VARCHAR(7) NOT NULL,

    PRIMARY KEY(`ID_theme`)
);

ALTER TABLE `t_theme` ENGINE InnoDB 
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
-------------------------------------------------------------------------------------------------------------------------

/* --Creation de la table Utilisateur-- */
CREATE TABLE IF NOT EXISTS `t_utilisateur`
(
    `ID_utilisateur` SMALLINT NOT NULL AUTO_INCREMENT,
    `utilisateur_nom_utilisateur` VARCHAR(20) NOT NULL,
    `utilisateur_mdp` VARCHAR(20) NOT NULL,
    `utilisateur_courriel` VARCHAR(40) NOT NULL,
    `utilisateur_prenom` VARCHAR(30) NOT NULL,
    `utilisateur_nom` VARCHAR(40) NOT NULL,
    `utilisateur_age` TINYINT NOT NULL,
    `utilisateur_sexe` ENUM('H', 'F', 'NB', 'NA') NOT NULL,
    `utilisateur_theme` TINYINT DEFAULT 0,
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