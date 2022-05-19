# django-template-converter
This program has made to add STATIC tag to all HREF and SRCs of an HTML web project. So, it makes an HTML project a Django template.

>Before starting; you should have an HTML template so you can test it yourself. But I've already added one which is in **src/example-template**.

## How to run?

It's simple as much as it could be. Just run the program using ```python3 src/main.py```  . This will try to convert file named `index.html` to `index-copy.html` if you don't give a path as a parameter.

### Convert only a specific file
There are *2 variables* named `TARGET` and `TARGET_OUT` in `src/main.py`. This variables are for set the **target HTML file which you want to convert** into Django template.  \
The other one is for set the output file which has been converted into Django template.   

### Convert whole folder 
You should run the program with a parameter to set the input files directory. \
Example: **`python3 src/main.py src/example-template`** \
> This will convert all the files inside the directory `src/example-template` and replace them  
