# Longest Common Subsequence
The Longest Common Subsequence (LCS) algorithm frequently appears in coding interviews conducted by major tech companies such as Google, Netflix, Meta, Amazon, and others. Many existing solutions for LCS on various online platforms can be challenging to comprehend. Consequently, we aim to provide a simplified solution for LCS which is easy to understand. Before delving into the solution, let’s first grasp the concept of the LCS algorithm.
<br>

What is the LCS Algorithm 
The "Longest Common Subsequence" (LCS) algorithm finds the longest sequence of characters that appears in the same order within two given sequences, but not necessarily consecutively. Given two input sequences, the task is to identify and output the longest common subsequence. 
<br>

###### Example 1:
Consider two sequences:  
Sequence 1: "ABCBDAB"  
Sequence 2: "BDCAB"  
Longest Common Subsequence: "BDAB"  
Note: Here "C" does not follow the order as it is present before "D" in Sequence 1 and after "D" in Sequence 2.  
<br>

###### Example 2:  
Consider two sequences:  
Sequence 1: "AGGTAB"  
Sequence 2: "GXTXAYB"  
Longest Common Subsequence: "GTAB"  
<br>

###### Example 3:  
Consider two sequences:   
Sequence 1: "XMJYAUZ"   
Sequence 2: "MZJAWXU"  
Longest Common Subsequence: "JAU"  
<br>

You can understand more about this algorithm in this [blog](https://medium.com/@rahul.madhani/coding-algorithm-question-longest-common-subsequence-lcs-1e0a4b3c47c7)


##### Sample commands to run the Python file from cmd
```
python longest_common_subsequence.py "serendipitous" "precipitation"
python longest_common_subsequence.py "longest" "stone"
python longest_common_subsequence.py "asdfwevad" "opkpoiklklj"
python longest_common_subsequence.py "dense" "condensed"
```
