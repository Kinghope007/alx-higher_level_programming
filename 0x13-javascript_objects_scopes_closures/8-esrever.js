exports.esrever = function (list) {
  // Create a new array to store the reversed elements
  const reversedList = [];
  // Iterate through the original list in reverse order and push each element to the new array
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
