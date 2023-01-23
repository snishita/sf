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
public class StringFigureNotationParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.11.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PU=1, UP=2, RE=3, OE=4, NE=5, TW=6, MO=7, MU=8, MA=9, MT=10, TH=11, S=12, 
		N=13, T=14, F=15, M=16, R=17, L=18, HT=19, HB=20, DN=21, DF=22, SIDEL=23, 
		SIDER=24, SEMICOLON=25, WS=26;
	public static final int
		RULE_commands = 0, RULE_command = 1, RULE_finger = 2, RULE_fingerWithSide = 3, 
		RULE_string = 4, RULE_stringWithSide = 5, RULE_move = 6, RULE_tb = 7, 
		RULE_nf = 8;
	private static String[] makeRuleNames() {
		return new String[] {
			"commands", "command", "finger", "fingerWithSide", "string", "stringWithSide", 
			"move", "tb", "nf"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'pu'", "'up'", "'re'", "'OE'", "'NE'", "'tw'", "'mo'", "'mu'", 
			"'ma'", "'mt'", "'th'", "'S'", "'N'", "'T'", "'F'", "'M'", "'R'", "'L'", 
			"'t'", "'b'", "'n'", "'f'", "'l'", "'r'", "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PU", "UP", "RE", "OE", "NE", "TW", "MO", "MU", "MA", "MT", "TH", 
			"S", "N", "T", "F", "M", "R", "L", "HT", "HB", "DN", "DF", "SIDEL", "SIDER", 
			"SEMICOLON", "WS"
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

	public StringFigureNotationParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CommandsContext extends ParserRuleContext {
		public List<CommandContext> command() {
			return getRuleContexts(CommandContext.class);
		}
		public CommandContext command(int i) {
			return getRuleContext(CommandContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(StringFigureNotationParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(StringFigureNotationParser.SEMICOLON, i);
		}
		public CommandsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_commands; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StringFigureNotationListener ) ((StringFigureNotationListener)listener).enterCommands(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StringFigureNotationListener ) ((StringFigureNotationListener)listener).exitCommands(this);
		}
	}

	public final CommandsContext commands() throws RecognitionException {
		CommandsContext _localctx = new CommandsContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_commands);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(23);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((_la) & ~0x3f) == 0 && ((1L << _la) & 25673788L) != 0) {
				{
				{
				setState(18);
				command();
				setState(19);
				match(SEMICOLON);
				}
				}
				setState(25);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class CommandContext extends ParserRuleContext {
		public FingerWithSideContext fingerWithSide() {
			return getRuleContext(FingerWithSideContext.class,0);
		}
		public StringWithSideContext stringWithSide() {
			return getRuleContext(StringWithSideContext.class,0);
		}
		public TerminalNode PU() { return getToken(StringFigureNotationParser.PU, 0); }
		public TerminalNode TW() { return getToken(StringFigureNotationParser.TW, 0); }
		public TerminalNode MA() { return getToken(StringFigureNotationParser.MA, 0); }
		public TerminalNode MT() { return getToken(StringFigureNotationParser.MT, 0); }
		public List<MoveContext> move() {
			return getRuleContexts(MoveContext.class);
		}
		public MoveContext move(int i) {
			return getRuleContext(MoveContext.class,i);
		}
		public TerminalNode UP() { return getToken(StringFigureNotationParser.UP, 0); }
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public TerminalNode RE() { return getToken(StringFigureNotationParser.RE, 0); }
		public TerminalNode OE() { return getToken(StringFigureNotationParser.OE, 0); }
		public TerminalNode NE() { return getToken(StringFigureNotationParser.NE, 0); }
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StringFigureNotationListener ) ((StringFigureNotationListener)listener).enterCommand(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StringFigureNotationListener ) ((StringFigureNotationListener)listener).exitCommand(this);
		}
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_command);
		int _la;
		try {
			setState(46);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T:
			case F:
			case M:
			case R:
			case L:
			case SIDEL:
			case SIDER:
				enterOuterAlt(_localctx, 1);
				{
				setState(26);
				fingerWithSide();
				setState(36);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PU:
				case MO:
				case MU:
				case TH:
					{
					{
					setState(30);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (((_la) & ~0x3f) == 0 && ((1L << _la) & 2432L) != 0) {
						{
						{
						setState(27);
						move();
						}
						}
						setState(32);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
					setState(33);
					match(PU);
					}
					break;
				case MA:
				case MT:
					{
					setState(34);
					_la = _input.LA(1);
					if ( !(_la==MA || _la==MT) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(35);
					match(TW);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(38);
				stringWithSide();
				}
				break;
			case UP:
				enterOuterAlt(_localctx, 2);
				{
				setState(40);
				match(UP);
				setState(41);
				string();
				}
				break;
			case RE:
				enterOuterAlt(_localctx, 3);
				{
				setState(42);
				match(RE);
				setState(43);
				stringWithSide();
				}
				break;
			case OE:
				enterOuterAlt(_localctx, 4);
				{
				setState(44);
				match(OE);
				}
				break;
			case NE:
				enterOuterAlt(_localctx, 5);
				{
				setState(45);
				match(NE);
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
		public TerminalNode T() { return getToken(StringFigureNotationParser.T, 0); }
		public TerminalNode F() { return getToken(StringFigureNotationParser.F, 0); }
		public TerminalNode M() { return getToken(StringFigureNotationParser.M, 0); }
		public TerminalNode R() { return getToken(StringFigureNotationParser.R, 0); }
		public TerminalNode L() { return getToken(StringFigureNotationParser.L, 0); }
		public FingerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_finger; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StringFigureNotationListener ) ((StringFigureNotationListener)listener).enterFinger(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StringFigureNotationListener ) ((StringFigureNotationListener)listener).exitFinger(this);
		}
	}

	public final FingerContext finger() throws RecognitionException {
		FingerContext _localctx = new FingerContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_finger);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			_la = _input.LA(1);
			if ( !(((_la) & ~0x3f) == 0 && ((1L << _la) & 507904L) != 0) ) {
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
	public static class FingerWithSideContext extends ParserRuleContext {
		public FingerContext finger() {
			return getRuleContext(FingerContext.class,0);
		}
		public TerminalNode SIDEL() { return getToken(StringFigureNotationParser.SIDEL, 0); }
		public TerminalNode SIDER() { return getToken(StringFigureNotationParser.SIDER, 0); }
		public FingerWithSideContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fingerWithSide; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StringFigureNotationListener ) ((StringFigureNotationListener)listener).enterFingerWithSide(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StringFigureNotationListener ) ((StringFigureNotationListener)listener).exitFingerWithSide(this);
		}
	}

	public final FingerWithSideContext fingerWithSide() throws RecognitionException {
		FingerWithSideContext _localctx = new FingerWithSideContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_fingerWithSide);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SIDEL:
				{
				setState(50);
				match(SIDEL);
				}
				break;
			case SIDER:
				{
				setState(51);
				match(SIDER);
				}
				break;
			case T:
			case F:
			case M:
			case R:
			case L:
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(55);
			finger();
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
		public TerminalNode S() { return getToken(StringFigureNotationParser.S, 0); }
		public TerminalNode N() { return getToken(StringFigureNotationParser.N, 0); }
		public StringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StringFigureNotationListener ) ((StringFigureNotationListener)listener).enterString(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StringFigureNotationListener ) ((StringFigureNotationListener)listener).exitString(this);
		}
	}

	public final StringContext string() throws RecognitionException {
		StringContext _localctx = new StringContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_string);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			tb();
			setState(58);
			nf();
			setState(59);
			finger();
			setState(60);
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
	public static class StringWithSideContext extends ParserRuleContext {
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public TerminalNode SIDEL() { return getToken(StringFigureNotationParser.SIDEL, 0); }
		public TerminalNode SIDER() { return getToken(StringFigureNotationParser.SIDER, 0); }
		public StringWithSideContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stringWithSide; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StringFigureNotationListener ) ((StringFigureNotationListener)listener).enterStringWithSide(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StringFigureNotationListener ) ((StringFigureNotationListener)listener).exitStringWithSide(this);
		}
	}

	public final StringWithSideContext stringWithSide() throws RecognitionException {
		StringWithSideContext _localctx = new StringWithSideContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_stringWithSide);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(65);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SIDEL:
				{
				setState(62);
				match(SIDEL);
				}
				break;
			case SIDER:
				{
				setState(63);
				match(SIDER);
				}
				break;
			case T:
			case F:
			case M:
			case R:
			case L:
			case HT:
			case HB:
			case DN:
			case DF:
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(67);
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
	public static class MoveContext extends ParserRuleContext {
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public TerminalNode MO() { return getToken(StringFigureNotationParser.MO, 0); }
		public TerminalNode MU() { return getToken(StringFigureNotationParser.MU, 0); }
		public TerminalNode TH() { return getToken(StringFigureNotationParser.TH, 0); }
		public MoveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_move; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StringFigureNotationListener ) ((StringFigureNotationListener)listener).enterMove(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StringFigureNotationListener ) ((StringFigureNotationListener)listener).exitMove(this);
		}
	}

	public final MoveContext move() throws RecognitionException {
		MoveContext _localctx = new MoveContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_move);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			_la = _input.LA(1);
			if ( !(((_la) & ~0x3f) == 0 && ((1L << _la) & 2432L) != 0) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(70);
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
		public TerminalNode HT() { return getToken(StringFigureNotationParser.HT, 0); }
		public TerminalNode HB() { return getToken(StringFigureNotationParser.HB, 0); }
		public TbContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tb; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StringFigureNotationListener ) ((StringFigureNotationListener)listener).enterTb(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StringFigureNotationListener ) ((StringFigureNotationListener)listener).exitTb(this);
		}
	}

	public final TbContext tb() throws RecognitionException {
		TbContext _localctx = new TbContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_tb);
		try {
			setState(75);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case HT:
				enterOuterAlt(_localctx, 1);
				{
				setState(72);
				match(HT);
				}
				break;
			case HB:
				enterOuterAlt(_localctx, 2);
				{
				setState(73);
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
		public TerminalNode DN() { return getToken(StringFigureNotationParser.DN, 0); }
		public TerminalNode DF() { return getToken(StringFigureNotationParser.DF, 0); }
		public NfContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nf; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StringFigureNotationListener ) ((StringFigureNotationListener)listener).enterNf(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StringFigureNotationListener ) ((StringFigureNotationListener)listener).exitNf(this);
		}
	}

	public final NfContext nf() throws RecognitionException {
		NfContext _localctx = new NfContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_nf);
		try {
			setState(80);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DN:
				enterOuterAlt(_localctx, 1);
				{
				setState(77);
				match(DN);
				}
				break;
			case DF:
				enterOuterAlt(_localctx, 2);
				{
				setState(78);
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
		"\u0004\u0001\u001aS\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0001\u0000\u0001\u0000\u0001\u0000\u0005\u0000\u0016\b\u0000"+
		"\n\u0000\f\u0000\u0019\t\u0000\u0001\u0001\u0001\u0001\u0005\u0001\u001d"+
		"\b\u0001\n\u0001\f\u0001 \t\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0003\u0001%\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001/\b\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003"+
		"6\b\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005"+
		"B\b\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007L\b\u0007\u0001\b\u0001"+
		"\b\u0001\b\u0003\bQ\b\b\u0001\b\u0000\u0000\t\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0000\u0004\u0001\u0000\t\n\u0001\u0000\u000e\u0012"+
		"\u0001\u0000\f\r\u0002\u0000\u0007\b\u000b\u000bX\u0000\u0017\u0001\u0000"+
		"\u0000\u0000\u0002.\u0001\u0000\u0000\u0000\u00040\u0001\u0000\u0000\u0000"+
		"\u00065\u0001\u0000\u0000\u0000\b9\u0001\u0000\u0000\u0000\nA\u0001\u0000"+
		"\u0000\u0000\fE\u0001\u0000\u0000\u0000\u000eK\u0001\u0000\u0000\u0000"+
		"\u0010P\u0001\u0000\u0000\u0000\u0012\u0013\u0003\u0002\u0001\u0000\u0013"+
		"\u0014\u0005\u0019\u0000\u0000\u0014\u0016\u0001\u0000\u0000\u0000\u0015"+
		"\u0012\u0001\u0000\u0000\u0000\u0016\u0019\u0001\u0000\u0000\u0000\u0017"+
		"\u0015\u0001\u0000\u0000\u0000\u0017\u0018\u0001\u0000\u0000\u0000\u0018"+
		"\u0001\u0001\u0000\u0000\u0000\u0019\u0017\u0001\u0000\u0000\u0000\u001a"+
		"$\u0003\u0006\u0003\u0000\u001b\u001d\u0003\f\u0006\u0000\u001c\u001b"+
		"\u0001\u0000\u0000\u0000\u001d \u0001\u0000\u0000\u0000\u001e\u001c\u0001"+
		"\u0000\u0000\u0000\u001e\u001f\u0001\u0000\u0000\u0000\u001f!\u0001\u0000"+
		"\u0000\u0000 \u001e\u0001\u0000\u0000\u0000!%\u0005\u0001\u0000\u0000"+
		"\"#\u0007\u0000\u0000\u0000#%\u0005\u0006\u0000\u0000$\u001e\u0001\u0000"+
		"\u0000\u0000$\"\u0001\u0000\u0000\u0000%&\u0001\u0000\u0000\u0000&\'\u0003"+
		"\n\u0005\u0000\'/\u0001\u0000\u0000\u0000()\u0005\u0002\u0000\u0000)/"+
		"\u0003\b\u0004\u0000*+\u0005\u0003\u0000\u0000+/\u0003\n\u0005\u0000,"+
		"/\u0005\u0004\u0000\u0000-/\u0005\u0005\u0000\u0000.\u001a\u0001\u0000"+
		"\u0000\u0000.(\u0001\u0000\u0000\u0000.*\u0001\u0000\u0000\u0000.,\u0001"+
		"\u0000\u0000\u0000.-\u0001\u0000\u0000\u0000/\u0003\u0001\u0000\u0000"+
		"\u000001\u0007\u0001\u0000\u00001\u0005\u0001\u0000\u0000\u000026\u0005"+
		"\u0017\u0000\u000036\u0005\u0018\u0000\u000046\u0001\u0000\u0000\u0000"+
		"52\u0001\u0000\u0000\u000053\u0001\u0000\u0000\u000054\u0001\u0000\u0000"+
		"\u000067\u0001\u0000\u0000\u000078\u0003\u0004\u0002\u00008\u0007\u0001"+
		"\u0000\u0000\u00009:\u0003\u000e\u0007\u0000:;\u0003\u0010\b\u0000;<\u0003"+
		"\u0004\u0002\u0000<=\u0007\u0002\u0000\u0000=\t\u0001\u0000\u0000\u0000"+
		">B\u0005\u0017\u0000\u0000?B\u0005\u0018\u0000\u0000@B\u0001\u0000\u0000"+
		"\u0000A>\u0001\u0000\u0000\u0000A?\u0001\u0000\u0000\u0000A@\u0001\u0000"+
		"\u0000\u0000BC\u0001\u0000\u0000\u0000CD\u0003\b\u0004\u0000D\u000b\u0001"+
		"\u0000\u0000\u0000EF\u0007\u0003\u0000\u0000FG\u0003\b\u0004\u0000G\r"+
		"\u0001\u0000\u0000\u0000HL\u0005\u0013\u0000\u0000IL\u0005\u0014\u0000"+
		"\u0000JL\u0001\u0000\u0000\u0000KH\u0001\u0000\u0000\u0000KI\u0001\u0000"+
		"\u0000\u0000KJ\u0001\u0000\u0000\u0000L\u000f\u0001\u0000\u0000\u0000"+
		"MQ\u0005\u0015\u0000\u0000NQ\u0005\u0016\u0000\u0000OQ\u0001\u0000\u0000"+
		"\u0000PM\u0001\u0000\u0000\u0000PN\u0001\u0000\u0000\u0000PO\u0001\u0000"+
		"\u0000\u0000Q\u0011\u0001\u0000\u0000\u0000\b\u0017\u001e$.5AKP";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}