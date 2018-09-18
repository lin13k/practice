class Solution {
    public int lenLongestFibSubseq(int[] A) {
        Map<Integer, Integer> indexMap = new HashMap();
        for (int i = 0; i < A.length; i ++){
        	indexMap.put(A[i], i);
        }
        int result = 0;
        Map<Integer, Integer> longestMap = new HashMap();
        int n = A.length;
        for (int i = 0; i<n; i++){
        	for (int j = 0; j<i; j++){
        		int t = A[i] - A[j];
        		int k = indexMap.getOrDefault(t, -1);
        		if (k != -1 && j < k){
        			// longestMap[k, i] = lonmap[j, k] + 1
        			int cand = longestMap.getOrDefault(j * n + k, 2) + 1;
        			longestMap.put(k * n + i, cand);
        			result = Math.max(result, cand);
        		}
        	}
        }
        return result;

    }
}