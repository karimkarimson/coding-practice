function reverseWords(s) {
    var splitted = s.trim().split(" ");
    var result = [];
    splitted.forEach((word) => {
        if(word != ' ' && word != '') {
            result.unshift(word);
        };
    });
    result.join(" ");
    return result;
};

var sentence = "This is a very long sentence";
var sentence2 = "a good   example"
console.log(reverseWords(sentence2));