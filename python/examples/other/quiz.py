import random
# Originally Created by Anna Uzonyi as a project for the course

true_values = ["T", "t", "True", "TRUE", "true", "1"]
false_values = ["F", "f", "False", "FALSE", "false", "0"]

def runchap(chapter):
    #questions, answers = chapter["q"], chapter["a"]
    quizzes = chapter["quiz"]
    counter=0
    for ix, quiz in enumerate(quizzes):
        print("\nQuestion {}".format(ix+1))
        inp = input(quiz["q"])
        answer = quiz["a"]
        ok = False
        if answer is True and inp in true_values:
            ok = True
        if answer is False and inp in false_values:
            ok = True
        if answer not in [True, False] and inp in answer:
            ok = True
        if ok:
            counter+=1
            print(random.choice(data['good']))
        else:
            print(random.choice(data['bad']))

    print("You gave " + str(counter) + " correct answers out of 3")

### define questions and answers as dictionary

import yaml

with open("quiz.yml") as fh:
    data = yaml.load(fh, Loader=yaml.Loader)
chapters = data['chapters']


while True:
    print(" \n**********************************************************************************")
    print("From which chapter do you want to be tested?")
    for idx, chapter in enumerate(chapters):
        print(f"{idx+1} {chapter['title']}")
    print("If you want to exit, press'x'.\nSelect a number: ")
    chapter = input()
    if chapter == "x":
        break
    elif chapter in list(map(str, range(len(chapters)))):
        print("Selected chapter: " + chapter)
        runchap(chapters[int(chapter)-1])
        continue
    else:
        print("wrong, choose only from ", [key for key in content.keys()]+["x"])
