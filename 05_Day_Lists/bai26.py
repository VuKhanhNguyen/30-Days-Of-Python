# 26. Join the following lists:

#     ```py
#     front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#     back_end = ['Node','Express', 'MongoDB']
#     ```

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

print(front_end + back_end)

full_stack = front_end + back_end
print(full_stack)

for i in full_stack:
    if "Redux" in i:
        Insertt = int(len(full_stack)/2)
        # full_stack = full_stack.append("Python", "SQL")
        full_stack.insert(Insertt+1,"Python")
        # break
        #print(full_stack)
        full_stack.insert(Insertt+2,"SQL")
        #print(full_stack)
        break       
print(full_stack)      
