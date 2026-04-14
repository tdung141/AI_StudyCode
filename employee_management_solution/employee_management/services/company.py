from __future__ import annotations

from typing import List, Optional

from exceptions.employee_exceptions import (
    DuplicateEmployeeError,
    EmployeeNotFoundError,
    ProjectAllocationError,
)
from models.developer import Developer
from models.employee import Employee
from models.intern import Intern
from models.manager import Manager


class Company:
    def __init__(self, name: str):
        self.name = name
        self.employees: List[Employee] = []
        self._auto_counter = 1000

    def _generate_id(self, prefix: str = "EMP") -> str:
        self._auto_counter += 1
        return f"{prefix}{self._auto_counter}"

    def _existing_ids(self) -> set:
        return {emp.employee_id for emp in self.employees}

    def ensure_unique_or_regenerate(self, employee: Employee) -> Employee:
        if employee.employee_id in self._existing_ids():
            employee.employee_id = self._generate_id(employee.get_role()[:3].upper())
        return employee

    def add_employee(self, employee: Employee) -> Employee:
        if employee.employee_id in self._existing_ids():
            raise DuplicateEmployeeError(employee.employee_id)
        self.employees.append(employee)
        return employee

    def add_employee_safe(self, employee: Employee) -> Employee:
        employee = self.ensure_unique_or_regenerate(employee)
        self.employees.append(employee)
        return employee

    def get_all(self) -> List[Employee]:
        return list(self.employees)

    def get_by_role(self, role: str) -> List[Employee]:
        return [emp for emp in self.employees if emp.get_role().lower() == role.lower()]

    def sort_by_performance(self, reverse: bool = True) -> List[Employee]:
        return sorted(self.employees, key=lambda emp: emp.performance_score, reverse=reverse)

    def find_by_id(self, employee_id: str) -> Employee:
        for emp in self.employees:
            if emp.employee_id.lower() == employee_id.lower():
                return emp
        raise EmployeeNotFoundError(employee_id)

    def find_by_name(self, name: str) -> List[Employee]:
        keyword = name.lower()
        return [emp for emp in self.employees if keyword in emp.name.lower()]

    def find_developer_by_language(self, language: str) -> List[Developer]:
        keyword = language.lower()
        return [
            emp
            for emp in self.employees
            if isinstance(emp, Developer)
            and any(keyword in lang.lower() for lang in emp.programming_languages)
        ]

    def assign_project(self, employee_id: str, project_name: str) -> None:
        employee = self.find_by_id(employee_id)
        if len(employee.projects) >= 5:
            raise ProjectAllocationError("Nhân viên đã có tối đa 5 dự án")
        if project_name not in employee.projects:
            employee.add_project(project_name)

    def remove_project(self, employee_id: str, project_name: str) -> None:
        employee = self.find_by_id(employee_id)
        if not employee.remove_project(project_name):
            raise ProjectAllocationError("Nhân viên không thuộc dự án này")

    def remove_employee(self, employee_id: str) -> Employee:
        employee = self.find_by_id(employee_id)
        self.employees.remove(employee)
        return employee

    def increase_base_salary(self, employee_id: str, amount: float) -> Employee:
        employee = self.find_by_id(employee_id)
        employee.base_salary += amount
        return employee

    def promote_employee(self, employee_id: str) -> Employee:
        employee = self.find_by_id(employee_id)
        if isinstance(employee, Intern):
            promoted = Developer(
                employee_id=employee.employee_id,
                name=employee.name,
                age=employee.age,
                email=employee.email,
                department="Engineering",
                base_salary=max(employee.base_salary * 1.5, 8_000_000),
                performance_score=employee.performance_score,
                projects=employee.projects,
                programming_languages=["Python"],
            )
        elif isinstance(employee, Developer):
            promoted = Manager(
                employee_id=employee.employee_id,
                name=employee.name,
                age=employee.age,
                email=employee.email,
                department=employee.department,
                base_salary=max(employee.base_salary * 1.4, 18_000_000),
                performance_score=employee.performance_score,
                projects=employee.projects,
                team_size=max(len(employee.projects), 3),
            )
        else:
            raise ValueError("Manager không thể thăng chức thêm trong mô hình hiện tại")

        idx = self.employees.index(employee)
        self.employees[idx] = promoted
        return promoted

    def excellent_employees(self) -> List[Employee]:
        return [emp for emp in self.employees if emp.performance_score > 8]

    def employees_need_improvement(self) -> List[Employee]:
        return [emp for emp in self.employees if emp.performance_score < 5]

    def update_performance(self, employee_id: str, score: float) -> Employee:
        employee = self.find_by_id(employee_id)
        employee.update_performance(score)
        return employee

    def seed_sample_data(self) -> None:
        if self.employees:
            return
        self.add_employee_safe(Manager("M001", "Nguyen Van A", 35, "a@abc.com", "Management", 25000000, 8.8, ["ERP", "HRM"], 12))
        self.add_employee_safe(Developer("D001", "Tran Thi B", 28, "b@abc.com", "Engineering", 18000000, 9.2, ["CRM", "Mobile"], ["Python", "JavaScript"]))
        self.add_employee_safe(Intern("I001", "Le Van C", 22, "c@abc.com", "Engineering", 5000000, 7.0, ["Testing"], "Tran Thi B"))
