// LeetCode - Two Sum
// https://leetcode.com/problems/two-sum/
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> aux = new HashMap<>();
        int[] resp = null;
        int i = 0;

        for (int x : nums){
            if (aux.containsKey(target - x)){
                resp = new int[]{i, aux.get(target - x)};
                break;
            }
            aux.put(x, i++);
        }

        return resp;
    }
}
