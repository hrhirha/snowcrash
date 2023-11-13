import gdb

gdb.execute('file /bin/getflag')
gdb.execute('b ptrace')
gdb.execute('b getuid')
gdb.execute('r')
gdb.execute('step')
gdb.execute('set $eax=0')
gdb.execute('c')
gdb.execute('step')
gdb.execute('set $eax = 3014')
gdb.execute('c')
gdb.execute('quit')