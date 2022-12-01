const sum = (a: number, b: number): number => a + b;
const split = (separator: string) => (inp: string): string[] => inp.split(separator);

const getElves = (inp: string): number[] => inp
    .split('\n\n')
    .map(split('\n'))
    .map((lineGroup) => lineGroup
        .map(Number.parseInt)
        .reduce(sum, 0)
    );

export const part1 = (inp: string): number => {
  return Math.max(...getElves(inp));
};

export const part2 = (inp: string): number => {
  const elves = getElves(inp).sort();
  return elves
      .slice(elves.length - 3)
      .reduce(sum, 0);
};
