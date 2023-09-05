

def copy_odd_lines(from_file,to_file):
    with open(from_file,'r') as f1, open(to_file,'w') as f2:
        lines = f1.readlines()
        odd_line = [line for i,line in enumerate(lines) if i%2!=0]
        f2.writelines(odd_line)
        print("Copy Successful")
from_file='input.txt'
to_file='output.txt'
copy_odd_lines(from_file,to_file)

from_file = "input.txt"
to_file = "output.txt"
copy(from_file, to_file)

input.txt:            
hello 
world 
again
python snake 
zebra

output.txt:
world 
python snake 

