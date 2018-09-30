class Solution {
    public String similarRGB(String color) {
        return "#" + f(color.substring(1, 3)) + f(color.substring(3, 5)) + f(color.substring(5, 7));
    }

    public String f(String comp){
    	int v = Integer.parseInt(comp, 16);
    	v = v / 17 + (v % 17 > 8 ? 1 : 0);
    	return String.format("%02x", 17* v);
    }
}