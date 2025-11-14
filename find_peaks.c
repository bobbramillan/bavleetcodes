#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *indices;
    int *values;
    int count;
} PeaksResult;

PeaksResult find_peaks(int nums[], int numsSize) {
    PeaksResult r;
    r.indices = malloc(numsSize * sizeof(int));
    r.values = malloc(numsSize * sizeof(int));
    r.count = 0;

    int i = 1;
    while (i < numsSize - 1) {
        if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) {
            r.indices[r.count] = i;
            r.values[r.count] = nums[i];
            r.count++;
            i += 2;
        } else {
            i += 1;
        }
    }

    return r;
}