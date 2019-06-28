# Modules and the functions within them can be imported
# in a variety of manners, especially if they are in the same
# file/folder

# This makes all functions/entire module available
import <module/file-name> #note no '.py'

# This instantiates the function
module/file-name.function_name()

# This imports the specific function
from module_name import function_name, function_name 1, function_name 2 #... etc

# With this above formatting you do NOT need call out the .function_name()

# If there is a naming conflict you can provide an alias()
from module_name import function_name as fn 

# This is also true for module alias
import module_name as mn

# Import all functions using '*'
from module_name import * 
