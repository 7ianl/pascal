class Solution {
public:
    double fact(int n) {
        return std::tgamma(n+1);
    }
    int numTrees(int n) {
        return round(fact(n*2)/fact(n)/fact(n+1));
    }
};