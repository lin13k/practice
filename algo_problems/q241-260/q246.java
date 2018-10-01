class Solution {
    public boolean isStrobogrammatic(String num) {
        int n = (num.length() + 1)/2;
        for (int i = 0; i < n; i++) {
        	char c = num.charAt(i);
        	char d = num.charAt(num.length() - 1 - i);
        	if ("018".indexOf(c) != -1 && c == d) {
        		continue;
        	}
        	if ("69".indexOf(c) != -1 && "69".indexOf(d) != -1 && c != d) {
        		continue;
        	}
        	return false;
        }
        return true;
    }
}