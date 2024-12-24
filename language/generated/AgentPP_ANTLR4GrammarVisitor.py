# Generated from AgentPP_ANTLR4Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AgentPP_ANTLR4GrammarParser import AgentPP_ANTLR4GrammarParser
else:
    from AgentPP_ANTLR4GrammarParser import AgentPP_ANTLR4GrammarParser

# This class defines a complete generic visitor for a parse tree produced by AgentPP_ANTLR4GrammarParser.

class AgentPP_ANTLR4GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#program.
    def visitProgram(self, ctx:AgentPP_ANTLR4GrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#taskDefinition.
    def visitTaskDefinition(self, ctx:AgentPP_ANTLR4GrammarParser.TaskDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#block.
    def visitBlock(self, ctx:AgentPP_ANTLR4GrammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#statement.
    def visitStatement(self, ctx:AgentPP_ANTLR4GrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#command.
    def visitCommand(self, ctx:AgentPP_ANTLR4GrammarParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#conditional.
    def visitConditional(self, ctx:AgentPP_ANTLR4GrammarParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#loopStmt.
    def visitLoopStmt(self, ctx:AgentPP_ANTLR4GrammarParser.LoopStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#assignment.
    def visitAssignment(self, ctx:AgentPP_ANTLR4GrammarParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#execution.
    def visitExecution(self, ctx:AgentPP_ANTLR4GrammarParser.ExecutionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#logStmt.
    def visitLogStmt(self, ctx:AgentPP_ANTLR4GrammarParser.LogStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#expression.
    def visitExpression(self, ctx:AgentPP_ANTLR4GrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:AgentPP_ANTLR4GrammarParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#functionCall.
    def visitFunctionCall(self, ctx:AgentPP_ANTLR4GrammarParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#condition.
    def visitCondition(self, ctx:AgentPP_ANTLR4GrammarParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#arguments.
    def visitArguments(self, ctx:AgentPP_ANTLR4GrammarParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#literal.
    def visitLiteral(self, ctx:AgentPP_ANTLR4GrammarParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:AgentPP_ANTLR4GrammarParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#arithmeticOperator.
    def visitArithmeticOperator(self, ctx:AgentPP_ANTLR4GrammarParser.ArithmeticOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#identifier.
    def visitIdentifier(self, ctx:AgentPP_ANTLR4GrammarParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#stringLiteral.
    def visitStringLiteral(self, ctx:AgentPP_ANTLR4GrammarParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#numberLiteral.
    def visitNumberLiteral(self, ctx:AgentPP_ANTLR4GrammarParser.NumberLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:AgentPP_ANTLR4GrammarParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#filepath.
    def visitFilepath(self, ctx:AgentPP_ANTLR4GrammarParser.FilepathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#destination.
    def visitDestination(self, ctx:AgentPP_ANTLR4GrammarParser.DestinationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#directory.
    def visitDirectory(self, ctx:AgentPP_ANTLR4GrammarParser.DirectoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#files.
    def visitFiles(self, ctx:AgentPP_ANTLR4GrammarParser.FilesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#archive.
    def visitArchive(self, ctx:AgentPP_ANTLR4GrammarParser.ArchiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#url.
    def visitUrl(self, ctx:AgentPP_ANTLR4GrammarParser.UrlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#data.
    def visitData(self, ctx:AgentPP_ANTLR4GrammarParser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#model.
    def visitModel(self, ctx:AgentPP_ANTLR4GrammarParser.ModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#recipient.
    def visitRecipient(self, ctx:AgentPP_ANTLR4GrammarParser.RecipientContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#message.
    def visitMessage(self, ctx:AgentPP_ANTLR4GrammarParser.MessageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#sender.
    def visitSender(self, ctx:AgentPP_ANTLR4GrammarParser.SenderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#key.
    def visitKey(self, ctx:AgentPP_ANTLR4GrammarParser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#function.
    def visitFunction(self, ctx:AgentPP_ANTLR4GrammarParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#taskCall.
    def visitTaskCall(self, ctx:AgentPP_ANTLR4GrammarParser.TaskCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#timerule.
    def visitTimerule(self, ctx:AgentPP_ANTLR4GrammarParser.TimeruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentPP_ANTLR4GrammarParser#input.
    def visitInput(self, ctx:AgentPP_ANTLR4GrammarParser.InputContext):
        return self.visitChildren(ctx)



del AgentPP_ANTLR4GrammarParser