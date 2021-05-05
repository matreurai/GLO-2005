
DROP DATABASE tes ;
CREATE DATABASE Tes;
USE tes;

CREATE TABLE IF NOT EXISTS t_projet
(
    projet_ticker           VARCHAR(9) NOT NULL,
    projet_logo             VARCHAR(50),
    projet_nom_du_coin      VARCHAR(20) NOT NULL,
    projet_secteur_activite  VARCHAR(20),
    projet_description      VARCHAR(300),
    projet_start_date       DATE,
    projet_forage_possible  BOOLEAN,

    PRIMARY KEY(projet_ticker),
    UNIQUE(projet_ticker)
);

ALTER TABLE t_projet ENGINE InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
CREATE INDEX idx_projet ON t_projet(projet_ticker);

SELECT * FROM t_projet;