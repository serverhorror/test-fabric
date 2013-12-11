tripping-wight
==============

Installation
------------

```bash
$ virtualenv --no-site-packages .
$ . bin/activate
$ pip install -U -r requirements.txt
```

Usage
-----

Each **executable** in the scripts directory will be copied to the target host and then executed under sudo.

```bash
(fabstuff)$ fab --hide aborts,running --eagerly-disconnect --abort-on-prompts -H localhost run-scripts -p 'f00b$r' 
[localhost] detect-mysql=0
[localhost] detect-nfs=0
[localhost] detect-oracle=0
[localhost] detect-os=<unknown> Darwin iMac.local 13.0.0 Darwin Kernel Version 13.0.0: Thu Sep 19 22:22:27 PDT 2013; root:xnu-2422.1.72~6/RELEASE_X86_64 x86_64
[localhost] detect-rsyncd=0
[localhost] hostname=iMac.local
[localhost] large-homes=/Users/martin,/Users/nena
[localhost] lost+found=0

Warning: [Errno 17] File exists: './results'

[localhost] target=/Users/martin/fabstuff/results/localhost.json
Disconnecting from localhost... done.

Done.
```

And here are the resulting files:

```bash
$ ls -l1 results/
127.0.0.1.json
localhost.json
```

Results
-------

You can actually do anything you want, however you may want to keep to a few guidelines:

* keep to unix return codes
 * a return code of zero indicates a success -- **nothing bad has happened**
 * a non-zero return code indicates a failure -- **something bad has happened**
* each host consists of a json dictionairy
  * `fqdn` guessed by trying to get the information from dns
  * `host_string` is the host fabric originally connected to
  * `time_of_run` when did fabric connect to the target host
  * furthermore there is a dictionairy for each *basename of a check*.  
    the keys within this dictionairy are the same everywhere
* try to keep the output short
  * have a look at the sample scripts

```
{
    "fqdn": "1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa",
    "host_string": "localhost",
    "time_of_run": "2013-12-11T01:08:56.638028",
    ...
    "detect-mysql": {
        "command": "/Users/martin/detect-mysql",
        "failed": false,
        "real_command": "sudo -S -p 'sudo password:'  /bin/bash -l -c \"/Users/martin/detect-mysql\"",
        "result_obj": "0",
        "return_code": 0,
        "stderr": "",
        "stdout": "0",
        "success": true
    },
    "detect-nfs": {
        "command": "/Users/martin/detect-nfs",
        "failed": false,
        "real_command": "sudo -S -p 'sudo password:'  /bin/bash -l -c \"/Users/martin/detect-nfs\"",
        "result_obj": "0",
        "return_code": 0,
        "stderr": "",
        "stdout": "0",
        "success": true
    },
    ...
    "detect-os": {
        "command": "/Users/martin/detect-os",
        "failed": false,
        "real_command": "sudo -S -p 'sudo password:'  /bin/bash -l -c \"/Users/martin/detect-os\"",
        "result_obj": "<unknown> Darwin iMac.local 13.0.0 Darwin Kernel Version 13.0.0: Thu Sep 19 22:22:27 PDT 2013; root:xnu-2422.1.72~6/RELEASE_X86_64 x86_64",
        "return_code": 0,
        "stderr": "",
        "stdout": "<unknown> Darwin iMac.local 13.0.0 Darwin Kernel Version 13.0.0: Thu Sep 19 22:22:27 PDT 2013; root:xnu-2422.1.72~6/RELEASE_X86_64 x86_64",
        "success": true
    ...
    "hostname": {
        "command": "/Users/martin/hostname",
        "failed": false,
        "real_command": "sudo -S -p 'sudo password:'  /bin/bash -l -c \"/Users/martin/hostname\"",
        "result_obj": "iMac.local",
        "return_code": 0,
        "stderr": "",
        "stdout": "iMac.local",
        "success": true
    },
    "large-homes": {
        "command": "/Users/martin/large-homes",
        "failed": false,
        "real_command": "sudo -S -p 'sudo password:'  /bin/bash -l -c \"/Users/martin/large-homes\"",
        "result_obj": "/Users/martin,/Users/nena",
        "return_code": 0,
        "stderr": "",
        "stdout": "/Users/martin,/Users/nena",
        "success": true
    },
    ...
}
```

Have fun!
