public class Solution {
    public IList<string> WordBreak(string s, IList<string> wordDict) {
        
        List<List<string>> combos = new List<List<string>>();

        void DfsHelper(int l, int r, List<string> currentList) {
            while (r <= s.Length) {
                var word = s.Substring(l,r-l);
                if (wordDict.Contains(word)) {
                    var cloned = currentList.ToList();
                    cloned.Add(word);
                    if (r == s.Length) 
                        combos.Add(cloned);
                    DfsHelper(r, r+1, cloned);
                }
                r ++;
            }
        }

        DfsHelper(0, 0, new List<string>());
        var res = combos.ConvertAll(combo => String.Join(" ", combo));
        return res;
    }
}