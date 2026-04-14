from dataclasses import dataclass

from .employee import Employee


@dataclass
class Intern(Employee):
    mentor_name: str = ""
    support_allowance: float = 1_500_000

    def calculate_salary(self) -> float:
        performance_bonus = self.base_salary * (self.performance_score / 200)
        return self.base_salary + self.support_allowance + performance_bonus

    def get_role(self) -> str:
        return "Intern"
