username: level14  
password: 2A31L79asukciNyi8uppkEuSx
---

## method 1 - reverse engineer level13

`strings` command reveals the following string which is the encrypted form of the flag14:  "`g <t61:|4_|!@IF.-62FH&G~DCK/Ekrvvdwz?v|`"

```
strings getflag
```

We could use `level13` binary wich uses the same decryption function as `getflag`, and inject the cipher for flag14 using `gdb`.

`rev_level13.py` was created to automate this process, we could copy it into SSH

```
scp -P 4242 resources/rev_level13.py level13@10.14.59.17:/tmp
```

Then execute the following command to get ther flag

```
gdb -q -x /tmp/rev_level13.py
```

## method 2 - reverse engineer getflag

The second method involves revrse engineering `getflag` command itself.

`getflag` uses `ptrace()` to prevent us from using tools such as `ltrace` or `gdb`. To bypass this we needed to manipuate the return value of `ptrace` and set it to `0`.

```
$ ltrace getflag 
...
ptrace(0, 0, 1, 0, 0)                                           = -1
puts("You should not reverse this"You should not reverse this
)                             = 28
...
```

After that we manipulated the return value of `getuid()` and set the uid of `flag14`.

This process was automated using `rev_getflag.py` script.


The flag is: 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
