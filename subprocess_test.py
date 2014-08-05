import subprocess
from sys import argv

script, branch_1, branch_2 = argv

def git(*args):
	# import pdb; pdb.set_trace()
	return subprocess.check_output(['git'] + list(args))

args = "%s...%s" %(branch_1, branch_2)
print git("diff", args)

# print subprocess.check_output(["echo", "Hello World!!!"])

# print subprocess.check_call(["ls"])

# def git(*args):
# 	return subprocess.check_call(['git'] + list(args))

# print git('status')