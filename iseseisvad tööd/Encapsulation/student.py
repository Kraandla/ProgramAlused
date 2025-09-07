"""Encapsulation exercise."""


class Student:
    """Represents student information."""
    STATUSES_ACTIVE = "Active"
    STATUS_EXPELLED = "Expelled"
    STATUS_FINISHED = "Finished"
    STATUS_INACTIVE = "Inactive"
    statuses = [STATUSES_ACTIVE, STATUS_EXPELLED, STATUS_FINISHED, STATUS_INACTIVE]

    def __init__(self, name: str, student_id: int):
        """Initation."""
        self.__name = name
        self.__id = student_id
        self.__status = Student.STATUSES_ACTIVE

    def get_id(self) -> int:
        """Get student id."""
        return self.__id

    def set_name(self, name: str) -> None:
        """Set student name."""
        self.__name = name

    def get_name(self) -> str:
        """Get student name."""
        return self.__name

    def set_status(self, status: str):
        """Set status."""
        if status in Student.statuses:
            self.__status = status

    def get_status(self) -> str:
        """Get status."""
        return self.__status
