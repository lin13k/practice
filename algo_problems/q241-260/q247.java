class Solution {
    public List<String> findStrobogrammatic(int n) {
        return this.helper(n, n);
    }

    private List<String> helper(int n, int m) {
    	if (n == 0) {
    		return new ArrayList<String>(Array.asList(""));
    	}
    	if (n == 1) {
    		return new ArrayList<String>(Array.asList("1", "8", "0"));
    	}

    	List<String> preList = this.helper(n - 2, m);
    	List<String> result = new ArrayList();
    	for (String s: preList) {
    		if(n != m)result.add("0" + s + "0");
    		result.add("1" + s + "1");
    		result.add("8" + s + "8");
    		result.add("6" + s + "9");
    		result.add("9" + s + "6");
    	}
    	return result;
    }
}