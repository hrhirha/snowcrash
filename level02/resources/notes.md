username: level02  
password: f2av5il02puano7naaf6adaaf
---

## using wireshark

Inspected level02.pcap using wireshark and found the password: ft_waNDReL0L

```
scp -P 4242 level02@192.168.56.104:level02.pcap resources/
chmod 644 resources/level02.pcap
wireshark resources/level02.pcap
```

## using tcpdump

we can get flag02's password using tcpdump
```
for line in $(tcpdump 2>/dev/null -nr level02.pcap -A tcp[13]==24 | sed -n '/Password/,$p' | egrep -v 'IP|E..5|@.@.J' | head -n 21 | tail -n 20); do echo $line | tail -c 2; done || sed 's/ndr...//' | sed 's/l.//' && echo
```

To get the flag, the following command was executed

```
su flag01 -c getflag
```

The flag is: kooda2puivaav1idi4f57q8iq
