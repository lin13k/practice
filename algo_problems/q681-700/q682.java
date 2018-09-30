class Solution {
    public int calPoints(String[] ops) {
        int i = 0;
        ArrayList<Integer> valueList = new ArrayList();
        while (i < ops.length) {
        	for (int v:valueList){
	        	System.out.print(v);
	        }
	        System.out.println();
    		int j = valueList.size();
    		int v = 0;
        	if (ops[i].equals("+")) {
        		if (j >= 2) {
        			v = valueList.get(j - 2) + valueList.get(j - 1);
        		}else if (j == 1){
        			v = valueList.get(0);
        		}
        		valueList.add(v);
        	}else if (ops[i].equals("D")) {
        		if (j != 0) {
        			v = valueList.get(j - 1) * 2;
        		}
        		valueList.add(v);
        	}else if (ops[i].equals("C")) {
        		valueList.remove(j - 1);
        	}else{
        		v = Integer.parseInt(ops[i]);
        		valueList.add(v);
        	}
        	i += 1;
        }
        int result = 0;
        for (int v:valueList){
        	result += v;
        }
        return result;
    }
}