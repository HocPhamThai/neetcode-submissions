public class Solution {
    public bool IsAnagram(string s, string t) {
        Dictionary<char,int> charCount = new Dictionary<char,int>();
        
        foreach (char c in s) {
            charCount[c] = charCount.GetValueOrDefault(c, 0) + 1;
        }
		
		foreach (char c in t) {
			charCount[c] = charCount.GetValueOrDefault(c, 0) - 1;
		}
		
		foreach (var pair in charCount) {
			if (pair.Value != 0) return false;
		}
		
		return true;
    }
}
