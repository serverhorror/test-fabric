import os
import socket
from datetime import datetime
from pprint import pprint
import json

from fabric import operations
from fabric.api import run, sudo
from fabric.api import task
from fabric.api import env
from fabric.api import execute
from fabric.utils import puts, warn
from fabric.context_managers import settings
from fabric.context_managers import hide
from fabric.decorators import with_settings
from fabric import tasks
from fabric.exceptions import CommandTimeout

class AbortError(Exception):
	pass
env.abort_exception = AbortError


def save_result(target, result):
	d = {}
	try:
		os.makedirs(u'./results')
	except OSError as err:
		errmsg = os.strerror(err.errno)
		warn(err)
	base_path = os.path.abspath(u'./results')
	target_file = u'%s.json' % ( target, )
	target_path = os.path.join(base_path, target_file)
	puts(u'target=%s' % (target_path, ))

	try:
		with open(target_path, u'w+b') as fd:
			d.update(result)
			json.dump(d, fd, sort_keys=True, indent=4,
					separators=(',', ': '))
	except (IOError, ValueError) as err:
		warn(err)
	# pprint(d)


class RunScripts(tasks.Task):
	"""Runs the scripts in the `./scripts` directory on the remote.

	This assumes that all the scripts have the executable bit set.
	"""

	name = 'run-scripts'

	def __init__(self, script_dir='./scripts', *args, **kwargs):
		super(RunScripts, self).__init__(*args, **kwargs)
		self.local_script_dir = script_dir
		self.remote_scripts = []
		self.results = {
				u'time_of_run': datetime.now().isoformat(),
				}

	def upload_scripts(self):
		local_path = os.path.join(self.local_script_dir, '*')
		self.remote_scripts = operations.put(local_path, mirror_local_mode=True)
		

	def run(self, *args, **kwargs):
		self.results[u'host_string'] = env.host_string
		self.results[u'fqdn'] = socket.getfqdn(env.host_string)
		with settings( hide('stdout', 'stderr', 'output'),
				combine_stderr=False,
				abort_on_prompts=True,
				):
			try:
				self.upload_scripts()
				for script in self.remote_scripts:
					checkname = os.path.basename(script)
					try:
						result = sudo(script, combine_stderr=False, quiet=True)
					except CommandTimeout as err:
						self.results[checkname][u'exception'] = '%s' % (err, )
					self.results[checkname] = {
							u'success': result.succeeded,
							u'failed': result.failed,
							u'command': result.command,
							u'real_command': result.real_command,
							u'return_code': result.return_code,
							u'stdout': result.stdout,
							u'stderr': result.stderr,
							u'result_obj': result,
							}
					puts(u'%s=%s' % (checkname, result))
			except Exception as err:
				puts(err)
				puts(type(err))
				self.results[u'error'] = err.message
			save_result(self.results[u'host_string'],
					self.results)

rs = RunScripts()


# vim: ts=4 sts=4 fenc=utf-8 expandtab:
