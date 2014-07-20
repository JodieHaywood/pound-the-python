pound-the-python
================

Instruction list for setting up python for data - science

"These Notes presume you are working on a mac... we can build out later :-)"

Get the tools:


Download and Install Anaconda: http://continuum.io/downloads

if you already have a python distribution installed
your system could get confused about which version to use
so it is recommended to uninstall any python you already have


Download and Install Sublime Text: http://www.sublimetext.com/

This is a great text editor if you plan to 
write scripts or edit code


Download and Install Iterm2: http://iterm2.com/

Here is where you can do lots of things like turn python on... run scripts...
and install new libraries 
try this one out:
"pip install seaborn" [The coolest plotting library you mother ever saw...]

Test Anaconda:

	1. open your favorite console[terminal or iTerm2]
	2. Navigate to the python_tutorial directory
		cd repos/pount-the-python/python_tutorial
	2. type "ipython notebook"
		An Ipython Dashboard should open in your web browser
	Note: Ipython Notebook is awesome! Use it :-)


Seting up repos
===============

Its Important to have a place for your code to live, and a place for you to work with the code

we use "repos" for git repos which is where the main code base will live and be developed.

and a playground for doing ad-hoc scripts and testing.

from your home in your terminal:
	cd ~

make two directories:
	mkdir repos
	mkdir playground
	cd playground
	mkdir sandbox

Most of my work happens in the sandbox:
	cd sandbox
	ipython notebook

Now you have ipython notebook open... start writing code!
to run what you write:
	shift+enter


