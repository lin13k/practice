class Solution {
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        long pre = lower;
        pre -= 1;
        List<String> result = new ArrayList();
        for (int num: nums) {
        	if (pre >= num) {
        		continue;
        	}
        	if (pre + 1 != num) {
        		if (num - pre == 2) {
        			result.add(Long.toString(pre + 1));
        		}else{
        			result.add(String.format("%d->%d", pre + 1, num - 1));
        		}
        	}
        	pre = num;
        }
        if (pre != upper) {
    		if (upper - pre == 1) {
    			result.add(Integer.toString(upper));
    		}else{
    			result.add(String.format("%d->%d", pre + 1, upper));
        	}
        }
        return result;
    }
}