const getElves = (inp: string): number[] => inp
    .split('\n\n')
    .map((lines) => lines.split('\n'))
    .map((lineGroup) => lineGroup
        .map(Number.parseInt)
        .reduce((a, b) => a + b, 0)
    );

export const part1 = (inp: string): number => {
  return Math.max(...getElves(inp));
};

export const part2 = (inp: string): number => {
  const elves = getElves(inp).sort();
  return elves
      .slice(elves.length - 3)
      .reduce((a, b) => a + b, 0);
};
