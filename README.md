# week1 — Python 工程化练习（Day 2–3）

把 Day 2 写的单文件脚本，拆成一个结构清晰的包：**数据 / 逻辑 / 入口** 分开。

## 目录结构

```
week1/
├── pyproject.toml              # 项目声明（依赖、Python 版本、命令入口）
├── uv.lock                     # 依赖锁定文件，别手改
├── .python-version             # 本项目使用的 Python 版本
├── README.md
├── day2_student_原始版.py       # Day 2 的单文件版本，留档，不再修改
└── src/
    └── week1/                  # ← 真正的包，导入名就叫 week1
        ├── __init__.py
        ├── models.py           # 数据模型：Student
        ├── utils.py            # 工具函数：print_report / find_top_student
        └── main.py             # 程序入口：main
```

## 怎么运行

```bash
cd ~/py_learning/week1
uv run python -m week1.main
```

也可以走命令入口（对应 pyproject 里的 `[project.scripts]`）：

```bash
uv run week1
```

## 为什么是 `week1.main`，不是 `src.week1.main`

uv 默认使用 **src 布局**：

- `src/` 只是「源码存放目录」，**它本身不是包**，不需要 `__init__.py`；
- 真正的包是 `src/week1/`，所以导入名是 `week1`；
- uv 会把 `src` 加进模块搜索路径，因此 `import week1` 能找到它。

`python -m src.week1.main` 之所以「看起来也能跑」，是因为 Python 会把没有
`__init__.py` 的 `src/` 当成**命名空间包**，于是同一批文件被当成了两个包
（`src.week1` 与 `week1`）——这正是之前越写越乱的根源。

**规则：固定只用 `week1.xxx` 这一种写法。**

## 文件分工

| 文件 | 放什么 | 不放什么 |
| --- | --- | --- |
| `models.py` | 数据结构与它自己的行为（平均分、是否及格） | 打印、文件读写 |
| `utils.py` | 对数据的加工与输出 | 定义数据结构 |
| `main.py` | 组装流程、接收输入、调用上面两者 | 具体业务逻辑 |

判断标准：**如果换一个入口（比如网页接口），哪些代码可以原样复用？** 能复用的就该放在 `models.py` / `utils.py`，不能复用的才留在 `main.py`。
