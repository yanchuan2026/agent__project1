from dataclasses import dataclass

@dataclass
class Student:
    name: str
    stu_id: str
    scores: list[int | float]

    def average_score(self) -> float:
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)

    def is_pass(self, threshold: float = 60.0) -> bool:
        return self.average_score() >= threshold

    def max_score(self) -> int | float | None:
        if not self.scores:
            return None
        return max(self.scores)