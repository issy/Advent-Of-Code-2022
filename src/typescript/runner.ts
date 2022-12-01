import * as fs from "fs";

console.log('running');
const args = process.argv.slice(2);
const dayNumber = args[0];
import(`./day_${dayNumber}/index`).then(({ part1, part2 }) => {
  const input = fs.readFileSync(`../../common/day_${dayNumber}/input.txt`);

  const result1 = part1(input);
  console.log('part 1 result:', result1);

  const result2 = part2(input);
  console.log('part 2 result:', result2);
});
