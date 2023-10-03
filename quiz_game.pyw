from tkinter import Tk, PhotoImage, Frame, Label, Button
from questions import *

root = Tk()
root.geometry('600x700')
root.resizable(0, 0)


starting_score = 0
top_score = 0
count = 1
scoring = 0
scoring_values = []
scoring_keys = []
score_key = 0


def record(rank):
    global score_key
    scores = open('scores.txt', 'a')
    scores.write("{}:{}\n".format(score_key, scoring))
    scores.close()

    global scoring_values
    scores = open('scores.txt', 'r')
    for line in scores:
        k, v = line.rstrip("\n").split(":")
        scoring_keys.append(int(k))
        scoring_values.append(int(v))
        score_key += 1
    scores.close()

    if scoring_values:
        scoring_values = list(set(scoring_values))
        rank = max(scoring_values)
        best_score.config(text="Top score: {}".format(rank))

def true():
    answer1.config(state='disable')
    answer2.config(state='disable')
    if count <= 20:
        next_button.config(state='normal')
        global scoring
        for k, v in answers.items():
            if k == count:
                if v == 1:
                    scoring += 1
                    score.config(text="Score: {}".format(scoring))

    if count == 21:
        record(top_score)

def false():
    answer1.config(state='disable')
    answer2.config(state='disable')
    if count <= 20:
        next_button.config(state='normal')
        global scoring
        for k, v in answers.items():
            if k == count:
                if v == 0:
                    scoring += 1
                    score.config(text="Score: {}".format(scoring))

    if count == 21:
        record(top_score)

def next_question(number):
    next_button.config(state='disabled')
    answer1.config(state='normal')
    answer2.config(state='normal')
    global count
    if number == 2:
        question.config(text=q2)
        count += 1
    elif number == 3:
        question.config(text=q3)
        count += 1
    elif number == 4:
        question.config(text=q4)
        count += 1
    elif number == 5:
        question.config(text=q5)
        count += 1
    elif number == 6:
        question.config(text=q6)
        count += 1
    elif number == 7:
        question.config(text=q7)
        count += 1
    elif number == 8:
        question.config(text=q8)
        count += 1
    elif number == 9:
        question.config(text=q9)
        count += 1
    elif number == 10:
        question.config(text=q10)
        count += 1
    elif number == 11:
        question.config(text=q11)
        count += 1
    elif number == 12:
        question.config(text=q12)
        count += 1
    elif number == 13:
        question.config(text=q13)
        count += 1
    elif number == 14:
        question.config(text=q14)
        count += 1
    elif number == 15:
        question.config(text=q15)
        count += 1
    elif number == 16:
        question.config(text=q16)
        count += 1
    elif number == 17:
        question.config(text=q17)
        count += 1
    elif number == 18:
        question.config(text=q18)
        count += 1
    elif number == 19:
        question.config(text=q19)
        count += 1
    elif number == 20:
        question.config(text=q20)
        count += 1
    elif number == 21:
        question.config(text=q21)
        count += 1

score = Label(root, text="Score: {}".format(starting_score), font=('vijaya', 25, 'bold'), fg='gray30')
score.grid(row=0, column=0, sticky='w')

best_score = Label(root, text="Top score: {}".format(top_score), font=('vijaya', 25, 'bold'), fg='gray30')
best_score.grid(row=0, column=0, sticky='e', padx=10)

name = Label(root, text='QUIZ GAME', font=('jasmine upc', 20, 'bold'), fg='snow4')
name.grid(row=0, column=0, sticky='n')

my_image = PhotoImage(file='png\\mind.png')
my_label = Label(root, image=my_image)
my_label.grid(row=1, column=0)

my_frame = Frame(root, bg='snow3')
my_frame.grid(row=2, column=0, columnspan=3)

question = Label(my_frame, text=q1, font=('gabriola', 25, 'bold'), bd=0, bg='snow3', fg='gray20')
question.pack(fill='both', expand=True)

answer1= Button(my_frame, text="TRUE ", font=('times new roman', 25), fg='gray20', bg='azure4', bd=1, command=true)
answer2= Button(my_frame, text="FALSE", font=('times new roman', 25), fg='gray20', bg='azure4', bd=1, command=false)
next_button= Button(root, text="NEXT", font=('times new roman', 25, 'bold'), fg='gray30', bg='snow3', bd=1, state='disabled', command=lambda:next_question(count+1))

answer1.pack(side='left', ipadx=25)
answer2.pack(side='right', ipadx=25)
next_button.grid(row=3, column=0, sticky='s', pady=35, ipadx=55)

record(top_score)

root.mainloop()
