tripping-wight
==============

Installation
------------

    $ virtualenv --no-site-packages .
    $ . bin/activate
    $ pip install -U -r requirements.txt

Usage
-----

    $ fab --abort-on-prompts --hide aborts --eagerly-disconnect -H localhost,127.0.0.1 run-sudo-with-prompt; echo $?
    [localhost] Executing task 'run-sudo-with-prompt'
    [localhost] sudo: I will prompt!
    [localhost] Needed to prompt for a connection or sudo password (host: localhost), but abort-on-prompts was set to True
    [127.0.0.1] Executing task 'run-sudo-with-prompt'
    [127.0.0.1] sudo: I will prompt!
    [127.0.0.1] Needed to prompt for a connection or sudo password (host: 127.0.0.1), but abort-on-prompts was set to True

    Done.
    0

Have fun!
