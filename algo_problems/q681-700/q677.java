class TrieNode {
	private int sum;
	private int num;
	private Map<Character, TrieNode> map;
	public TrieNode(){
		this.map = new HashMap();
	}

	public int add(String key, int val){
		int change = 0;
		if (key.length() == 0) {
			change = val - this.num;
			this.num = val;
		}else{
			if (!this.map.containsKey(key.charAt(0))) {
				map.put(key.charAt(0), new TrieNode());
			}
			change = map.get(key.charAt(0)).add(key.substring(1), val);
		}
		this.sum += change;
		return change;
	}

	public int get(String key){
		if (key.length() == 0) {
			return this.sum;
		}
		return this.map.getOrDefault(key.charAt(0), new TrieNode()).get(key.substring(1));
	}
}


class MapSum {

    /** Initialize your data structure here. */
    private TrieNode root;
    public MapSum() {
        this.root = new TrieNode();
    }
    
    public void insert(String key, int val) {
        this.root.add(key, val);
    }
    
    public int sum(String prefix) {
        return this.root.get(prefix);
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */