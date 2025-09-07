from course import Course

class Student:
    def __init__(self, name:str):
        self.name = name
        self.id = None
        self.grades = {}
    def set_id(self, int: int):
        self.id = int
    def get_id(self) -> int:
        return self.id
    def get_grades(self)-> list[tuple[Course,int]]:
        result = []
        for course, grades_list in self.grades.items():
            for grade in grades_list:
                result.append((course, grade))
        return result

    def get_average_grade(self):
        if not self.grades:
            return -1
        total_grades = 0
        count = 0
        for grade_list in self.grades.values():
            total_grades += sum(grade_list)
            count += len(grade_list)
        return total_grades / count if count > 0 else 0

    def __repr__(self) -> str:
        return f"{self.name}"

