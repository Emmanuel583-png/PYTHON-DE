is_active = True
is_admin = False

checking_and= is_active and is_admin #since both arent true its gonna return false
checking_or = is_active or is_admin #since the is only checks for one positive condition its gonna return as true
checking_not = not is_admin #reverses the original bool so true becomes false and false becomes true

print(checking_or)
print(checking_and)
print(checking_not)