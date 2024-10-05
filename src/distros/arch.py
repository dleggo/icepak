"""Arch Linux"""
#
#                   _       _      _                  
#    /\            | |     | |    (_)                 
#   /  \   _ __ ___| |__   | |     _ _ __  _   ___  __
#  / /\ \ | '__/ __| '_ \  | |    | | '_ \| | | \ \/ /
# / ____ \| | | (__| | | | | |____| | | | | |_| |>  < 
#/_/    \_\_|  \___|_| |_| |______|_|_| |_|\__,_/_/\_\
#                                                     

import os
import subprocess

def run_cmd(cmd):
    return bytes.decode(subprocess.check_output(cmd, shell=True), "utf-8")

def list_pkg_files(pkgname):
	l = run_cmd(f"pacman -Qql {pkgname}").split("\n")
	return l

def list_pkg_dirs(pkgname):
	"""
	Lists all folders that are owned by an installed package
	Mabye needs a bit of clarifying... ;D
	"""
	l = list_pkg_files(pkgname)
	d = [] # is the path a directory
	for a in l:
		assert os.path.exists(a), "Package file does not exist! Mabye your package is broken."
		is_dir = os.path.isdir(a)
		assert is_dir != None, "Error telling if path was a directory!"
		d.append(is_dir)
	r = []
	for a,b in zip(l, d):
		if b:
			r.append(a)


if __name__ == "__main__":
	print(list_pkg_files("git"))