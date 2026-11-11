"""任务数据模型与文件持久化管理器。

任务保存在本地 JSON 文件（默认 tasks.json），进程重启后数据保留。
后续可替换为数据库存储，只需替换 TaskManager 内部读写实现。
"""

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Optional, Union


@dataclass
class Task:
    """一条任务。"""

    title: str
    done: bool = False
    id: Optional[int] = None


class TaskManager:
    """任务管理器，任务持久化到 JSON 文件。"""

    def __init__(self, path: Union[str, Path] = "tasks.json") -> None:
        self.path = Path(path)
        self._tasks: List[Task] = []
        self._next_id: int = 1
        self._load()

    def _load(self) -> None:
        """从 JSON 文件加载任务；文件不存在或内容损坏时忽略。"""
        if not self.path.exists():
            return
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return
        if not isinstance(raw, list):
            return
        self._tasks = [Task(**item) for item in raw if isinstance(item, dict)]
        used_ids = [t.id for t in self._tasks if isinstance(t.id, int)]
        self._next_id = (max(used_ids) + 1) if used_ids else 1

    def _save(self) -> None:
        """将当前任务写入 JSON 文件。"""
        data = [asdict(t) for t in self._tasks]
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def add(self, title: str) -> Task:
        """新增一条任务并落盘，返回创建后的 Task 对象。"""
        task = Task(title=title, id=self._next_id)
        self._next_id += 1
        self._tasks.append(task)
        self._save()
        return task

    def list_tasks(self) -> List[Task]:
        """返回当前所有任务的副本。"""
        return list(self._tasks)

    def complete(self, task_id: int) -> bool:
        """标记指定 ID 的任务为已完成并落盘，成功返回 True。"""
        for task in self._tasks:
            if task.id == task_id:
                task.done = True
                self._save()
                return True
        return False
