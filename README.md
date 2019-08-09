# Frida iOS
For more information about frida: https://trelis24.github.io/

## Scripts
### start_frida.py
Python script that given a script and a app bundle, it starts the app, inject de script and resume the execution.

### find_classes.js
Search for classes
* If no strings are specified in "search_class" array, the script will print all the classes.
* If one or more strings are specified in "search_class array", the script will only print classes which contains the strings in their name.


### find_methods.js
Search for methods
* If no strings are specified in "search_class" nor "search_method" arrays, the script will print the methods of all the classes (frida server might stop running if there are a lot of	classes).
* If one or more strings are specified in "search_class array", the script will print the methods of the classes which contains the strings in their name.
* If one or more strings are specified in "search_method" array, the script will print the classes which contains the strings in the name of one or more of their methods.
* If one or more strings are specified in "search_method" and "search_class" array, the script will print only the classes and methods that meet with the search criteria.

### hooking.js
Hooks into methods
* Given one or more classes in "search_class", it hooks into all their methods.
* Given one or more methods in "search_method", it hooks into all methods of any classes that meet with the search criteria.
* Given a class and a method, it hooks into the method of this class.
* Neither class nor method full name is needed in order to hook. If a partial string is given, the script will hook into all the methods that have the string in their name.

### replace.js
Replace methods return values
* Given an especific class, method and value it replaces the return value of the method.
* Method format: for example:  "- isJailbroken:"
* Data must be in the same array position (classNmes, methodNames, returnValues). For example: ['class1','class2']\['method1','method2']['retvalue1','retvalue2']
* If returnValues of a method is left empty, the method will be hooken but the script will not modify the return value.