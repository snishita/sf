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
public class IntermediateLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.11.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PURL=1, PULR=2, PUR=3, PUL=4, PU=5, UP=6, RE=7, REL=8, RER=9, TW=10, MO=11, 
		MU=12, MA=13, MT=14, S=15, N=16, T=17, F=18, M=19, R=20, L=21, HT=22, 
		HB=23, DN=24, DF=25, SEMICOLON=26, WS=27;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"PURL", "PULR", "PUR", "PUL", "PU", "UP", "RE", "REL", "RER", "TW", "MO", 
			"MU", "MA", "MT", "S", "N", "T", "F", "M", "R", "L", "HT", "HB", "DN", 
			"DF", "SEMICOLON", "WS"
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


	public IntermediateLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Intermediate.g4"; }

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
		"\u0004\u0000\u001b\u008e\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0002\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001"+
		"\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f"+
		"\u0001\f\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001"+
		"\u0012\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0015\u0001"+
		"\u0015\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0018\u0001"+
		"\u0018\u0001\u0019\u0001\u0019\u0001\u001a\u0004\u001a\u0089\b\u001a\u000b"+
		"\u001a\f\u001a\u008a\u0001\u001a\u0001\u001a\u0000\u0000\u001b\u0001\u0001"+
		"\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f"+
		"\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f"+
		"\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017/\u0018"+
		"1\u00193\u001a5\u001b\u0001\u0000\u0001\u0003\u0000\t\n\r\r  \u008e\u0000"+
		"\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000"+
		"\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000"+
		"\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r"+
		"\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011"+
		"\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015"+
		"\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019"+
		"\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d"+
		"\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001"+
		"\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000"+
		"\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000"+
		"\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000\u0000\u0000/"+
		"\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u00003\u0001\u0000"+
		"\u0000\u0000\u00005\u0001\u0000\u0000\u0000\u00017\u0001\u0000\u0000\u0000"+
		"\u0003=\u0001\u0000\u0000\u0000\u0005C\u0001\u0000\u0000\u0000\u0007H"+
		"\u0001\u0000\u0000\u0000\tM\u0001\u0000\u0000\u0000\u000bP\u0001\u0000"+
		"\u0000\u0000\rS\u0001\u0000\u0000\u0000\u000fV\u0001\u0000\u0000\u0000"+
		"\u0011[\u0001\u0000\u0000\u0000\u0013`\u0001\u0000\u0000\u0000\u0015c"+
		"\u0001\u0000\u0000\u0000\u0017f\u0001\u0000\u0000\u0000\u0019i\u0001\u0000"+
		"\u0000\u0000\u001bl\u0001\u0000\u0000\u0000\u001do\u0001\u0000\u0000\u0000"+
		"\u001fq\u0001\u0000\u0000\u0000!s\u0001\u0000\u0000\u0000#u\u0001\u0000"+
		"\u0000\u0000%w\u0001\u0000\u0000\u0000\'y\u0001\u0000\u0000\u0000){\u0001"+
		"\u0000\u0000\u0000+}\u0001\u0000\u0000\u0000-\u007f\u0001\u0000\u0000"+
		"\u0000/\u0081\u0001\u0000\u0000\u00001\u0083\u0001\u0000\u0000\u00003"+
		"\u0085\u0001\u0000\u0000\u00005\u0088\u0001\u0000\u0000\u000078\u0005"+
		"p\u0000\u000089\u0005u\u0000\u00009:\u0005-\u0000\u0000:;\u0005r\u0000"+
		"\u0000;<\u0005l\u0000\u0000<\u0002\u0001\u0000\u0000\u0000=>\u0005p\u0000"+
		"\u0000>?\u0005u\u0000\u0000?@\u0005-\u0000\u0000@A\u0005l\u0000\u0000"+
		"AB\u0005r\u0000\u0000B\u0004\u0001\u0000\u0000\u0000CD\u0005p\u0000\u0000"+
		"DE\u0005u\u0000\u0000EF\u0005-\u0000\u0000FG\u0005r\u0000\u0000G\u0006"+
		"\u0001\u0000\u0000\u0000HI\u0005p\u0000\u0000IJ\u0005u\u0000\u0000JK\u0005"+
		"-\u0000\u0000KL\u0005l\u0000\u0000L\b\u0001\u0000\u0000\u0000MN\u0005"+
		"p\u0000\u0000NO\u0005u\u0000\u0000O\n\u0001\u0000\u0000\u0000PQ\u0005"+
		"u\u0000\u0000QR\u0005p\u0000\u0000R\f\u0001\u0000\u0000\u0000ST\u0005"+
		"r\u0000\u0000TU\u0005e\u0000\u0000U\u000e\u0001\u0000\u0000\u0000VW\u0005"+
		"r\u0000\u0000WX\u0005e\u0000\u0000XY\u0005-\u0000\u0000YZ\u0005l\u0000"+
		"\u0000Z\u0010\u0001\u0000\u0000\u0000[\\\u0005r\u0000\u0000\\]\u0005e"+
		"\u0000\u0000]^\u0005-\u0000\u0000^_\u0005r\u0000\u0000_\u0012\u0001\u0000"+
		"\u0000\u0000`a\u0005t\u0000\u0000ab\u0005w\u0000\u0000b\u0014\u0001\u0000"+
		"\u0000\u0000cd\u0005m\u0000\u0000de\u0005o\u0000\u0000e\u0016\u0001\u0000"+
		"\u0000\u0000fg\u0005m\u0000\u0000gh\u0005u\u0000\u0000h\u0018\u0001\u0000"+
		"\u0000\u0000ij\u0005m\u0000\u0000jk\u0005a\u0000\u0000k\u001a\u0001\u0000"+
		"\u0000\u0000lm\u0005m\u0000\u0000mn\u0005t\u0000\u0000n\u001c\u0001\u0000"+
		"\u0000\u0000op\u0005S\u0000\u0000p\u001e\u0001\u0000\u0000\u0000qr\u0005"+
		"N\u0000\u0000r \u0001\u0000\u0000\u0000st\u0005T\u0000\u0000t\"\u0001"+
		"\u0000\u0000\u0000uv\u0005F\u0000\u0000v$\u0001\u0000\u0000\u0000wx\u0005"+
		"M\u0000\u0000x&\u0001\u0000\u0000\u0000yz\u0005R\u0000\u0000z(\u0001\u0000"+
		"\u0000\u0000{|\u0005L\u0000\u0000|*\u0001\u0000\u0000\u0000}~\u0005t\u0000"+
		"\u0000~,\u0001\u0000\u0000\u0000\u007f\u0080\u0005b\u0000\u0000\u0080"+
		".\u0001\u0000\u0000\u0000\u0081\u0082\u0005n\u0000\u0000\u00820\u0001"+
		"\u0000\u0000\u0000\u0083\u0084\u0005f\u0000\u0000\u00842\u0001\u0000\u0000"+
		"\u0000\u0085\u0086\u0005;\u0000\u0000\u00864\u0001\u0000\u0000\u0000\u0087"+
		"\u0089\u0007\u0000\u0000\u0000\u0088\u0087\u0001\u0000\u0000\u0000\u0089"+
		"\u008a\u0001\u0000\u0000\u0000\u008a\u0088\u0001\u0000\u0000\u0000\u008a"+
		"\u008b\u0001\u0000\u0000\u0000\u008b\u008c\u0001\u0000\u0000\u0000\u008c"+
		"\u008d\u0006\u001a\u0000\u0000\u008d6\u0001\u0000\u0000\u0000\u0002\u0000"+
		"\u008a\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}