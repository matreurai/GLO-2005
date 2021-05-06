/* -- Script à rouler pour Restart de BD et Création -- */
/* -- Creation de la base de donnees GLO-2005 -- */
DROP DATABASE `GLO-2005-Projet`;
CREATE DATABASE `GLO-2005-Projet`;
USE `GLO-2005-Projet`;

DROP TABLE IF EXISTS `t_projet`;
DROP TABLE IF EXISTS `t_cryptomonnaie`;
DROP TABLE IF EXISTS `t_utilisateur`;
DROP TABLE IF EXISTS `t_password`;
DROP TABLE IF EXISTS `t_alerte`;
DROP TABLE IF EXISTS `t_portfolio`;
DROP TABLE IF EXISTS `t_titre`;
/*--------------------------------------------------*/

/* -- Creation de la table Projet -- */
CREATE TABLE IF NOT EXISTS `t_projet`
(
    `projet_ticker` VARCHAR(9) NOT NULL,
    `projet_logo` VARCHAR(50),
    `projet_nom_du_coin` VARCHAR(50) NOT NULL,
    `projet_description` VARCHAR(300),
    `projet_start_date` DATE,
    `projet_forage_possible` BOOLEAN,

    PRIMARY KEY(`projet_ticker`),
    UNIQUE(`projet_ticker`)
);

ALTER TABLE `t_projet` ENGINE InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
CREATE INDEX `idx_projet` ON `t_projet`(`projet_ticker`);
/*-------------------------------------------------------------------------------------------------------------------------*/

/* -- Creation de la table Cryptomonnaie -- */
CREATE TABLE IF NOT EXISTS `t_cryptomonnaie`
(
    `cryptomonnaie_id` SMALLINT NOT NULL AUTO_INCREMENT,
    `cryptomonnaie_ticker` VARCHAR(9) NOT NULL,
    `cryptomonnaie_nom_du_coin` VARCHAR(20),
    `cryptomonnaie_prix_actuel` DECIMAL(13,4) NOT NULL,
    `cryptomonnaie_prix_haut` DECIMAL(13,4),
    `cryptomonnaie_prix_bas` DECIMAL(13,4),
    `cryptomonnaie_market_cap` BIGINT,
    `cryptomonnaie_max_supply` BIGINT,
    `cryptomonnaie_qte_circulation` BIGINT,
    `cryptomonnaie_volume_24h` BIGINT,

    PRIMARY KEY (`cryptomonnaie_id`),
    FOREIGN KEY (`cryptomonnaie_ticker`) REFERENCES `t_projet`(`projet_ticker`)
);

ALTER TABLE `t_cryptomonnaie` ENGINE InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
CREATE INDEX `idx_crypto` ON `t_cryptomonnaie`(`cryptomonnaie_id`);
/*------------------------------------------------------------------------------------------------------------------------*/

/* -- Creation de la table Utilisateur -- */
CREATE TABLE IF NOT EXISTS `t_utilisateur`
(
    `utilisateur_id` SMALLINT NOT NULL AUTO_INCREMENT,
    `utilisateur_username` VARCHAR(20) NOT NULL,
    `utilisateur_email` VARCHAR(40) NOT NULL,
    `utilisateur_phone` VARCHAR(20),
    `utilisateur_prenom` VARCHAR(30),
    `utilisateur_nom` VARCHAR(40),
    `utilisateur_date_creation` DATE NOT NULL,

    PRIMARY KEY(`utilisateur_id`),
    UNIQUE(`utilisateur_username`),
    UNIQUE(`utilisateur_email`),
    UNIQUE(`utilisateur_phone`)
);

ALTER TABLE `t_utilisateur` ENGINE InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
/*----------------------------------------------------------------------------------------------------------------------*/

/* -- Creation de la table Password -- */
CREATE TABLE IF NOT EXISTS `t_password`
(
    `password_id_utilisateur` SMALLINT NOT NULL,
    `password_password` VARCHAR(128) NOT NULL,

    FOREIGN KEY(`password_id_utilisateur`) REFERENCES `t_utilisateur`(`utilisateur_id`)
);

ALTER TABLE `t_password` ENGINE InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
CREATE INDEX `idx_password_id` USING HASH ON `t_password`(`password_id_utilisateur`);
/*----------------------------------------------------------------------------------------------------------------------*/

/* -- Creation de la table Alerte -- */
CREATE TABLE IF NOT EXISTS `t_alerte`
(
    `alerte_id` TINYINT NOT NULL AUTO_INCREMENT,
    `alerte_user` SMALLINT,
    `alerte_ticker` VARCHAR(25),
    `alerte_below_price` DECIMAL(13, 4),
    `alerte_above_price` DECIMAL(13, 4),
    `alerte_end_date` DATE,

    PRIMARY KEY (`alerte_id`),
    FOREIGN KEY (`alerte_ticker`) REFERENCES `t_projet`(`projet_ticker`),
    FOREIGN KEY (`alerte_user`) REFERENCES `t_utilisateur`(`utilisateur_id`)
);

ALTER TABLE `t_alerte` ENGINE InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
CREATE INDEX `alerte_idx` USING HASH ON `t_alerte` (`alerte_user`, `alerte_ticker`, `alerte_below_price`, `alerte_above_price`, `alerte_end_date`);
/*-------------------------------------------------------------------------------------------------------------------------*/

/* -- Creation de la table Portfolio -- */
CREATE TABLE IF NOT EXISTS `t_portfolio`
(
    `portfolio_id` SMALLINT NOT NULL AUTO_INCREMENT,
    `portfolio_user` SMALLINT NOT NULL,
    `portfolio_balance` DECIMAL(13,4),
    `portfolio_cout_total` DECIMAL(13,4),

    PRIMARY KEY(`portfolio_id`),
    FOREIGN KEY(portfolio_user) REFERENCES `t_utilisateur`(`utilisateur_id`)
);

ALTER TABLE `t_portfolio` ENGINE InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
/*-------------------------------------------------------------------------------------------------------------------------*/

/* -- Creation de la table Titre -- */
CREATE TABLE IF NOT EXISTS `t_titre`
(
    `titre_crypto_id` SMALLINT NOT NULL,
    `titre_portfolio_id` SMALLINT,
    `titre_qte` INT DEFAULT 1,
    `titre_prix_moyen_paye` DECIMAL(13,4),

    FOREIGN KEY(`titre_crypto_id`) REFERENCES `t_cryptomonnaie`(`cryptomonnaie_id`),
    FOREIGN KEY(`titre_portfolio_id`) REFERENCES `t_portfolio`(`portfolio_id`)
);

ALTER TABLE `t_titre` ENGINE InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
CREATE INDEX `titre_idx` USING HASH ON `t_titre` (`titre_crypto_id`, `titre_prix_moyen_paye`, `titre_qte`);
/*---------------------------------------------------------------------------------------------------------------------*/

/* -- Creation de la Procedure Create_User -- */
DELIMITER %%
CREATE PROCEDURE Create_User (  IN username VARCHAR(20),
                                IN email VARCHAR(40),
                                IN date_creation DATE,
                                IN password VARCHAR(128))
    BEGIN
        INSERT INTO `t_utilisateur` (utilisateur_username, utilisateur_email, utilisateur_date_creation)
        VALUES                  (username,
                                email,
                                date_creation);
        SELECT @id := LAST_INSERT_ID() FROM `t_utilisateur`;
        INSERT INTO `t_password` (password_id_utilisateur, password_password) VALUES (@id, password);
    END %%
DELIMITER ;
/*---------------------------------------------------------------------------------------------------------------------*/
CALL Create_User('rjovis0f','rjovis0@toplist.cz','2020-12-17', 'PASSWORD123@');

