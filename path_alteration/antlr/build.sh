#!/bin/bash
# brew install antlr
# pip install antlr4_python3_runtime

#JARFILE='/usr/local/Cellar/antlr/4.8_1/antlr-4.8-complete.jar'
#JARFILE='/usr/local/Cellar/antlr/4.9.3/antlr-4.9.3-complete.jar'
JARFILE='/opt/homebrew/Cellar/antlr/4.11.1/antlr-4.11.1-complete.jar'

echo 'あやとり表記法のパーサを作ります．'
antlr StringFigureNotation.g4 
javac -cp .:${JARFILE} *.java
#echo 'あやとり表記法のテストする文字列を入力してください．'
#grun StringFigureNotation commands -tree
echo 'Python3 のコードを作成します'
antlr -Dlanguage=Python3 StringFigureNotation.g4

echo
echo '中間表現のパーサを作ります．'
antlr Intermediate.g4 
javac -cp .:${JARFILE} *.java
#echo '中間表現のテストする文字列を入力してください．'
#grun Intermediate intermediate -tree
echo 'Python3 のコードを作成します'
antlr -Dlanguage=Python3 Intermediate.g4

