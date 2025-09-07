from typing import Any

class Course:
    def __init__(self, name:str):
        self.name = name
        self.student_grades = []
    def get_grades(self) -> list[tuple[Any,float]]:
        return self.student_grades
    def get_average_grade(self) -> float:
        if not self.student_grades:
            return -1
        total_grades = sum(grade for _, grade in self.student_grades)
        return total_grades / len(self.student_grades)
    def __repr__(self):
        return f"{self.name}"

