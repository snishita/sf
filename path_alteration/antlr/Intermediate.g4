grammar Intermediate;

intermediate : (command SEMICOLON)+ EOF
;

command : finger (move* (PU | PUR | PUL) | (MA | MT) TW | PURL | PULR) string
		| UP string
		| (RE | REL | RER) string
;

finger : T | F | M | R | L
;

string : tb nf finger (S | N)
;

move : (MO | MU) string
;

tb : HT | HB |
;

nf : DN | DF |
;

PURL : 'pu-rl';
PULR : 'pu-lr';
PUR : 'pu-r';
PUL : 'pu-l';
PU : 'pu';
UP : 'up';
RE : 're';
REL : 're-l';
RER : 're-r';
TW : 'tw';
MO : 'mo';
MU : 'mu';
MA : 'ma';
MT : 'mt';
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
SEMICOLON : ';';

WS : [ \t\r\n]+ -> skip ;
