function mergeAlt(word1, word2) {
    var i = 0;
    var resultstring ="";
    while(true){
        let char1 = word1.charAt(i);
        let char2 = word2.charAt(i);
        i++;
        console.log(char1, char2);
        if(char1 && char2) {
            resultstring += char1 + char2;
        } else if (char1) {
            resultstring += word1.substring(i-1);
            break;
        } else if (char2) {
            resultstring += word2.substring(i-1);
            break;
        } else {
            break;
        };
    };
    return resultstring;
};

console.log(mergeAlt("abcr", "def"));