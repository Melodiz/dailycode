/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution
{
public:
    int guessNumber(int n)
    {
        return binarySearch(1, n);
    }
    int binarySearch(int left, int right)
    {
        int mid = left + (right - left) / 2;
        if (guess(mid) == 0)
        {
            return mid;
        }
        else if (guess(mid) == 1)
        {
            return binarySearch(mid + 1, right);
        }
        else
        {
            return binarySearch(left, mid - 1);
        }
    }
};