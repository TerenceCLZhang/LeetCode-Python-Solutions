/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function (word1, word2) {
  const l1 = word1.length;
  const l2 = word2.length;
  const maxLength = Math.max(l1, l2);
  let ans = "";

  for (let i = 0; i < maxLength; i++) {
    if (i < l1) {
      ans += word1[i];
    }
    if (i < l2) {
      ans += word2[i];
    }
  }

  return ans;
};

// Time: O(n)
// Space: O(1)
