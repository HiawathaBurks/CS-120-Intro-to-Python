#created by Hiawatha B
#Q2 Module
def calculateAverage(score1,score2,score3,score4,score5):

    avgerageScore = (score1 + score2 + score3 + score4 + score5)/5
    return avgerageScore

def determineGrade(score):
    if(score<50):
        return 'F'
    elif(score<60):
        return 'E'
    elif(score<70):
        return 'D'
    elif(score<80):
        return 'C'
    elif(score<90):
        return 'B'
    elif(score<=100):
        return 'A'
    else:
        return 'Not a Valid Score Entered'
