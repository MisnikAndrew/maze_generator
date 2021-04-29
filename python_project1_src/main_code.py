from random import randrange

a1 = input().split()
a = int(a1[0])
b = int(a1[1])
n = a * b
p = [0 for i in range(0, n)]
def get_num(x, y):
    return x * b + y; 
def get_pair(num):
    return (num // b, num % b); 

def dsu_get (v) :
	if (v == p[v]):
	    return v;
	else : 
	    p[v] = dsu_get(p[v]);
	    return p[v];
	    
def dsu_unite (a, b): 
	a = dsu_get (a);
	b = dsu_get (b);
	if (randrange(2)):
		tmp = a;
		a = b;
		b = tmp; 
	if (a != b):
		p[a] = b;



g = [[] for i in range(0, n)]
find = {}
for i in range(-1, a + 1):
    for j in range(-1, b + 1):
        find[(get_num(i, j), get_num(i - 1, j))] = -1
        find[(get_num(i, j), get_num(i + 1, j))] = -1
        find[(get_num(i, j), get_num(i, j - 1))] = -1
        find[(get_num(i, j), get_num(i, j + 1))] = -1
for i in range(0, a):
    for j in range(0, b):
        if (i > 0):
            q1 = get_num(i, j); 
            q2 = get_num(i - 1, j);
            
            if (find[(q1, q2)] == -1): 
                find[(q1, q2)]  =randrange(100);
                find[(q2, q1)] = find[(q1, q2)];
                g[q1].append((q2, find[(q1, q2)]));
            else: 
                g[q1].append((q2, find[(q1, q2)]));
        
        
        if (i + 1 < a):
            q1 = get_num(i, j); 
            q2 = get_num(i + 1, j);
            
            if (find[(q1, q2)] == -1): 
                find[(q1, q2)] = randrange(100);
                find[(q2, q1)] = find[(q1, q2)];
                g[q1].append((q2, find[(q1, q2)]));
            else: 
                g[q1].append((q2, find[(q1, q2)]));
                
        if (j > 0):
            q1 = get_num(i, j); 
            q2 = get_num(i, j - 1);
            
            if (find[(q1, q2)] == -1): 
                find[(q1, q2)] = randrange(100);
                find[(q2, q1)] = find[(q1, q2)];
                g[q1].append((q2, find[(q1, q2)]));
            else: 
                g[q1].append((q2, find[(q1, q2)]));
                
                
        if (j + 1 < b):
            q1 = get_num(i, j); 
            q2 = get_num(i, j + 1);
            
            if (find[(q1, q2)] == -1): 
                find[(q1, q2)] = randrange(100);
                find[(q2, q1)] = find[(q1, q2)];
                g[q1].append((q2, find[(q1, q2)]));
            else: 
                g[q1].append((q2, find[(q1, q2)]));


        
m = 0;
g1 = []; 

for i in range(0, n):
    for j in g[i]:
        if (i < j[0]):
            g1.append((j[1], (i, j[0])))

cost = 0;
res = []; 
m=len(g1); 
g1.sort();  

for i in range(0, n):
	p[i] = i;
for i in range(0, m):
	a1 = g1[i][1][0];
	b1 = g1[i][1][1];
	l = g1[i][0];
	if (dsu_get(a1) != dsu_get(b1)):
		cost += l;
		res.append (g1[i][1]);
		dsu_unite (a1, b1);
print(); 
print("tree size: " + str(a * b - 1));
print("obstacles: " + str(a * b - a - b + 1)); 

locked = {};
for i in range(-1, a + 1):
    for j in range(-1, b + 1):
        locked[((i, j), (i + 1, j))] = 1; 
        locked[((i + 1, j), (i, j))] = 1;
        locked[((i, j), (i - 1, j))] = 1; 
        locked[((i - 1, j), (i, j))] = 1;
        locked[((i, j), (i, j + 1))] = 1; 
        locked[((i, j + 1), (i, j))] = 1;
        locked[((i, j), (i, j - 1))] = 1; 
        locked[((i, j - 1), (i, j))] = 1;

for i in range(0, len(res)):
    c1 = get_pair(res[i][0]);
    c2 = get_pair(res[i][1]);
    locked[(c1, c2)] = 0; 
    locked[(c2, c1)] = 0; 


symbols = [" ", "╴", "╷", "┐", "╶", "─", "┌", "┬", "╵", "┘", "│", "┤", "└", "┴", "├", "┼"];
for i in range(0, a + 1):
    to_print = "";
    for j in range(0, b + 1):
        c1 = locked[((i - 1, j - 1), (i - 1, j))]; # U
        c2 = locked[((i - 1, j), (i, j))]; # R
        c3 = locked[((i, j), (i, j - 1))]; # D
        c4 = locked[((i, j - 1), (i - 1, j - 1))]; # L
        if (i == 0):
            c1 = 0;
        if (j == b):
            c2 = 0;
        if (i == a):
            c3 = 0; 
        if (j == 0):
            c4 = 0;
        num=8 * c1 + 4 * c2  +2 * c3 + c4; 
        if (j > 0):
            if (locked[((i - 1, j - 1), (i, j - 1))]):
                to_print += "─"; 
            else:
                to_print += " ";
        
        to_print += symbols[num]; 
    print(to_print); 
print("Try to copy to Notepad"); 
