// Code by Vedant Kokate
//Code refered-cerberus97

import java.util.*;

public class Solution {
   
	public static void main(String[] args) {
    	Scanner sc=new Scanner(System.in);
    	int a[]=new int[25];
    	int b[]=new int[25];
    	int T=sc.nextInt();
    	for(int t=1;t<=T;t++) {
    		//input
    		int n=sc.nextInt();
    		int h=sc.nextInt();
    		for(int i=0;i<n;i++)a[i]=sc.nextInt();
    		for(int i=0;i<n;i++)b[i]=sc.nextInt();
    		//checking number of ways for b
    		int tot=1<<n;
    		int ways[]=new int[tot];
    		for(int mask=0;mask<tot;++mask) {
    			long sum=0;
    			for(int i=0;i<n;i++) {
    				if((mask&(1<<i))==0)
    					sum+=b[i];
    			}
    			if (sum>=h)
    				ways[mask]=1;
       		}
    		//check all the ways for a particular permutation
    		for (int i = 0; i < n; ++i) {
    			for (int mask = 0; mask < tot; ++mask) {
    				
    				if ((mask & (1 << i))>=1) {
    				
    					ways[mask] += ways[mask ^ (1 << i)];
    				}
    			}
    		}
    	
    		long ans=0;
    		for (int mask = 0; mask < tot; ++mask) {
    			long sum = 0;
    			for (int i = 0; i < n; ++i) {
    				if ((mask & (1 << i))>=1) {
    					
    					sum += a[i];
    				}
    			}
    			if (sum >= h) {
    				/*if possible for a then all the possible ways in which b might 
    				 * also succeed
    				 * */
    				 
    				ans += ways[mask];
    			}
    		}
    		System.out.println("Case #"+t+": "+ans);
    	}
    }
}