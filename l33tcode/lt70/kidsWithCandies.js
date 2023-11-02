var kidsWithCandies = function(candies, extraCandies) {
    let result = [];
    for(let i=0; i < candies.length; i++) {
        var kidmitextrabonbons = candies[i] + extraCandies;
        var hatmeisste = true;
        candies.forEach((kid) => {
            (kid > kidmitextrabonbons) ? hatmeisste = false : null; 
        });
        result.push(hatmeisste);
    }
    return result;
};