students = ("Jon", "Kim", "Lee")

# convert to mutable list so we can add more names after creation
students = list(students)
students.extend(["Sara", "Miko"])

def greet_students(student_list):
	for name in student_list:
		print(f"Hi {name}")
	# after iterating through everyone, also show how many there are
	print(f"Total students: {len(student_list)}")
	
# run the greeting with the updated list

greet_students(students)