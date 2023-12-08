with open("data.txt") as data:
    
    lines = data.readlines();
    
    seeds = list(map(lambda x: int(x), lines[0][6:].split()))
    inputs = []
    for i in range(0,len(seeds),2):
        inputs.append((seeds[i], seeds[i+1]))

    def transform(rule, inp): 
        des_start, src_start, range_len = rule
        inp_start, inp_range_len = inp
        
        if inp_start + inp_range_len <= src_start:
            return [(inp_start, inp_range_len)], [],[]
        
        if inp_start >= src_start + range_len:
            return [],[],[(inp_start, inp_range_len)]

        src_end = src_start + range_len - 1
        before_count = src_start - min(inp_start, src_start) # either 0 or count between src_start and inp_start
        after_count = max(src_end, inp_start+inp_range_len) - src_end
        within_count = inp_range_len - before_count - after_count
        
        before = []
        within = []
        after = []
        
        if before_count != 0:
            before = [(inp_start, before_count)]
        if after_count != 0:
            after = [(src_end+1, after_count)]
        
        if inp_start <= src_start:
            within_start = des_start
        else:
            within_start = inp_start - src_start + des_start
        
        within = [(within_start, within_count)]
        return before, within, after
        
    new_inputs = []
    for line in lines[1:]:
        if line == "\n":
            inputs = inputs + new_inputs
            new_inputs = []
        if line[0].isdigit():
            dest_r_start, source_r_start, range_len = list(map(lambda x: int(x),line.split()))
            curr_len = len(inputs)
            for _ in range(curr_len):
                before, within, after = transform((dest_r_start, source_r_start, range_len), inputs.pop(0))
                inputs += before
                inputs += after
                new_inputs += within
                
    full_l = inputs+new_inputs
    m = full_l[0][0] 
    for i in full_l:
        m = min(i[0], m)
    print(m)


                
            

            
        
        
        
    
    
   