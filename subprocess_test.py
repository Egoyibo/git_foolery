import subprocess
from sys import argv

script, branch_1, branch_2 = argv

def git(*args):
	return subprocess.check_call(['git'] + args)

args = ('diff,--name-status,%s...%s') %(branch_1, branch_2)
args_split = args.split(',')
print git(args_split )

# print subprocess.check_output(["echo", "Hello World!!!"])

# print subprocess.check_call(["ls"])

# def git(*args):
# 	return subprocess.check_call(['git'] + list(args))

# print git('status')