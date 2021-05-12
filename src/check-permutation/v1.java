public class v1{

    boolean checkPermutation(String s1, String s2){
        if(s1.length() != s2.length()) return false;
        int p1[] = new int[128];
        int p2[] = new int[128];

        for(int i = 0; i < s1.length(); i ++){
            p1[s1.charAt(i)] ++;
            p2[s2.charAt(i)] ++;
        }  
        for(int i = 0; i < 128; i ++)
            if(p1[i] != p2[i]) 
                return false;
        return true;
    }
    public static void main(String args[]){
        v1 test = new v1();
        System.out.println(test.checkPermutation("form", "from"));
        System.out.println(test.checkPermutation("form", "frome"));
        System.out.println(test.checkPermutation("faorm", "froma"));
    }
}