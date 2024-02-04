# IP Recognition 

### Use:

```shell
❯ python3 inforecon.py -d google.com
ip : 172.217.192.101
hostname : cf-in-f101.1e100.net
city : Santiago
region : Santiago Metropolitan
country : CL
loc : -33.4569,-70.6483
org : AS15169 Google LLC
postal : 8320000
timezone : America/Santiago
readme : https://ipinfo.io/missingauth
```

# MD5 cracking

### Use:

```shell
Example
❯ python3 md5crack.py -md5 5f4dcc3b5aa765d61d8327deb882cf99 -w /usr/share/wordlists/rockyou.txt
MD5 hash successfully cracked: 5f4dcc3b5aa765d61d8327deb882cf99 -> password

```

# Nmap scan port

### Use:

```shell
❯ python3 nmapScan.py -i 10.10.63.231
```

# PortScan
Use:
### Step 1

```python
pip install -r requirements.txt
```
### Step 2
```python
python3 portScan.py -i 192.168.98.14
```
```bash
    [+] Host: 192.168.98.14 
[<] Scaning: 
    Discovering port 65535
    [+] Port 8080 : OPEN
```

# domain enumeration

```shell
❯ python3 subDomains.py -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -d google.com
Valid subdomain: http://images.google.com
```
