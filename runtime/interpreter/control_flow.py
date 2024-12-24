# control_flow.py
# Handles if/else, loops, and parallel constructs.

class ControlFlow:
    def evaluate_condition(self, condition_str: str) -> bool:
        # Very naive evaluation. Replace with safer logic in production.
        try:
            return eval(condition_str)
        except Exception:
            return False

    def execute_if(self, condition_str: str, true_block, false_block=None):
        if self.evaluate_condition(condition_str):
            true_block()
        elif false_block is not None:
            false_block()

    def execute_loop(self, condition_str: str, loop_body):
        while self.evaluate_condition(condition_str):
            loop_body()

    def execute_parallel(self, tasks: list):
        # Simplified approach. Use threading/async for real concurrency.
        for task in tasks:
            task()
