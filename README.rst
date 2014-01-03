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

**Verbose output**::

	$ clear; fab --config ./fabricrc -H 2001:DB8::1 puppet-bootstrap
	
	[2001:DB8::1] Executing task 'puppet-bootstrap'
	[2001:DB8::1] sudo: apt-get update --option=DPkg::Options::=--force-confold --option=DPkg::Options::=--force-confdef --option=DPkg::Options::=--force-confmiss --quiet=2 --yes
	[2001:DB8::1] sudo: apt-get upgrade --option=DPkg::Options::=--force-confold --option=DPkg::Options::=--force-confdef --option=DPkg::Options::=--force-confmiss --quiet=2 --yes
	[2001:DB8::1] out: Preconfiguring packages ...
	[2001:DB8::1] out: (Reading database ... 
	[2001:DB8::1] out: (Reading database ... 5%
	[2001:DB8::1] out: (Reading database ... 10%
	[2001:DB8::1] out: (Reading database ... 15%
	[2001:DB8::1] out: (Reading database ... 20%
	[2001:DB8::1] out: (Reading database ... 25%
	[2001:DB8::1] out: (Reading database ... 30%
	[2001:DB8::1] out: (Reading database ... 35%
	[2001:DB8::1] out: (Reading database ... 40%
	[2001:DB8::1] out: (Reading database ... 45%
	[2001:DB8::1] out: (Reading database ... 50%
	[2001:DB8::1] out: (Reading database ... 55%
	[2001:DB8::1] out: (Reading database ... 60%
	[2001:DB8::1] out: (Reading database ... 65%
	[2001:DB8::1] out: (Reading database ... 70%
	[2001:DB8::1] out: (Reading database ... 75%
	[2001:DB8::1] out: (Reading database ... 80%
	[2001:DB8::1] out: (Reading database ... 85%
	[2001:DB8::1] out: (Reading database ... 90%
	[2001:DB8::1] out: (Reading database ... 95%
	[2001:DB8::1] out: (Reading database ... 100%
	[2001:DB8::1] out: (Reading database ... 51614 files and directories currently installed.)
	[2001:DB8::1] out: Preparing to replace gcc-4.8-base:amd64 4.8.1-10ubuntu8 (using .../gcc-4.8-base_4.8.1-10ubuntu9_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement gcc-4.8-base:amd64 ...
	[2001:DB8::1] out: Setting up gcc-4.8-base:amd64 (4.8.1-10ubuntu9) ...
	[2001:DB8::1] out: (Reading database ... 
	[2001:DB8::1] out: (Reading database ... 5%
	[2001:DB8::1] out: (Reading database ... 10%
	[2001:DB8::1] out: (Reading database ... 15%
	[2001:DB8::1] out: (Reading database ... 20%
	[2001:DB8::1] out: (Reading database ... 25%
	[2001:DB8::1] out: (Reading database ... 30%
	[2001:DB8::1] out: (Reading database ... 35%
	[2001:DB8::1] out: (Reading database ... 40%
	[2001:DB8::1] out: (Reading database ... 45%
	[2001:DB8::1] out: (Reading database ... 50%
	[2001:DB8::1] out: (Reading database ... 55%
	[2001:DB8::1] out: (Reading database ... 60%
	[2001:DB8::1] out: (Reading database ... 65%
	[2001:DB8::1] out: (Reading database ... 70%
	[2001:DB8::1] out: (Reading database ... 75%
	[2001:DB8::1] out: (Reading database ... 80%
	[2001:DB8::1] out: (Reading database ... 85%
	[2001:DB8::1] out: (Reading database ... 90%
	[2001:DB8::1] out: (Reading database ... 95%
	[2001:DB8::1] out: (Reading database ... 100%
	[2001:DB8::1] out: (Reading database ... 51614 files and directories currently installed.)
	[2001:DB8::1] out: Preparing to replace libstdc++6:amd64 4.8.1-10ubuntu8 (using .../libstdc++6_4.8.1-10ubuntu9_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement libstdc++6:amd64 ...
	[2001:DB8::1] out: Preparing to replace libgcc1:amd64 1:4.8.1-10ubuntu8 (using .../libgcc1_1%3a4.8.1-10ubuntu9_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement libgcc1:amd64 ...
	[2001:DB8::1] out: Setting up libgcc1:amd64 (1:4.8.1-10ubuntu9) ...
	[2001:DB8::1] out: Setting up libstdc++6:amd64 (4.8.1-10ubuntu9) ...
	[2001:DB8::1] out: Processing triggers for libc-bin ...
	[2001:DB8::1] out: (Reading database ... 
	[2001:DB8::1] out: (Reading database ... 5%
	[2001:DB8::1] out: (Reading database ... 10%
	[2001:DB8::1] out: (Reading database ... 15%
	[2001:DB8::1] out: (Reading database ... 20%
	[2001:DB8::1] out: (Reading database ... 25%
	[2001:DB8::1] out: (Reading database ... 30%
	[2001:DB8::1] out: (Reading database ... 35%
	[2001:DB8::1] out: (Reading database ... 40%
	[2001:DB8::1] out: (Reading database ... 45%
	[2001:DB8::1] out: (Reading database ... 50%
	[2001:DB8::1] out: (Reading database ... 55%
	[2001:DB8::1] out: (Reading database ... 60%
	[2001:DB8::1] out: (Reading database ... 65%
	[2001:DB8::1] out: (Reading database ... 70%
	[2001:DB8::1] out: (Reading database ... 75%
	[2001:DB8::1] out: (Reading database ... 80%
	[2001:DB8::1] out: (Reading database ... 85%
	[2001:DB8::1] out: (Reading database ... 90%
	[2001:DB8::1] out: (Reading database ... 95%
	[2001:DB8::1] out: (Reading database ... 100%
	[2001:DB8::1] out: (Reading database ... 51614 files and directories currently installed.)
	[2001:DB8::1] out: Preparing to replace libdrm2:amd64 2.4.46-1 (using .../libdrm2_2.4.46-1ubuntu1_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement libdrm2:amd64 ...
	[2001:DB8::1] out: Preparing to replace libprocps0:amd64 1:3.3.3-2ubuntu8 (using .../libprocps0_1%3a3.3.3-2ubuntu9_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement libprocps0:amd64 ...
	[2001:DB8::1] out: Preparing to replace udev 204-0ubuntu19 (using .../udev_204-0ubuntu19.1_amd64.deb) ...
	[2001:DB8::1] out: Adding 'diversion of /bin/udevadm to /bin/udevadm.upgrade by fake-udev'
	[2001:DB8::1] out: Unpacking replacement udev ...
	[2001:DB8::1] out: Preparing to replace libudev1:amd64 204-0ubuntu19 (using .../libudev1_204-0ubuntu19.1_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement libudev1:amd64 ...
	[2001:DB8::1] out: Preparing to replace libcurl3-gnutls:amd64 7.32.0-1ubuntu1 (using .../libcurl3-gnutls_7.32.0-1ubuntu1.2_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement libcurl3-gnutls:amd64 ...
	[2001:DB8::1] out: Preparing to replace libsystemd-daemon0:amd64 204-0ubuntu19 (using .../libsystemd-daemon0_204-0ubuntu19.1_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement libsystemd-daemon0:amd64 ...
	[2001:DB8::1] out: Preparing to replace libpam-systemd:amd64 204-0ubuntu19 (using .../libpam-systemd_204-0ubuntu19.1_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement libpam-systemd:amd64 ...
	[2001:DB8::1] out: Preparing to replace systemd-services 204-0ubuntu19 (using .../systemd-services_204-0ubuntu19.1_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement systemd-services ...
	[2001:DB8::1] out: Preparing to replace libsystemd-login0:amd64 204-0ubuntu19 (using .../libsystemd-login0_204-0ubuntu19.1_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement libsystemd-login0:amd64 ...
	[2001:DB8::1] out: Preparing to replace curl 7.32.0-1ubuntu1 (using .../curl_7.32.0-1ubuntu1.2_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement curl ...
	[2001:DB8::1] out: Preparing to replace libcurl3:amd64 7.32.0-1ubuntu1 (using .../libcurl3_7.32.0-1ubuntu1.2_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement libcurl3:amd64 ...
	[2001:DB8::1] out: Preparing to replace gpgv 1.4.14-1ubuntu2 (using .../gpgv_1.4.14-1ubuntu2.1_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement gpgv ...
	[2001:DB8::1] out: Processing triggers for ureadahead ...
	[2001:DB8::1] out: Processing triggers for man-db ...
	[2001:DB8::1] out: Setting up gpgv (1.4.14-1ubuntu2.1) ...
	[2001:DB8::1] out: (Reading database ... 
	[2001:DB8::1] out: (Reading database ... 5%
	[2001:DB8::1] out: (Reading database ... 10%
	[2001:DB8::1] out: (Reading database ... 15%
	[2001:DB8::1] out: (Reading database ... 20%
	[2001:DB8::1] out: (Reading database ... 25%
	[2001:DB8::1] out: (Reading database ... 30%
	[2001:DB8::1] out: (Reading database ... 35%
	[2001:DB8::1] out: (Reading database ... 40%
	[2001:DB8::1] out: (Reading database ... 45%
	[2001:DB8::1] out: (Reading database ... 50%
	[2001:DB8::1] out: (Reading database ... 55%
	[2001:DB8::1] out: (Reading database ... 60%
	[2001:DB8::1] out: (Reading database ... 65%
	[2001:DB8::1] out: (Reading database ... 70%
	[2001:DB8::1] out: (Reading database ... 75%
	[2001:DB8::1] out: (Reading database ... 80%
	[2001:DB8::1] out: (Reading database ... 85%
	[2001:DB8::1] out: (Reading database ... 90%
	[2001:DB8::1] out: (Reading database ... 95%
	[2001:DB8::1] out: (Reading database ... 100%
	[2001:DB8::1] out: (Reading database ... 51615 files and directories currently installed.)
	[2001:DB8::1] out: Preparing to replace gnupg 1.4.14-1ubuntu2 (using .../gnupg_1.4.14-1ubuntu2.1_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement gnupg ...
	[2001:DB8::1] out: Processing triggers for install-info ...
	[2001:DB8::1] out: Processing triggers for man-db ...
	[2001:DB8::1] out: Setting up gnupg (1.4.14-1ubuntu2.1) ...
	[2001:DB8::1] out: (Reading database ... 
	[2001:DB8::1] out: (Reading database ... 5%
	[2001:DB8::1] out: (Reading database ... 10%
	[2001:DB8::1] out: (Reading database ... 15%
	[2001:DB8::1] out: (Reading database ... 20%
	[2001:DB8::1] out: (Reading database ... 25%
	[2001:DB8::1] out: (Reading database ... 30%
	[2001:DB8::1] out: (Reading database ... 35%
	[2001:DB8::1] out: (Reading database ... 40%
	[2001:DB8::1] out: (Reading database ... 45%
	[2001:DB8::1] out: (Reading database ... 50%
	[2001:DB8::1] out: (Reading database ... 55%
	[2001:DB8::1] out: (Reading database ... 60%
	[2001:DB8::1] out: (Reading database ... 65%
	[2001:DB8::1] out: (Reading database ... 70%
	[2001:DB8::1] out: (Reading database ... 75%
	[2001:DB8::1] out: (Reading database ... 80%
	[2001:DB8::1] out: (Reading database ... 85%
	[2001:DB8::1] out: (Reading database ... 90%
	[2001:DB8::1] out: (Reading database ... 95%
	[2001:DB8::1] out: (Reading database ... 100%
	[2001:DB8::1] out: (Reading database ... 51615 files and directories currently installed.)
	[2001:DB8::1] out: Preparing to replace initramfs-tools 0.103ubuntu1 (using .../initramfs-tools_0.103ubuntu1.1_all.deb) ...
	[2001:DB8::1] out: Unpacking replacement initramfs-tools ...
	[2001:DB8::1] out: Preparing to replace initramfs-tools-bin 0.103ubuntu1 (using .../initramfs-tools-bin_0.103ubuntu1.1_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement initramfs-tools-bin ...
	[2001:DB8::1] out: Preparing to replace procps 1:3.3.3-2ubuntu8 (using .../procps_1%3a3.3.3-2ubuntu9_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement procps ...
	[2001:DB8::1] out: Preparing to replace libapparmor1 2.8.0-0ubuntu31 (using .../libapparmor1_2.8.0-0ubuntu31.1_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement libapparmor1 ...
	[2001:DB8::1] out: Preparing to replace libapparmor-perl 2.8.0-0ubuntu31 (using .../libapparmor-perl_2.8.0-0ubuntu31.1_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement libapparmor-perl ...
	[2001:DB8::1] out: Preparing to replace apparmor 2.8.0-0ubuntu31 (using .../apparmor_2.8.0-0ubuntu31.1_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement apparmor ...
	[2001:DB8::1] out: Preparing to replace systemd-shim 3+real-0ubuntu1 (using .../systemd-shim_6-0ubuntu0.13.10_amd64.deb) ...
	[2001:DB8::1] out: Unpacking replacement systemd-shim ...
	[2001:DB8::1] out: Processing triggers for man-db ...
	[2001:DB8::1] out: Processing triggers for ureadahead ...
	[2001:DB8::1] out: Setting up libdrm2:amd64 (2.4.46-1ubuntu1) ...
	[2001:DB8::1] out: Setting up libprocps0:amd64 (1:3.3.3-2ubuntu9) ...
	[2001:DB8::1] out: Setting up libudev1:amd64 (204-0ubuntu19.1) ...
	[2001:DB8::1] out: Setting up udev (204-0ubuntu19.1) ...
	[2001:DB8::1] out: udev stop/waiting
	[2001:DB8::1] out: udev start/running, process 2916
	[2001:DB8::1] out: Removing 'diversion of /bin/udevadm to /bin/udevadm.upgrade by fake-udev'
	[2001:DB8::1] out: update-initramfs: deferring update (trigger activated)
	[2001:DB8::1] out: Setting up libcurl3-gnutls:amd64 (7.32.0-1ubuntu1.2) ...
	[2001:DB8::1] out: Setting up libsystemd-daemon0:amd64 (204-0ubuntu19.1) ...
	[2001:DB8::1] out: Setting up systemd-services (204-0ubuntu19.1) ...
	[2001:DB8::1] out: Setting up libpam-systemd:amd64 (204-0ubuntu19.1) ...
	[2001:DB8::1] out: Setting up libsystemd-login0:amd64 (204-0ubuntu19.1) ...
	[2001:DB8::1] out: Setting up libcurl3:amd64 (7.32.0-1ubuntu1.2) ...
	[2001:DB8::1] out: Setting up curl (7.32.0-1ubuntu1.2) ...
	[2001:DB8::1] out: Setting up initramfs-tools-bin (0.103ubuntu1.1) ...
	[2001:DB8::1] out: Setting up initramfs-tools (0.103ubuntu1.1) ...
	[2001:DB8::1] out: update-initramfs: deferring update (trigger activated)
	[2001:DB8::1] out: Setting up procps (1:3.3.3-2ubuntu9) ...
	[2001:DB8::1] out: procps stop/waiting
	[2001:DB8::1] out: Setting up libapparmor1 (2.8.0-0ubuntu31.1) ...
	[2001:DB8::1] out: Setting up libapparmor-perl (2.8.0-0ubuntu31.1) ...
	[2001:DB8::1] out: Setting up apparmor (2.8.0-0ubuntu31.1) ...
	[2001:DB8::1] out:  * Starting AppArmor profiles
	[2001:DB8::1] out: Skipping profile in /etc/apparmor.d/disable: usr.sbin.rsyslogd
	[2001:DB8::1] out:    ...done.
	[2001:DB8::1] out:  * Reloading AppArmor profiles
	[2001:DB8::1] out: Skipping profile in /etc/apparmor.d/disable: usr.sbin.rsyslogd
	[2001:DB8::1] out:    ...done.
	[2001:DB8::1] out: Setting up systemd-shim (6-0ubuntu0.13.10) ...
	[2001:DB8::1] out: Processing triggers for libc-bin ...
	[2001:DB8::1] out: Processing triggers for initramfs-tools ...
	[2001:DB8::1] out: update-initramfs: Generating /boot/initrd.img-3.11.0-13-generic
	[2001:DB8::1] out: 
	
	[2001:DB8::1] sudo: apt-get install --option=DPkg::Options::=--force-confold --option=DPkg::Options::=--force-confdef --option=DPkg::Options::=--force-confmiss --quiet=2 --yes curl debsums vim
	[2001:DB8::1] out: Selecting previously unselected package libgpm2:amd64.
	[2001:DB8::1] out: (Reading database ... 
	[2001:DB8::1] out: (Reading database ... 5%
	[2001:DB8::1] out: (Reading database ... 10%
	[2001:DB8::1] out: (Reading database ... 15%
	[2001:DB8::1] out: (Reading database ... 20%
	[2001:DB8::1] out: (Reading database ... 25%
	[2001:DB8::1] out: (Reading database ... 30%
	[2001:DB8::1] out: (Reading database ... 35%
	[2001:DB8::1] out: (Reading database ... 40%
	[2001:DB8::1] out: (Reading database ... 45%
	[2001:DB8::1] out: (Reading database ... 50%
	[2001:DB8::1] out: (Reading database ... 55%
	[2001:DB8::1] out: (Reading database ... 60%
	[2001:DB8::1] out: (Reading database ... 65%
	[2001:DB8::1] out: (Reading database ... 70%
	[2001:DB8::1] out: (Reading database ... 75%
	[2001:DB8::1] out: (Reading database ... 80%
	[2001:DB8::1] out: (Reading database ... 85%
	[2001:DB8::1] out: (Reading database ... 90%
	[2001:DB8::1] out: (Reading database ... 95%
	[2001:DB8::1] out: (Reading database ... 100%
	[2001:DB8::1] out: (Reading database ... 51614 files and directories currently installed.)
	[2001:DB8::1] out: Unpacking libgpm2:amd64 (from .../libgpm2_1.20.4-6.1_amd64.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package libpython2.7:amd64.
	[2001:DB8::1] out: Unpacking libpython2.7:amd64 (from .../libpython2.7_2.7.5-8ubuntu3_amd64.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package libfile-fnmatch-perl.
	[2001:DB8::1] out: Unpacking libfile-fnmatch-perl (from .../libfile-fnmatch-perl_0.02-1build2_amd64.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package libdpkg-perl.
	[2001:DB8::1] out: Unpacking libdpkg-perl (from .../libdpkg-perl_1.16.12ubuntu1_all.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package debsums.
	[2001:DB8::1] out: Unpacking debsums (from .../debsums_2.0.52+nmu1_all.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package libfile-fcntllock-perl.
	[2001:DB8::1] out: Unpacking libfile-fcntllock-perl (from .../libfile-fcntllock-perl_0.14-2_amd64.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package vim-runtime.
	[2001:DB8::1] out: Unpacking vim-runtime (from .../vim-runtime_2%3a7.4.000-1ubuntu2_all.deb) ...
	[2001:DB8::1] out: Adding 'diversion of /usr/share/vim/vim74/doc/help.txt to /usr/share/vim/vim74/doc/help.txt.vim-tiny by vim-runtime'
	[2001:DB8::1] out: Adding 'diversion of /usr/share/vim/vim74/doc/tags to /usr/share/vim/vim74/doc/tags.vim-tiny by vim-runtime'
	[2001:DB8::1] out: Selecting previously unselected package vim.
	[2001:DB8::1] out: Unpacking vim (from .../vim_2%3a7.4.000-1ubuntu2_amd64.deb) ...
	[2001:DB8::1] out: Processing triggers for man-db ...
	[2001:DB8::1] out: Setting up libgpm2:amd64 (1.20.4-6.1) ...
	[2001:DB8::1] out: Setting up libpython2.7:amd64 (2.7.5-8ubuntu3) ...
	[2001:DB8::1] out: Setting up libfile-fnmatch-perl (0.02-1build2) ...
	[2001:DB8::1] out: Setting up libdpkg-perl (1.16.12ubuntu1) ...
	[2001:DB8::1] out: Setting up debsums (2.0.52+nmu1) ...
	[2001:DB8::1] out: 
	[2001:DB8::1] out: Configuration file `/etc/cron.weekly/debsums', does not exist on system.
	[2001:DB8::1] out: Installing new config file as you requested.
	[2001:DB8::1] out: 
	[2001:DB8::1] out: Configuration file `/etc/cron.monthly/debsums', does not exist on system.
	[2001:DB8::1] out: Installing new config file as you requested.
	[2001:DB8::1] out: 
	[2001:DB8::1] out: Configuration file `/etc/default/debsums', does not exist on system.
	[2001:DB8::1] out: Installing new config file as you requested.
	[2001:DB8::1] out: 
	[2001:DB8::1] out: Configuration file `/etc/debsums-ignore', does not exist on system.
	[2001:DB8::1] out: Installing new config file as you requested.
	[2001:DB8::1] out: 
	[2001:DB8::1] out: Configuration file `/etc/cron.daily/debsums', does not exist on system.
	[2001:DB8::1] out: Installing new config file as you requested.
	[2001:DB8::1] out: Setting up libfile-fcntllock-perl (0.14-2) ...
	[2001:DB8::1] out: Setting up vim-runtime (2:7.4.000-1ubuntu2) ...
	[2001:DB8::1] out: Processing /usr/share/vim/addons/doc
	[2001:DB8::1] out: Setting up vim (2:7.4.000-1ubuntu2) ...
	[2001:DB8::1] out: update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/vim (vim) in auto mode
	[2001:DB8::1] out: update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/vimdiff (vimdiff) in auto mode
	[2001:DB8::1] out: update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/rvim (rvim) in auto mode
	[2001:DB8::1] out: update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/rview (rview) in auto mode
	[2001:DB8::1] out: update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/vi (vi) in auto mode
	[2001:DB8::1] out: update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/view (view) in auto mode
	[2001:DB8::1] out: update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/ex (ex) in auto mode
	[2001:DB8::1] out: Processing triggers for libc-bin ...
	[2001:DB8::1] out: 
	
	[2001:DB8::1] sudo: apt-get clean --option=DPkg::Options::=--force-confold --option=DPkg::Options::=--force-confdef --option=DPkg::Options::=--force-confmiss --quiet=2 --yes
	[2001:DB8::1] sudo: debsums_init
	[2001:DB8::1] out: Finished generating md5sums!
	[2001:DB8::1] out: Checking still missing md5files...
	[2001:DB8::1] out: 
	
	[2001:DB8::1] run: lsb_release -c -s
	[2001:DB8::1] out: saucy
	[2001:DB8::1] out: 
	
	[2001:DB8::1] run: mktemp
	[2001:DB8::1] out: /tmp/tmp.libsHHgIgm
	[2001:DB8::1] out: 
	
	[2001:DB8::1] run: curl -o /tmp/tmp.libsHHgIgm http://apt.puppetlabs.com/puppetlabs-release-saucy.deb
	[2001:DB8::1] out:   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
	[2001:DB8::1] out:                                  Dload  Upload   Total   Spent    Left  Speed
	[2001:DB8::1] out: 
	[2001:DB8::1] out:   0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
	[2001:DB8::1] out: 100  3422  100  3422    0     0  77972      0 --:--:-- --:--:-- --:--:-- 79581
	[2001:DB8::1] out: 
	
	[2001:DB8::1] sudo: dpkg --install --force-confold --force-confdef --force-confmiss /tmp/tmp.libsHHgIgm
	[2001:DB8::1] out: Selecting previously unselected package puppetlabs-release.
	[2001:DB8::1] out: (Reading database ... 
	[2001:DB8::1] out: (Reading database ... 5%
	[2001:DB8::1] out: (Reading database ... 10%
	[2001:DB8::1] out: (Reading database ... 15%
	[2001:DB8::1] out: (Reading database ... 20%
	[2001:DB8::1] out: (Reading database ... 25%
	[2001:DB8::1] out: (Reading database ... 30%
	[2001:DB8::1] out: (Reading database ... 35%
	[2001:DB8::1] out: (Reading database ... 40%
	[2001:DB8::1] out: (Reading database ... 45%
	[2001:DB8::1] out: (Reading database ... 50%
	[2001:DB8::1] out: (Reading database ... 55%
	[2001:DB8::1] out: (Reading database ... 60%
	[2001:DB8::1] out: (Reading database ... 65%
	[2001:DB8::1] out: (Reading database ... 70%
	[2001:DB8::1] out: (Reading database ... 75%
	[2001:DB8::1] out: (Reading database ... 80%
	[2001:DB8::1] out: (Reading database ... 85%
	[2001:DB8::1] out: (Reading database ... 90%
	[2001:DB8::1] out: (Reading database ... 95%
	[2001:DB8::1] out: (Reading database ... 100%
	[2001:DB8::1] out: (Reading database ... 53399 files and directories currently installed.)
	[2001:DB8::1] out: Unpacking puppetlabs-release (from /tmp/tmp.libsHHgIgm) ...
	[2001:DB8::1] out: Setting up puppetlabs-release (1.0-9) ...
	[2001:DB8::1] out: 
	[2001:DB8::1] out: Configuration file `/etc/apt/trusted.gpg.d/puppetlabs-keyring.gpg', does not exist on system.
	[2001:DB8::1] out: Installing new config file as you requested.
	[2001:DB8::1] out: 
	[2001:DB8::1] out: Configuration file `/etc/apt/sources.list.d/puppetlabs.list', does not exist on system.
	[2001:DB8::1] out: Installing new config file as you requested.
	[2001:DB8::1] out: 
	
	[2001:DB8::1] run: rm -f /tmp/tmp.libsHHgIgm
	[2001:DB8::1] sudo: apt-get update --option=DPkg::Options::=--force-confold --option=DPkg::Options::=--force-confdef --option=DPkg::Options::=--force-confmiss --quiet=2 --yes
	[2001:DB8::1] sudo: apt-get upgrade --option=DPkg::Options::=--force-confold --option=DPkg::Options::=--force-confdef --option=DPkg::Options::=--force-confmiss --quiet=2 --yes
	[2001:DB8::1] sudo: apt-get install --option=DPkg::Options::=--force-confold --option=DPkg::Options::=--force-confdef --option=DPkg::Options::=--force-confmiss --quiet=2 --yes puppet
	[2001:DB8::1] out: Selecting previously unselected package augeas-lenses.
	[2001:DB8::1] out: (Reading database ... 
	[2001:DB8::1] out: (Reading database ... 5%
	[2001:DB8::1] out: (Reading database ... 10%
	[2001:DB8::1] out: (Reading database ... 15%
	[2001:DB8::1] out: (Reading database ... 20%
	[2001:DB8::1] out: (Reading database ... 25%
	[2001:DB8::1] out: (Reading database ... 30%
	[2001:DB8::1] out: (Reading database ... 35%
	[2001:DB8::1] out: (Reading database ... 40%
	[2001:DB8::1] out: (Reading database ... 45%
	[2001:DB8::1] out: (Reading database ... 50%
	[2001:DB8::1] out: (Reading database ... 55%
	[2001:DB8::1] out: (Reading database ... 60%
	[2001:DB8::1] out: (Reading database ... 65%
	[2001:DB8::1] out: (Reading database ... 70%
	[2001:DB8::1] out: (Reading database ... 75%
	[2001:DB8::1] out: (Reading database ... 80%
	[2001:DB8::1] out: (Reading database ... 85%
	[2001:DB8::1] out: (Reading database ... 90%
	[2001:DB8::1] out: (Reading database ... 95%
	[2001:DB8::1] out: (Reading database ... 100%
	[2001:DB8::1] out: (Reading database ... 53405 files and directories currently installed.)
	[2001:DB8::1] out: Unpacking augeas-lenses (from .../augeas-lenses_1.1.0-0ubuntu2_all.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package debconf-utils.
	[2001:DB8::1] out: Unpacking debconf-utils (from .../debconf-utils_1.5.50ubuntu1_all.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package libruby1.9.1.
	[2001:DB8::1] out: Unpacking libruby1.9.1 (from .../libruby1.9.1_1.9.3.194-8.1ubuntu2.1_amd64.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package ruby1.9.1.
	[2001:DB8::1] out: Unpacking ruby1.9.1 (from .../ruby1.9.1_1.9.3.194-8.1ubuntu2.1_amd64.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package ruby.
	[2001:DB8::1] out: Unpacking ruby (from .../ruby_1%3a1.9.3_all.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package virt-what.
	[2001:DB8::1] out: Unpacking virt-what (from .../virt-what_1.12-1_amd64.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package facter.
	[2001:DB8::1] out: Unpacking facter (from .../facter_1.7.4-1puppetlabs1_amd64.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package libaugeas0.
	[2001:DB8::1] out: Unpacking libaugeas0 (from .../libaugeas0_1.1.0-0ubuntu2_amd64.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package ruby-augeas.
	[2001:DB8::1] out: Unpacking ruby-augeas (from .../ruby-augeas_0.5.0-1_amd64.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package libaugeas-ruby.
	[2001:DB8::1] out: Unpacking libaugeas-ruby (from .../libaugeas-ruby_0.5.0-1_all.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package libruby.
	[2001:DB8::1] out: Unpacking libruby (from .../libruby_1%3a1.9.3_all.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package ruby-shadow.
	[2001:DB8::1] out: Unpacking ruby-shadow (from .../ruby-shadow_2.1.4-2_amd64.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package ruby-json.
	[2001:DB8::1] out: Unpacking ruby-json (from .../ruby-json_1.8.0-1_amd64.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package hiera.
	[2001:DB8::1] out: Unpacking hiera (from .../hiera_1.3.0-1puppetlabs1_all.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package ruby-rgen.
	[2001:DB8::1] out: Unpacking ruby-rgen (from .../ruby-rgen_0.6.5-1puppetlabs1_all.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package puppet-common.
	[2001:DB8::1] out: Unpacking puppet-common (from .../puppet-common_3.4.1-1puppetlabs1_all.deb) ...
	[2001:DB8::1] out: Selecting previously unselected package puppet.
	[2001:DB8::1] out: Unpacking puppet (from .../puppet_3.4.1-1puppetlabs1_all.deb) ...
	[2001:DB8::1] out: Processing triggers for man-db ...
	[2001:DB8::1] out: Processing triggers for ureadahead ...
	[2001:DB8::1] out: Setting up augeas-lenses (1.1.0-0ubuntu2) ...
	[2001:DB8::1] out: Setting up debconf-utils (1.5.50ubuntu1) ...
	[2001:DB8::1] out: Setting up libruby1.9.1 (1.9.3.194-8.1ubuntu2.1) ...
	[2001:DB8::1] out: 
	[2001:DB8::1] out: Configuration file `/etc/bash_completion.d/gem1.9.1', does not exist on system.
	[2001:DB8::1] out: Installing new config file as you requested.
	[2001:DB8::1] out: Setting up ruby1.9.1 (1.9.3.194-8.1ubuntu2.1) ...
	[2001:DB8::1] out: update-alternatives: using /usr/bin/gem1.9.1 to provide /usr/bin/gem (gem) in auto mode
	[2001:DB8::1] out: update-alternatives: using /usr/bin/ruby1.9.1 to provide /usr/bin/ruby (ruby) in auto mode
	[2001:DB8::1] out: Setting up ruby (1:1.9.3) ...
	[2001:DB8::1] out: Setting up virt-what (1.12-1) ...
	[2001:DB8::1] out: Setting up facter (1.7.4-1puppetlabs1) ...
	[2001:DB8::1] out: Setting up libaugeas0 (1.1.0-0ubuntu2) ...
	[2001:DB8::1] out: Setting up ruby-augeas (0.5.0-1) ...
	[2001:DB8::1] out: Setting up libaugeas-ruby (0.5.0-1) ...
	[2001:DB8::1] out: Setting up libruby (1:1.9.3) ...
	[2001:DB8::1] out: Setting up ruby-shadow (2.1.4-2) ...
	[2001:DB8::1] out: Setting up ruby-json (1.8.0-1) ...
	[2001:DB8::1] out: Setting up hiera (1.3.0-1puppetlabs1) ...
	[2001:DB8::1] out: 
	[2001:DB8::1] out: Configuration file `/etc/hiera.yaml', does not exist on system.
	[2001:DB8::1] out: Installing new config file as you requested.
	[2001:DB8::1] out: Setting up ruby-rgen (0.6.5-1puppetlabs1) ...
	[2001:DB8::1] out: Setting up puppet-common (3.4.1-1puppetlabs1) ...
	[2001:DB8::1] out: 
	[2001:DB8::1] out: Configuration file `/etc/puppet/puppet.conf', does not exist on system.
	[2001:DB8::1] out: Installing new config file as you requested.
	[2001:DB8::1] out: 
	[2001:DB8::1] out: Configuration file `/etc/logcheck/ignore.d.server/puppet-common', does not exist on system.
	[2001:DB8::1] out: Installing new config file as you requested.
	[2001:DB8::1] out: Setting up puppet (3.4.1-1puppetlabs1) ...
	[2001:DB8::1] out: 
	[2001:DB8::1] out: Configuration file `/etc/init.d/puppet', does not exist on system.
	[2001:DB8::1] out: Installing new config file as you requested.
	[2001:DB8::1] out: 
	[2001:DB8::1] out: Configuration file `/etc/default/puppet', does not exist on system.
	[2001:DB8::1] out: Installing new config file as you requested.
	[2001:DB8::1] out: 
	[2001:DB8::1] out: Configuration file `/etc/logrotate.d/puppet', does not exist on system.
	[2001:DB8::1] out: Installing new config file as you requested.
	[2001:DB8::1] out:  * Starting puppet agent
	[2001:DB8::1] out: 
	[2001:DB8::1] out: puppet not configured to start, please edit /etc/default/puppet to enable
	[2001:DB8::1] out:    ...done.
	[2001:DB8::1] out: Processing triggers for libc-bin ...
	[2001:DB8::1] out: Processing triggers for ureadahead ...
	[2001:DB8::1] out: 
	
	[2001:DB8::1] put: puppet-bootstrap/noop.pp -> /root/puppet-bootstrap/noop.pp
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
