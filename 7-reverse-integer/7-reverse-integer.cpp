class Solution {
public:
    int reverse(int x) {
        long long int a = 0;
    long long int b = abs(x);
    while (b != 0)
    {
        a *= 10;
        a += (b%10);
        b /= 10;
    }
    
    if (x < 0)
        a *= -1;
    if (a > INT_MAX || a < INT_MIN)
        return 0;
    return a;
    }
};