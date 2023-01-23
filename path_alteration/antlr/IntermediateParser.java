// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class IntermediateParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.11.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PURL=1, PULR=2, PUR=3, PUL=4, PU=5, UP=6, RE=7, REL=8, RER=9, TW=10, MO=11, 
		MU=12, MA=13, MT=14, S=15, N=16, T=17, F=18, M=19, R=20, L=21, HT=22, 
		HB=23, DN=24, DF=25, SEMICOLON=26, WS=27;
	public static final int
		RULE_intermediate = 0, RULE_command = 1, RULE_finger = 2, RULE_string = 3, 
		RULE_move = 4, RULE_tb = 5, RULE_nf = 6;
	private static String[] makeRuleNames() {
		return new String[] {
			"intermediate", "command", "finger", "string", "move", "tb", "nf"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'pu-rl'", "'pu-lr'", "'pu-r'", "'pu-l'", "'pu'", "'up'", "'re'", 
			"'re-l'", "'re-r'", "'tw'", "'mo'", "'mu'", "'ma'", "'mt'", "'S'", "'N'", 
			"'T'", "'F'", "'M'", "'R'", "'L'", "'t'", "'b'", "'n'", "'f'", "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PURL", "PULR", "PUR", "PUL", "PU", "UP", "RE", "REL", "RER", "TW", 
			"MO", "MU", "MA", "MT", "S", "N", "T", "F", "M", "R", "L", "HT", "HB", 
			"DN", "DF", "SEMICOLON", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "java-escape"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public IntermediateParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IntermediateContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(IntermediateParser.EOF, 0); }
		public List<CommandContext> command() {
			return getRuleContexts(CommandContext.class);
		}
		public CommandContext command(int i) {
			return getRuleContext(CommandContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(IntermediateParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(IntermediateParser.SEMICOLON, i);
		}
		public IntermediateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_intermediate; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof IntermediateListener ) ((IntermediateListener)listener).enterIntermediate(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof IntermediateListener ) ((IntermediateListener)listener).exitIntermediate(this);
		}
	}

	public final IntermediateContext intermediate() throws RecognitionException {
		IntermediateContext _localctx = new IntermediateContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_intermediate);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(17); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(14);
				command();
				setState(15);
				match(SEMICOLON);
				}
				}
				setState(19); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( ((_la) & ~0x3f) == 0 && ((1L << _la) & 4064192L) != 0 );
			setState(21);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CommandContext extends ParserRuleContext {
		public FingerContext finger() {
			return getRuleContext(FingerContext.class,0);
		}
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public TerminalNode TW() { return getToken(IntermediateParser.TW, 0); }
		public TerminalNode PURL() { return getToken(IntermediateParser.PURL, 0); }
		public TerminalNode PULR() { return getToken(IntermediateParser.PULR, 0); }
		public TerminalNode PU() { return getToken(IntermediateParser.PU, 0); }
		public TerminalNode PUR() { return getToken(IntermediateParser.PUR, 0); }
		public TerminalNode PUL() { return getToken(IntermediateParser.PUL, 0); }
		public TerminalNode MA() { return getToken(IntermediateParser.MA, 0); }
		public TerminalNode MT() { return getToken(IntermediateParser.MT, 0); }
		public List<MoveContext> move() {
			return getRuleContexts(MoveContext.class);
		}
		public MoveContext move(int i) {
			return getRuleContext(MoveContext.class,i);
		}
		public TerminalNode UP() { return getToken(IntermediateParser.UP, 0); }
		public TerminalNode RE() { return getToken(IntermediateParser.RE, 0); }
		public TerminalNode REL() { return getToken(IntermediateParser.REL, 0); }
		public TerminalNode RER() { return getToken(IntermediateParser.RER, 0); }
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof IntermediateListener ) ((IntermediateListener)listener).enterCommand(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof IntermediateListener ) ((IntermediateListener)listener).exitCommand(this);
		}
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_command);
		int _la;
		try {
			setState(43);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T:
			case F:
			case M:
			case R:
			case L:
				enterOuterAlt(_localctx, 1);
				{
				setState(23);
				finger();
				setState(35);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PUR:
				case PUL:
				case PU:
				case MO:
				case MU:
					{
					setState(27);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==MO || _la==MU) {
						{
						{
						setState(24);
						move();
						}
						}
						setState(29);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(30);
					_la = _input.LA(1);
					if ( !(((_la) & ~0x3f) == 0 && ((1L << _la) & 56L) != 0) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					break;
				case MA:
				case MT:
					{
					setState(31);
					_la = _input.LA(1);
					if ( !(_la==MA || _la==MT) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(32);
					match(TW);
					}
					break;
				case PURL:
					{
					setState(33);
					match(PURL);
					}
					break;
				case PULR:
					{
					setState(34);
					match(PULR);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(37);
				string();
				}
				break;
			case UP:
				enterOuterAlt(_localctx, 2);
				{
				setState(39);
				match(UP);
				setState(40);
				string();
				}
				break;
			case RE:
			case REL:
			case RER:
				enterOuterAlt(_localctx, 3);
				{
				setState(41);
				_la = _input.LA(1);
				if ( !(((_la) & ~0x3f) == 0 && ((1L << _la) & 896L) != 0) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(42);
				string();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FingerContext extends ParserRuleContext {
		public TerminalNode T() { return getToken(IntermediateParser.T, 0); }
		public TerminalNode F() { return getToken(IntermediateParser.F, 0); }
		public TerminalNode M() { return getToken(IntermediateParser.M, 0); }
		public TerminalNode R() { return getToken(IntermediateParser.R, 0); }
		public TerminalNode L() { return getToken(IntermediateParser.L, 0); }
		public FingerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_finger; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof IntermediateListener ) ((IntermediateListener)listener).enterFinger(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof IntermediateListener ) ((IntermediateListener)listener).exitFinger(this);
		}
	}

	public final FingerContext finger() throws RecognitionException {
		FingerContext _localctx = new FingerContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_finger);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			_la = _input.LA(1);
			if ( !(((_la) & ~0x3f) == 0 && ((1L << _la) & 4063232L) != 0) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StringContext extends ParserRuleContext {
		public TbContext tb() {
			return getRuleContext(TbContext.class,0);
		}
		public NfContext nf() {
			return getRuleContext(NfContext.class,0);
		}
		public FingerContext finger() {
			return getRuleContext(FingerContext.class,0);
		}
		public TerminalNode S() { return getToken(IntermediateParser.S, 0); }
		public TerminalNode N() { return getToken(IntermediateParser.N, 0); }
		public StringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof IntermediateListener ) ((IntermediateListener)listener).enterString(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof IntermediateListener ) ((IntermediateListener)listener).exitString(this);
		}
	}

	public final StringContext string() throws RecognitionException {
		StringContext _localctx = new StringContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_string);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			tb();
			setState(48);
			nf();
			setState(49);
			finger();
			setState(50);
			_la = _input.LA(1);
			if ( !(_la==S || _la==N) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MoveContext extends ParserRuleContext {
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public TerminalNode MO() { return getToken(IntermediateParser.MO, 0); }
		public TerminalNode MU() { return getToken(IntermediateParser.MU, 0); }
		public MoveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_move; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof IntermediateListener ) ((IntermediateListener)listener).enterMove(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof IntermediateListener ) ((IntermediateListener)listener).exitMove(this);
		}
	}

	public final MoveContext move() throws RecognitionException {
		MoveContext _localctx = new MoveContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_move);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			_la = _input.LA(1);
			if ( !(_la==MO || _la==MU) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(53);
			string();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TbContext extends ParserRuleContext {
		public TerminalNode HT() { return getToken(IntermediateParser.HT, 0); }
		public TerminalNode HB() { return getToken(IntermediateParser.HB, 0); }
		public TbContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tb; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof IntermediateListener ) ((IntermediateListener)listener).enterTb(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof IntermediateListener ) ((IntermediateListener)listener).exitTb(this);
		}
	}

	public final TbContext tb() throws RecognitionException {
		TbContext _localctx = new TbContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_tb);
		try {
			setState(58);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case HT:
				enterOuterAlt(_localctx, 1);
				{
				setState(55);
				match(HT);
				}
				break;
			case HB:
				enterOuterAlt(_localctx, 2);
				{
				setState(56);
				match(HB);
				}
				break;
			case T:
			case F:
			case M:
			case R:
			case L:
			case DN:
			case DF:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NfContext extends ParserRuleContext {
		public TerminalNode DN() { return getToken(IntermediateParser.DN, 0); }
		public TerminalNode DF() { return getToken(IntermediateParser.DF, 0); }
		public NfContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nf; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof IntermediateListener ) ((IntermediateListener)listener).enterNf(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof IntermediateListener ) ((IntermediateListener)listener).exitNf(this);
		}
	}

	public final NfContext nf() throws RecognitionException {
		NfContext _localctx = new NfContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_nf);
		try {
			setState(63);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DN:
				enterOuterAlt(_localctx, 1);
				{
				setState(60);
				match(DN);
				}
				break;
			case DF:
				enterOuterAlt(_localctx, 2);
				{
				setState(61);
				match(DF);
				}
				break;
			case T:
			case F:
			case M:
			case R:
			case L:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001bB\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0004\u0000\u0012\b\u0000\u000b\u0000\f\u0000\u0013\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0005\u0001\u001a\b\u0001\n\u0001"+
		"\f\u0001\u001d\t\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u0001$\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001,\b\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0003\u0005;\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006"+
		"@\b\u0006\u0001\u0006\u0000\u0000\u0007\u0000\u0002\u0004\u0006\b\n\f"+
		"\u0000\u0006\u0001\u0000\u0003\u0005\u0001\u0000\r\u000e\u0001\u0000\u0007"+
		"\t\u0001\u0000\u0011\u0015\u0001\u0000\u000f\u0010\u0001\u0000\u000b\f"+
		"E\u0000\u0011\u0001\u0000\u0000\u0000\u0002+\u0001\u0000\u0000\u0000\u0004"+
		"-\u0001\u0000\u0000\u0000\u0006/\u0001\u0000\u0000\u0000\b4\u0001\u0000"+
		"\u0000\u0000\n:\u0001\u0000\u0000\u0000\f?\u0001\u0000\u0000\u0000\u000e"+
		"\u000f\u0003\u0002\u0001\u0000\u000f\u0010\u0005\u001a\u0000\u0000\u0010"+
		"\u0012\u0001\u0000\u0000\u0000\u0011\u000e\u0001\u0000\u0000\u0000\u0012"+
		"\u0013\u0001\u0000\u0000\u0000\u0013\u0011\u0001\u0000\u0000\u0000\u0013"+
		"\u0014\u0001\u0000\u0000\u0000\u0014\u0015\u0001\u0000\u0000\u0000\u0015"+
		"\u0016\u0005\u0000\u0000\u0001\u0016\u0001\u0001\u0000\u0000\u0000\u0017"+
		"#\u0003\u0004\u0002\u0000\u0018\u001a\u0003\b\u0004\u0000\u0019\u0018"+
		"\u0001\u0000\u0000\u0000\u001a\u001d\u0001\u0000\u0000\u0000\u001b\u0019"+
		"\u0001\u0000\u0000\u0000\u001b\u001c\u0001\u0000\u0000\u0000\u001c\u001e"+
		"\u0001\u0000\u0000\u0000\u001d\u001b\u0001\u0000\u0000\u0000\u001e$\u0007"+
		"\u0000\u0000\u0000\u001f \u0007\u0001\u0000\u0000 $\u0005\n\u0000\u0000"+
		"!$\u0005\u0001\u0000\u0000\"$\u0005\u0002\u0000\u0000#\u001b\u0001\u0000"+
		"\u0000\u0000#\u001f\u0001\u0000\u0000\u0000#!\u0001\u0000\u0000\u0000"+
		"#\"\u0001\u0000\u0000\u0000$%\u0001\u0000\u0000\u0000%&\u0003\u0006\u0003"+
		"\u0000&,\u0001\u0000\u0000\u0000\'(\u0005\u0006\u0000\u0000(,\u0003\u0006"+
		"\u0003\u0000)*\u0007\u0002\u0000\u0000*,\u0003\u0006\u0003\u0000+\u0017"+
		"\u0001\u0000\u0000\u0000+\'\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000"+
		"\u0000,\u0003\u0001\u0000\u0000\u0000-.\u0007\u0003\u0000\u0000.\u0005"+
		"\u0001\u0000\u0000\u0000/0\u0003\n\u0005\u000001\u0003\f\u0006\u00001"+
		"2\u0003\u0004\u0002\u000023\u0007\u0004\u0000\u00003\u0007\u0001\u0000"+
		"\u0000\u000045\u0007\u0005\u0000\u000056\u0003\u0006\u0003\u00006\t\u0001"+
		"\u0000\u0000\u00007;\u0005\u0016\u0000\u00008;\u0005\u0017\u0000\u0000"+
		"9;\u0001\u0000\u0000\u0000:7\u0001\u0000\u0000\u0000:8\u0001\u0000\u0000"+
		"\u0000:9\u0001\u0000\u0000\u0000;\u000b\u0001\u0000\u0000\u0000<@\u0005"+
		"\u0018\u0000\u0000=@\u0005\u0019\u0000\u0000>@\u0001\u0000\u0000\u0000"+
		"?<\u0001\u0000\u0000\u0000?=\u0001\u0000\u0000\u0000?>\u0001\u0000\u0000"+
		"\u0000@\r\u0001\u0000\u0000\u0000\u0006\u0013\u001b#+:?";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}