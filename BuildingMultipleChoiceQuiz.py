from Question import Question

question_prompts = [
    "What color are apples?\nA Red/Green\nB Purple\nC Orange\n\n",
    "What color are bananas?\nA Teal\nB Magenta\nC Yellow\n\n",
    "What color are strawberries?\nA Yellow\nB Red\nC Blue\n\n"
]

questions = [
    Question(question_prompts[0], "A"),
    Question(question_prompts[1], "C"),
    Question(question_prompts[2], "B")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)