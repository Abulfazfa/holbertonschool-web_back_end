export default function createIteratorObject(report) {
  const arr = [];
  Object.values(report.allEmployees).forEach((value) => arr.push(...value));
  return arr;
}
