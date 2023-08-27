def getMinLength(seq):
    # Write your code here
    res = ""
    while True:
        pos = set()
        for i  in range(len(seq)):
            if seq[i] == "A" and (i + 1) <= (len(seq) - 1) and seq[i + 1] == "B":
                pos.add(i)
                pos.add(i + 1)
                break
            elif seq[i] == "B" and (i + 1) <= (len(seq) - 1) and seq[i + 1] == "B":
                pos.add(i)
                pos.add(i + 1)
                break
        
        if len(pos) == 0:
            break
        
        for j in range(len(seq)):
            if j not in pos:
                res += seq[j]
        
        seq = res
    
    return len(res)

def substringRemoval(seq):
    while ("AB" in seq or "BB" in seq):
        if "AB" in seq:
            seq = seq.replace("AB", "", 1)
        elif "BB" in seq:
            seq = seq.replace("BB", "", 1)
    
    return len(seq)

print(substringRemoval("BABB"))