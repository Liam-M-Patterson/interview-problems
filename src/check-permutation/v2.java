public class v2{

    boolean checkPermutation(String s1, String s2){
        if(s1.length() != s2.length()) return false;
        int letters[] = new int[128];

        for(int i = 0; i < s1.length(); i ++){
            letters[s1.charAt(i)] ++;
        }  
        for(int i = 0; i < s1.length(); i ++){
            letters[s2.charAt(i)] --;
            if(letters[s2.charAt(i)] < 0) return false;
        }
            
            
        return true;
    }
    public static void main(String args[]){
        v2 test = new v2();
        System.out.println(test.checkPermutation("form", "from"));
        System.out.println(test.checkPermutation("form", "frome"));
        System.out.println(test.checkPermutation("faorm", "froma"));
        System.out.println(test.checkPermutation("Racecar", "racecar"));
        System.out.println(test.checkPermutation("", ""));
        System.out.println(test.checkPermutation("Racecar", "racecarsad"));
    }
}