public class Solution {
	public bool IsPalindrome(string s) {
        string formatStr = "";

        for (int i = 0; i < s.Length; i++) {
            if (Char.IsLetterOrDigit(s[i])) {
				formatStr += char.ToLower(s[i]);
			}
        }
		
		return formatStr == new string(formatStr.Reverse().ToArray());
    }
}
