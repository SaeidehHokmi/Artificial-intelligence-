def my_final_grade_calculation(filename):
    # Dictionary to store the final results
    results = {}
    
    # Open the file and process each line
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into parts and remove any extra spaces
            parts = line.split(',')
            parts = [p.strip() for p in parts]
            
            # Extract the name and convert it to lowercase
            name = parts[0].lower()
            
            # Convert scores to integers
            quizzes = list(map(int, parts[1:7]))  # q1 to q6
            assignments = list(map(int, parts[7:11]))  # a1 to a4
            midterm = int(parts[11])  # midterm
            final = int(parts[12])  # final
            
            # Process quiz scores: drop the two lowest scores and average the rest
            quizzes.sort()
            quiz_avg = sum(quizzes[2:]) / 4  # Average of the top 4 quizzes
            
            # Process assignment scores: drop the lowest score and average the rest
            assignments.sort()
            assignment_avg = sum(assignments[1:]) / 3  # Average of the top 3 assignments
            
            # Calculate the final grade based on the given percentages
            final_score = (quiz_avg * 0.25) + (assignment_avg * 0.25) + (midterm * 0.25) + (final * 0.25)
            
            # Determine if the student passed or failed
            if final_score >= 60:
                results[name] = "pass"
            else:
                results[name] = "fail"
    
    return results

# گرفتن ورودی فایل از کاربر
filename = input("نام فایل حاوی نمرات را وارد کنید: ")

# اجرای تابع و چاپ خروجی
result = my_final_grade_calculation(filename)
print(result)
