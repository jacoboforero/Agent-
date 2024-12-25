# command_handlers.py
# Handles individual Agent++ commands.

import os
import requests
from runtime_environment import RuntimeEnvironment

class CommandHandlers:
    def __init__(self, runtime_env: RuntimeEnvironment):
        self.runtime_env = runtime_env
        # Dispatch table for commands
        self.command_dispatch = {
            "read": self.read_file,
            "write": self.write_file,
            "delete": self.delete_file,
            "move": self.move_file,
            "log": self.log_message,
            "fetch": self.fetch_url,
            "execute": self.execute_task,
            # Add more commands here as needed
        }

    def handle(self, command_text: str):
        """
        Dispatch the command text to the appropriate handler.
        """
        try:
            parts = command_text.split(" ", 1)
            command = parts[0]
            args = parts[1] if len(parts) > 1 else ""

            if command in self.command_dispatch:
                self.command_dispatch[command](args)
            else:
                raise ValueError(f"Unknown command: {command}")
        except Exception as e:
            self.runtime_env.log_event(f"Error handling command '{command_text}': {e}")

    def read_file(self, args: str):
        """
        Reads the content of a file and stores it in the runtime environment.
        """
        file_path = args.strip()
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        file_extension = os.path.splitext(file_path)[-1].lower()
        
        with open(file_path, "rb" if file_extension not in [".txt", ".csv", ".log"] else "r") as file:
            content = file.read()

        self.runtime_env.variables["last_read"] = {
            "content": content,
            "format": file_extension
        }
        self.runtime_env.log_event(f"Read file: {file_path} with format: {file_extension}")

    def write_file(self, args: str):
        """
        Writes data to a specified file.
        """
        try:
            data, file_path = args.split(" to ", 1)
            file_path = file_path.strip()

            with open(file_path, "w") as file:
                file.write(data)

            self.runtime_env.log_event(f"Wrote data to file: {file_path}")
        except ValueError:
            raise ValueError("Invalid syntax for write command. Use: write <data> to <file>")

    def delete_file(self, args: str):
        """
        Deletes a specified file or directory.
        """
        file_path = args.strip()
        if os.path.isdir(file_path):
            os.rmdir(file_path)
        elif os.path.isfile(file_path):
            os.remove(file_path)
        else:
            raise FileNotFoundError(f"Path not found: {file_path}")

        self.runtime_env.log_event(f"Deleted file or directory: {file_path}")

    def move_file(self, args: str):
        """
        Moves a file or directory to a new location.
        """
        try:
            source, destination = args.split(" to ", 1)
            os.rename(source.strip(), destination.strip())
            self.runtime_env.log_event(f"Moved {source} to {destination}")
        except ValueError:
            raise ValueError("Invalid syntax for move command. Use: move <file> to <destination>")

    def log_message(self, args: str):
        """
        Logs a message to the runtime environment.
        """
        message = args.strip()
        self.runtime_env.log_event(message)

    def fetch_url(self, args: str):
        """
        Fetches data from a URL and stores it in the runtime environment.
        """
        url = args.strip()
        response = requests.get(url)

        if response.status_code == 200:
            self.runtime_env.variables["last_fetch"] = response.text
            self.runtime_env.log_event(f"Fetched data from {url}")
        else:
            raise ConnectionError(f"Failed to fetch URL: {url} (status code: {response.status_code})")

    def execute_task(self, args: str):
        """
        Executes a defined task or system command.
        """
        task_name = args.strip()

        if task_name in self.runtime_env.tasks:
            # Execute a predefined task
            task = self.runtime_env.tasks[task_name]
            for command in task:
                self.handle(command)
        else:
            # Treat as a system command
            os.system(task_name)
            self.runtime_env.log_event(f"Executed system command: {task_name}")

# Additional commands can be implemented similarly
