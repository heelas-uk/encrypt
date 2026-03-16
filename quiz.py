import time as time
play = True
while play == True:
        score = 0

        questions = ["What is the capital city of Australia?", "Who painted the famous artwork Mona Lisa?", "Which planet is known as the Red Planet?", "In which year did the First Moon Landing occur?", "Which ocean is the largest on Earth?"]

        choices = ["A. Sydney\nB. Melbourne\nC. Canberra\nD. Brisbane\n", "A. Pablo Picasso\nB. Leonardo da Vinci\nC. Vincent van Gogh\nD. Michelangelo\n", "A. Venus\nB. Mars\nC. Jupiter\nD. Saturn\n", "A. 1965\nB. 1967\nC. 1969\nD. 1971\n", "A. Atlantic Ocean\nB. Indian Ocean\nC. Pacific Ocean\nD. Arctic Ocean\n"]

        answers = ["C", "B", "B", "C", "C"]




        print("Welcome to the game")
        if int(input("1. Start Quiz \n2. Quit\n")) == 2:
                exit(0)
        else:
                1+1
        print("Starting quiz in 3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)

        ans = input(questions[0] + "\n" + choices[0])
        if ans == answers[0]:
                print("Correct yipee")
                score += 1 
        ans = input(questions[1] + "\n" + choices[1])
        if ans == answers[1]:
                print("Correct yipee")
                score += 1 
        ans = input(questions[2] + "\n" + choices[2])
        if ans == answers[2]:
                print("Correct yipee")
                score += 1 
        print("Your score is "+ str(score))
        if input("1.Yes\n2.No") == '1':
                print("Yay")
        else: quit(0)