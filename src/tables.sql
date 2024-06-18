CREATE DATABASE lasses_media;

\c lasses_media

CREATE TABLE genre(
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(20),
    describtion TEXT
);

CREATE TABLE meia_type(
    type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(20)
);

CREATE TABLE platform(
    platform vARCHAR(7) PRIMARY KEY,
    input_hardware VARCHAR(40),
    output_hardware VARCHAR(40)
);

CREATE TABLE media(
    id SERIAL PRIMARY KEY,
    name vARCHAR(50),
    type_id INT REFERENCES meia_type(type_id),
    genre_id INT REFERENCES genre(genre_id),
    publisher VARCHAR(20),
    publishing_date DATE,
    fsk INT,
    carrier_type VARCHAR(10),
    platform VARCHAR(20) REFERENCES platform(platform)
);
