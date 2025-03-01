# 1.Create an empty tuple
# 2.Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# 3.Join brothers and sisters tuples and assign it to siblings
# 4.How many siblings do you have?
# 5.Modify the siblings tuple and add the name of your father and mother and assign it to family_members



emptyTuple = ()
sis_Tuple = ('sister1', 'sister2', 'sister3', 'sister4')
bro_Tuple = ('brother1', 'brother2', 'brother3', 'brother4')
siblings = sis_Tuple + bro_Tuple
print(siblings)
print(len(siblings))
family_members = ('father', 'mother') + siblings
print(family_members)

#Unpack siblings and parents from family_members
# print(family_members[0:2])
# print(family_members[2:])
father, mother, *siblingss = family_members
print(father)
print(mother)
print(siblings)
