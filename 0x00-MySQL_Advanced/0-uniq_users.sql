-- Task : 0. We are all unique! - creates a table users
-- script can be executed on any database
CREATE TABLE If NOT EXISTS `users` (  
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255)
);