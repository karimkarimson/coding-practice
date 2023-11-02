function biggestAverage (nums, k) {
    var biggestSum = -Infinity;
    var sum = 0;
    var j = 0;
    // Iterate through the array
    for(let i = 0; i < nums.length; i++) {
        sum += nums[i];
        // if the window the size of k is reached start checking for the biggest sum
        if((i-j+1) === k ) {
            if (sum > biggestSum) {
                biggestSum = sum;
            }
            // remove the first element of the window and increment j to the new/next first element 
            sum -= nums[j];
            j++;
        }
    }
    return (biggestSum/k);
};