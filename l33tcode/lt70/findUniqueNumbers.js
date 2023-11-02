var findDifference = function(nums1, nums2) {
    let result = [[],[]];
    nums1.forEach((number) => {
        if(!nums2.includes(number)) {
            (result[0].includes(number)) ? null : result[0].push(number);
        };
    });
    nums2.forEach((number) => {
        if(!nums1.includes(number)) {
            (result[1].includes(number)) ? null : result[1].push(number);
        };
    });
    return result;
};