total_questions = 0
correct = 0

questionnaire = [["What is the capital of Norway? ", "Oslo"], ["What is the capital of Finnland? ", "Helsinki"]]

for question_answer_pair in questionnaire:
    question = question_answer_pair[0]
    answer = input(question)
    correct_answer = question_answer_pair[1]
    if answer == correct_answer:
        print("Correct!")
        correct += 1
    else:
        print("Wrong!")
    total_questions += 1

print("Correctly answered " + str(correct) + " out of " + str(total_questions) + " questions.")



