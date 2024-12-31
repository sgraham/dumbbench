@echo off

wc -l dumbbench.py
tim python.exe dumbbench.py

wc -l dumbbench.c
tim clang.exe -fsyntax-only dumbbench.c
tim cl.exe /nologo /Zs dumbbench.c
tim tcc.exe -run dumbbench.c

wc -l dumbbench*.lua
tim lua.exe dumbbench0.lua dumbbench1.lua dumbbench2.lua dumbbench3.lua dumbbench4.lua dumbbench5.lua dumbbench6.lua dumbbench7.lua dumbbench8.lua dumbbench9.lua
