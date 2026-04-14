from dataclasses import dataclass, field
from typing import List

from .employee import Employee


@dataclass
class Developer(Employee):
    programming_languages: List[str] = field(default_factory=list)
    bug_fix_bonus: float = 2_000_000

    def calculate_salary(self) -> float:
        performance_bonus = self.base_salary * (self.performance_score / 120)
        lang_bonus = len(self.programming_languages) * 300_000
        return self.base_salary + self.bug_fix_bonus + performance_bonus + lang_bonus

    def get_role(self) -> str:
        return "Developer"
