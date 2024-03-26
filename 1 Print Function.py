# Write a Python program to print "Hello Python"  <- Single line comment

""" This is a multi line comment in python
    we can use with print function to print this content

    * Difference between valid & Invalid variable *
               Valid           invalid
            var_1 = '56'        int
            _var = 652          1var
            var_cal = "kp"      var cal         
    
    * We can see ascape sequence charector * 
            1. \n = new line
            2. \t = space between
            3. \' = print ' 
            4. \" print "    """

print('Hello Welcome to Python world',end=' ')

print("""to take challenge 150 Days python code for bigginer to advance level 
        including \n \t python framework \'Django\', \"Flask\", Numpy, Pandas""")

"""Type casting :- convert type of data
    we can convert type from smaller to higher
    not possible to convert higher to smaller"""

var1 = 123
var2 = 'kanak'
var3 = '8618'

print(type(int(var3)))
print(var2 + var3)
print(10 *  var2)