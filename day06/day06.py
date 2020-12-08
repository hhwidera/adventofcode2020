import string

input_file = open("input.txt", "r")

group_answered_list = input_file.read().split("\n\n")

print("Part 1")
sum = 0
for group_answered in group_answered_list:
    group_sum = 0
    for question in list(string.ascii_lowercase):
        if question in group_answered:
            group_sum += 1
    print(group_sum)
    sum += group_sum

print("Sum:", sum)

print("Part 2")
sum = 0
for group_answered in group_answered_list:
    group_sum = 0
    yes_questions = set(list(string.ascii_lowercase))
    for person_answered in group_answered.splitlines():
        person_yes_question = set()
        for question in yes_questions:
            if question in person_answered:
                person_yes_question.add(question)
        yes_questions = person_yes_question
    group_sum = len(yes_questions)
    print(group_sum)
    sum += group_sum

print("Sum:", sum)
