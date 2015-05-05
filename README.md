# How-to-Python
Instructions to using python for data analytics/science. Instructions currently only written for OSX. Windows instructions possibly coming eventually.

### 1. Get the tools
1. Download and install Xcode developer tools from the app store https://developer.apple.com/xcode/downloads/
2. Download and install Anaconda: http://continuum.io/downloads
>This simplifies the installation process of python 2.7, ipython, pandas (dataframes library), numpy (math library), scipy (statistics library), matplotlib (plotting library), and several other key tools/libraries for data science.  
*If you already have a python distribution installed, your system could get confused about which version to use.  We recommend to uninstall any python dist you may already have before installing Anaconda. http://stackoverflow.com/questions/3819449/how-to-uninstall-python-2-7-on-a-mac-os-x-10-6-4  
>After installation, use Anaconda's gui to install ipython notebook http://ipython.org/notebook.html 
3. Download and install Sublime Text: http://www.sublimetext.com/3
>This is a great text editor if you plan to write scripts or edit code in any language. After installation, run the below code in Terminal to add the sublime text command line interface allowing you to open any directory in sublime by typing 'subl'

```sh
$sudo ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/bin/subl
```

### 2. Test your python installation:
1. Open up Terminal
2. Try running a pip install to install a library we will use: 

    ```sh
    $ pip install seaborn
    ```
    Fun fact: pip is a recursive acronym that can stand for either "Pip Installs Packages" or "Pip Installs Python"  
    Seaborn is an awesome library which extends matplotlib's plotting functionality.  

3. Navigate to your Documents directory using 'cd', and create a new folder named repos using 'mkdir'

    ```sh
    $ cd Documents
    $ mkdir repos
    $ cd repos
    ```  

4. Git clone the 'how-to-python' repository from stash

    ```sh
    $ git clone https://stash.teslamotors.com/scm/rel/how-to-python.git
    ```  

5. Navigate to the how-to-python python_tutorial folder

    ```sh
    $ cd how-to-python/python_tutorial
    ```  

6. Launch an IPython notebook. IPy notebook is a web-based interactive computational environment where you can combine code execution, text, mathematics, plots and rich media into a single document

    ```sh
    $ ipython notebook
    ```
    Note: IPython Notebook is awesome! Use it :-)

7. Navigate to the first lesson, open it, and start pythoning

### 3. Setting up repositories
It's important to have a place for your code to live, and a place for you to work with your code. We use 'repos', or git repos to store and develop our main code base. You can also create a playground for doing ad-hoc scripts and testing.

To view an example folder structure, git clone the 'root' repo from github, and open it in finder or sublime text

```sh
$ cd ~
$ git clone https://github.com/jshiv/root.git
$ cd root
$ open . 
$ subl .
```
To launch an IPython notebook from here 

```sh
$ ipython notebook
```

### 4. Introduction to Python
Now that you have IPython notebook open, it's time to start writing code!  

#####How to learn python
Find a problem, and use python to solve it!  
Example: need to create virtual dice  

1. Create a new notebook by clicking 'New Notebook' at the top right corner of the IPy notebook tree screen  

2. Import the 'random' library to generate random numbers

    ```  
    import random
    ```
    Type shift+enter within a cell to run the cell. IPy notebook is a read-eval-print-loop environment. In a REPL, the user enters one or more expressions (rather than an entire compilation unit) and the REPL evaluates them and display the results.

3. Create a class called 'die' in a second cell

```
class die:
    # every class needs an __init__ method
    # __init__ gets run automatically when you instantiate an object
    def __init__(self, sides = 6):
        """die represents a single die with property of 'sides' and methods of 'roll' and 'rolln'"""
        self.sides = sides

    def roll(self):
        self.rolled = random.randint(1, self.sides)
        print self.rolled

    def rolln(self, n = 10):
        self.rolled = [random.randint(1, self.sides) for x in range(n)]
        print self.rolled
```

4. Instantiate your die with the instance 'myDie' in a third cell. Roll myDie twice and view the results.

    ```  
    myDie = die(10)
    myDie.rolln(n=2)
    ```

##### Do you want more?
Here are some awesome instructional websites:  
Jason's favorite: http://nbviewer.ipython.org/gist/rpmuller/5920182  
How Anmol originally learned python: http://learnpythonthehardway.org/book/

Recommendations from the data science course on Coursera:  
Google's Python Class: https://developers.google.com/edu/python/  
Code Academy Python: http://www.codecademy.com/tracks/python  
Syntax checking for Python: http://www.jetbrains.com/pycharm/  
Python for beginners by a beginner: http://www.sthurlow.com/python/  
A guide for finding resources: http://docs.python-guide.org/en/latest/

##### What are the coolest tools?
pandas: DataFrames are awesome!  
numpy: Maths are awesome!  
scipy: Statistics are awesome!

```
import pandas as pd
import numpy as np
from scipy import stats
```

#### How do I do data-science? 
##### Make data, find data, combine data, then do something awesome with it
Links!  
http://blog.yhathq.com/posts/data-science-in-python-tutorial.html  
http://www.quora.com/Data-Science/How-do-I-become-a-data-scientist
https://www.mysliderule.com/learning-paths/data-analysis/learn/?
