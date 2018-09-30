class Solution {
    public List<Integer> partitionLabels(String S) {
        Set<Character> hs = new HashSet();
        ArrayList<Character> startIndex = new ArrayList();
        for (int i = 0; i < S.length(); i++) {
        	char c = S.charAt(i);
        	if (!hs.contains(c)) {
        		hs.add(c);
        		startIndex.add(c);
        	}else{
        		startIndex.add(' ');
        	}
        }
        ArrayList<Character> endIndex = new ArrayList();
        hs = new HashSet();
        for (int i = S.length() - 1; i > -1; i--) {
        	char c = S.charAt(i);
        	if (!hs.contains(c)) {
        		hs.add(c);
        		endIndex.add(0, c);
        	}else{
        		endIndex.add(0, ' ');
        	}
        }

        int cnt = 0;
        int preIndex = 0;
        List<Integer> result = new ArrayList();
        for (int i = 0; i < S.length(); i++){
        	if (startIndex.get(i) != ' ') {
        		cnt += 1;
        	}
        	if (endIndex.get(i) != ' ') {
        		cnt -= 1;
        	}
        	if (cnt == 0) {
        		result.add(i + 1 - preIndex);
                preIndex = i + 1;
        	}
        }
        return result;
    }
}