// codingbat.com/prob/p117334

class stringSplosion {

	public static void main(String[] args) {
		stringSplosion("abc");
		assert stringSplosion("abc").equals("aababc") : "string not exploded";
	}

	public static String stringSplosion(String str) {

		String exploded_string = "";

		for (int i = 0; i < str.length(); i++) {
			for (int j = 0; j <= i; j++) {
				// System.out.println(str.charAt(j));
				exploded_string = exploded_string + str.charAt(j);

			}
		}

		System.out.println(exploded_string);
		return exploded_string;
	}

}

// !javac stringSplosion.java && java -ea stringSplosion
