import java.util.*;

/*Code By Vedant Kokate
 * Reffered-Zhang Chen*/
public class Solution {

	static int ans = 0;
	private static Scanner sc;

	public static void dfs(int n, int start, boolean[] used, int[][] edges, LinkedList<Integer> sticks) {
		if (IsPolygon(sticks))
			ans++;

		for (int i = start; i < n; i++) {
			if (used[i])
				continue;

			used[i] = true;
			for (int j = i + 1; j < n; j++) {
				if (used[j] || edges[i][j] == 0)
					continue;
				used[j] = true;
				sticks.offerLast(edges[i][j]);

				dfs(n, i + 1, used, edges, sticks);
				sticks.pollLast();

				used[j] = false;
			}
			used[i] = false;
		}
	}

	public static boolean IsPolygon(LinkedList<Integer> sticks) {
		if (sticks.size() < 3)
			return false;
		int sum = 0, max = 0;
		for (int v : sticks) {
			sum += v;
			if (max < v)
				max = v;
		}
		return sum > 2 * max;
	}

	public static void main(String[] args) throws Exception {

		sc = new Scanner(System.in);
		int T = sc.nextInt();

		for (int t = 1; t <= T; t++) {
		    ans=0;
			int n = sc.nextInt();
			int[][] L = new int[n][n];
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					L[i][j] = sc.nextInt();
			boolean[] used = new boolean[n];
			dfs(n, 0, used, L, new LinkedList<>());

			System.out.println("Case #" + t + ": " + ans);
		}
	}
}