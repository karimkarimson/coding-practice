var largestAltitude = function(gain) {
    let highest = 0;
    let heigth = 0;
    gain.forEach((diff) => {
        heigth += diff;
        (heigth > highest) ? highest = heigth : null;
    });
    return highest;
};