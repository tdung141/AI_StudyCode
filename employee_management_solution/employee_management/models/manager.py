from dataclasses import dataclass

from .employee import Employee


@dataclass
class Manager(Employee):
    team_size: int = 0
    allowance: float = 5_000_000

    def calculate_salary(self) -> float:
        performance_bonus = self.base_salary * (self.performance_score / 100)
        team_bonus = self.team_size * 200_000
        return self.base_salary + self.allowance + performance_bonus + team_bonus

    def get_role(self) -> str:
        return "Manager"
