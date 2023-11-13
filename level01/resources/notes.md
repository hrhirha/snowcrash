username: level01  
password: x24ti5gi3x0ol2eh4esiuxias
---

Password hash stored in /etc/passwd:

```
$ cat /etc/passwd
...
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
...
```

Cracked it with hashcat: abcdefg

```
hashcat -a 0 resources/hash /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt
```

To get the flag, the following command was executed

```
su flag01 -c getflag
```

The flag is: f2av5il02puano7naaf6adaaf
