class Solution:
    def groupAnagrams(self, strs):
        
        #convert a dictionary into a sorted, hashable tuple
        def getHash(d):
             return tuple(sorted(d.items()))
        
        #array to hold array of all grouped words
        res = []
        #hashmap containing the index in res, for that anagram type
        anagrams = {}
        #pointer to current index
        i = 0
    
        for word in strs:
            
            #tally up occurences of each letter in the word
            freqs = {}    
            for c in word:
                if c in freqs:
                    freqs[c] += 1
                else:
                    freqs[c] = 1
            
            #using the hash of the letter frequencies, get a hashable value
            #if that frequency hash has already occured, append curr word to that anagram list in res
            if getHash(freqs) in anagrams:
                index = anagrams[getHash(freqs)]
                res[index].append(word)
                
            #make new array for that anagram type
            else:
                anagrams[getHash(freqs)] = i
                res.append([word])
                i += 1
                
        return res
                