class Grade:
    def __init__(self, student):
        self.student = student
        self.result = None


def mark_student(grade, mark):
    if mark < 50:
        grade.result = "fail"
    elif mark < 65:
        grade.result = "pass"
    elif mark < 75:
        grade.result = "credit"
    elif mark < 85:
        grade.result = "distinction"
    elif mark <= 100:
        grade.result = "high distinction"


# For testing
def test(student, mark, result):
    mark_student(student, mark)
    assert student.result == result

test(Grade("James"),   15, "fail")
test(Grade("Billy"),   51, "pass")
test(Grade("Matthew"), 65, "credit")
test(Grade("Tim"),     80, "distinction")
test(Grade("Bob"),     97, "high distinction")