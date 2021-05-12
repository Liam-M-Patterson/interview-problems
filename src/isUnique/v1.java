package isUnique;

public class v1 {
	
	boolean isUnique(String str) {
		if(str.length() > 128) return false;
		boolean chars[] = new boolean[128];
		for(int i = 0; i < str.length(); i ++) {
			char ch = str.charAt(i);
			if(!chars[ch]) chars[ch] = true;
			else return false;
		}
		return true;
	}
	
	public static void main(String[] args) {
		v1 foo = new v1();
		
		System.out.println(foo.isUnique("Hello world!"));
		System.out.println(foo.isUnique("Liam"));
		System.out.println(foo.isUnique("Liam Patterson"));
		System.out.println(foo.isUnique("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+=[{]};:,<.>?|`~"));
	}
}
