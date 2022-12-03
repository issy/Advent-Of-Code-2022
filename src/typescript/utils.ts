import * as fs from 'fs';

export const sum = (a: number, b: number): number => a + b;

export const split = (separator: string) => (inp: string): string[] => inp.split(separator);

export const readInputFile = (day: number, filename: string): string => {
    return fs.readFileSync(`../../common/day_${day}/${filename}`, 'utf-8');
};
