import re

from exceptions.employee_exceptions import InvalidAgeError, InvalidSalaryError


EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def validate_age(age: int) -> int:
    if not 18 <= age <= 65:
        raise InvalidAgeError("Tuổi phải nằm trong khoảng 18-65")
    return age


def validate_salary(salary: float) -> float:
    if salary <= 0:
        raise InvalidSalaryError("Lương phải lớn hơn 0")
    return salary


def validate_email(email: str) -> str:
    if not EMAIL_PATTERN.match(email):
        raise ValueError("Email không đúng định dạng")
    return email


def validate_performance(score: float) -> float:
    if not 0 <= score <= 10:
        raise ValueError("Điểm hiệu suất phải trong khoảng 0-10")
    return score


def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ.")


def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")
