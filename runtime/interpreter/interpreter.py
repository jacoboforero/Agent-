# interpreter.py
# Core interpreter logic that walks the parse tree and coordinates command execution.

from language.generated.AgentPP_ANTLR4GrammarVisitor import AgentPP_ANTLR4GrammarVisitor
from runtime.interpreter.runtime_environment import RuntimeEnvironment
from runtime.interpreter.command_handlers import CommandHandlers
from runtime.interpreter.control_flow import ControlFlow
from runtime.interpreter.task_manager import TaskManager

class AgentPPInterpreter(AgentPP_ANTLR4GrammarVisitor):
    def __init__(self):
        super().__init__()
        self.runtime_env = RuntimeEnvironment()
        self.command_handlers = CommandHandlers(self.runtime_env)
        self.control_flow = ControlFlow()
        self.task_manager = TaskManager()

    def visitProgram(self, ctx):
        # Entry point for visiting the parse tree.
        return self.visitChildren(ctx)

    def visitTaskDefinition(self, ctx):
        # Example: handle "task <name>" definitions if that's part of the grammar.
        return self.visitChildren(ctx)

    def visitCommand(self, ctx):
        # Get the raw text or parse the command structure
        command_text = ctx.getText()
        self.command_handlers.handle(command_text)
        return super().visitCommand(ctx)

    # Add other visitor methods for control flow, loops, conditionals, etc.
