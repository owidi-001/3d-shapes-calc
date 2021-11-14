# A program that calculates the average quiz scores and letter grade
# Date: 10/24/2021
# Author: Kevin Owidi

# display a welcome or title message
print("Average Scores Calculator")
print()


# get scores from the user
def get_scores(quiz_num):
    score = int(input("Please enter the quiz #" + quiz_num + " score: "))
    return score

# calculate the average score and display it
def calc_average(score1, score2, score3):
    average = (score1 + score2 + score3) / 3
    # test the average score against the range for each letter
    if average >= 90:
        letter_grade = "A"
    elif average >= 80:
        letter_grade = "B"
    elif average >= 70:
        letter_grade = "C"
    elif average >= 60:
        letter_grade = "D"
    else:
        letter_grade >= "F"
    print("Your quiz average is:", round(average, 2), "and your letter grade is:", letter_grade)
#function calls
score1 = get_scores("1")
score2 = get_scores("2")
score3 = get_scores("3")
calc_average(score1,score2,score3)