class Solution {
    public long solution(int a, int b) {
        return sumMethod(Math.min(a,b), Math.max(a,b));
    }
    public long sumMethod(long x, long y){
        return (y-x+1) * (x+y) / 2;
    }
}