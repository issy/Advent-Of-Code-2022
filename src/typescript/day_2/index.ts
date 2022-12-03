import * as utils from '../utils.js';

const convertToNumbers = ([enemyMove, myMove]: string[]): number[] => ['ABC'.indexOf(enemyMove), 'XYZ'.indexOf(myMove)];
const calculateScore = ([enemyMove, myMove]: number[]): number => (3 * (2 - (((enemyMove - myMove) + 4) % 3))) + myMove + 1;
const calculateMoveFromOutcome = ([enemyMove, desiredOutcome]: number[]) => [enemyMove, ((enemyMove - 1) + desiredOutcome) % 3];

export const part1 = (): number => {
  return utils.readInputFile(2, 'input.txt')
    .split('\n')
    .map(utils.split(' '))
    .map(convertToNumbers)
    .map(calculateScore)
    .reduce(utils.sum, 0);
};

export const part2 = (): number => {
  return utils.readInputFile(2, 'input.txt')
    .split('\n')
    .map(utils.split(' '))
    .map(convertToNumbers)
    .map(calculateMoveFromOutcome)
    .map(calculateScore)
    .reduce(utils.sum, 0);
};

console.log(part1());
console.log(part2());
