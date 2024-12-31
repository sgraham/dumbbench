@echo off

::wc -l dumbbench*.lua
echo.
echo.
echo ... lua, pucrio 5.4.7
tim lua.exe dumbbench.lua
echo.
echo.
echo ... lua, luajit 2.1
tim luajit.exe dumbbench.lua

::wc -l dumbbench.py
echo.
echo.
echo ... python
tim python.exe dumbbench.py

::wc -l dumbbench.c
echo.
echo.
echo ... c, clang
tim clang.exe -fsyntax-only dumbbench.c
echo.
echo.
echo ... c, cl
tim cl.exe /nologo /Zs dumbbench.c
echo.
echo.
echo ... c, tcc
tim tcc.exe -run dumbbench.c
