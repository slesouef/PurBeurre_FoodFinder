
CREATE TABLE Categories (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(100) NOT NULL,
                PRIMARY KEY (id)
);


CREATE TABLE Products (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(100) NOT NULL,
                quantity VARCHAR(10) NOT NULL,
                brand VARCHAR(100) NOT NULL,
                description VARCHAR(100) NOT NULL,
                url VARCHAR(100) NOT NULL,
                rating VARCHAR(1) NOT NULL,
                category_id INT NOT NULL,
                PRIMARY KEY (id)
);


CREATE TABLE History (
                searched_pid INT NOT NULL,
                substituted_pid INT NOT NULL,
                date DATETIME NOT NULL,
                PRIMARY KEY (searched_pid, substituted_pid)
);


ALTER TABLE Products ADD CONSTRAINT categories_products_fk
FOREIGN KEY (category_id)
REFERENCES Categories (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE History ADD CONSTRAINT products_history_fk
FOREIGN KEY (substituted_pid)
REFERENCES Products (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE History ADD CONSTRAINT products_history_fk1
FOREIGN KEY (searched_pid)
REFERENCES Products (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
