class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
                
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

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

Even though there are nested conditions, no character is processed repeatedly.
"""
