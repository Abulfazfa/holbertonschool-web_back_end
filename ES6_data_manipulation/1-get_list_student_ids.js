// List students

const getListStudentIds = (stds) => {
  if (!Array.isArray(stds)) {
    return [];
  }
  const meids = stds.map((item) => item.id);
  return meids;
};
export default getListStudentIds;
