class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // left = 0,0 right = m-1, n-1;
        // if i1>i2; vo1>vi2 for all j 
        // for same i, vj2>vj1, given j2>j1.
        int m = matrix.size();
        int n = matrix[0].size();
        //int row_mid , int col_mid;
        int top = 0, bottom = m-1;
        int left = 0, right = n-1;
        int row_mid = 0;
        while(top<=bottom){
            int _row_mid = top + (bottom - top)/2;
            if(matrix[_row_mid][n-1] == target || matrix[_row_mid][0] == target){
                return true;
            }
            else if(matrix[_row_mid][n-1] < target){
                top = _row_mid + 1;
            }
            else if(matrix[_row_mid][0] > target){
                bottom = _row_mid-1;
            }
            else{
                row_mid = _row_mid;
                break;
            }
            

        }
        while(left<=right){
            int col_mid = left + (right-left)/2;
            if(matrix[row_mid][col_mid] == target){
                return true;
            }
            else if(target<matrix[row_mid][col_mid]){
                right = col_mid - 1;
            }
            else{
                left = col_mid+1;
            }

        }

        return false;
        
    }
};