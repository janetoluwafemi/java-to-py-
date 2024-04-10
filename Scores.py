total = 0
student_passed = 0
student_failed = 0
score = int(input("Enter score: "))
if score < 45:
	print("failed")
	student_failed += 1
else:
	print("passed")
	student_passed += 1

	total += score
print(student_failed)
print(student_passed)