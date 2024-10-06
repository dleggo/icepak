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
```
The ```dep``` file is not mandatory to exist.
If dependencies are listed, for any givin dependency, icepak will attempt to install it in the following
order.

 - Icepak repos. Icepak is planned to have a ***small*** repository of dependencies. Apps should not go in
   the repos but dependencies like packages. For instance ```libjpg``` is an example of a dependency
   ```abiword``` is an example of an app.

 - Distros package manager. Might not work this way on immutable systems, but if the distros repositorys
   contain the dependency then it would be installed, into its own seperate icepak.

