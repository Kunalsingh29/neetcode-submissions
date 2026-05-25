class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for(int i = 0; i<9; i++){
            unordered_map<char, int> row_map;
            for(int j = 0; j<9; j++){
                if(board[i][j] == '.') continue;
                else{
                    row_map[board[i][j]]++;
                    if(row_map[board[i][j]] > 1){
                        return false;
                    }
                }
            }
        }
        for(int j = 0; j<9; j++){
            unordered_map<char, int> column_map;
            for(int i = 0; i<9; i++){
                if(board[i][j] == '.') continue;
                else{
                    column_map[board[i][j]]++;
                    if(column_map[board[i][j]] > 1){
                        return false;
                    }
                }
            }
        }

        for(int i = 0; i<9; i+=3){
            
            for(int j = 0; j<9; j+=3){
                unordered_map<char, int> box_map;
                for(int k = i; k<i+3; k++){
                   //unordered_map<char, int> box_map;
                    for(int h = j; h<j+3; h++){
                        if(board[k][h] == '.') continue;
                        else{
                            box_map[board[k][h]]++;
                            if(box_map[board[k][h]] > 1){
                            return false;
                            }
                        }
                    }
                }
            }
        }
        // for sub-box;

        return true;
        
    }
};