#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    #display list1[1], the second item in the list.
    print(list1[1])

    #creates a new list
    list2 = ["juniper"]

    #extend the list with an iterable
    list1.extend(list2) # This should go cleanly

    print(list1)

    # create list3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    list1.append(list3)

    # display the new complex list1
    print(list1)

    # This should create an awkward nested list
    # Let's return the awkward portion
    print(list1[4])
    
    # Print the first IP address within the list at list1[4]  
    print(list1[4][0])

main()

