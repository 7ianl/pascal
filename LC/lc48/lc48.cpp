class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int l = matrix.size();
        for (int x = 0; x < l/2; x++) {
            for (int y = 0; y < l/2+l%2; y++) {
                swap(matrix[x][y], matrix[l-1-y][x]);
                swap(matrix[l-1-y][x], matrix[l-1-x][l-1-y]);
                swap(matrix[l-1-x][l-1-y], matrix[y][l-1-x]);
            }
        }
    }
};