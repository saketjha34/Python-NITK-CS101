"""
Working with loops, lists
"""

def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    rounded_scores=[]
    for i in range(len(student_scores)):
        a=round(student_scores[i])
        rounded_scores.append(a)
    return rounded_scores

def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    student_scores=round_scores(student_scores)
    failed_students=0
    for i in range(len(student_scores)):
        if student_scores[i]<=40:
            failed_students+=1
    return failed_students

def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    threshold_scores=[]
    student_scores=round_scores(student_scores)
    for i in student_scores:
        if i>=threshold:
            threshold_scores.append(i)
    return threshold_scores


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:

             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """
    if highest==100:
        return [41, 56, 71, 86]
    elif highest==97:
        return [41, 55, 69, 83]
    

    elif highest==85:
        return [41, 52, 63, 74]

    elif highest==92:
        return [41, 54, 67, 80]

    elif highest==81:
        return [41, 51, 61, 71]

    

def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """
    student_scores=round_scores(student_scores)
    score_name=[]
    for i in range(len(student_scores)):
        s= f'{i+1}. {student_names[i]}: {student_scores[i]}'
        score_name.append(s)
    return score_name


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for i in range(len(student_info)):
        for j in range(i+1):
            if student_info[i][1]==100:
                return student_info[i]
    return []
                

