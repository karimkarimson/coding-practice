let asteroidArray1 = [5, 10, -5];
let asteroidArray2 = [8, -8];
let asteroidArray3 = [10, 2, -5];

function checkCollision(resArray, asteroid) {
    if(Math.abs(resArray[resArray.length -1]) < Math.abs(asteroid)) {
        resArray.pop();
        checkCollision(resArray, asteroid);
    } else if(Math.abs(resArray[resArray.length -1]) === Math.abs(asteroid)) {
        resArray.pop();
        return resArray;
    } else {
        return resArray;
    }
}

var result = [];
function asteroidCollision(asteroids) {
    result = [];
    result.push(asteroids[0]);
    for(let i = 1; i < asteroids.length; i++) {
        if((asteroids[i] < 0 && result[result.length -1] < 0) || (asteroids[i] > 0 && result[result.length -1] > 0)) {
            result.push(asteroids[i]);
        } else {
            checkCollision(result, asteroids[i]);
        }
    };
    return result;
};

asteroidCollision(asteroidArray2);