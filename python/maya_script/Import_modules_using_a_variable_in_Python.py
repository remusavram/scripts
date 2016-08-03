"""
This question already has an answer here:

    Dynamic module import in Python 9 answers

I have a script which imports modules on-the-fly. Because modules name are changed as soon as a new version appears, it is difficult to check if the specific module name is also changed in the script. Because of this, I keep the modules name in the top of the script, in variables, like in this example:

var1 = 'moduleName1_v04'
var2 = 'moduleName2_v08'
...................
import var1
...................
import var2
...................

But if I am writing like this, I will get an error.

The question is: how to import a module using a variable like in the example? Is it possible?


Answer_1:

 6 down vote unaccept
	

Yes, you can achieve this quite easily by using importlib.import_module:

import importlib

module = importlib.import_module(var1)

Alternatively, you can use the __import__() built-in function

>>> sys = __import__("sys")
>>> sys
<module 'sys' (built-in)>

The __import__() function is the function that the interpreter uses to import modules. However, it's discouraged to use or modify this in favor of the simpler, safer import hooks, such as the first one i mentioned above. Quoting the important docs:

    This function is invoked by the import statement. It can be replaced (by importing the builtins module and assigning to builtins.__import__) in order to change semantics of the import statement, but doing so is strongly discouraged as it is usually simpler to use import hooks (see PEP 302) to attain the same goals and does not cause issues with code which assumes the default import implementation is in use. Direct use of __import__() is also discouraged in favor of importlib.import_module().

Hope this helps!



Answer_2:


Yes, you can.

For example, using importlib.import_module:

>>> var1 = 'sys'
>>> import importlib
>>> mod = importlib.import_module(var1)
>>> mod
<module 'sys' (built-in)>





"""