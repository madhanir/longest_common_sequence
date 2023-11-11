import sys

def Sorting(lst, reverse_setting=True):
    '''
        Function to sort the passed list based on the length of the elements
        Using reverse_setting we can choose ascending or descending (default) order
    '''
    lst2 = sorted(lst, key=len, reverse=reverse_setting)
    return lst2

def longest_common_sequence(str1, str2):
    '''
        Find the longest common sequence between the two strings
        Problem statement: https://www.youtube.com/watch?v=sSno9rV8Rhg

    '''
    common_seq_lst = []

    #  Prepare all the combination sub-strings from str2
    str_lst1 = [str2[i:] for i in range(len(str2))]
    str_lst2 = [str2[i:] for i in range(1, len(str2))]
    str_lst = str_lst1 + str_lst2
    str_lst = Sorting(str_lst)
    
    # Take each string from prepared list and check the matching sequence in str1
    for list1 in str_lst:
        search_index = 0
        chars_found = ""

        # Loop through each character to validate which characters follow sequence with str1
        for char in list1:
            index_found = str1.find(char, search_index)

            #  Character is following sequence with str1 hence store its value
            if index_found != -1:
                chars_found += char
                if len(str1) > index_found + 1:
                    search_index = index_found + 1
                else:
                    break

        # Add the characters following the sequence in common_seq_lst if it is not already in it
        if len(chars_found) > 0:
            if chars_found not in common_seq_lst:
                common_seq_lst.append(chars_found)

    # Sort the list to find longest sequence and return it
    common_seq_lst = Sorting(common_seq_lst)
    if len(common_seq_lst) > 0:
        return common_seq_lst[0]
    else:
        return None

if __name__ == "__main__":

    # Parse the system arguments
    if len(sys.argv) == 3:
        str1 = sys.argv[1]
        str2 = sys.argv[2]

        # Call the longest_common_sequence function
        print(longest_common_sequence(str1, str2))
    else:
        print("Please pass two string arguments")

# Command to run the Python file from cmd
# python longest_common_sequence.py "serendipitous" "precipitation"
# python longest_common_sequence.py "longest" "stone"
# python longest_common_sequence.py "asdfwevad" "opkpoiklklj"
# python longest_common_sequence.py "dense" "condensed"