tripping-wight
==============

* http://docs.fabfile.org/

Installation
------------

::

	virtualenv --no-site-packages .
	. bin/activate
	pip install -U -r requirements.txt

Usage
-----

This task installs ``vim``, ``debsums``,
``puppetlabs-release-${lsbdistcodename}.deb`` (from
``http://apt.puppetlabs.com/puppetlabs-release-saucy.deb``)  and ``puppet``. Upon
successfull completion it outputs an ``info``-message from puppet::

	$ clear; fab --config ./fabricrc -H 2001:DB8::1 puppet-bootstrap
	
	[2001:DB8::1] Executing task 'puppet-bootstrap'
	
	[...]
	
	[2001:DB8::1] sudo: puppet apply --verbose puppet-bootstrap/noop.pp
	[2001:DB8::1] out: Warning: Could not retrieve fact fqdn
	[2001:DB8::1] out: Info: Scope(Class[Noop]): Puppet is installed and running!
	[2001:DB8::1] out: Notice: Compiled catalog for srv01 in environment production in 0.03 seconds
	[2001:DB8::1] out: Info: Applying configuration version '1388708935'
	[2001:DB8::1] out: Info: Creating state file /var/lib/puppet/state/state.yaml
	[2001:DB8::1] out: Notice: Finished catalog run in 0.02 seconds
	[2001:DB8::1] out: 
	
	Disconnecting from 2001:DB8::1... done.
		
	Done.
	
	real	3m25.595s
	user	0m1.944s
	sys	0m1.174s
