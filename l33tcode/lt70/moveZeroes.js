function moveZeroes(nums) {
    for(var i = nums.length -1; i >= 0; i--) {
        if(nums[i] === 0) {
            nums.splice(i, 1);
            nums.push(0);
        }
    };
    console.log(nums);
    return nums;
}

var array1= [0,1,0,3,12];
moveZeroes(array1);