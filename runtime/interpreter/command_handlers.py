# command_handlers.py
# Encapsulates logic for handling individual Agent++ commands.

class CommandHandlers:
    def __init__(self, runtime_env):
        self.runtime_env = runtime_env

    def handle(self, command_text: str):
        """
        Dispatch command_text to a relevant handler based on the grammar.
        """
        # This simplistic approach uses string matching. 
        # In a real interpreter, you'll parse ctx nodes for more precise handling.
        cmd_parts = command_text.split()
        if not cmd_parts:
            return

        cmd_name = cmd_parts[0]
        if cmd_name == "read":
            return self.handle_read(cmd_parts)
        elif cmd_name == "write":
            return self.handle_write(cmd_parts)
        else:
            self.runtime_env.log_event(f"Unhandled command: {command_text}")

    def handle_read(self, cmd_parts):
        # Example: Agent++ "read <file>"
        if len(cmd_parts) < 2:
            self.runtime_env.log_event("Usage: read <file>")
            return
        file_path = cmd_parts[1]
        try:
            with open(file_path, "r") as f:
                content = f.read()
            self.runtime_env.log_event(f"Read file: {file_path}")
            return content
        except FileNotFoundError:
            self.runtime_env.log_event(f"File not found: {file_path}")

    def handle_write(self, cmd_parts):
        # Example: Agent++ "write <data> to <file>"
        # This is just a naive approach.
        if len(cmd_parts) < 4 or cmd_parts[2] != "to":
            self.runtime_env.log_event("Usage: write <data> to <file>")
            return
        data = cmd_parts[1]
        file_path = cmd_parts[3]
        with open(file_path, "w") as f:
            f.write(data)
        self.runtime_env.log_event(f"Wrote data to: {file_path}")
