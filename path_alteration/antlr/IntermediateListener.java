// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link IntermediateParser}.
 */
public interface IntermediateListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link IntermediateParser#intermediate}.
	 * @param ctx the parse tree
	 */
	void enterIntermediate(IntermediateParser.IntermediateContext ctx);
	/**
	 * Exit a parse tree produced by {@link IntermediateParser#intermediate}.
	 * @param ctx the parse tree
	 */
	void exitIntermediate(IntermediateParser.IntermediateContext ctx);
	/**
	 * Enter a parse tree produced by {@link IntermediateParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(IntermediateParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link IntermediateParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(IntermediateParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link IntermediateParser#finger}.
	 * @param ctx the parse tree
	 */
	void enterFinger(IntermediateParser.FingerContext ctx);
	/**
	 * Exit a parse tree produced by {@link IntermediateParser#finger}.
	 * @param ctx the parse tree
	 */
	void exitFinger(IntermediateParser.FingerContext ctx);
	/**
	 * Enter a parse tree produced by {@link IntermediateParser#string}.
	 * @param ctx the parse tree
	 */
	void enterString(IntermediateParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by {@link IntermediateParser#string}.
	 * @param ctx the parse tree
	 */
	void exitString(IntermediateParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by {@link IntermediateParser#move}.
	 * @param ctx the parse tree
	 */
	void enterMove(IntermediateParser.MoveContext ctx);
	/**
	 * Exit a parse tree produced by {@link IntermediateParser#move}.
	 * @param ctx the parse tree
	 */
	void exitMove(IntermediateParser.MoveContext ctx);
	/**
	 * Enter a parse tree produced by {@link IntermediateParser#tb}.
	 * @param ctx the parse tree
	 */
	void enterTb(IntermediateParser.TbContext ctx);
	/**
	 * Exit a parse tree produced by {@link IntermediateParser#tb}.
	 * @param ctx the parse tree
	 */
	void exitTb(IntermediateParser.TbContext ctx);
	/**
	 * Enter a parse tree produced by {@link IntermediateParser#nf}.
	 * @param ctx the parse tree
	 */
	void enterNf(IntermediateParser.NfContext ctx);
	/**
	 * Exit a parse tree produced by {@link IntermediateParser#nf}.
	 * @param ctx the parse tree
	 */
	void exitNf(IntermediateParser.NfContext ctx);
}