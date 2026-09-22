"""week1 入口：从文本文件读取学生数据，生成成绩报告文件。

运行方式（在任意目录下都行）：
    uv run python -m week1.main
"""

from week1.file_handler import load_students
from week1.utils import save_report_to_file


def main() -> None:
    try:
        students = load_students()
        report_path = save_report_to_file(students)
    except FileNotFoundError:
        print("错误：找不到数据文件 data.txt")
    except ValueError as exc:
        print(f"错误：数据有问题 —— {exc}")
    else:
        print(f"已读取 {len(students)} 名学生，报告写入：{report_path}")


if __name__ == "__main__":
    main()
# 测试 commit 规范
print("故意改错"