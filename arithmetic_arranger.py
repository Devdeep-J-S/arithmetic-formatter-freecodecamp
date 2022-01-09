# Done by Devdeep J S
# arithmetic formatter 
def arithmetic_arranger(problems,value=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    op1 = ""
    op2 = ""
    op3 = ""
    ans = ""
    for i in problems:
        l = i.split()
        # special cases
        if l[1] != "+" and l[1] != "-":
            return "Error: Operator must be '+' or '-'."
        try:
            x = int(l[0])
            y = int(l[2])
        except:
            return "Error: Numbers must only contain digits."
        if x > 9999 or y > 9999:
            return "Error: Numbers cannot be more than four digits."
        if (len(l[0])>len(l[2])):
            num = 1 + len(l[0]) - len(l[2])
        else:
            num= 1 
        line2= l[1] + " "*num + l[2] + "    "        
        op2 = op2 + line2
        op3 = op3 + "-"*(len(line2)-4)+"    "
        op1 = op1 + " "*(len(line2)-4-len(l[0])) + l[0] + "    "
        # print((len(line2)-4-len(l[0])))
        if value:
            if (l[1]=='+'):
                s =  str (int(l[0]) + int(l[2]))
                ans = ans  + " "*(len(line2)-4-len(s)) + s + "    "
            if (l[1]=='-'):
                s =  str (int(l[0]) - int(l[2]))
                ans = ans  + " "*(len(line2)-4-len(s)) + s + "    "
    if value:            
        return op1.rstrip() + "\n" + op2.rstrip() + "\n" + op3.rstrip() + "\n" + ans.rstrip()
    else:
        return  op1.rstrip() + "\n" + op2.rstrip() + "\n" + op3.rstrip()  