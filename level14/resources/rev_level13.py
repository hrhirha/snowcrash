import gdb

gdb.execute('file ~/level13')
gdb.execute('b *main+14')
gdb.execute('b *ft_des+10')
gdb.execute('r')
gdb.execute('set $eax=4242')
gdb.execute('c')
gdb.execute('set $eax="g <t61:|4_|!@IF.-62FH&G~DCK/Ekrvvdwz?v|"')
gdb.execute('c')
gdb.execute('quit')