## Table of contents
* [General info](#general-info)
* [Dependencies](#Dependencies)
* [Create Database](#Create-Database)
* [Setup](#setup)


## General info
This project is a Plagiarism Detector that determines the category under which the test document falls and returns it similarity score (plagiarism score).

Group members are :

Tanay Gupta : 2018AAPS0343H : https://github.com/Tanay0101\

Mudit Chaturvedi : 2018A7PS0248H : https://github.com/TheRhetorician\

Sristi Sharma : 2018A7PS0299H : https://github.com/judyhopps24\
	
## Dependencies
Dependencies in the Project :
* nltk 
* nltk english stopwords
* porters stemming
* flask

##Create Database
$ cd ../directory
$ pip install flask
$ pip install nltk
* In the create database file set path to the directory which contains all the documents and mention the category of each document
$ python create_database.py

## Setup
To run this project, install it locally using pip (package manager for python):

```
$ cd ../directory
$ python app.py

```
