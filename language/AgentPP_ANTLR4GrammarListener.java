// Generated from AgentPP_ANTLR4Grammar.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link AgentPP_ANTLR4GrammarParser}.
 */
public interface AgentPP_ANTLR4GrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(AgentPP_ANTLR4GrammarParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(AgentPP_ANTLR4GrammarParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#taskDefinition}.
	 * @param ctx the parse tree
	 */
	void enterTaskDefinition(AgentPP_ANTLR4GrammarParser.TaskDefinitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#taskDefinition}.
	 * @param ctx the parse tree
	 */
	void exitTaskDefinition(AgentPP_ANTLR4GrammarParser.TaskDefinitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(AgentPP_ANTLR4GrammarParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(AgentPP_ANTLR4GrammarParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(AgentPP_ANTLR4GrammarParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(AgentPP_ANTLR4GrammarParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(AgentPP_ANTLR4GrammarParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(AgentPP_ANTLR4GrammarParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#conditional}.
	 * @param ctx the parse tree
	 */
	void enterConditional(AgentPP_ANTLR4GrammarParser.ConditionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#conditional}.
	 * @param ctx the parse tree
	 */
	void exitConditional(AgentPP_ANTLR4GrammarParser.ConditionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#loopStmt}.
	 * @param ctx the parse tree
	 */
	void enterLoopStmt(AgentPP_ANTLR4GrammarParser.LoopStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#loopStmt}.
	 * @param ctx the parse tree
	 */
	void exitLoopStmt(AgentPP_ANTLR4GrammarParser.LoopStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(AgentPP_ANTLR4GrammarParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(AgentPP_ANTLR4GrammarParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#execution}.
	 * @param ctx the parse tree
	 */
	void enterExecution(AgentPP_ANTLR4GrammarParser.ExecutionContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#execution}.
	 * @param ctx the parse tree
	 */
	void exitExecution(AgentPP_ANTLR4GrammarParser.ExecutionContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#logStmt}.
	 * @param ctx the parse tree
	 */
	void enterLogStmt(AgentPP_ANTLR4GrammarParser.LogStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#logStmt}.
	 * @param ctx the parse tree
	 */
	void exitLogStmt(AgentPP_ANTLR4GrammarParser.LogStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(AgentPP_ANTLR4GrammarParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(AgentPP_ANTLR4GrammarParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryExpression(AgentPP_ANTLR4GrammarParser.PrimaryExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryExpression(AgentPP_ANTLR4GrammarParser.PrimaryExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(AgentPP_ANTLR4GrammarParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(AgentPP_ANTLR4GrammarParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(AgentPP_ANTLR4GrammarParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(AgentPP_ANTLR4GrammarParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#arguments}.
	 * @param ctx the parse tree
	 */
	void enterArguments(AgentPP_ANTLR4GrammarParser.ArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#arguments}.
	 * @param ctx the parse tree
	 */
	void exitArguments(AgentPP_ANTLR4GrammarParser.ArgumentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(AgentPP_ANTLR4GrammarParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(AgentPP_ANTLR4GrammarParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#comparisonOperator}.
	 * @param ctx the parse tree
	 */
	void enterComparisonOperator(AgentPP_ANTLR4GrammarParser.ComparisonOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#comparisonOperator}.
	 * @param ctx the parse tree
	 */
	void exitComparisonOperator(AgentPP_ANTLR4GrammarParser.ComparisonOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#arithmeticOperator}.
	 * @param ctx the parse tree
	 */
	void enterArithmeticOperator(AgentPP_ANTLR4GrammarParser.ArithmeticOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#arithmeticOperator}.
	 * @param ctx the parse tree
	 */
	void exitArithmeticOperator(AgentPP_ANTLR4GrammarParser.ArithmeticOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(AgentPP_ANTLR4GrammarParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(AgentPP_ANTLR4GrammarParser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#stringLiteral}.
	 * @param ctx the parse tree
	 */
	void enterStringLiteral(AgentPP_ANTLR4GrammarParser.StringLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#stringLiteral}.
	 * @param ctx the parse tree
	 */
	void exitStringLiteral(AgentPP_ANTLR4GrammarParser.StringLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#numberLiteral}.
	 * @param ctx the parse tree
	 */
	void enterNumberLiteral(AgentPP_ANTLR4GrammarParser.NumberLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#numberLiteral}.
	 * @param ctx the parse tree
	 */
	void exitNumberLiteral(AgentPP_ANTLR4GrammarParser.NumberLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#booleanLiteral}.
	 * @param ctx the parse tree
	 */
	void enterBooleanLiteral(AgentPP_ANTLR4GrammarParser.BooleanLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#booleanLiteral}.
	 * @param ctx the parse tree
	 */
	void exitBooleanLiteral(AgentPP_ANTLR4GrammarParser.BooleanLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#filepath}.
	 * @param ctx the parse tree
	 */
	void enterFilepath(AgentPP_ANTLR4GrammarParser.FilepathContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#filepath}.
	 * @param ctx the parse tree
	 */
	void exitFilepath(AgentPP_ANTLR4GrammarParser.FilepathContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#destination}.
	 * @param ctx the parse tree
	 */
	void enterDestination(AgentPP_ANTLR4GrammarParser.DestinationContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#destination}.
	 * @param ctx the parse tree
	 */
	void exitDestination(AgentPP_ANTLR4GrammarParser.DestinationContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#directory}.
	 * @param ctx the parse tree
	 */
	void enterDirectory(AgentPP_ANTLR4GrammarParser.DirectoryContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#directory}.
	 * @param ctx the parse tree
	 */
	void exitDirectory(AgentPP_ANTLR4GrammarParser.DirectoryContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#files}.
	 * @param ctx the parse tree
	 */
	void enterFiles(AgentPP_ANTLR4GrammarParser.FilesContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#files}.
	 * @param ctx the parse tree
	 */
	void exitFiles(AgentPP_ANTLR4GrammarParser.FilesContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#archive}.
	 * @param ctx the parse tree
	 */
	void enterArchive(AgentPP_ANTLR4GrammarParser.ArchiveContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#archive}.
	 * @param ctx the parse tree
	 */
	void exitArchive(AgentPP_ANTLR4GrammarParser.ArchiveContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#url}.
	 * @param ctx the parse tree
	 */
	void enterUrl(AgentPP_ANTLR4GrammarParser.UrlContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#url}.
	 * @param ctx the parse tree
	 */
	void exitUrl(AgentPP_ANTLR4GrammarParser.UrlContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#data}.
	 * @param ctx the parse tree
	 */
	void enterData(AgentPP_ANTLR4GrammarParser.DataContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#data}.
	 * @param ctx the parse tree
	 */
	void exitData(AgentPP_ANTLR4GrammarParser.DataContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#model}.
	 * @param ctx the parse tree
	 */
	void enterModel(AgentPP_ANTLR4GrammarParser.ModelContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#model}.
	 * @param ctx the parse tree
	 */
	void exitModel(AgentPP_ANTLR4GrammarParser.ModelContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#recipient}.
	 * @param ctx the parse tree
	 */
	void enterRecipient(AgentPP_ANTLR4GrammarParser.RecipientContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#recipient}.
	 * @param ctx the parse tree
	 */
	void exitRecipient(AgentPP_ANTLR4GrammarParser.RecipientContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#message}.
	 * @param ctx the parse tree
	 */
	void enterMessage(AgentPP_ANTLR4GrammarParser.MessageContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#message}.
	 * @param ctx the parse tree
	 */
	void exitMessage(AgentPP_ANTLR4GrammarParser.MessageContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#sender}.
	 * @param ctx the parse tree
	 */
	void enterSender(AgentPP_ANTLR4GrammarParser.SenderContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#sender}.
	 * @param ctx the parse tree
	 */
	void exitSender(AgentPP_ANTLR4GrammarParser.SenderContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#key}.
	 * @param ctx the parse tree
	 */
	void enterKey(AgentPP_ANTLR4GrammarParser.KeyContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#key}.
	 * @param ctx the parse tree
	 */
	void exitKey(AgentPP_ANTLR4GrammarParser.KeyContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(AgentPP_ANTLR4GrammarParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(AgentPP_ANTLR4GrammarParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#taskCall}.
	 * @param ctx the parse tree
	 */
	void enterTaskCall(AgentPP_ANTLR4GrammarParser.TaskCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#taskCall}.
	 * @param ctx the parse tree
	 */
	void exitTaskCall(AgentPP_ANTLR4GrammarParser.TaskCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#timerule}.
	 * @param ctx the parse tree
	 */
	void enterTimerule(AgentPP_ANTLR4GrammarParser.TimeruleContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#timerule}.
	 * @param ctx the parse tree
	 */
	void exitTimerule(AgentPP_ANTLR4GrammarParser.TimeruleContext ctx);
	/**
	 * Enter a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#input}.
	 * @param ctx the parse tree
	 */
	void enterInput(AgentPP_ANTLR4GrammarParser.InputContext ctx);
	/**
	 * Exit a parse tree produced by {@link AgentPP_ANTLR4GrammarParser#input}.
	 * @param ctx the parse tree
	 */
	void exitInput(AgentPP_ANTLR4GrammarParser.InputContext ctx);
}