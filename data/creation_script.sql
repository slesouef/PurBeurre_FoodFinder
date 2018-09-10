CREATE TABLE Categories (cid INT AUTO_INCREMENT NOT NULL, name VARCHAR(255) NOT NULL, PRIMARY KEY (cid));
CREATE TABLE Products (pid INT AUTO_INCREMENT NOT NULL, name VARCHAR(255) NOT NULL, quantity VARCHAR(255) NOT NULL, brand VARCHAR(255) NOT NULL, description VARCHAR(255) NOT NULL, url VARCHAR(255) NOT NULL, rating VARCHAR(1) NOT NULL, cid INT NOT NULL, PRIMARY KEY (pid));
CREATE TABLE History (pid INT NOT NULL, sub_pid INT NOT NULL, date DATETIME NOT NULL, PRIMARY KEY (pid, sub_pid));
ALTER TABLE Products ADD CONSTRAINT categories_products_fk FOREIGN KEY (cid) REFERENCES Categories (cid) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE History ADD CONSTRAINT products_history_fk FOREIGN KEY (sub_pid) REFERENCES Products (pid) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE History ADD CONSTRAINT products_history_fk1 FOREIGN KEY (pid) REFERENCES Products (pid) ON DELETE NO ACTION ON UPDATE NO ACTION;
