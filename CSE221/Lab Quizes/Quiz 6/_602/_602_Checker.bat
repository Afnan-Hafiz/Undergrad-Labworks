@echo off
set TID=_602
@REM for %%a in ("%CD%") do set TID=%%~nxa
set SID=23241004
set LNG=py
c++ %TID%.cpp
.\a.exe %TID% %SID% %LNG%
for %%a in (*) do if %%~za==0 del %%a
del /f /s /q /a .\out.txt >nul
del /f /s /q /a .\in.txt >nul
del /f /s /q /a .\*.exe >nul
del /f /s /q /a .\*.class >nul
rd /s /q __pycache__ >nul
pause
