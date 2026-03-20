# --encoding:utf-8--
import curses
import time

strLine = "Hello World!!! Printing Square!!! Press Any Key To Exit!!!"
scr = curses.initscr()
curses.curs_set(0)
scr.clear()
nLen = len(strLine)
for i in range(0, nLen - 1):
    scr.addstr(10, 10 + i, strLine[i] + chr(0x2588))
    scr.refresh() 
    time.sleep(.5) 
scr.addstr(10, 10, strLine + " ")
scr.getch()
curses.endwin()