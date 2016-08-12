# Game Design

### NDB Models

Code Path: `/models.py`

`Enum: GameStatus`

|    Value   | Number | 
|------------|--------|
| IN_SESSION |   1    |
| WON        |   2    |
| LOST       |   3    |
| ABORTED    |   4    |

`Model: User`

|      Key     |    Property    |
|--------------|----------------|
| user_name    | StringProperty |
| email        | StringProperty |
| display_name | StringProperty |
| mu           | FloatProperty  |
| sigma        | FloatProperty  |


`Model: Score`

|     Key    |    Property      |
|------------|------------------|
| score_id   | IntegerProperty  |
| game_key   | KeyProperty      |
| timestamp  | DateTimeProperty |
| game_score | IntegerProperty  |


`Model: Game`

|          Key          |     Property     |
|-----------------------|------------------|
| game_id               | IntegerProperty  |
| game_name             | StringProperty   |
| word                  | StringProperty   |
| guessed_chars_of_word | StringProperty   |
| guesses_left          | IntegerProperty  |
| game_over             | BooleanProperty  |
| game_status           | EnumProperty     |
| timestamp             | DateTimeProperty |


`Model: GameHistory`

|       Key      |      Property      |
|----------------|--------------------|
| step_timestamp | DateTimeProperty   |
| step_char      | StringProperty     |
| game_snapshot  | StructuredProperty |


---

### Messages/Resource Containers

For Contributors:  
All response messages and forms for resource container can be referred in `messages.py`  
Code Path: `/messages.py`



---


### Endpoints

 I have 3 APIs:

|  API  |  Path  | Ver.|                                         Endpoints                                                              |
|-------|--------|-----|----------------------------------------------------------------------------------------------------------------|
| User  | /user  | /v1 | /create_user, /get_user, /update_user, /delete_user                                                            |
| Score | /score | /v1 | /get_game_score, /get_user_scores, /get_all_scores, /get_user_ranking, /get_leaderboard                        |
| Game  | /game  | /v1 | /new_game, /get_game, /guess_char, /get_user_games, /get_user_completed_games, /cancel_game, /get_game_history |


---


### Scoring Impl

Current scoring logic is straight forward, no. of guesses left when player guesses the word is his/her score. But down the path we will have score game depending upon the word length/toughness.

---


### Ranking Impl

For ranking players, game is using [TrueSkill](http://trueskill.org/). 

TrueSkill is a rating system among game players. It was developed by Microsoft Research and has been used on Xbox LIVE for ranking and matchmaking service. This system quantifies players’ TRUE skill points by the Bayesian inference algorithm. It also works well with any type of match rule including N:N team game or free-for-all.

The game is using [Head-to-head (1 vs. 1)](http://trueskill.org/#head-to-head-1-vs-1-match-rule) match rule to rank players.


---


### Game Word Generator

For generating game words, project is using [RandomWords](https://pypi.python.org/pypi/RandomWords/0.2.0) python module.  

What were some of the trade-offs or struggles you faced when implementing the
new game logic?

- Firstly, on what game to implement, because the more the game deviated from
  the reference code base (hangman) the more work / complexity / time
  would be required to complete the project. I ultimately decided on
  hangman as it was quite a bit more complicated than guess-a-number,
  , but wasn't so complicated that it would takes months to complete. 


- There was quite a lot of thought (struggle) in deciding the games modes, but
  eventually just decided to implement both two and more players modes each
  with unique high scores.

- The idea of consecutive turns as a high score was appealing but didn't fit
  into traditional scores for either single or two player games, so decided to
  implement it as a bonus score for all game modes!

- I don't like writing duplicate code, but I had to trade-off a lean API for a broader
  range of endpoints with quite a bit of duplicate code. It seems that this is
  a problem with API endpoints in general though, where they tend to grow in
  the number of endpoints and duplicate code as time goes on to support ever
  growing functionality.
