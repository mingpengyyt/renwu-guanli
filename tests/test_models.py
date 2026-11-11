"""TaskManager 基础行为测试。"""

from task_manager.models import TaskManager


def test_add_and_list(tmp_path):
    m = TaskManager(tmp_path / "tasks.json")
    m.add("写文档")
    tasks = m.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "写文档"
    assert tasks[0].done is False


def test_complete(tmp_path):
    m = TaskManager(tmp_path / "tasks.json")
    t = m.add("提交代码")
    assert m.complete(t.id) is True
    assert m.complete(999) is False


def test_persistence_across_instances(tmp_path):
    path = tmp_path / "tasks.json"
    m1 = TaskManager(path)
    m1.add("持久化任务")
    m1.add("第二条")
    m1.complete(1)

    # 用同一文件重新构造管理器，模拟进程重启
    m2 = TaskManager(path)
    tasks = m2.list_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == "持久化任务"
    assert tasks[0].done is True
    # ID 自增应基于已存数据，不重复
    assert m2.add("第三条").id == 3
