class Solution {
    public int maxProduct(int[] nums) {
        if (nums == null || nums.length == 0) {
        	return 0;
        }

        int r = nums[0];
        int imax, imin;
        imax = imin = r;
        for (int i = 1; i < nums.length; i++) {
        	if (nums[i] < 0) {
        		int tmp = imax;
        		imax = imin;
        		imin = tmp;
        	}
        	imax = Math.max(nums[i], nums[i]*imax);
        	imin = Math.min(nums[i], nums[i]*imin);
        	r = Math.max(r, imax);
        }
        return r;
    }
}