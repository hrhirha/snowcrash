username: level09
password: 25749xKZ8L7DkSCwJkT9dyv6f
---

`level09` has SUID bit set, it can be run as `flag09`. it takes an argument and encrypt it.

The encryption goes as follow; the index of each character is added to its ascii number, the character that has the resulting ascii number is the cipher.

```
$ ./level09 0000000000
0123456789
```

A program to reverse this procedure was created: `dec.c`. We can copy it into the machine using `scp`

```
scp -P 4242 resources/dec.c level09@10.14.59.17:/tm
```

`dec.c` takes `token` file as argument and outputs the cleartext which is `flag09`'s password: f3iji1ju5yuevaus41q1afiuq

```
$(cd /tmp && gcc -o dec --std=c99 /tmp/dec.c) && /tmp/dec
```

The following command gives the flag

```
su flag09 -c getflag
```

The flag is: s5cAJpM8ev6XHw998pRWG728z
