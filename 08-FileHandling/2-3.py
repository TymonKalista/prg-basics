###
# Makes a copy of a text file
#

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'
with open(original_file) as file:
      og_content = file.read()
# read the content of the original file
print(og_content)

# write the content to the target file (copy)
with open(target_file, 'w') as file:
    file.write(og_content)