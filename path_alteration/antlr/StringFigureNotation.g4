grammar StringFigureNotation;

commands : (command SEMICOLON) *
;

command : fingerWithSide ((move*) PU | (MA | MT) TW) stringWithSide
		| UP string
		| RE stringWithSide
		| OE | NE
;

finger : T | F | M | R | L
;

fingerWithSide : (SIDEL | SIDER | ) finger
;

string : tb nf finger (S | N)
;

stringWithSide : (SIDEL | SIDER | ) string
;

move : (MO | MU | TH) string
;

tb : HT | HB |
;

nf : DN | DF |
;

PU : 'pu';
UP : 'up';
RE : 're';
OE : 'OE';
NE : 'NE';
TW : 'tw';
MO : 'mo';
MU : 'mu';
MA : 'ma';
MT : 'mt';
TH :'th';
S : 'S';
N : 'N';
T : 'T';
F : 'F';
M : 'M';
R : 'R';
L : 'L';
HT : 't';
HB : 'b';
DN : 'n';
DF : 'f';
SIDEL : 'l';
SIDER : 'r';
SEMICOLON : ';';

WS : [ \t\r\n]+ -> skip ;
