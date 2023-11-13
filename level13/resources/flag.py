import gdb

gdb.execute('file ~/level13')
gdb.execute('set disassembly-flavor intel')
gdb.execute('b *main+14')
gdb.execute('r')
gdb.execute('set $eax=4242')
gdb.execute('c')
gdb.execute('quit')