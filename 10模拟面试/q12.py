'''
71. Simplify Path
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.
The rules of a Unix-style file system are as follows:
A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:
The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.

Example 1:
Input: path = "/home/"
Output: "/home"
Explanation:
The trailing slash should be removed.
Example 2:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation:
Multiple consecutive slashes are replaced by a single one.
Example 3:
Input: path = "/home/user/Documents/../Pictures"
Output: "/home/user/Pictures"
Explanation:
A double period ".." refers to the directory up a level (the parent directory).
Example 4:
Input: path = "/../"
Output: "/"
Explanation:
Going one level up from the root directory is not possible.
Example 5:
Input: path = "/.../a/../b/c/../d/./"
Output: "/.../b/d"
Explanation:
"..." is a valid name for a directory in this problem.


def solution(path:str)->str:
	path = path.split(“/”)
	stack = [ ]
	for s in path:
		if s == “”:
			continue
		if s == “.”:
			continue
		if s == “..”:
			if len(stack) >0:
				stack.pop()
		else:
			stack.push(s)
	return “/”.join(stack)

time:O(n)
space:O(n)

'''


'''
题意：
Give you a string representing a path, but there are some operations in the path. We need to simplify this path to make the length of the string the shortest.

Input: path = "/home/user/Documents/../Pictures"
Output: "/home/user/Pictures"

For example, /../ in this string actually returns to the previous directory.


思路：
Data structure used: stack
steps:
1. We can use stack pushing to simulate entering the next folder, and popping means returning to the previous folder.
2. For /// in the string, we re-represent it as /, which is beneficial to data processing.
3. The specific steps are to define a stack and then split the string according to the characters /
4. Access each string after segmentation. If it is a single ".", the stack will remain unchanged. If it encounters "..", it will be popped from the stack. If it is another string, it will be pushed onto the stack.
5. Finally, the elements in the stack are taken out to form a string, which is the final simplified path.
'''

#代码
def solution(path:str)->str:
    path = path.split("/") # Split the string according to characters /
    stack = [] # define a stack
    for s in path:
        if s == "": # Skip empty strings
            continue
        if s == ".": # Stay in the current file directory
            continue
        if s == "..": # Return to the previous directory and pop out of the stack
            if len(stack) > 0:
                stack.pop()
        else: # If it is another string, it means that this string is the name of the folder.
            stack.push(s)
    return  "/".join(stack) # Use slash to connect the names of each folder in the stack to form a file path


'''
Time complexity: O(n) It only needs to split the string, push and pop it into the stack
Space complexity: O(n) because an array needs to be opened
'''