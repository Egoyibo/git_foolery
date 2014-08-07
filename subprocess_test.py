import subprocess
from sys import argv

script, branch_1, branch_2 = argv




args = "%s...%s" %(branch_2, branch_1)
print git("diff", args)

def git(*args):
	# import pdb; pdb.set_trace()
	return subprocess.check_output(['git'] + list(args))