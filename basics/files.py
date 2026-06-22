# open takes 3 arguments filename, mode, encoding
# modes - r(read), w(write), r+(read & write), a(append)
f = open('sample.txt', 'r', encoding="utf-8")
# print(f.read())
f.close()
# print(f.read()) # it gives error, once file is closed

# When using the 'with' keyword, the file is automatically closed
# after the block finishes, even if an exception occurs.
# This helps release system resources and prevents file leaks.
with open('sample.txt', 'r', encoding='utf-8') as f1:
    data = f1.read()
    # print(data)

# readline() is used to read each line
f2 = open('sample.txt', 'r', encoding='utf-8')
print(f2.readline())
f2.close()

# read each line using for loop
f3 = open('sample.txt', 'r', encoding='utf-8')
print(list(f3)) # reads all lines into a list
for line in f3:
    print(f"Each line: {line}", end=' ') # end will append the value at end of the line.
f3.close()

# f3.write('Testing file write operation') # this will io.UnsupportedOperation: not writable error

# write to a file
f4 = open('sample.txt', 'w')
f4.write("""Testing file to write the content 
Next line """) # it will replace the file content with given text
print(f4.tell())
f4.close()

# read & write
f5 = open('sample.txt', 'r+', encoding='utf-8')
print(f5.read(36))
f5.close()