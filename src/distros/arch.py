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
    return subprocess.check_output(cmd, shell=True)

def list_pkg_files(pkgname):
	l = run_cmd(f"pacman -Qql {pkgname}")
	print(l)


if __name__ == "__main__":
	list_pkg_files("git")