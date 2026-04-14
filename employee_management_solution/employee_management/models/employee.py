from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List


@dataclass
class Employee(ABC):
    employee_id: str
    name: str
    age: int
    email: str
    department: str
    base_salary: float
    performance_score: float = 5.0
    projects: List[str] = field(default_factory=list)

    @abstractmethod
    def calculate_salary(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_role(self) -> str:
        raise NotImplementedError

    def add_project(self, project_name: str) -> None:
        self.projects.append(project_name)

    def remove_project(self, project_name: str) -> bool:
        if project_name in self.projects:
            self.projects.remove(project_name)
            return True
        return False

    def update_performance(self, score: float) -> None:
        self.performance_score = score

    def to_dict(self) -> dict:
        return {
            "id": self.employee_id,
            "name": self.name,
            "role": self.get_role(),
            "department": self.department,
            "salary": self.calculate_salary(),
            "projects": list(self.projects),
            "performance": self.performance_score,
        }
