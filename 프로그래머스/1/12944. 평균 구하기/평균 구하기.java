class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        int length = 0;
        for(int num : arr){
            answer += num;
            length++;
        }
        answer /= length;
        return answer;
    }
}