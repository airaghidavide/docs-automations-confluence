"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

Typical usage example:
  i = indent(txt='ciaone')
  res = MYClass.func_1(x=1)
"""

def indent(txt: str) -> int:
    '''Count the indentation in whitespace characters.
        
        Args:
        txt (str): text with indents
    Returns:
        int: Number of whitespace indentations
    '''
    return sum(4 if char == '\t' else 1 for char in txt[: -len(txt.lstrip())])

def indent_2(txt: str) -> int:
    '''Count the indentation in whitespace characters.
        
        Args:
        txt (str): text with indents
    Returns:
        int: Number of whitespace indentations
    '''
    return sum(4 if char == '\t' else 1 for char in txt[: -len(txt.lstrip())])

def another_function_to_confluence(txt: str) -> int:
    '''Count the indentation in whitespace characters.
        
        Args:
        txt (str): text with indents
    Returns:
        int: Number of whitespace indentations
    '''
    return sum(4 if char == '\t' else 1 for char in txt[: -len(txt.lstrip())])

class MYClass:

    def func_1(x):
        '''Example function with types documented in the docstring.

            Args:
            param1 (int): The first parameter.
            param2 (str): The second parameter.

        Returns:
            bool: The return value. True for success, False otherwise.
        '''
        
        x = x * 3
        return x