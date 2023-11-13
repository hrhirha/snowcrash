username: level00  
password: level00
---

Text found at /usr/sbin/john: cdiiddwpgswtgt

```sh
find / -user flag00 2>/dev/null
cat /usr/sbin/john
```
The found text is encoded using rot11, a script `rot11.py` was created to decode it

```sh
python3 rot11.py
```

The password: nottoohardhere

To get the flag, the following command was executed

```
su flag00 -c getflag
```

The flag is: x24ti5gi3x0ol2eh4esiuxias
