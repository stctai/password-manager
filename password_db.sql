-- Author: Ke

CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    username VARCHAR(255),
    url VARCHAR(255) NOT NULL,
    app_name VARCHAR(255) NOT NULL
);
