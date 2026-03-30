from predictor import predict

print("Student Performance Predictor")
print("-----------------------------")

hours = float(input("Hours studied per day: "))
attendance = float(input("Attendance (%): "))
assignments = float(input("Assignments completed: "))
previous = float(input("Previous marks: "))

result = predict(hours, attendance, assignments, previous)

print("\nPrediction:", result)

if result == "Fail":
    print("Recommendation: Increase study hours and attendance.")
else:
    print("Good performance! Keep it up.")