create database anht0iCTF02;
USE anht0iCTF02;

CREATE TABLE `log` (
  `id` int(11) NOT NULL,
  `username` varchar(500) NOT NULL,
  `time` datetime NOT NULL,
  `browser` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `user` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `log`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

CREATE USER 'chall2' IDENTIFIED BY 'asddva8439hefe4j';
GRANT SELECT ON anht0iCTF02.* to 'chall2'@'%';
FLUSH PRIVILEGES;
GRANT INSERT ON anht0iCTF02.* to 'chall2'@'%';
FLUSH PRIVILEGES;

