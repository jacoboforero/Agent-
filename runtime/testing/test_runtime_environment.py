import pytest
from runtime.interpreter.runtime_environment import RuntimeEnvironment

@pytest.fixture
def setup_runtime_environment():
    """
    Fixture to set up a fresh RuntimeEnvironment instance for each test.
    """
    return RuntimeEnvironment()

def test_store_and_get_task(setup_runtime_environment):
    runtime_env = setup_runtime_environment

    # Store a task
    runtime_env.store_task("example_task", "mock_task_block")

    # Retrieve the task
    stored_task = runtime_env.get_task("example_task")

    assert stored_task == "mock_task_block"
    assert "example_task" in runtime_env.tasks

def test_store_and_get_variable(setup_runtime_environment):
    runtime_env = setup_runtime_environment

    # Store a variable
    runtime_env.store_variable("example_var", 42)

    # Retrieve the variable
    stored_value = runtime_env.get_variable("example_var")

    assert stored_value == 42
    assert "example_var" in runtime_env.variables

def test_log_event(setup_runtime_environment):
    runtime_env = setup_runtime_environment

    # Log an event
    runtime_env.log_event("Test log message")

    # Verify the log contains the message
    assert "Test log message" in runtime_env.log_data

def test_execute_shell_command_disallowed(setup_runtime_environment):
    runtime_env = setup_runtime_environment

    # Verify that shell commands are disallowed by default
    with pytest.raises(PermissionError):
        runtime_env.execute_shell_command("echo 'Hello World'")

def test_execute_shell_command_allowed(setup_runtime_environment):
    runtime_env = setup_runtime_environment

    # Enable shell commands
    runtime_env.safety_settings["allow_shell"] = True

    # Test shell command execution (mocking subprocess would be ideal here)
    try:
        runtime_env.execute_shell_command("echo 'Hello World'")
    except Exception as e:
        pytest.fail(f"Shell command execution failed with error: {e}")

def test_overwrite_task_warning(setup_runtime_environment):
    runtime_env = setup_runtime_environment

    # Store a task
    runtime_env.store_task("example_task", "mock_task_block")

    # Overwrite the same task
    runtime_env.store_task("example_task", "new_task_block")

    assert "Warning: Overwriting existing task 'example_task'" in runtime_env.log_data
    assert runtime_env.get_task("example_task") == "new_task_block"

def test_store_variable_overwrite(setup_runtime_environment):
    runtime_env = setup_runtime_environment

    # Store a variable
    runtime_env.store_variable("example_var", 42)

    # Overwrite the variable
    runtime_env.store_variable("example_var", 100)

    assert runtime_env.variables["example_var"] == 100
    assert "Variable 'example_var' set to '100'." in runtime_env.log_data

def test_get_nonexistent_task(setup_runtime_environment):
    runtime_env = setup_runtime_environment

    # Try to get a task that doesn't exist
    assert runtime_env.get_task("nonexistent_task") is None

def test_get_nonexistent_variable(setup_runtime_environment):
    runtime_env = setup_runtime_environment

    # Try to get a variable that doesn't exist
    assert runtime_env.get_variable("nonexistent_var") is None

def test_call_function_logging(setup_runtime_environment):
    runtime_env = setup_runtime_environment

    # Call a function
    result = runtime_env.call_function("mock_function", [1, 2, 3])

    assert result is None
    assert "Function 'mock_function' called with arguments: [1, 2, 3]" in runtime_env.log_data

def test_safety_settings_modification(setup_runtime_environment):
    runtime_env = setup_runtime_environment

    # Modify safety settings
    runtime_env.safety_settings["allow_shell"] = True

    assert runtime_env.safety_settings["allow_shell"] is True

def test_empty_environment_initialization(setup_runtime_environment):
    runtime_env = setup_runtime_environment

    assert runtime_env.log_data == []
    assert runtime_env.variables == {}
    assert runtime_env.tasks == {}
    assert runtime_env.safety_settings["allow_shell"] is False
