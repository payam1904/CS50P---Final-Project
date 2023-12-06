from ui_class import UI
import csv
import random
import tkinter
from tkinter import messagebox
import tkinter.simpledialog
import re
from pathlib import Path

csv_file = Path("scores.csv")

def get_player_name():
    name = tkinter.simpledialog.askstring("Name", "Who is playing?")
    if len(name) == 0:
        response1 = messagebox.askyesno(title="Warning",
                                        message="You haven't entered any name. Do you want to play as guest? ")
        if response1:
            player_name = "Guest"
            return player_name
        elif response1 == False:
            return get_player_name()

    elif re.search("[^A-Za-z]", name):
        response2 = messagebox.askyesno(title="Warning",
                                        message="Your name must only contain alphabetic cahracters. Do you want to try again? ")
        if response2:
            return get_player_name()

        elif response2 == False:
            messagebox.showinfo(title="Info", message="You will be playing as guest ")
            player_name = "Guest"
            return player_name
    else:
        player_name = name.title()
        return player_name

def create_random_question_list():
    random_question_list = []
    with open("questions.csv", "r") as csv_file:
        question_object = csv.reader(csv_file)
        next(question_object)
        questions_file = []
        for q in question_object:
            questions_file.append(q)
        random.shuffle(questions_file)

        for i in range (0, 10):
            questions_file[i].remove(questions_file[i][0])
            random_question_list.append(questions_file[i])
        return random_question_list

def find_game_records(csv_file):
    game_recs = []
    game_highest_score = 0
    try:
        with open(csv_file, "r") as scores:
            csv_lines = csv.reader(scores)
            next(csv_lines)
            for line in csv_lines:
                game_recs.append(line[2])
                if int(line[2]) > int(game_highest_score):
                    game_highest_score = line[2]

        return game_highest_score

    except (FileNotFoundError, IndexError):
        with open("scores.csv", "w", newline="\n") as scores:
            writer = csv.writer(scores)
            header_row = ["Player Name", "Player's Highest Score", "Highest Score"]
            writer.writerow(header_row)
            return game_highest_score

def find_player_records(name, csv_file):
    with open(csv_file, "r") as scores:
        csv_lines = csv.reader(scores)
        next(csv_lines)

        player_highest_score = 0
        for line in csv_lines:
            if name in line:
                if int(line[1]) > int(player_highest_score):
                    player_highest_score = int(line[1])

        return player_highest_score


def main():
    name = get_player_name()
    random_question_list = create_random_question_list()
    game_highest_score = find_game_records(csv_file)
    player_record = find_player_records(name, csv_file)
    quiz = UI(name, random_question_list, player_record, game_highest_score)

    quiz.mainloop()


if __name__ == "__main__":
    main()