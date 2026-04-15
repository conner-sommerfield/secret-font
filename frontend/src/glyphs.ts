const ASCII_a = "a".charCodeAt(0);
const ASCII_z = "z".charCodeAt(0);

const range = (start: number, end: number): string[] =>
  Array.from({ length: end - start + 1 }, (_, i) =>
    String.fromCharCode(start + i)
  );

export const glyphs: string[] = [
  ...range(ASCII_a, ASCII_z),
];
