import sys

def longest_common_subsequence(str1 : str, str2: str) -> str:
    '''
        Function to return the longest common sub-sequence between the two strings
    '''
    # Initialize subseq_lst as empty list
    subseq_lst = []

    #  Prepare all the unique sub-strings from str2
    str_lst = [str2[i:] for i in range(len(str2))]
    
    # Take each string from prepared list and check the matching sequence with str1
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

        # Add the characters following the sequence in subseq_lst if it is not already in it
        if len(chars_found) > 0:
            if chars_found not in subseq_lst:
                subseq_lst.append(chars_found)

    # Sort the list to find longest subsequence and return it
    sorted_subseq_lst = sorted(subseq_lst, key=len, reverse=True)
    
    # Return the longest common subsequence
    if len(sorted_subseq_lst) > 0:
        return sorted_subseq_lst[0]
    else:
        return None

if __name__ == "__main__":

    # Parse the system arguments
    if len(sys.argv) == 3:
        str1 = sys.argv[1]
        str2 = sys.argv[2]

        # Call the longest_common_subsequence function
        print(longest_common_subsequence(str1, str2))
    else:
        print("Please pass two string arguments")

# Command to run the Python file from cmd
# python longest_common_subsequence.py "serendipitous" "precipitation"
# python longest_common_subsequence.py "longest" "stone"
# python longest_common_subsequence.py "asdfwevad" "opkpoiklklj"
# python longest_common_subsequence.py "dense" "condensed"