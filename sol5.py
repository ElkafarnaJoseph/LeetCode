def longestPalindrome(s):
        s_len = len(s)
        longest_pali_sub = ''

        def expand_left_right(left , right):
            while left >= 0 and right < s_len and s[left] == s[right]:
                    left -= 1
                    right += 1
            return s[left + 1 : right]

        for i in range(s_len):
            expand_left_right(i , i)
            expand_left_right(i , i + 1)
            longest_pali_sub = max(longest_pali_sub , expand_left_right(i , i) , expand_left_right(i , i +1) , key=len)
        return longest_pali_sub

test = 'babad'
print(longestPalindrome(test))

# what we did is get the length of the string 
# make a new variable to store the longest palindrome 
# creating an expand function that goes to two points the left to the right end of the string 
# then we created a while loop the expands as long as left is not less than 0 and right is <= length of the string 
# characters at positions are equal s[left] == s[left]
# after exiting the loop returns the substring from left + 1 and right 
# we use left + 1 so it doesn't move too far to the left 
# expand_left_right(i , i) is called to check for odd-length palindromes centered at i.

# expand_left_right(i , i + 1) is called to check for even-length palindromes centered between i and i+1.
# For each iteration, this line uses the max function to compare the current longest palindrome (longest_pali_sub)
# with the palindromes found by expand_left_right(i , i) and expand_left_right(i , i + 1). The key=len argument ensures
# that the comparison is based on the length of the substrings.