# 6. Union of Two Sorted Arrays
## Easy 
<div class="problem-statement">
                <p><a onclick="gtagHelperFunction('clickopen','salesevent_gsc_problemspage_promobanner')" href="https://practice.geeksforgeeks.org/summer-carnival-2022?utm_source=practiceproblems&amp;utm_medium=problemspromobanner&amp;utm_campaign=gsc22" target="_blank"></a></p><div style="margin: 14px 0px !important;" class="row"><a onclick="gtagHelperFunction('clickopen','salesevent_gsc_problemspage_promobanner')" href="https://practice.geeksforgeeks.org/summer-carnival-2022?utm_source=practiceproblems&amp;utm_medium=problemspromobanner&amp;utm_campaign=gsc22" target="_blank">             <div class="col-md-12" style="cursor:pointer;background: #EFF8F3 0% 0% no-repeat padding-box; display: flex; align-items: center; position:                 relative; padding: 1.5%; border-radius: 10px; display: inline-block; text-align: center; font-weight: 600; color: #333"> <img src="https://media.geeksforgeeks.org/img-practice/gcs2022thumbnail-1649059370.png" alt="Lamp" width="46" height="40" style="background: transparent 0% 0% no-repeat padding-box;opacity: 1; margin: 0 16px;" class="img-responsive"> Geeks Summer Carnival is LIVE NOW &nbsp; <i class="fa fa-external-link" aria-hidden="true"></i> </div></a></div><p><span style="font-size:18px">Union of two arrays can be defined as the common and distinct elements in the two arrays.<br>
Given two sorted arrays of size <strong>n</strong> and <strong>m</strong>&nbsp;respectively, find their union.</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: 
n = 5, arr1[] = {1, 2, 3, 4, 5}  
m = 3, arr2 [] = {1, 2, 3}
<strong>Output</strong>: 1 2 3 4 5
<strong>Explanation</strong>: Distinct elements including 
both the arrays are: 1 2 3 4 5.</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: 
n = 5, arr1[] = {2, 2, 3, 4, 5}  
m = 5, arr2[] = {1, 1, 2, 3, 4}
<strong>Output</strong>: 1 2 3 4 5
<strong>Explanation</strong>: Distinct elements including 
both the arrays are: 1 2 3 4 5.</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 3:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>:
n = 5, arr1[] = {1, 1, 1, 1, 1}
m = 5, arr2[] = {2, 2, 2, 2, 2}
<strong>Output</strong>: 1 2
<strong>Explanation</strong>: Distinct elements including 
both the arrays are: 1 2.</span></pre>

<p><br>
<strong><span style="font-size:18px">Your Task:&nbsp;</span></strong><br>
<span style="font-size:18px">You do not need to read input or print anything. Complete the <strong>function findUnion()&nbsp;</strong>that takes two arrays <strong>arr1[]</strong>, <strong>arr2[],</strong> and their size <strong>n&nbsp;and m&nbsp;</strong>as input parameters and returns a list containing the&nbsp;<strong>union of the two arrays</strong>.&nbsp;</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(n+m).<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(n+m).</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= n, m&nbsp;&lt;= 10<sup>5</sup><br>
1 &lt;= arr[i], brr[i] &lt;= 10<sup>6</sup></span></p>
 <p></p>
            </div>