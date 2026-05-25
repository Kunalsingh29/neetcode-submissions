class Solution {
public:
    bool isValid(string s) {
        stack<char> stak;
        for(char cur:s){
            if(!stak.empty()){
                char last = stak.top();
                if(isPair(last, cur)){
                    stak.pop();
                    continue;

                }
            }
            stak.push(cur);
        }
        return stak.empty();
    
    }
private:
    bool isPair(char last, char curr){
        return(( last == '(' && curr == ')')
                ||( last == '{' && curr == '}')
                ||( last == '[' && curr == ']'));
    }

};