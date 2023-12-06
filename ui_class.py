import csv
import tkinter
import sys
import random


class UI(tkinter.Tk):
    def __init__(self, name, random_question_list, player_record, game_highest_score):
        self.player_name = name
        self.player_highest_score = player_record
        self.game_highest_score = game_highest_score
        self.remaining_time = 15
        self.question_number = 1
        self.score = 0

        self.questions_list = random_question_list
        self.chosen_answer = ""
        self.question = ""
        self.option1 = ''
        self.option2 = ''
        self.option3 = ''
        self.option4 = ''

        super().__init__()
        self.title("Test Your Bible Knowledge")
        self.config(width=800, height=800, background="aqua")
        self.create_welcome_canvas(self.player_name)

    def create_welcome_canvas(self, name):
        self.wl_canvas = tkinter.Canvas(width=600, height=600, background="#98E4FF")
        self.wl_canvas.pack()

        self.canvas_center_x = self.wl_canvas.winfo_reqwidth() // 2
        self.canvas_center_y = self.wl_canvas.winfo_reqheight() // 2

        self.wl_label = tkinter.Label(self.wl_canvas, text=f"Welcome {name} 🙂", background="#98E4FF",
                                      font=("Arial", 30, "bold"))
        self.wl_label.place(relx=0.5, rely=0.3, anchor="center")

        self.instructions_label = tkinter.Label(self.wl_canvas, text=
        "1. Read each qustion carefully.\n"
        "2. Choose the correct answer.\n"
        "3. After answering all of the questions, you will see the result", background="#98E4FF", font=("Arial", 15))
        self.instructions_label.place(relx=0.5, rely=0.5, anchor="center")

        self.gl_label = tkinter.Label(self.wl_canvas, text="GOOD LUCK", foreground="orange", background="#98E4FF",
                                      font=("Arial", 30, "bold"))
        self.gl_label.place(relx=0.5, rely=0.65, anchor="center")

        self.ready_button = tkinter.Button(self.wl_canvas, text="Ready", command=self.start_game, width=20, height=3,
                                           background="#16FF00",
                                           font=(50))
        self.ready_button.place(relx=0.5, rely=0.8, anchor="center")

        self.mainloop()

    def start_game(self):
        self.wl_canvas.destroy()
        self.create_ui()

    def create_ui(self):
        self.new_question()
        self.main_canvas = tkinter.Canvas(width=800, height=800).place()
        self.info_sec1 = tkinter.Canvas(self.main_canvas, width=400, height=200, background="aqua",
                                        highlightthickness=0)
        self.info_sec1.grid(row=0, column=0, sticky="w", pady=(15, 0))

        self.info_sec2 = tkinter.Canvas(self.main_canvas, width=400, height=200, background="aqua",
                                        highlightthickness=0)
        self.info_sec2.grid(row=0, column=1)

        # ------------Info section

        self.player_name_label = tkinter.Label(self.info_sec1, background="aqua",
                                               text=f"Player Name: {self.player_name}", font=("arial", 20))
        self.player_name_label.grid(row=0, column=0, padx=(20, 0), pady=(15, 0), sticky="w")

        self.player_highscore_label = tkinter.Label(self.info_sec1, background="aqua",
                                                    text=f"Your best score: {self.player_highest_score}",
                                                    font=("arial", 20))
        self.player_highscore_label.grid(row=1, column=0, padx=(20, 0), pady=5, sticky="w")

        self.game_highest_score_label = tkinter.Label(self.info_sec1, background="aqua",
                                                      text=f"Highest score: {self.game_highest_score}",
                                                      font=("arial", 20))
        self.game_highest_score_label.grid(row=2, column=0, padx=(20, 0), pady=(0, 15), sticky="w")

        self.time_label = tkinter.Label(self.info_sec2, text="Time", background="aqua", font=("arial", 30))
        self.time_label.grid(row=0, column=1)

        self.question_tracker_label = tkinter.Label(self.info_sec2, text=f'{self.question_number}/10',
                                                    background="aqua", font=("arial", 15))
        self.question_tracker_label.grid(row=2, column=1, pady=(20, 0))

        # ---------------------------------------- Question Sec (row 2/3, column 0/0)

        self.question_sec = tkinter.Canvas(self.main_canvas, width=800, height=400, bg="light blue",
                                           highlightthickness=5)
        self.question_sec.grid(row=1, column=0, columnspan=2)

        self.question_label = tkinter.Label(self.question_sec, text=self.question, bg="light blue", font=("arial", 30),
                                            wraplength=700)
        self.question_label.place(relx=0.5, rely=0.5, anchor="center")

        # ---------------------------------------- Options Sec (row 3/3, column 0/0)

        # ------------Left side options

        self.options_sec_l = tkinter.Canvas(self.main_canvas, width=400, height=200, background="aqua",
                                            highlightthickness=0)
        self.options_sec_l.grid(row=2, column=0, pady=20)

        self.option1_button = tkinter.Button(self.options_sec_l, width=25, height=2, text=self.option1, wraplength=350,
                                             relief="solid", font=("arial", 20))
        self.option1_button.place(relx=0, rely=0)
        self.option1_button.bind("<Button-1>", self.on_button_click)

        self.option2_button = tkinter.Button(self.options_sec_l, width=25, height=2, text=self.option2, wraplength=350,
                                             relief="solid", font=("arial", 20))
        self.option2_button.place(relx=0, rely=0.5)
        self.option2_button.bind("<Button-1>", self.on_button_click)

        # # ------------Right side options

        self.options_sec_r = tkinter.Canvas(self.main_canvas, width=400, height=200, background="aqua",
                                            highlightthickness=0)
        self.options_sec_r.grid(row=2, column=1, pady=20)

        self.option3_button = tkinter.Button(self.options_sec_r, width=25, height=2, text=self.option3, wraplength=350,
                                             relief="solid", font=("arial", 20))
        self.option3_button.place(relx=0, rely=0)
        self.option3_button.bind("<Button-1>", self.on_button_click)

        self.option4_button = tkinter.Button(self.options_sec_r, width=25, height=2, text=self.option4, wraplength=350,
                                             relief="solid", font=("arial", 20))
        self.option4_button.place(relx=0, rely=0.5)
        self.option4_button.bind("<Button-1>", self.on_button_click)

        self.check_remaining_time()

    def update_ui(self):
        self.next_question()
        self.question_label.config(text=self.question)
        self.question_tracker_label.config(text=f'{self.question_number}/10')

        self.option1_button.config(text=self.option1)
        self.option2_button.config(text=self.option2)
        self.option3_button.config(text=self.option3)
        self.option4_button.config(text=self.option4)
        self.check_remaining_time()

    def check_answer(self, chosen_answer):
        if self.correct_answer == self.chosen_answer:
            self.score += 10
            self.question_number += 1
            self.update_ui()

        else:
            self.question_number += 1
            self.update_ui()

    def check_remaining_time(self):
        if 10 <= int(self.remaining_time):
            self.time_label.config(text=f"Time: 00:{self.remaining_time}")
            self.remaining_time -= 1
            self.timer_id = self.after(1000, self.check_remaining_time)

        elif 0 < self.remaining_time < 10:
            self.time_label.config(text=f"Time: 00:0{self.remaining_time}")
            self.remaining_time -= 1
            self.timer_id = self.after(1000, self.check_remaining_time)
        elif self.remaining_time == 0:
            self.question_number += 1
            self.reset_time()
            self.update_ui()

    def reset_time(self):
        self.remaining_time = 15

    def on_button_click(self, event):
        self.after_cancel(self.timer_id)
        self.reset_time()
        self.chosen_answer = event.widget["text"]
        self.check_answer(self.chosen_answer)

    def next_question(self):
        if self.question_number < 11:
            # self.question_number += 1
            self.question, self.correct_answer, self.option1, self.option2, self.option3, self.option4 = self.new_question()
            return self.question, self.correct_answer, self.option1, self.option2, self.option3, self.option4
        elif self.question_number == 11:
            self.end_the_game()

    def end_the_game(self):
        self.destroy()
        self.show_result()

    def show_result(self):
        self.update_score_file()

        self.result_canvas = tkinter.Canvas(width=600, height=600, background="#FAFAD2")
        self.result_canvas.pack()
        self.canvas_center_x = self.result_canvas.winfo_reqwidth() // 2
        self.canvas_center_y = self.result_canvas.winfo_reqheight() // 2

        self.instructions_label = tkinter.Label(self.result_canvas, text="Game Over", background="#FAFAD2",
                                                font=("Arial", 30))
        self.instructions_label.place(relx=0.5, rely=0.3, anchor="center")

        self.your_score_label = tkinter.Label(self.result_canvas, text=f"Your score: {self.score} out of 100 🙂",
                                              background="#FAFAD2", font=("Arial", 20, "bold"))
        self.your_score_label.place(relx=0.5, rely=0.5, anchor="center")

        self.end_game_button = tkinter.Button(self.result_canvas, text="Exit", command=self.exit_game, width=20,
                                              height=3, background="lightcoral", font=(50))
        self.end_game_button.place(relx=0.5, rely=0.7, anchor="center")

        self.mainloop()

    def new_question(self):
        self.question = self.questions_list[0][0]
        self.correct_answer = self.questions_list[0][1]
        options = []
        for i in range(1, 5):
            options.append(self.questions_list[0][i])
        random.shuffle(options)
        self.option1 = options[0]
        self.option2 = options[1]
        self.option3 = options[2]
        self.option4 = options[3]
        self.questions_list.remove(self.questions_list[0])
        return self.question, self.correct_answer, self.option1, self.option2, self.option3, self.option4

    def update_score_file(self):
        if int(self.score) > int(self.game_highest_score):
            self.game_highest_score = self.score
        new_record = []
        new_record.append(self.player_name)
        new_record.append(self.score)
        new_record.append(self.game_highest_score)
        with open("scores.csv", "a", newline="\n") as score_csv_file:
            writer = csv.writer(score_csv_file)
            writer.writerow(new_record)

    def exit_game(self):
        sys.exit()
