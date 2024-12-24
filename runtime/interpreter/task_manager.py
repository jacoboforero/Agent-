# task_manager.py
# Orchestrates tasks, scheduling, and concurrency.

import time
import threading

class TaskManager:
    def __init__(self):
        self.scheduled_tasks = []

    def schedule_task(self, task, run_at: float):
        """
        Schedules a task (callable) to run at a specific timestamp (run_at).
        """
        self.scheduled_tasks.append((task, run_at))

    def run_scheduled_tasks(self):
        """
        Checks if any tasks are due to run, and runs them. 
        In a production scenario, you'd likely run this on a loop or timer.
        """
        now = time.time()
        for task_info in list(self.scheduled_tasks):
            task, run_at = task_info
            if now >= run_at:
                threading.Thread(target=task).start()
                self.scheduled_tasks.remove(task_info)

    def run_parallel_tasks(self, tasks: list):
        """
        Runs a list of callables in parallel using threads. 
        This is a simplistic approach—consider more robust concurrency if needed.
        """
        threads = []
        for task in tasks:
            t = threading.Thread(target=task)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()
