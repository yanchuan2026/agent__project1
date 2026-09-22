from week1.models import Student
from pathlib import Path

REPORT_FILE=Path(__file__).parent/"report.txt"
def format_report(student: Student) -> str:
    """把一个学生格式化成一行报告文本（纯函数：不打印、不写文件）。"""
    status = "及格" if student.is_pass() else "不及格"
    return (
        f"{student.name} (学号 {student.stu_id}) "
        f" 平均分 {student.average_score():.2f}"
        f" 最高分 {student.max_score():g}"
        f" {status}"
    )


def print_report(student: Student) -> None:
    """打印单个学生的成绩报告。"""
    print(format_report(student))


def find_top_student(students: list[Student]) -> Student:
    """返回平均分最高的学生。空列表直接报错，不返回 None。"""
    if not students:
        raise ValueError("students 不能为空")
    return max(students, key=lambda s: s.average_score())


def build_report(students: list[Student]) -> str:
    """生成完整报告文本：每名学生一行 + 最优学生。"""
    if not students:
        raise ValueError("students 不能为空")

    lines = [format_report(s) for s in students]
    top = find_top_student(students)
    lines.append("")
    lines.append(f"最优学生：{top.name}，平均分 {top.average_score():.2f}")
    return "\n".join(lines) + "\n"


def save_report_to_file(
    students: list[Student], path: Path | str = REPORT_FILE
) -> Path:
    """把报告写入文本文件，返回实际写入的路径。"""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(build_report(students), encoding="utf-8")
    return file_path