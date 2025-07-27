CREATE TABLE person (
	id INTEGER NOT NULL, 
	name VARCHAR(250) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE genre (
	id INTEGER NOT NULL, 
	title VARCHAR(250), 
	PRIMARY KEY (id)
);
CREATE TABLE movie (
	id INTEGER NOT NULL, 
	title VARCHAR(250), 
	genre_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(genre_id) REFERENCES genre (id)
);
CREATE TABLE "cast" (
	id INTEGER NOT NULL, 
	character VARCHAR(250), 
	person_id INTEGER, 
	movie_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(person_id) REFERENCES person (id), 
	FOREIGN KEY(movie_id) REFERENCES movie (id)
);
