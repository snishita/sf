// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class StringFigureNotationLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.11.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PU=1, UP=2, RE=3, OE=4, NE=5, TW=6, MO=7, MU=8, MA=9, MT=10, TH=11, S=12, 
		N=13, T=14, F=15, M=16, R=17, L=18, HT=19, HB=20, DN=21, DF=22, SIDEL=23, 
		SIDER=24, SEMICOLON=25, WS=26;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"PU", "UP", "RE", "OE", "NE", "TW", "MO", "MU", "MA", "MT", "TH", "S", 
			"N", "T", "F", "M", "R", "L", "HT", "HB", "DN", "DF", "SIDEL", "SIDER", 
			"SEMICOLON", "WS"
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


	public StringFigureNotationLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "StringFigureNotation.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u001ay\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001"+
		"\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012"+
		"\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015"+
		"\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018"+
		"\u0001\u0019\u0004\u0019t\b\u0019\u000b\u0019\f\u0019u\u0001\u0019\u0001"+
		"\u0019\u0000\u0000\u001a\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004"+
		"\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017"+
		"\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'"+
		"\u0014)\u0015+\u0016-\u0017/\u00181\u00193\u001a\u0001\u0000\u0001\u0003"+
		"\u0000\t\n\r\r  y\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001"+
		"\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001"+
		"\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000"+
		"\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000"+
		"\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000"+
		"\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000"+
		"\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000"+
		"\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000"+
		"\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000"+
		"%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001"+
		"\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000"+
		"\u0000\u0000/\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u0000"+
		"3\u0001\u0000\u0000\u0000\u00015\u0001\u0000\u0000\u0000\u00038\u0001"+
		"\u0000\u0000\u0000\u0005;\u0001\u0000\u0000\u0000\u0007>\u0001\u0000\u0000"+
		"\u0000\tA\u0001\u0000\u0000\u0000\u000bD\u0001\u0000\u0000\u0000\rG\u0001"+
		"\u0000\u0000\u0000\u000fJ\u0001\u0000\u0000\u0000\u0011M\u0001\u0000\u0000"+
		"\u0000\u0013P\u0001\u0000\u0000\u0000\u0015S\u0001\u0000\u0000\u0000\u0017"+
		"V\u0001\u0000\u0000\u0000\u0019X\u0001\u0000\u0000\u0000\u001bZ\u0001"+
		"\u0000\u0000\u0000\u001d\\\u0001\u0000\u0000\u0000\u001f^\u0001\u0000"+
		"\u0000\u0000!`\u0001\u0000\u0000\u0000#b\u0001\u0000\u0000\u0000%d\u0001"+
		"\u0000\u0000\u0000\'f\u0001\u0000\u0000\u0000)h\u0001\u0000\u0000\u0000"+
		"+j\u0001\u0000\u0000\u0000-l\u0001\u0000\u0000\u0000/n\u0001\u0000\u0000"+
		"\u00001p\u0001\u0000\u0000\u00003s\u0001\u0000\u0000\u000056\u0005p\u0000"+
		"\u000067\u0005u\u0000\u00007\u0002\u0001\u0000\u0000\u000089\u0005u\u0000"+
		"\u00009:\u0005p\u0000\u0000:\u0004\u0001\u0000\u0000\u0000;<\u0005r\u0000"+
		"\u0000<=\u0005e\u0000\u0000=\u0006\u0001\u0000\u0000\u0000>?\u0005O\u0000"+
		"\u0000?@\u0005E\u0000\u0000@\b\u0001\u0000\u0000\u0000AB\u0005N\u0000"+
		"\u0000BC\u0005E\u0000\u0000C\n\u0001\u0000\u0000\u0000DE\u0005t\u0000"+
		"\u0000EF\u0005w\u0000\u0000F\f\u0001\u0000\u0000\u0000GH\u0005m\u0000"+
		"\u0000HI\u0005o\u0000\u0000I\u000e\u0001\u0000\u0000\u0000JK\u0005m\u0000"+
		"\u0000KL\u0005u\u0000\u0000L\u0010\u0001\u0000\u0000\u0000MN\u0005m\u0000"+
		"\u0000NO\u0005a\u0000\u0000O\u0012\u0001\u0000\u0000\u0000PQ\u0005m\u0000"+
		"\u0000QR\u0005t\u0000\u0000R\u0014\u0001\u0000\u0000\u0000ST\u0005t\u0000"+
		"\u0000TU\u0005h\u0000\u0000U\u0016\u0001\u0000\u0000\u0000VW\u0005S\u0000"+
		"\u0000W\u0018\u0001\u0000\u0000\u0000XY\u0005N\u0000\u0000Y\u001a\u0001"+
		"\u0000\u0000\u0000Z[\u0005T\u0000\u0000[\u001c\u0001\u0000\u0000\u0000"+
		"\\]\u0005F\u0000\u0000]\u001e\u0001\u0000\u0000\u0000^_\u0005M\u0000\u0000"+
		"_ \u0001\u0000\u0000\u0000`a\u0005R\u0000\u0000a\"\u0001\u0000\u0000\u0000"+
		"bc\u0005L\u0000\u0000c$\u0001\u0000\u0000\u0000de\u0005t\u0000\u0000e"+
		"&\u0001\u0000\u0000\u0000fg\u0005b\u0000\u0000g(\u0001\u0000\u0000\u0000"+
		"hi\u0005n\u0000\u0000i*\u0001\u0000\u0000\u0000jk\u0005f\u0000\u0000k"+
		",\u0001\u0000\u0000\u0000lm\u0005l\u0000\u0000m.\u0001\u0000\u0000\u0000"+
		"no\u0005r\u0000\u0000o0\u0001\u0000\u0000\u0000pq\u0005;\u0000\u0000q"+
		"2\u0001\u0000\u0000\u0000rt\u0007\u0000\u0000\u0000sr\u0001\u0000\u0000"+
		"\u0000tu\u0001\u0000\u0000\u0000us\u0001\u0000\u0000\u0000uv\u0001\u0000"+
		"\u0000\u0000vw\u0001\u0000\u0000\u0000wx\u0006\u0019\u0000\u0000x4\u0001"+
		"\u0000\u0000\u0000\u0002\u0000u\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}