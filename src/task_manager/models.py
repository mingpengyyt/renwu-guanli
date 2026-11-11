"""任务数据模型与内存管理器。

当前为骨架版本：任务保存在内存中，进程重启后数据清空。
后续可替换为文件持久化或数据库存储。
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Task:
    """一条任务。"""

    title: str
    done: bool = False
    id: Optional[int] = None


class TaskManager:
    """简单的任务管理器（内存存储）。"""

    def __init__(self) -> None:
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add(self, title: str) -> Task:
        """新增一条任务，返回创建后的 Task 对象。"""
        task = Task(title=title, id=self._next_id)
        self._next_id += 1
        self._tasks.append(task)
        return task

    def list_tasks(self) -> List[Task]:
        """返回当前所有任务的副本。"""
        return list(self._tasks)

    def complete(self, task_id: int) -> bool:
        """标记指定 ID 的任务为已完成，成功返回 True。"""
        for task in self._tasks:
            if task.id == task_id:
                task.done = True
                return True
        return False
