# hikvision_recorder

g++ -std=c99 -ggdb3 -O0 -pedantic-errors -Wall -Wextra   -fpie $(python3-config --cflags --embed) -o 'test' src/hikvisionmodule.cpp  $(python3-config --embed --ldflags)