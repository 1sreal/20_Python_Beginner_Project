quiz = {
    "question1": {
        "question": "How many regions are in ghana",
        "answer": "16"
    },
    "question2": {
      "question": "What is the capital town of western north region ",
        "answer" : "sefwi wiaso"  
    },
    "question3": {
        "question": "How many years did the first president of the Republic of Ghana rule?",
        "answer" : "11"
    }   
}
score = 0
for key, value in quiz.items():
     print(value['question'])
     answer = input ("Answer? ")

     if answer.lower() == value ['answer'].lower():
        print ('Correct')
        score = score + 1
        print("you're score is " + str(score))
     else:
        print("Wrong!! ")
        print("the answer is: " + value['answer'])
        print("Your score is: " + str(score))
