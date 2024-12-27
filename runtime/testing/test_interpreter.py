import pytest
import tempfile
from runtime.interpreter.runtime_environment import RuntimeEnvironment
from runtime.interpreter.command_handlers import CommandHandlers
from runtime.interpreter.interpreter import AgentPPInterpreter

@pytest.fixture
def setup_interpreter():
    """
    Sets up an interpreter instance with a fresh runtime environment.
    """
    runtime_env = RuntimeEnvironment()
    command_handlers = CommandHandlers(runtime_env)
    interpreter = AgentPPInterpreter()
    return interpreter, runtime_env

def write_temp_file(content):
    """
    Helper function to write content to a temporary file and return its path.
    """
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp_file:
        temp_file.write(content)
        temp_file.flush()
        return temp_file.name

def test_define_task(setup_interpreter):
    interpreter, runtime_env = setup_interpreter

    # Simulate defining a task
    task_definition = """
    task test_task:
        log "This is a test task"
    """
    temp_file_path = write_temp_file(task_definition)
    interpreter.interpret_file(temp_file_path)

    assert "test_task" in runtime_env.tasks
    assert "This is a test task" in runtime_env.log_data

def test_execute_task(setup_interpreter):
    interpreter, runtime_env = setup_interpreter

    # Define and execute a task
    task_definition = """
    task test_task:
        log "Executing test task"
    execute test_task
    """
    temp_file_path = write_temp_file(task_definition)
    interpreter.interpret_file(temp_file_path)

    assert "Executing test task" in runtime_env.log_data

def test_parallel_execution(setup_interpreter):
    interpreter, runtime_env = setup_interpreter

    # Define and execute parallel tasks
    task_definition = """
    task parallel_task:
        parallel:
            log "Task 1"
            log "Task 2"
    execute parallel_task
    """
    temp_file_path = write_temp_file(task_definition)
    interpreter.interpret_file(temp_file_path)

    assert "Task 1" in runtime_env.log_data
    assert "Task 2" in runtime_env.log_data

def test_variable_assignment(setup_interpreter):
    interpreter, runtime_env = setup_interpreter

    # Define variable assignment in a task
    task_definition = """
    task assign_variables:
        let example_var = 42
        log example_var
    execute assign_variables
    """
    temp_file_path = write_temp_file(task_definition)
    interpreter.interpret_file(temp_file_path)

    assert runtime_env.get_variable("example_var") == 42
    assert "42" in runtime_env.log_data

def test_conditional_execution(setup_interpreter):
    interpreter, runtime_env = setup_interpreter

    # Define a task with conditional logic
    task_definition = """
    task conditional_task:
        if 1 == 1:
            log "Condition met"
        else:
            log "Condition not met"
    execute conditional_task
    """
    temp_file_path = write_temp_file(task_definition)
    interpreter.interpret_file(temp_file_path)

    assert "Condition met" in runtime_env.log_data
    assert "Condition not met" not in runtime_env.log_data

def test_loop_execution(setup_interpreter):
    interpreter, runtime_env = setup_interpreter

    # Define a task with a loop
    task_definition = """
    task loop_task:
        let counter = 0
        loop:
            log counter
            let counter = counter + 1
        until counter == 3
    execute loop_task
    """
    temp_file_path = write_temp_file(task_definition)
    interpreter.interpret_file(temp_file_path)

    assert "0" in runtime_env.log_data
    assert "1" in runtime_env.log_data
    assert "2" in runtime_env.log_data

def test_schedule_task(setup_interpreter):
    interpreter, runtime_env = setup_interpreter

    # Schedule a task
    task_definition = """
    task scheduled_task:
        log "Scheduled task executed"
    schedule scheduled_task at 1234567890
    """
    temp_file_path = write_temp_file(task_definition)
    interpreter.interpret_file(temp_file_path)

    # Validate the task is scheduled
    assert "scheduled_task" in runtime_env.tasks
    # Since scheduling is time-based, this will require mocking for full validation