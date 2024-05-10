# Write a Python program to insertion at the beginning in OrderedDict.

from collections import OrderedDict
ordered_dict = OrderedDict([('b', 2), ('c', 3), ('d', 4)])
new_item = ('a', 1)
new_ordered_dict = OrderedDict([new_item])
new_ordered_dict.update(ordered_dict)
print("Updated OrderedDict:", new_ordered_dict)


# Write a Python program to check order of character in string using OrderedDict()

from collections import OrderedDict
def check_order(string, reference):
    string_dict = OrderedDict.fromkeys(string)
    reference_dict = OrderedDict.fromkeys(reference)
 
    return string_dict == reference_dict

input_string = "hello world"
reference_string = "helo wrd"
if check_order(input_string, reference_string):
    print("The order of characters in the input string matches the refe")
else:
    print("The order of characters in the input string does not match the refe")