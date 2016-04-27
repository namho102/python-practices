file = open('the_bible.txt', 'r')

with open('the_bible.txt','r') as f:
	for line in file:
		print(line)
		# if re.match("^#",line):
			# starts_with_hash += 1

# 'r' means read-only
# file_for_reading = open('reading_file.txt', 'r')
# 'w' is write -- will destroy the file if it already exists!
# file_for_writing = open('writing_file.txt', 'w')
# 'a' is append -- for adding to the end of the file
# file_for_appending = open('appending_file.txt', 'a')
# don't forget to close your files when you're done
# file_for_writing.close()