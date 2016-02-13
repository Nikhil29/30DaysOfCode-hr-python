//Write your code here
class Calculator: public AdvancedArithmetic{
    int divisorSum(int n){
        int i,ans=0;
        for(i=1;i<=n;i++){
            if(n%i==0){
                ans=ans+i;
            }
        }
        return ans;
    }
};
