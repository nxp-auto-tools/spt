
SetLocal

IF NOT DEFINED ADL_VER        SET ADL_VER=adl-3.23.11
IF NOT DEFINED ZIP_BIN_DIR    SET ZIP_BIN_DIR=C:\cygwin64\bin
IF NOT DEFINED CLEANUP_DIRS   SET CLEANUP_DIRS=0

SET PATH=%PATH%;%ZIP_BIN_DIR%

SET SPT_SRC=tools_spt
SET SPT_BIN=SPT3
SET SPT_BUILD=SPT_build
SET ADL_SPT_SRC=adl_spt_src

IF NOT EXIST %SPT_SRC% goto :nosrc

set BUILD_PATH=%SPT_BUILD%
set RELEASE_PATH=%BUILD_PATH%\Release\
set DEBUG_PATH=%BUILD_PATH%\Debug\
set WIN_ZIP=SPT_%date:~-2,2%%date:~-10,2%%date:~-7,2%_win.zip

RMDIR /s /q %SPT_BUILD%
RMDIR /s /q %SPT_BIN%

MD %BUILD_PATH%
MD %BUILD_PATH%\tools_spt\dev\
MD %ADL_SPT_SRC%
MD art

@REM Download the required adl version source file and extract
CD %BUILD_PATH%
MD %ADL_VER%\
cd ..\
XCOPY /E /I C:\SPT_DO_NOT_DELETE\%ADL_VER% %BUILD_PATH%\%ADL_VER%\
del /Q %BUILD_PATH%\%ADL_VER%.tar.bz2

@REM Apply patch file if present.
CD %SPT_SRC%\build\
for %%a in (*.patch) do set "PATCHFILE=%%~fa"
CD ..\..\
IF DEFINED PATCHFILE (
  CD %BUILD_PATH%\%ADL_VER%\
  patch.exe -p1 -i %PATCHFILE% --binary -t                  || goto :error
  CD ..\..
)

unzip -o adl_src.zip -d %ADL_SPT_SRC%                       || goto :error

@REM Prepare the SPT source for build
COPY /Y %SPT_SRC%\build\win\vs2015\* %BUILD_PATH%\%ADL_VER%\
COPY /Y %ADL_SPT_SRC%\dev\* %BUILD_PATH%\tools_spt\dev\
COPY /Y %ADL_SPT_SRC%\dev\* %BUILD_PATH%\%ADL_VER%\


del /Q %RELEASE_PATH%\*

@REM Execute the VS project to build the tools
SET BOOST_ROOT=c:\boost\boost_1_65_1
call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\Tools\vsvars32.bat"
msbuild %BUILD_PATH%\%ADL_VER%\as-spt3.1.vcxproj /p:Configuration=Release      || goto :error
msbuild %BUILD_PATH%\%ADL_VER%\objdump-spt3.1.vcxproj /p:Configuration=Release      || goto :error

MD %SPT_BIN%\bin
MD %SPT_BIN%\doc
MD %SPT_BIN%\inc

copy /B %RELEASE_PATH%\as-spt3.1.exe %SPT_BIN%\bin\as-spt.exe
copy /B %RELEASE_PATH%\objdump-spt3.1.exe %SPT_BIN%\bin\objdump-spt.exe
copy /Y %SPT_SRC%\inc\*3.inc %SPT_BIN%\inc
copy /Y %SPT_SRC%\doc\as-spt3-manual.pdf %SPT_BIN%\doc
copy /Y "%SPT_SRC%\doc\SPT3 mnemonics QuickRef" %SPT_BIN%\doc
copy /Y %SPT_SRC%\doc\gas-manual.pdf %SPT_BIN%\doc
copy /Y %SPT_SRC%\doc\ReadMe.spt3.pdf %SPT_BIN%\ReadMe.pdf

zip -9 -r "%WIN_ZIP%" %SPT_BIN% 	                                                  || goto :error

copy %WIN_ZIP% art\%WIN_ZIP%


IF %CLEANUP_DIRS% NEQ 0 (
    RMDIR /s /q %SPT_BUILD%
    RMDIR /s /q %SPT_BIN%
    RMDIR /s /q %SPT_SRC%
    RMDIR /s /q %ADL_SPT_SRC%
)

EndLocal
goto :EOF

:error
echo Failed with error #%errorlevel%.
exit /b %errorlevel%

:nosrc
echo Missing %SPT_SRC% directory
exit /b 1
