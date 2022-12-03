import * as utils from "../utils.js";

const getElves = (): number[] => utils.readInputFile(1, "input.txt")
  .split("\n\n")
  .map(utils.split("\n"))
  .map((lineGroup) => lineGroup
    .map(Number.parseInt)
    .reduce(utils.sum, 0)
  );

export const part1 = (): number => {
  return Math.max(...getElves());
};

export const part2 = (): number => {
  const elves = getElves();
  return elves
    .sort()
    .slice(elves.length - 3)
    .reduce(utils.sum, 0);
};

console.log(part1());
console.log(part2());
