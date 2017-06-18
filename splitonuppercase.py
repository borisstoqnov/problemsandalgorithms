import re
x = "saveChangesInTheEditor"
listofs = [s for s in re.split("([A-Z][^A-Z]*)", x) if s]
print(listofs)
