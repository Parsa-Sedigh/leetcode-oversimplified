/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function(target, position, speed) {
    const arr = []; // position and speed combined
    const fleets = [];

    position.forEach((p, i) => {
        arr.push([p, speed[i]]);
    });

    arr.sort((a, b) => b[0] - a[0]);

    arr.forEach(([pos, speed]) => {
        const time = (target - pos) / speed;
        fleets.push((target - pos) / speed);

        if (fleets.length >= 2 && fleets[fleets.length - 2] >= time) {
            fleets.pop();
        }
    });

    return fleets.length;
};