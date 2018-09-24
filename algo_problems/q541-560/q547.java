public class Solution {
    public int findCircleNum(int[][] M) {
    	if (M.length == 1){
    		return 1;
    	}
    	boolean[] visited = new boolean[M.length];
    	for (int i = 0; i < M.length; i ++) {
    		visited[i] = false;
    	}
    	Stack <Integer> stack = new Stack();
    	int result = 0;
    	for (int i = 0; i < M.length; i ++) {
    		if (visited[i] == true) {
    			continue;
    		}
    		result += 1;
    		stack.push(i);
    		visited[i] = true;
    		while(stack.size() != 0) {
    			Integer t = stack.pop();
    			for (int j = 0; j < M.length; j ++) {
    				if (visited[j] == false && M[t][j] == 1 ) {
    					visited[j] = true;
    					stack.push(j);
    				}
    			}
    		}
    	}
    	return result;

    }
}