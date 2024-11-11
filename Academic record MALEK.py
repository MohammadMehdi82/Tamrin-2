def calculate_weighted_average(grades, weights, subjects):
    if len(grades) != len(weights) or len(grades) != len(subjects):
        raise ValueError("The number of grades, weights, and subjects must be the same")
    
    total_weighted_sum = sum(g * w for g, w in zip(grades, weights))
    total_weights = sum(weights)
    
    weighted_average = total_weighted_sum / total_weights
    
    for subject, grade, weight in zip(subjects, grades, weights):
        print(f"Subject: {subject}, Grade: {grade}, Weight: {weight}")
        
    return weighted_average

subjects = ["Precision instrument laboratory","Laboratory of linear control systems","Applied electronics",
"Thematic interpretation of the Qur'an","Industrial operators","Industrial control","Programmable logic controllers","Documentation of automation project documents",
"Microcontrollers"] 
grades = [12,20,14,10,10,19.5,19,18,14]
weights = [1,1,3,2,3,2,2,2,2]  

average = calculate_weighted_average(grades, weights, subjects)
print(f"The weighted average is {average}")
