// codingbat.com/prob/p189576
import java.util.*;

class maxSpan {

	public static void main(String[] args) {
		int max = maxSpan(new int[]{1,2,1,1,3});
		assert max == 4;
	}

	public static Map<Integer, List<Integer>> mapSpan(int[] nums) {
		Map<Integer, List<Integer>> m = new HashMap<>();
		for (int i = 0; i < nums.length; i++) {
			int key = nums[i];
			if (m.get(key) == null) {
				m.put(key, new ArrayList<Integer>(Arrays.asList(i)));
			} else {
				m.get(key).add(i);
			}
			System.out.println(m);
		}
		return m;

	}

	public static int maxSpan(int[] nums) {
		// run through the array and map the index of where a number is found into a dictionary
		// e.g. [1, 2, 1, 1, 3]
		// returns { 1: [0, 2, 3], 2: [1], 3: [4] }
		// for each key, find the difference between positions, then return the biggest difference + 1
		Map<Integer, List<Integer>> m = mapSpan(new int[]{1,2,1,1,3});
		int max = 0;
		for (List v: m.values()) {
			int first = (int)v.get(0);
			int last = (int)v.get(v.size() - 1);
			int span = last - first + 1;
			if (span > max) {
				max = span;
			}
		}
		// System.out.println(max);
		return max; 

	}

}

// !javac maxSpan.java && java -ea maxSpan
