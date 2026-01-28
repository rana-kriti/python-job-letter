print("Job letter")
print("-----------------")
name=input("Enter your name: ")
job_role=input("Enter your job role: ")
age=int(input("Enter your age: "))
sal=int(input("Enter your salary: "))
print("-----------------")
letter=f'''Dear {name},
You have been employed as {job_role} at SMITH INDUSTRIES 
since November 01,2025 for an annual salary of INR {sal}.
\n Please report to MR. Anuj (Manager of {job_role} department) 
for documentation and orientation amd confirm your acceptance of this offer.
\nSincerely,
MS. Saloni
HR Manager'''
print(letter)
