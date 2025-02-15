
CREATE DATABASE IF NOT EXISTS `malicip`;

REVOKE ALL ON `malicip`.* FROM 'malicip'@'%';

GRANT SELECT ON `malicip`.* TO `malicip`@`%`;



USE `malicip`;


DROP TABLE IF EXISTS `REDACTED_TABLE`;

CREATE TABLE `REDACTED_TABLE` (
  `REDACTED_COLUMN` varchar(128) NOT NULL
);

INSERT INTO `REDACTED_TABLE` (`REDACTED_COLUMN`)
VALUES
('KMA{redacted, of course}');



DROP TABLE IF EXISTS `malicious_ip`;

CREATE TABLE `malicious_ip` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ip` varchar(64) NOT NULL,
  `message` varchar(512) DEFAULT '',
  PRIMARY KEY (`id`)
);

INSERT INTO `malicious_ip` (`ip`,`message`)
VALUES
('13.37.13.37', 'too leet'),
('103.12.104.72', 'phishing'),
('42.112.213.88', 'phishing'),
('2405:f980::1:12', 'phishing'),
('103.12.104.29', 'command & control server'),
('1337::dead:beef', 'dead leet');

