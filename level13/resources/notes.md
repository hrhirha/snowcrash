username: level13  
password: g1qKMiRpXf53AWhDaU7FEkczr
---

`level13` gets the current user id using `getuid()`, and compares it with `4242`, if it doesn't match it prints an error and exits.
```
$ ltrace ./level13 
...
getuid()                                                        = 2013
printf("UID %d started us but we we expe"..., 2013UID 2013 started us but we we expect 4242
)             = 42
...
```

We ran `gdb` and set a breakpoint after `getuid()` call and changed the returned value to `4242`.

To automate this process we created a script `flag.py`, it can be copied to SSH using this command

```
scp -P 4242 resources/flag.py level12@10.14.59.17:/tmp
```

After that on SSH we can run the following command to get the flag

```
gdb -q -x /tmp/flag.py
```

The flag is: 2A31L79asukciNyi8uppkEuSx
