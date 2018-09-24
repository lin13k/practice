class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int total = 0;
        int tank = 0;
        int start = 0;
        for (int i = 0 ; i < gas.length; i ++) {
        	tank = tank + gas[i] - cost[i];
        	if (tank < 0){
        		total += tank;
        		tank = 0;
        		start = i + 1;
        	}
        }
        if (total + tank < 0){
        	return -1;
        }else{
        	return start;
        }
    }
}