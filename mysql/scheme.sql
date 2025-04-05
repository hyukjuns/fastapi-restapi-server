-- CREATE DATABASE playerdb;
-- USE playerdb;

DROP TABLE IF EXISTS notes;

CREATE TABLE notes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  note VARCHAR(100),
  created DATETIME DEFAULT CURRENT_TIMESTAMP,
);

INSERT INTO notes (name,team,goal)
VALUES ('sonny','spurs',10);

INSERT INTO notes (name,team,goal)
VALUES ('kane','spurs',5);

INSERT INTO notes (name,team,goal)
VALUES ('hyukjun','spurs',1);