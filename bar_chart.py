import matplotlib.pyplot as plt

students = ["Cyril", "John", "Mary"]
marks = [90, 85, 95]

plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()