public class Solution {
    public bool IsPalindrome(string s) {
        int l = 0, r = s.Length - 1;
		
		while (l < r) {
			while (l < r && !IsAlphaNum(s[l])) {
				l++;
			}
			while (r > l && !IsAlphaNum(s[r])) {
				r--;
			}
			if (char.ToLower(s[l]) != char.ToLower(s[r])) return false;
			l++; r--;
		}
		
        return true;
    }

    private static bool IsAlphaNum(char c) {
		return ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z') || ('0' <= c && c <= '9');
	}
}
