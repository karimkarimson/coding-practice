function uniqueOccurrences(arr) {
    var numbers = {};
    arr.forEach((number) => {
        if (!numbers[number]) {
            numbers[number] = 1;
        } else {
            numbers[number] += 1;
        }
    });
    var occurences = Object.values(numbers);
    var unique = true;
    for (var i = 0; i < occurences.length; i++) {
        let testvalue = occurences[i];
        for (let j = 0; j < occurences.length; j++) {
            if (j === i) {
                null;
            } else {
                if (occurences[i] === occurences[j]) {
                    unique = false;
                };
            };
        }
    }
    return unique;
};