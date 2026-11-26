

def calculate_grade_stats(student_list, pass_threshold=50):
    passed_students = []
    total_score = 0
    passed_score_total = 0


    for students in student_list:
        score = float(students['score'])
        if score >= pass_threshold:
            passed_students.append(students['name'])
            passed_score_total += score
        total_score += score

    avg = passed_score_total / len(passed_students) if len(passed_students) > 0 else 0

    return {
        'average': avg,
        'passed': passed_students,
        'total_count': len(student_list)
    }


def print_summary(stats_dict, courseName="Python 101"): 
    print(" === Summary for " + courseName + " === ")
    print("Average Score: " + str(stats_dict['average']))
    print("Passed Students: " + ", ".join(stats_dict['passed']))


data =[
    {'name': 'Charlie', 'score': '85.5'},
    {'name': 'River', 'score': '42.0'},
    {'name': 'Jordan', 'score': '68.0'}
]
result = calculate_grade_stats(data)
print_summary(result)