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
        """
        for task in ctx.taskDefinition():
            self.visit(task)

    def visitTaskDefinition(self, ctx):
        """
        Handles task definitions.
        Extracts task name and block and stores it in the runtime environment.
        """
        task_name = ctx.identifier().getText()
        task_block = ctx.block()
        self.runtime_env.log_event(f"Defining task: {task_name}")
        self.runtime_env.store_task(task_name, task_block)

    def visitBlock(self, ctx):
        """
        Executes a block by visiting each statement.
        """
        for statement in ctx.statement():
            self.visit(statement)

    def visitStatement(self, ctx):
        """
        Routes statement execution to the appropriate handler.
        """
        if ctx.command():
            self.visit(ctx.command())
        elif ctx.conditional():
            self.visit(ctx.conditional())
        elif ctx.loopStmt():
            self.visit(ctx.loopStmt())
        elif ctx.assignment():
            self.visit(ctx.assignment())
        elif ctx.execution():
            self.visit(ctx.execution())
        elif ctx.logStmt():
            self.visit(ctx.logStmt())

    def visitCommand(self, ctx):
        """
        Handles individual commands by dispatching them to the CommandHandlers.
        """
        command_text = ctx.getText()
        self.command_handlers.handle(command_text)

    def visitConditional(self, ctx):
        """
        Handles 'if-else' conditionals.
        """
        condition = ctx.condition().getText()  # Adjust as needed for evaluating conditions
        true_block = ctx.block(0)
        false_block = ctx.block(1) if ctx.ELSE() else None

        if self.control_flow.evaluate_condition(condition):
            self.visit(true_block)
        elif false_block:
            self.visit(false_block)

    def visitLoopStmt(self, ctx):
        """
        Handles 'loop' statements.
        """
        condition = ctx.condition().getText()
        loop_block = ctx.block()

        while self.control_flow.evaluate_condition(condition):
            self.visit(loop_block)

    def visitAssignment(self, ctx):
        """
        Handles variable assignment.
        """
        variable_name = ctx.identifier().getText()
        value = self.visit(ctx.expression())
        self.runtime_env.store_variable(variable_name, value)

    def visitExecution(self, ctx):
        """
        Handles task execution, parallel blocks, and scheduling.
        """
        if ctx.EXECUTE():
            task_call = ctx.taskCall()
            self.task_manager.execute_task(task_call)
        elif ctx.PARALLEL():
            block = ctx.block()
            self.task_manager.run_parallel_tasks(block.statement())
        elif ctx.WAIT():
            task_call = ctx.taskCall()
            self.task_manager.wait_for_task(task_call)
        elif ctx.SCHEDULE():
            task_call = ctx.taskCall()
            time_rule = ctx.timerule().getText()
            self.task_manager.schedule_task(task_call, time_rule)

    def visitLogStmt(self, ctx):
        """
        Handles log statements.
        """
        message = ctx.stringLiteral().getText()
        self.runtime_env.log_event(message)

    def visitCondition(self, ctx):
        """
        Evaluates a condition.
        """
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.comparisonOperator().getText()
        return self.control_flow.evaluate_condition(f"{left} {operator} {right}")

    def visitFunctionCall(self, ctx):
        """
        Handles function calls.
        """
        function_name = ctx.identifier().getText()
        arguments = [self.visit(arg) for arg in ctx.arguments().expression()] if ctx.arguments() else []
        return self.runtime_env.call_function(function_name, arguments)

if __name__ == "__main__":
    # Optional: a simple CLI for testing
    if len(sys.argv) < 2:
        print("Usage: python interpreter.py <path_to_agentpp_script>")
        sys.exit(1)

    script_path = sys.argv[1]
    interpreter = AgentPPInterpreter()
    interpreter.interpret_file(script_path)
