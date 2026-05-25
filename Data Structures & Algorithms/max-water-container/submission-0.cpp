class Solution {
public:
    int maxArea(vector<int>& height) {
        // int
        // height[i].
        // left and right, while left is less than right?
        // increment left and right. 
        int n = height.size();
        int left = 0, right = n-1;
        int maxArea = 0;
        while(left<right){
            int width = right-left;

            int h = min(height[left], height[right]);
            int area = width*h;
            maxArea = max(maxArea, area);
            
            if(height[left]< height[right]){
                left++;
            }
            else{
                right--;
            }

        
        }
        return maxArea;
    }
};