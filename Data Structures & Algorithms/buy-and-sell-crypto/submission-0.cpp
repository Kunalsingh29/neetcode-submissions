class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int size = prices.size();
        int maxProfit = 0;
        int left = 0; //right = 0;
        for(int right = 1; right<size; right++){
            int profit = 0;
            if(prices[right] <= prices[left]){
                left = right;
            }
            else{
                maxProfit = max(maxProfit, prices[right] - prices[left]);
                cout<<profit<<endl;
            }

        }
        return maxProfit;
    }
      
};