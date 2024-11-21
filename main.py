def quiz():
    print("Welcome to the Quiz")
    score = 0
    start = input("Type begin to start the quiz:")
    if start == "begin":
        q1 = int(input("What is 3*7:"))
        if q1 == 21:
            print("Correct")
            score = score + 2
        else:
            print("incorrect")
        q2 = input("When an apple fell from a tree what did Newton discover:")
        if q2 == "gravity":
            print("Correct")
            score = score + 2
        else:
            print("Incorrect")
        q3 = input("What year is it:")
        if q3 == "2024":
            print("Correct")
            score = score + 2
        else:
            print("Incorrect")
        q4 = input("Who is the president of USA:")
        if q4 == "trump":
            print("Correct")
            score = score + 2
        else:
            print("Incorrect")
        q5 = input("What rhymes with orange:")
        if q5 == "nothing":
            print("Correct")
            score = score + 2
        else:
            print("Incorrect")
        print("You finished the quiz your score is:", score*10,"%")
quiz()