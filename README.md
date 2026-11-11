# renwu-guanli

> trying out automation in my spare time

一个简单的任务管理（待办事项）命令行工具，使用 Python 编写。

## 功能

- 新增任务（`add`）
- 列出任务（`list`）
- 标记任务完成（`done`）

> 当前为骨架版本：任务保存在内存中，进程重启后数据清空，后续可接入文件或数据库持久化。

## 安装与运行

```bash
pip install -e .
python -m task_manager.cli add "写文档"
python -m task_manager.cli list
python -m task_manager.cli done 1
```

## 开发

```bash
pip install -e ".[dev]"
pytest
```

## 目录结构

```
renwu-guanli/
├── pyproject.toml        # 项目元信息与构建配置
├── src/task_manager/     # 主程序包
│   ├── models.py         # 任务模型与内存管理器
│   └── cli.py            # 命令行入口
└── tests/                # 单元测试
```
