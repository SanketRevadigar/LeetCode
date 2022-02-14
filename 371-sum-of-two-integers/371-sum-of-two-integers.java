class Solution {
    public int getSum(int a, int b) {
        while(b!=0){
            int temp=(a&b)<<1;          //storing and operatinon in temp for next iteration
            a=a^b;                      //exor operation basically is adding
            b=temp;                     //calling temp(add operation)
        }
        return a;
        
    }
}


//Space Complexity-O(1)
//Time Complexity-O(1)