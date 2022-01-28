# **Horse Blinders**

**Horse Blinders** is a command-line utility for speeding up experimental coding procedures 
when manual coding is necessary. Essentially, this utility provides 
a way to reduce the coder's on-screen distractions and facilitate 
rapid input of coding values.

<br />

## **Installation**

This Python script requires Python 3.7 or later. For Windows, this can be installed from [**here**](https://www.python.org/downloads/windows/). For OSx users, open a terminal and check your native python installation by running `python --version`. If it is older than 3.7, install the latest version [**here**](https://www.python.org/downloads/macos/).

Once the correct version of Python is installed, open a terminal in the directory containing the files to be processed and create a virtual environment using the following command.

### *Windows*
```bash
python -m venv venv
```

### *OSx*
```bash
python3 -m venv venv
```
Next, install the `colorama` package using the commands below in sequence.

### *Windows*
```bash
venv\Scripts\activate
pip install colorama
deactivate
```

### *OSx*
```bash
source venv/bin/activate
pip3 install colorama
deactivate
```
No further installation is necessary. Just download **`horse_blinders_v6.py`**.

<br />

## **Usage**

Start up **Horse Blinders** using the following procedure.

The following command initiates the virtual environment in which the program should be run (*`Note`*: Windows requires backslashes ( \\ ), while OSx requires slashes ( / ) for these commands). **This should be done every time you use the program**.

### *Windows*
```bash
venv\Scripts\activate
```

### *OSx*
```bash
source venv/bin/activate
```

Once initiated, the working directory should be prepended by the name of the virtual environment (in this case: `venv`).

```bash
(venv) C:\usr\...>

OR

(venv) user:~
```
Next, run the script with the following command, substituting the name of the input file for **[inputfile.txt]** and the name of the desired outputfile for **[outputfile.txt]**, both with no brackets. If the output file does not exist yet, the script will create it for you.

### *Windows*
```bash
python horse_blinders_v6.py [inputfile.txt] [outputfile.txt]
```

### *OSx*
```bash
python3 horse_blinders_v6.py [inputfile.txt] [outputfile.txt]
```

On startup, the splash page displays the logo, attributions, and a brief description of the purpose and functionality of the program.
  
  \
![Splash Page](/images/splashpage.png)  
  \
Below this, the current active files are listed and the user is prompted for input. Enter the number of entries you plan to code during the current session and press enter. Then enter your initials or coder ID if applicable and press enter. This ID will be appended to the end of each line to help differentiate multiple coders.

<br />

## **Coding**

An example of the coding view is given below.  
  
- At the top of the resulting window, your progress in the current coding session is displayed.

- In the next section of the window, the **metadata** and **content** of the current entry are displayed. The **target word** is highlighted in red.

- The **target sentence** itself is displayed in the middle of the window with token boundaries marked by the indices in green.

- Below this, the available **input options** for the current coding parameter are outlined, along with their respective meanings. Enter any of these character sequences in the input line at the bottom of the window.

<br />

![Coding Page](/images/coding_page.png)  

<br />

## **Input**

Currently, **Horse Blinders** expects input in the form of a tab-delineated text file containing single-line entries. It expects that the file takes the following form:


```txt
Corpus	Subcorpus	Filename	LineNumber	CitationID	SentID		...
COCA	60minutes	##21693_tagged.txt	60	NA	3f38d177d8aa1663ccd5f0b  ...
...
```
Where the first line is a header row containing the name of each coding parameter. Each subsequent line after that should contain a single entry with its corresponding parameters.

## **Output**

After processing, **Horse Blinders** outputs a single tab-delineated file at the level of the working directory labeled with the filename displayed on the splash page. This file is identical to the input file in form, but has the additional coding parameters appended to the end of each line that you have completed. 

As long as you continue to start the program with the **same input and output files**, the program will pick up where you left off in the last session.

## **License**

CC0