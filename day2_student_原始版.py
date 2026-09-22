"""【留档】Day 2 的单文件原始版本，不再修改。

它的内容已经拆进 src/week1/ 下的 models.py / utils.py / main.py。
这个文件仍可单独运行：uv run python day2_student_原始版.py
"""

from dataclasses import dataclass
from typing import Optional

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


    def max_score(self) -> Optional[int | float]:
        if not self.scores:
            return None
        return max(self.scores)


if __name__ == "__main__":
    s = Student("张三", "2025150291", [85, 98, 76, 43])
    print(f"姓名：{s.name}")
    print(f"平均分：{s.average_score():.2f}")
    print(f"是否及格：{'yes' if s.is_pass() else 'no'}")
    print(f"最高分：{s.max_score()}")
