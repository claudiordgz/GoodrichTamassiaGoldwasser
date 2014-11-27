@ECHO OFF
:: Prepare the Command Processor
SETLOCAL ENABLEEXTENSIONS
SETLOCAL ENABLEDELAYEDEXPANSION

set SolutionDirectory=%~dp0
START  /b /wait "HTLATEX" /d  "%SolutionDirectory%" htlatex GoodrichTamassiaGoldwasserPages.tex blogConfig.cfg
echo.
echo.
echo  			HTLATEX done...
echo.
echo.
START  /b /wait "Bootstrapify" /d  "%SolutionDirectory%" Bootstrapify.exe GoodrichTamassiaGoldwasserPages.html index.html
echo.
echo.
echo  			Bootstrapify done...
echo.
echo.
START /b /wait "Tidy2" %SolutionDirectory%\..\tools\tidy2\tidy.exe "index.html"
echo.
echo.
echo  			Tidy2 done...
echo.
echo.
goto :eof