from fabric import operations
from fabric import tasks
from fabric.api import run
from fabric.api import sudo
from fabric import context_managers

class PuppetBootstrap(tasks.Task):
	u'''This installs puppet on a bare OS
	'''
	name = u'puppet-bootstrap'

	def __init__(self, flavour=u'debian', *args, **kwargs):
		super(PuppetBootstrap, self).__init__(*args, **kwargs)
	def run(self, *args, **kwargs):
		self.install_packages([u'curl', u'debsums', u'vim'])
		with context_managers.shell_env(DEBIAN_FRONTEND=u'noninteractive'):
			sudo(u'apt-get clean --option=DPkg::Options::=--force-confold --option=DPkg::Options::=--force-confdef --option=DPkg::Options::=--force-confmiss --quiet=2 --yes')
		sudo(u'debsums_init')
		self.prepare_puppet()
		self.install_packages([u'puppet'])
		self.puppet_apply(u'puppet-bootstrap')
		# self.purge_packages()
	def purge_packages(self):
		with context_managers.shell_env(DEBIAN_FRONTEND=u'noninteractive'):
			sudo(u'apt-get remove --purge --option=DPkg::Options::=--force-confold --option=DPkg::Options::=--force-confdef --option=DPkg::Options::=--force-confmiss --quiet=2 --yes curl debsums')
	def install_packages(self, packages):
		with context_managers.shell_env(DEBIAN_FRONTEND=u'noninteractive'):
			sudo(u'apt-get update --option=DPkg::Options::=--force-confold --option=DPkg::Options::=--force-confdef --option=DPkg::Options::=--force-confmiss --quiet=2 --yes')
			sudo(u'apt-get upgrade --option=DPkg::Options::=--force-confold --option=DPkg::Options::=--force-confdef --option=DPkg::Options::=--force-confmiss --quiet=2 --yes')
			sudo(u'apt-get install --option=DPkg::Options::=--force-confold --option=DPkg::Options::=--force-confdef --option=DPkg::Options::=--force-confmiss --quiet=2 --yes {}'.format(" ".join(packages)))
	def prepare_puppet(self):
		distname = run("lsb_release -c -s")
		package_path = run(u'mktemp')
		run(u'curl -o {} http://apt.puppetlabs.com/puppetlabs-release-{}.deb'.format(package_path, distname))
		with context_managers.shell_env(DEBIAN_FRONTEND=u'noninteractive'):
			sudo(u'dpkg --install --force-confold --force-confdef --force-confmiss {}'.format(package_path))
			run(u'rm -f {}'.format(package_path))
	def puppet_apply(self, manifestdir):
		self.put_scripts(manifestdir)
		sudo(u'puppet apply --verbose {}/noop.pp'.format(manifestdir))
	def put_scripts(self, what):
		operations.put(what, mirror_local_mode=True)

puppet_bootstrap = PuppetBootstrap()


# vim: ts=4 sts=4 fenc=utf-8 expandtab:
