int search(int* nums, int numsSize, int target) {
    int len = numsSize;
    int i = len / 2;

    /*this is not binary search(704) it's a linear search version aka runs O(n) time not O(lgn)*/

    /*loop goes while i is greater than or equal to 0, 
    AND i doesn't exceed the length of array (nums), 
    AND index i of array (nums) is not the target */
    while (i >= 0 && i < len && nums[i] != target) {
        if (nums[i] > target) {
            i--;
        } else if (nums[i] < target) {
            i++;
        } else if (nums[i] == target) {
            return i;
        }
    }

    if (i >= 0 && i < len && nums[i] == target)
        return i;

    return -1;
}