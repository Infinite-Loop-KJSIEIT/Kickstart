import java.util.Scanner;

public class Solution {
	private static final long MOD = 1000000007L;

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int T = s.nextInt();
		for (int t = 1; t <= T; t++) {
			int n = s.nextInt();
			int k = s.nextInt();
			long x = s.nextLong(), y = s.nextLong(), c = s.nextLong(), d = s.nextLong(), e1 = s.nextLong(),
					e2 = s.nextLong(), f = s.nextLong();
			;

			long a[] = new long[n];
			for (int i = 0; i < n; i++) {
				a[i] = (x + y) % f;
				long nx = (c * x + d * y + e1) % f;
				long ny = (d * x + c * y + e2) % f;
				x = nx;
				y = ny;
			}

			long sum = 0, ans = 0;
			for (int p = 1; p <= n; p++) {
				sum += sum(p, k);
				sum %= MOD;

				ans += (n - p + 1) % MOD * a[p - 1] % MOD * sum % MOD;
				ans %= MOD;
				// System.out.println((n-p+1)+" "+a[p-1]+" "+sum+" "+ans);
			}
			System.out.println("Case #" + t + ": " + ans);
		}
	}

	private static long sum(int p, int k) {
		if (p == 1)
			return k;
		return ((p % MOD * (quickpow(p, k) - 1) % MOD) * quickpow(p - 1, MOD - 2)) % MOD;
	}

	private static long quickpow(long x, long n) {
		if (n == 0)
			return 1;
		if (n == 1)
			return x;
		long v = quickpow(x, n / 2);
		return v * v % MOD * (n % 2 == 1 ? x : 1) % MOD;
	}
}