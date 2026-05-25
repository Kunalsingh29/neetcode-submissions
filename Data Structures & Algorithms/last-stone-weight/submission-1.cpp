class Solution {
public:
    priority_queue<int> maxQ;
    int lastStoneWeight(vector<int>& stones) {
        for(int num:stones){
            maxQ.push(num);
        }
        while(maxQ.size()>1){
            //if(maxQ.size() ==1) return maxQ.top();
            int stone1 = maxQ.top();
            maxQ.pop();
            int stone2 = maxQ.top();
            maxQ.pop();
            if(stone1!=stone2){
                maxQ.push(abs(stone1-stone2));

            }
            //if (maxQ.size() == 0) return 0;


        }
        return maxQ.empty() ? 0 : maxQ.top();
        
    }
};