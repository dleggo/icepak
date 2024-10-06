# Icepak

```
File structure of package

pkg
|- run.sh
|- usr
	|- bin
		|- pkg
	|- share
		|- pkg
			|- data
|- var
	|- lib
		|- pkg
```

## How a package gets installed

### User clicks on .pak file in their downloads.
Which pops up a dialog, proceding through the installation.

A package can choose one of two options.
 - An installation script is run from the pkg file. ```install.sh``` The installation itself is sandboxed with ```/``` being the root of the package, and /src being the installation files.
 - If install.sh does not exist then icepak will run a default installation which copies all files from the .pkg into the ```/``` folder of the installation location.

Both choices result in an installation wizard coming up.

After the files have been copied to the installed directory the package is then queried for dependencies.
Dependencies will be specified in a file called ```deps``` in the root of the package. dependencies are
listed in the format like
```
dep1
dep2
dep3==1.2.3
dep4==https://your/url/here/pkg.pak
```
The ```dep``` file is not mandatory to exist.
If dependencies are listed, for any givin dependency, icepak will attempt to install it in the following
order.

 - If a URL is specified, icepak will attempt to fetch it. If it is successfull icepak will install it in
   the normal way. If it fails to retrieve it, then it will display an error message in the installation
   wizard, explaining the problem, and suggesting to notify the application developer.

 - Icepak repos. Icepak is planned to have a ***small*** repository of librarys. Apps should not go in
   the repos but librarys. For instance ```libjpg``` is an example of a library
   ```abiword``` is an example of an app.

 - Distros package manager. Might not work this way on immutable systems, but if the distros repositorys
   contain the dependency then it would be installed, into its own seperate icepak.


> Sidenote. Icepak is planned to have each .pak file distributed from the application developers
> themselves. For migration purposes however, Icepak will have temporary repos with applications, until
> it is maintained by the developers themselves. The project model of icepak is not to have repos, but to
> have each .pak come from the developers, similar to how Mac OS and Windows do it.

The package is installed in its enviroment. ```application/version```

### User runs the application
Icepak fires up and begins setup

 - Icepak checks dependencies, and loads them in their respective location in the sandbox.

 - Icepak finalizes sandbox, and runs ```run.sh```

For instance.

#### Package A:
```
pkg-a
|- 1.2.3
	|- usr
	|	|- bin
	|		|- a.py
	|- deps
```
with ```deps``` being
```
pkg-b==1.12
```

#### Package B:
```
pkg-b
|- 4.5
	...
|- 1.2
	|- usr
	|	|- share
	|		|- important-list.txt
	|- bin
		|- b.py

```

When pkg-a is ran, pkg-b will be loaded in the pkg-a tree as follows