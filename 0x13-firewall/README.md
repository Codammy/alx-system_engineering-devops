# Firewall
`DevOps`
`SysAdmin`
`Security`


![FireWall](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png)

## Background Context
**Your servers without a firewall…**


![LOL](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/155/holbertonschool-firewall.gif)

### Resources
**Read or watch:**

* [What is a firewall](https://en.wikipedia.org/wiki/Firewall_%28computing%29)

### More Info
<p>Telnet is a very good tool to check if sockets are open with telnet IP PORT. For example, if you want to check if port 22 is open on `web-02`:</p>

```bash
sylvain@ubuntu$ telnet web-02.holberton.online 22
Trying 54.89.38.100...
Connected to web-02.holberton.online.
Escape character is '^]'.
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

Protocol mismatch.
Connection closed by foreign host.
sylvain@ubuntu$
```

We can see for this example that the connection is successful: Connected to web-02.holberton.online.


Now let’s try connecting to port 2222:

```bash
sylvain@ubuntu$ telnet web-02.holberton.online 2222
Trying 54.89.38.100...
^C
sylvain@ubuntu$
```
We can see that the connection never succeeds, so after some time I just use ctrl+c to kill the process.
