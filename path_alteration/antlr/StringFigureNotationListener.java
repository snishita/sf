// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link StringFigureNotationParser}.
 */
public interface StringFigureNotationListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link StringFigureNotationParser#commands}.
	 * @param ctx the parse tree
	 */
	void enterCommands(StringFigureNotationParser.CommandsContext ctx);
	/**
	 * Exit a parse tree produced by {@link StringFigureNotationParser#commands}.
	 * @param ctx the parse tree
	 */
	void exitCommands(StringFigureNotationParser.CommandsContext ctx);
	/**
	 * Enter a parse tree produced by {@link StringFigureNotationParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(StringFigureNotationParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link StringFigureNotationParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(StringFigureNotationParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link StringFigureNotationParser#finger}.
	 * @param ctx the parse tree
	 */
	void enterFinger(StringFigureNotationParser.FingerContext ctx);
	/**
	 * Exit a parse tree produced by {@link StringFigureNotationParser#finger}.
	 * @param ctx the parse tree
	 */
	void exitFinger(StringFigureNotationParser.FingerContext ctx);
	/**
	 * Enter a parse tree produced by {@link StringFigureNotationParser#fingerWithSide}.
	 * @param ctx the parse tree
	 */
	void enterFingerWithSide(StringFigureNotationParser.FingerWithSideContext ctx);
	/**
	 * Exit a parse tree produced by {@link StringFigureNotationParser#fingerWithSide}.
	 * @param ctx the parse tree
	 */
	void exitFingerWithSide(StringFigureNotationParser.FingerWithSideContext ctx);
	/**
	 * Enter a parse tree produced by {@link StringFigureNotationParser#string}.
	 * @param ctx the parse tree
	 */
	void enterString(StringFigureNotationParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by {@link StringFigureNotationParser#string}.
	 * @param ctx the parse tree
	 */
	void exitString(StringFigureNotationParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by {@link StringFigureNotationParser#stringWithSide}.
	 * @param ctx the parse tree
	 */
	void enterStringWithSide(StringFigureNotationParser.StringWithSideContext ctx);
	/**
	 * Exit a parse tree produced by {@link StringFigureNotationParser#stringWithSide}.
	 * @param ctx the parse tree
	 */
	void exitStringWithSide(StringFigureNotationParser.StringWithSideContext ctx);
	/**
	 * Enter a parse tree produced by {@link StringFigureNotationParser#move}.
	 * @param ctx the parse tree
	 */
	void enterMove(StringFigureNotationParser.MoveContext ctx);
	/**
	 * Exit a parse tree produced by {@link StringFigureNotationParser#move}.
	 * @param ctx the parse tree
	 */
	void exitMove(StringFigureNotationParser.MoveContext ctx);
	/**
	 * Enter a parse tree produced by {@link StringFigureNotationParser#tb}.
	 * @param ctx the parse tree
	 */
	void enterTb(StringFigureNotationParser.TbContext ctx);
	/**
	 * Exit a parse tree produced by {@link StringFigureNotationParser#tb}.
	 * @param ctx the parse tree
	 */
	void exitTb(StringFigureNotationParser.TbContext ctx);
	/**
	 * Enter a parse tree produced by {@link StringFigureNotationParser#nf}.
	 * @param ctx the parse tree
	 */
	void enterNf(StringFigureNotationParser.NfContext ctx);
	/**
	 * Exit a parse tree produced by {@link StringFigureNotationParser#nf}.
	 * @param ctx the parse tree
	 */
	void exitNf(StringFigureNotationParser.NfContext ctx);
}