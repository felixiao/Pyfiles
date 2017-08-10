@echo off& setlocal EnableDelayedExpansion
echo [ >>AVS.txt
for /r "Z:\video\" %%s in (*.mp4,*.wmv,*.avi,*.mkv) do (
   set var=%%~dps
   set var=!var:\=\\!
   echo {"path":"!var!","name":"%%~nxs"}, >>AVS.txt
)
echo {}] >>AVS.txt
python GetAllFiles.py
del AVS.txt
pause
