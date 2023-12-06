import pytest
from project import create_random_question_list
from project import find_game_records
from project import find_player_records
import csv


def test_create_random_question_list():
    random_question_lsit = create_random_question_list()
    assert len(random_question_lsit) == 10

@pytest.fixture()
def score_file(tmp_path):
    score_file = tmp_path / "scores_testing.csv"
    score_file.write_text("Player's Name, Player's Highest Score, Game's Highest Score\n")
    return score_file


def test_find_game_records_filewithdata(score_file):
    score_file.write_text("John, 20, 30\nAlice, 40, 10\n Pedro, 40, 70\n")
    game_highest_score = find_game_records(score_file)
    assert int(game_highest_score) == 70


def test_find_game_records_filenotfound(tmp_path):
    score_file = tmp_path / "Nofilefound.csv"
    game_highest_score = find_game_records(score_file)
    assert game_highest_score == 0


def test_find_game_records_filefoundempty(score_file):
    game_highest_score = find_game_records(score_file)
    assert game_highest_score == 0


def test_find_player_records_namenotfound(score_file):
    score_file.write_text("John, 20, 30\nAlice, 40, 10\n John, 40, 70\n")
    name = "Pamela"
    player_highest_score = find_player_records(name, score_file)
    assert player_highest_score == 0


def test_find_player_records_namefound(score_file):
    with open(score_file, "w") as scores_file:
        info = [["Player's Name", "Player's Highest Score", "Game's Highest Score"],
                ["John", 20, 30],
                ["Alice", 40, 10],
                ["John", 40, 70]]
        writer = csv.writer(scores_file)
        writer.writerows(info)
        name = "John"
    player_highest_score = find_player_records(name, score_file)
    assert player_highest_score == 40
