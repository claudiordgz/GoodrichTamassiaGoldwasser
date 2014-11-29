@ECHO OFF
:: Prepare the Command Processor
SETLOCAL ENABLEEXTENSIONS
SETLOCAL ENABLEDELAYEDEXPANSION

set SolutionDirectory=%~dp0
START  /b /wait "HTLATEX" /d  "%SolutionDirectory%" htlatex GoodrichTamassiaGoldwasserPages.tex blog.cfg
echo.
echo.
echo  			HTLATEX done...
echo.
echo.
START  /b /wait "Bootstrapify" /d  "%SolutionDirectory%" Bootstrapify.exe GoodrichTamassiaGoldwasserPages.html file.html
echo.
echo.
echo  			Bootstrapify done...
echo.
echo.
START /b /wait "BeautifulSoup"  C:\Anaconda\python.exe ..\BeautifyHtml\BeautifyHtml.py
echo.
echo.
echo  			BeautifulSoup done...
echo.
echo.
del file.html
START  /b /wait "XELATEX" /d  "%SolutionDirectory%" xelatex -enable-write18 -synctex=-1 -max-print-line=120 "GoodrichTamassiaGoldwasserPages.tex" 
echo.
echo.
echo  			XELATEX done...
echo.
echo.
goto :eof