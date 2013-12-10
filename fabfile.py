import os
from pprint import pprint

from fabric import operations
from fabric.api import run, sudo
from fabric.api import task
from fabric.api import env
from fabric.api import execute
from fabric.utils import puts
from fabric.context_managers import settings
from fabric.context_managers import hide
from fabric.decorators import with_settings
from fabric import tasks

class AbortError(Exception):
	pass


@task(name='run-sudo-with-prompt')
def run_sudo_with_prompt():
	try:
		sudo("I will prompt!")
	except AbortError as err:
		puts(err)

class RunScripts(tasks.Task):
	"""Runs the scripts in the `./scripts` directory on the remote.

	This assumes that all the scripts have the executable bit set.
	"""

	name = 'run-scripts'

	def __init__(self, script_dir='./scripts', *args, **kwargs):
		super(RunScripts, self).__init__(*args, **kwargs)
		self.local_script_dir = script_dir
		self.remote_scripts = []

	def upload_scripts(self):
		local_path = os.path.join(self.local_script_dir, '*')
		self.remote_scripts = operations.put(local_path, mirror_local_mode=True)
		

	def run(self, *args, **kwargs):
		try:
			self.upload_scripts()
			for script in self.remote_scripts:
				result = sudo(script)
				puts(result)
		except AbortError as err:
			puts(err)

rs = RunScripts()

class Hostname(tasks.Task):

	name = 'detect-hostname'

	def __init__(self, *args, **kwargs):
		super(Hostname, self).__init__(*args, **kwargs)

	def run(self, *args, **kwargs):
		try:
			hostname = run('hostname -f')
			puts(hostname.strip())
		except AbortError as err:
			puts(err)
h = Hostname()


env.abort_exception = AbortError


# vim: ts=4 sts=4 fenc=utf-8 expandtab:
