class Solution {
    public int[] findErrorNums(int[] nums) {
        int[] flags = new int[nums.length + 1];
        flags[0] = 1;
        for (int num: nums) {
        	flags[num] += 1;
        }
        int[] result = new int[2];
        result[0] = Array.asList(flags).indexOf(2);
        result[1] = Array.asList(flags).indexOf(0);
        return result;
    }
}