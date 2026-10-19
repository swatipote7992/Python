# Tennis
# This Kata is about implementing a simple tennis game.
# Rather than using standard Tennis scoring, we consider scoring in Wii tennis, which has a simplified version of tennis, so each set is one game.
# The scoring system is as follows:
# Each player can have either of these points in one game 0 15 30 40
# If you have 40 and you win the ball you win the game, however there are special rules.
# If both have 40 the players are deuce.
# a. If the game is in deuce, the winner of a ball will have advantage and game ball.
# b. If the player with advantage wins the ball they win the game
# c. If the player without advantage wins they are back at deuce.
# Alternative description of rules
# A game is won by the first player to have won at least four points in total and at least two points more than the opponent.
# The running score of each game is described in a manner peculiar to tennis: scores from zero to three points are described as “love”, “fifteen”, “thirty”, and “forty” respectively.
# If at least three points have been scored by each player, and the scores are equal, the score is “deuce”.
# If at least three points have been scored by each side and a player has one more point than their opponent, the score of the game is “advantage” for the player in the lead.

from tennis import TennisGame


# new game - Love-All
def test_new_game_is_love_all():
    game = TennisGame()
    assert game.score() == "Love-All"


# player 1 score - Fifteen-Love
def test_player1_scores_once_is_fifteen_love():
    game = TennisGame()
    game.point_won_by("player1")
    assert game.score() == "Fifteen-Love"


# player 2 score - Love-Fifteen
def test_player2_score_once_is_love_fifteen():
    game = TennisGame()
    game.point_won_by("player2")
    assert game.score() == "Love-Fifteen"


# if both score, Fifteen-All
def test_both_score_once_is_fifteen_all():
    game = TennisGame()
    game.point_won_by("player1")
    game.point_won_by("player2")
    assert game.score() == "Fifteen-All"


## If at least three points have been scored by each player, and the scores are equal, the score is “deuce”.
def test_three_points_each_is_deuce():
    game = TennisGame()
    for _ in range(3):
        game.point_won_by("player1")
        game.point_won_by("player2")
    assert game.score() == "Deuce"


# when both players have at least 3 points and one leads by exactly 1
def test_player1_ahead_by_one_after_deuce_is_advantage():
    game = TennisGame()
    for _ in range(3):
        game.point_won_by("player1")
        game.point_won_by("player2")
    game.point_won_by("player1")
    assert game.score() == "Advantage player1"


# Advantage player win, they win game
def test_player1_wins_four_points_to_love():
    game = TennisGame()
    for _ in range(4):
        game.point_won_by("player1")
    assert game.score() == "Win for player1"


# player2 wins, from deuce.
def test_player2_wins_after_deuce():
    game = TennisGame()
    for _ in range(3):
        game.point_won_by("player1")
        game.point_won_by("player2")
    game.point_won_by("player2")
    game.point_won_by("player2")
    assert game.score() == "Win for player2"


# back to deuce. Advantage, then the other player scores
def test_advantage_then_opponent_scores_is_deuce():
    game = TennisGame()
    for _ in range(3):
        game.point_won_by("player1")
        game.point_won_by("player2")
    game.point_won_by("player1")
    game.point_won_by("player2")
    assert game.score() == "Deuce"


def test_forty_thirty():
    game = TennisGame()
    for _ in range(3):
        game.point_won_by("player1")
    for _ in range(2):
        game.point_won_by("player2")
    assert game.score() == "Forty-Thirty"


def test_long_deuce_game_player1_wins():
    game = TennisGame()
    for _ in range(5):
        game.point_won_by("player1")
        game.point_won_by("player2")
    game.point_won_by("player1")
    game.point_won_by("player1")
    assert game.score() == "Win for player1"
