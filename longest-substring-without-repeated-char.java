class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max = 0;
        int n = s.length();
        HashSet<Character> set = new HashSet<Character>(); // used to keep track of unique chars
        
        int i = 0;
        int j = 0;
        
        while( j < n ){
            if( !set.contains(s.charAt(j)) ){
                set.add(s.charAt(j));
                max = Math.max(max, set.size());
                j++;
            }
            else {
                set.remove( s.charAt(i) );
                i++;                
            }
        }
               
        return max;
    }
}

/**
* Runtime: 6 ms, faster than 64.31% of Java online submissions for Longest Substring Without Repeating Characters.
* Memory Usage: 38.9 MB, less than 88.62% of Java online submissions for Longest Substring Without Repeating Characters.
**/