'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''


def num_decodings(s: str) -> int:
        # Initialize a previous count 'prev_count' of decodings and a current count 'curr_count'.
        prev_count, curr_count = 0, 1
      
        # Iterate over the string with index to keep track of positions.
        for i in range(len(s)):
            # The next count of decodings 'next_count' should start at 0.
            next_count = 0
          
            # If current character is not '0', we can use it for a valid decoding.
            if s[i] != '0':
                next_count = curr_count
          
            # If the current and the previous digit make a number ≤ 26, it can be decoded as well.
            # We need to ensure that we're at the second or later character and that
            # the previous character isn't '0'.
            if i > 0 and s[i-1] != '0' and (s[i-1] == '1' or (s[i-1] == '2' and s[i] < '7')):
                # If the condition is true, add the previous count of decodings.
                next_count += prev_count
          
            # Update 'prev_count' and 'curr_count' for the next iteration.
            prev_count, curr_count = curr_count, next_count
      
        # The final 'curr_count' is the total number of decodings for the string.
        return curr_count

x = '224511'
print(num_decodings(x))


def numDecodings(s): 
	if not s:
		return 0

	dp = [0 for x in range(len(s) + 1)] 
	
	# base case initialization
	dp[0] = 1 
	dp[1] = 0 if s[0] == "0" else 1   #(1)

	for i in range(2, len(s) + 1): 
		# One step jump
		if 0 < int(s[i-1:i]) <= 9:    #(2)
			dp[i] += dp[i - 1]
		# Two step jump
		if 10 <= int(s[i-2:i]) <= 26: #(3)
			dp[i] += dp[i - 2]
	return dp[len(s)]

print(numDecodings(x))