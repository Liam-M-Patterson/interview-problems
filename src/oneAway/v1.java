public class v1{
    boolean oneDiff(String s1, String s2){
        boolean oneDifferent = false;
        for(int i = 0; i < s1.length(); i ++){
            if(s1.charAt(i) == s2.charAt(i)){
                if(oneDifferent) return false;
                oneDifferent = true;
            }
        }
        return true;
    }

    boolean oneAway(String s1, String s2){
        int l1 = s1.length();
        int l2 = s2.length();

        if(l1 == l2) return oneDiff(s1, s2);
        if(l2 < l1) return oneAway(s1, s2);

        boolean isDifferent = false;
        l1 = 0; l2 = 0;
        while(l1 < s1.length()){
            if(s1.charAt(l1) == s2.charAt(l2)){
                l1 ++;
                l2 ++;
            } else {
                if (isDifferent) return false;
                isDifferent = true;
                l2 ++;
             }
        }
        return true;
    }

    public static void main(String args[]){
        System.out.println("hello world");
        v1 obj = new v1();
        System.out.println(obj.oneAway("liam", "lia"));
    }
}