# task_manager.py
# Orchestrates tasks, scheduling, and concurrency.

import time
import threading
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from enum import Enum

class TaskState(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

class TaskManager:
    def __init__(self, runtime_env, max_threads=10):
        self.runtime_env = runtime_env  # Reference to RuntimeEnvironment for task definitions
        self.scheduled_tasks = Queue()
        self.executor = ThreadPoolExecutor(max_threads)
        self.task_states = {}  # Tracks the state of tasks

    def schedule_task(self, task_name, run_at: float):
        """
        Schedules a task (by name) to run at a specific timestamp (run_at).
        """
        task_definition = self.runtime_env.get_task(task_name)
        if not task_definition:
            raise ValueError(f"Task '{task_name}' is not defined.")
        
        self.scheduled_tasks.put((task_definition, run_at))
        self.task_states[task_name] = TaskState.PENDING

    def run_scheduled_tasks(self):
        """
        Checks if any tasks are due to run, and runs them.
        Uses a thread pool to manage execution.
        """
        now = time.monotonic()
        tasks_to_run = []

        while not self.scheduled_tasks.empty():
            task, run_at = self.scheduled_tasks.get()
            if now >= run_at:
                tasks_to_run.append(task)
                self.task_states[task] = TaskState.RUNNING
            else:
                # Put the task back if it's not ready yet
                self.scheduled_tasks.put((task, run_at))

        for task in tasks_to_run:
            self.executor.submit(self._safe_task_wrapper, task)

    def run_parallel_tasks(self, task_names: list):
        """
        Runs a list of task names in parallel using a thread pool.
        """
        for task_name in task_names:
            task_definition = self.runtime_env.get_task(task_name)
            if not task_definition:
                raise ValueError(f"Task '{task_name}' is not defined.")

            self.task_states[task_name] = TaskState.PENDING
            self.executor.submit(self._safe_task_wrapper, task_definition)

    def _safe_task_wrapper(self, task):
        """
        Wraps task execution to handle errors and update task state.
        """
        try:
            self.task_states[task] = TaskState.RUNNING
            task()
            self.task_states[task] = TaskState.COMPLETED
        except Exception as e:
            self.task_states[task] = TaskState.FAILED
            print(f"Task failed with error: {e}")

    def get_task_state(self, task_name):
        """
        Returns the current state of a task.
        """
        return self.task_states.get(task_name, None)

    # Future Feature: Scheduling tasks based on global conditions or flags
    # Intend to support tasks that trigger when specific conditions are met.
    # Example: Add `condition` parameter to `schedule_task` and evaluate
    # these conditions in `run_scheduled_tasks`. This will require extending
    # the grammar and runtime environment.
