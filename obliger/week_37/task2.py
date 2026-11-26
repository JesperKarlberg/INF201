


def process_class_scores(scores: list[float], pass_threshold: float = 50.0) -> float:
    # returns the average of all passing scores, or 0.0 if nobody passes

    passing_scores = []

    for score in scores:
        if score >= pass_threshold:
            passing_scores.append(score) 


    if len(passing_scores) == 0:
        return 0.0


    avg = sum(passing_scores) / len(passing_scores)
    return avg


student_scores = [45, 30, 85, 90, 25, 10, 60]
avg = process_class_scores(student_scores)
print(f"Average: {avg:.2f}")

