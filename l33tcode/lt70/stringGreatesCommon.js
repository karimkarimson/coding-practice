var gcdOfStrings = function(str1, str2) {
    if(str1 + str2 !== str2 + str1) {
        return "";
    };
    var result = "";
    function gcd(x, y) {
        if(!y) {
            return x;
        }
        return gcd(y, x % y);
    }
    let l1 = str1.length;
    let l2 = str2.length;
    let gcdNumber = gcd(l1, l2);
    return str1.slice(0, gcdNumber);
};