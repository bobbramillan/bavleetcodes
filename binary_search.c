/* 
    704
    [1,2,3,6,7,8] 
    target = 9
*/

int search(int* nums, int numsSize, int target) {
    int low = 0;
    int high = numsSize - 1;
    /* we do this because for array size 6, indexes are only 0-5 */

    while (low <= high) {
        int mid = low + (high - low) / 2; 
        /* we add low to make sure mid never gets smaller than low */

        if (nums[mid] == target) {
            return mid; 
        } else if (nums[mid] < target) {
            low = mid + 1;
            /* +1 prevents the loop from going on and on in the ex */
        } else {
            high = mid - 1;
        }
    }

    return -1; 
}
