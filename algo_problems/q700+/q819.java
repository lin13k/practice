class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        String[] words = paragraph.replaceAll("[!?',;.]", "").toLowerCase().split(" ");
        Map<String, Integer> map = new HashMap<>();
        List<String> bannedList = Arrays.asList(banned);
        for(String str: words){
            if(!bannedList.contains(str)){
                map.put(str, map.getOrDefault(str, 0) + 1);
            }
        }
        int curMax = 0;
        String res = "";
        for(Map.Entry<String, Integer> e: map.entrySet()){
            System.out.print(e.getKey() + " ");
            System.out.println(e.getValue());
            res = map.get(e.getKey()) > curMax? e.getKey() : res;
            curMax = curMax > e.getValue()? curMax: e.getValue();
        }
        System.out.println(curMax);

        return res;
    }
}