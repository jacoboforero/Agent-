# task_manager.py
# Orchestrates tasks, scheduling, and concurrency.

import threading
import time

class TaskManager:
    def __init__(self):
        self.scheduled_tasks = []

    def schedule_task(self, task, run_at: float):
        # `task` can be a callable, `run_at` a timestamp
        self.scheduled_tasks.append((task, run_at))

    def run_scheduled_tasks(self):
        # Poll or handle tasks whose run_at time has passed
        now = time.time()
        for task, run_at in list(self.scheduled_tasks):
            if now >= run_at:
                # In production, handle concurrency properly
                threading.Thread(target=task).start()
                self.scheduled_tasks.remove((task, run_at))

    def run_parallel_tasks(self, tasks: list):
        threads = []
        for task in tasks:
            t = threading.Thread(target=task)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
