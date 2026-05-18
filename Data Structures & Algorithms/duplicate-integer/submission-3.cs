public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> hashNums = new HashSet<int>();

        for (int i = 0; i < nums.Length; i++) {
            if (hashNums.Contains(nums[i])) return true;
            hashNums.Add(nums[i]);
        }
        return false;
    }
    // sort, loop i = 1 .. nums.length - 1
}