# command_handlers.py
# Encapsulates logic for handling individual commands (read, write, fetch, etc.).

class CommandHandlers:
    def __init__(self, runtime_env):
        self.runtime_env = runtime_env

    def handle(self, command_text: str):
        # Dispatch to specific methods based on command type.
        # For example, parse out command name and arguments.
        if command_text.startswith("read "):
            return self.handle_read(command_text)
        elif command_text.startswith("write "):
            return self.handle_write(command_text)
        else:
            self.runtime_env.log_event(f"Unknown or unimplemented command: {command_text}")

    def handle_read(self, command_text: str):
        # Example: "read <file>"
        _, file_path = command_text.split(" ", 1)
        try:
            with open(file_path, "r") as f:
                content = f.read()
            self.runtime_env.log_event(f"Read file: {file_path}")
            return content
        except FileNotFoundError:
            self.runtime_env.log_event(f"File not found: {file_path}")

    def handle_write(self, command_text: str):
        # Example: "write <data> to <file>"
        # This is just one possible parsing approach:
        parts = command_text.split(" ")
        # 'write', <data>, 'to', <file>
        if len(parts) < 4:
            self.runtime_env.log_event(f"Invalid write command syntax: {command_text}")
            return
        data = parts[1]
        file_path = parts[3]
        with open(file_path, "w") as f:
            f.write(data)
        self.runtime_env.log_event(f"Wrote data to: {file_path}")
