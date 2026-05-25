class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> result(n, 0);
        // Monotonic stack: 
        stack<int> s;
        // start from temp end, so aas to keep future values as reference. store index in stack so as to/
        // give differe3nce between the days noted as index. 
        // if stack empty, add 0 as no biggger temp exist. 
        // if stack non empty, checkwith top values, com[are and proceed. ]
        // proceed: pop if current top is les than value, move until you find higher value, compare and add current value;
        for(int i = n-1; i>=0; --i){
            while(!s.empty() && temperatures[i] >= temperatures[s.top()]){
                s.pop();
            }
            if(!s.empty()){
                result[i] = s.top() - i;
            }
            s.push(i);

        }
        return result;
    }
};