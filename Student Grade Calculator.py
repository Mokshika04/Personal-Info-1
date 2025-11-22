# Student Grade Calculator

# Take input marks
marks = float(input("Enter your marks (0-100): "))

# Determine grade and message
if marks >= 90:
    grade = "A"
    message = "Outstanding work! Keep shining! "
elif marks >= 80:
    grade = "B"
    message = "Great job! You're doing really well! "
elif marks >= 70:
    grade = "C"
    message = "Good effort! Keep improving! "
elif marks >= 60:
    grade = "D"
    message = "You passed! Stay focused and you’ll do even better! "
else:
    grade = "F"
    message = "Don't give up! Every setback is a setup for a comeback! "

# Display result
print(f"\nYour Grade: {grade}")
print(message)
