const regionsBySlashes = require('./regionsCutBySlashes'); // Adjust the path as needed

describe('regionsBySlashes', () => {
  test('Example 1: [" /","/ "]', () => {
    expect(regionsBySlashes([" /","/ "])).toBe(2);
  });

  test('Example 2: [" "," "]', () => {
    expect(regionsBySlashes([" "," "])).toBe(1);
  });

  test('Example 3: ["\\/","/\\"]', () => {
    expect(regionsBySlashes(["\\/","/\\"])).toBe(4);
  });

  test('Example 4: ["/\\","\\/"]', () => {
    expect(regionsBySlashes(["/\\","\\/"])).toBe(5);
  });

  test('Single slash: ["/"]', () => {
    expect(regionsBySlashes(["/"])).toBe(2);
  });

  test('Empty grid: [" "]', () => {
    expect(regionsBySlashes([" "])).toBe(1);
  });

});
