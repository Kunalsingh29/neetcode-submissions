class KthLargest {
public:
    // min heap to store k largest elements. 
    priority_queue<int, vector<int>, greater<int>> minQ; // O(k) for k elements. 
    
    int max;
    KthLargest(int k, vector<int>& nums) {
        max = k;
        // insert array, to the element. 
        for(int num: nums){
            minQ.push(num);
            if(minQ.size()>max) minQ.pop();
        } 
        // T.C: O(n) to heapify the array.  
    }
    
    int add(int val) {
        // add next mew val to the min heap to update Q.
        //update to keep only k elements. 
        // push operation goes into with TC o(logk)
        minQ.push(val);
        if(minQ.size()>max) minQ.pop();
        return minQ.top(); // O(1) 
        
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */