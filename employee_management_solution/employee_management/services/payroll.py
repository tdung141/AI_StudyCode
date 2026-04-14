from typing import List

from models.employee import Employee


def total_company_salary(employees: List[Employee]) -> float:
    return sum(emp.calculate_salary() for emp in employees)


def top_paid_employees(employees: List[Employee], top_n: int = 3) -> List[Employee]:
    return sorted(employees, key=lambda emp: emp.calculate_salary(), reverse=True)[:top_n]


def count_by_role(employees: List[Employee]) -> dict:
    result = {"Manager": 0, "Developer": 0, "Intern": 0}
    for emp in employees:
        result[emp.get_role()] = result.get(emp.get_role(), 0) + 1
    return result


def salary_by_department(employees: List[Employee]) -> dict:
    result = {}
    for emp in employees:
        result.setdefault(emp.department, 0)
        result[emp.department] += emp.calculate_salary()
    return result


def average_projects_per_employee(employees: List[Employee]) -> float:
    if not employees:
        return 0.0
    return sum(len(emp.projects) for emp in employees) / len(employees)
