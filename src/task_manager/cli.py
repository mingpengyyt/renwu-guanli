"""命令行入口。

基于标准库 argparse 实现，无需第三方依赖即可运行基础功能：
    python -m task_manager.cli add "写文档"
    python -m task_manager.cli list
    python -m task_manager.cli done 1
"""

import argparse

from .models import TaskManager


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="任务管理 renwu-guanli")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="新增任务")
    add.add_argument("title", help="任务标题")

    sub.add_parser("list", help="列出所有任务")

    done = sub.add_parser("done", help="标记任务为已完成")
    done.add_argument("id", type=int, help="任务 ID")

    return parser


def main(argv=None) -> int:
    manager = TaskManager()
    args = build_parser().parse_args(argv)

    if args.command == "add":
        task = manager.add(args.title)
        print(f"已添加任务 #{task.id}: {task.title}")
    elif args.command == "list":
        for t in manager.list_tasks():
            mark = "x" if t.done else " "
            print(f"[{mark}] #{t.id} {t.title}")
    elif args.command == "done":
        ok = manager.complete(args.id)
        print("已完成" if ok else "未找到该任务")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
