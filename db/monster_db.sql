DROP TABLE monsters;
DROP TABLE games;
DROP TABLE teams;
DROP TABLE leagues;

CREATE TABLE leagues(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE teams(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),    
    league_id INT REFERENCES leagues(id) ON DELETE CASCADE
);

CREATE TABLE games(
    id SERIAL PRIMARY KEY,
    home_team_id INT REFERENCES teams(id) ON DELETE CASCADE,
    away_team_id INT REFERENCES teams(id) ON DELETE CASCADE,
    draw BOOLEAN,
    winning_team_id INT REFERENCES teams(id) ON DELETE CASCADE NULL    
);

CREATE TABLE monsters(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    limbs INT,
    team_id INT REFERENCES teams(id) ON DELETE CASCADE
);