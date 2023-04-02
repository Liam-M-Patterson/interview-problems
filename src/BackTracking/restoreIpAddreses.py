# Leetcode #93 Restore IP Addresses
# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

# Example 1:
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]

# Example 2:
# Input: s = "0000"
# Output: ["0.0.0.0"]

# Example 3:
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

# Constraints:
# 1 <= s.length <= 20
# s consists of digits only.
class Solution:
    def restoreIpAddresses(self, s: str):

        res = []
        ip = []
        self.dfs(s, ip, res)
        return res

    def dfs(self, s, ip, res):
        
        # length is 4, and empty string, used all digits
        if len(ip) == 4 and not s: 
            ipstr = ".".join(ip)
            res.append(ipstr)
            return
        # length is 4, but string not empty, not valid
        elif len(ip) == 4:
            return
        else:
            # iterate through string from 1 to max length of an ip section (3)
            for i in range(1, min(3, len(s))+1):

                # if the section is a valid ip section 
                if int(s[:i]) >=0 and int(s[:i]) <= 255:

                    # the ip section can not begin with leading zero
                    if not (s[0] == '0' and len(s[:i]) > 1):
                        self.dfs(s[i:], ip+[s[:i]], res)
            return
