class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1
        while left < right:

            #Skip everything invalid on the left.
            while left < right and not s[left].isalnum():
                left += 1

            #Skip everything invalid on the right.
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
"""Pattern

Two Pointers (Converging with Skipping)

Recognition

Use this pattern when:

Compare both ends.
Need to ignore certain characters.
Palindrome problems.
Validation while traversing.

Key Insight

Don't preprocess the string.

Instead, filter on the fly.

This saves memory because you never build a second string.

Why It Works

Each pointer only moves inward.

Even though there are nested loop, no character is processed repeatedly.
"""

