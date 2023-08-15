#!/usr/bin/node
let number = 0;
/**
 * Logs a message to the console.
 * @param {String} item The message to be logged.
 */
exports.logMe = function (item) {
  console.log(number + ': ' + item);
  number++;
};
