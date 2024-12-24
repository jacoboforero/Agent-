# interpreter.py
# Core interpreter logic that uses ANTLR-generated files to parse and interpret Agent++ scripts.

import sys
from antlr4 import FileStream, CommonTokenStream
from language.generated.AgentPP_ANTLR4GrammarLexer import AgentPP_ANTLR4GrammarLexer
from language.generated.AgentPP_ANTLR4GrammarParser import AgentPP_ANTLR4GrammarParser
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

    def interpret_file(self, file_path: str):
        """
        High-level method to parse and interpret an Agent++ script from a file.
        """
        input_stream = FileStream(file_path)
        lexer = AgentPP_ANTLR4GrammarLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = AgentPP_ANTLR4GrammarParser(token_stream)

        # 'program' should match the start rule in your grammar (change if different).
        parse_tree = parser.program()
        
        # Visit the parse tree
        self.visit(parse_tree)

    def visitProgram(self, ctx):
        """
        Called when the parser recognizes a 'program' node.
        Override as needed to handle top-level constructs.
        """
        return super().visitProgram(ctx)

    def visitTaskDefinition(self, ctx):
        """
        Example of a visitor method for a 'taskDefinition' rule in your grammar.
        Implement how you want to store or handle tasks.
        """
        # You might extract task info from ctx here
        # For example: task_name = ctx.TASK_NAME().getText() if your grammar defines it
        return super().visitTaskDefinition(ctx)

    def visitCommand(self, ctx):
        """
        Example of a visitor method for a 'command' rule in your grammar.
        Dispatch to your command handlers.
        """
        # Extract the command text or sub-nodes from ctx
        command_text = ctx.getText()
        self.command_handlers.handle(command_text)
        return super().visitCommand(ctx)


if __name__ == "__main__":
    # Optional: a simple CLI for testing
    if len(sys.argv) < 2:
        print("Usage: python interpreter.py <path_to_agentpp_script>")
        sys.exit(1)

    script_path = sys.argv[1]
    interpreter = AgentPPInterpreter()
    interpreter.interpret_file(script_path)
