-- Create table to store user ids and names --
CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, hash TEXT NOT NULL, spoon_total NUMERIC NOT NULL DEFAULT 15);
CREATE UNIQUE INDEX username ON users (username);

-- Create table to store activities and default "spoon" values --
CREATE TABLE activities (activity_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title TEXT NOT NULL, summary TEXT NOT NULL, graphic TEXT NOT NULL, def_val INTEGER NOT NULL DEFAULT 3);
CREATE UNIQUE INDEX title ON activities (title);

-- Create table to store graphics --
CREATE TABLE graphics (graphic_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, graphic_name TEXT NOT NULL, path TEXT NOT NULL);
CREATE UNIQUE INDEX graphic_name ON graphics (graphic_name);

-- Create table to store profiles --
CREATE TABLE profiles (profile_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, user INTEGER NOT NULL, activity INTEGER NOT NULL, user_value INTEGER NOT NULL)
CREATE UNIQUE INDEX profile_id ON profiles (profile_id);