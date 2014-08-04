import subprocess

print subprocess.check_output(["echo", "Hello World!!!"])

print subprocess.check_call(["ls"])

def git(*args):
	return subprocess.check_call(['git'] + list(args))

print git('status')