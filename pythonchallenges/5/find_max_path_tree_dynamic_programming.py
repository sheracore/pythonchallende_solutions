if n == 0, return 0

OPT(1)=max(v1​+OPT(next[1]),OPT(2))



job = sorted(job, key = lambda j: j.start) 
    
    	# Create an array to store solutions of subproblems. table[i] 
    	# stores the profit for jobs till arr[i] (including arr[i]) 
    	n = len(job) 
    	table = [0 for _ in range(n)] 
    
    	table[0] = job[0].profit; 
    
    	# Fill entries in table[] using recursive property 
    	for i in range(1, n): 
    
    		# Find profit including the current job 
    		inclProf = job[i].profit 
    		l = binarySearch(job, i) 
    		if (l != -1): 
    			inclProf += table[l]; 
    
    		# Store maximum of including and excluding 
    		table[i] = max(inclProf, table[i - 1]) 
    
    	return table[n-1] 
