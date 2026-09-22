"""week1 文件读写模块。

职责：只负责「文件 ←→ Python 对象」的转换，不掺业务逻辑。
"""

from pathlib import Path

from week1.models import Student

# 数据文件固定放在本模块所在目录（src/week1/）下。
# 用 __file__ 定位，程序无论从哪个目录启动都能找对文件。
DATA_FILE = Path(__file__).parent / "data.txt"


def load_students(path: Path | str = DATA_FILE) -> list[Student]:
    """从文本文件读取学生数据，返回 Student 列表。

    文件格式：每行一个学生，逗号分隔 —— 姓名,学号,分数1,分数2,...
    空行、以 # 开头的注释行会被跳过。
    """
    file_path = Path(path)
    students: list[Student] = []

    with file_path.open(encoding="utf-8") as f:
        for line_no, raw_line in enumerate(f, start=1):
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue

            parts = [p.strip() for p in line.split(",")]
            if len(parts) < 3:
                raise ValueError(f"第 {line_no} 行字段不足：{line!r}")

            name, stu_id = parts[0], parts[1]
            try:
                scores = [float(s) for s in parts[2:]]
            except ValueError as exc:
                raise ValueError(f"第 {line_no} 行分数不是数字：{line!r}") from exc

            students.append(Student(name, stu_id, scores))

    if not students:
        raise ValueError(f"{file_path} 里没有任何学生数据")

    return students
