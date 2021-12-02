DROP TABLE monsters;
DROP TABLE teams;
DROP TABLE league;

CREATE TABLE leagues(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE teams(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    league_id INT REFERENCES leagues(id)
);

CREATE TABLE monsters(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    limbs INT,
    team_id INT REFERENCES teams(id)
);