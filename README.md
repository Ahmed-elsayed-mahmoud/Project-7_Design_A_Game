# Design A Game (Hangman)

A scalable game(hangman) architected as a Web Service API using Google App Engine backed by Google Datastore.



## Project Overview

Hangman is a paper and pencil guessing game for two or more players. One player thinks of a word, phrase or sentence and the other tries to guess it by suggesting letters or numbers, within a certain number of guesses.

This implementation is a one player game. The word is provided by the app and player has to guess char in every step, if user is unable to guess the word in 6 steps player looses.

For more information on game, check wikipedia page [here](https://en.wikipedia.org/wiki/Hangman_%28game%29)


### Scoring

As of now scoring logic of the game is simple, no. of guesses left when player guesses the word is his/her score. For e.g. if player guesses the word when 'guesses left' is 5, the score of that game is 5.

The maximum player can score in a game is 6 and minimum is 1. Player scores 0 for lost or aborted games.

---


### Ranking

Ranking of players on the other hand is very complex and it uses python module [TrueSkill](http://trueskill.org/) for ranking of players.

TrueSkill is a rating system among game players. It was developed by Microsoft Research and has been used on Xbox LIVE for ranking and matchmaking service. This system quantifies players’ TRUE skill points by the Bayesian inference algorithm. It also works well with any type of match rule including N:N team game or free-for-all.

Player is ranked using TrueSkill's 'A Bayesian Skill Rating System', it is difficult to explain how it is done in this readme file so to further understand the algorithm read ['Further More'](http://trueskill.org/#further-more) section in trueskill.org. 

---


### How to access APIs

Read full API usage [here](api_usage.md)  

---

### Cron Job

`/crons/send_email_reminders`  
Send reminders to players who have not made any move in past 24 hrs.  
Scheduled everyday at: `06:00 GMT`  

---

### Design Document

The design document is [here](design.md)
