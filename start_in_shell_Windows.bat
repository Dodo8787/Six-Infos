@echo off
set Date=%date%
set Heure=%time:~0,8%
set CourentDir=%cd%
echo ____________________________ >> log_error.txt
echo (Windows) Started: >> log_error.txt
echo Current Date and Time is: %Date% %Heure% >> log_error.txt
start "" /b "C:/Users/fbat9/AppData/Local/Programs/Python/Python311/python.exe" %CourentDir%/main.py >> log_error.txt 2>&1