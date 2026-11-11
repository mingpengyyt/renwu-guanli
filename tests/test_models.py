"""TaskManager 基础行为测试。"""

from task_manager.models import TaskManager


def test_add_and_list():
    m = TaskManager()
    m.add("写文档")
    tasks = m.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "写文档"
    assert tasks[0].done is False


def test_complete():
    m = TaskManager()
    t = m.add("提交代码")
    assert m.complete(t.id) is True
    assert m.complete(999) is False
