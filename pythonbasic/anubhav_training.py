course_catalog = { "ui5" : { "course_name" : "UI5 Development", 
                            "course_duration" : "3 months", 
                            "course_fee" : 5000 }, 
                    "python" : { "course_name" : "Python Programming",
                                 "course_duration" : "4 months", 
                                 "course_fee" : 6000 }, 
                    "data_science" : { "course_name" : "Data Science with Python", 
                                      "course_duration" : "6 months", 
                                      "course_fee" : 8000 } 
             } 

user_inut_courses = []

while True:
    user_input = input("Enter the course you want to enroll in (or 'exit' to finish): ")
    if user_input.lower() == 'exit':
        break
    elif user_input in course_catalog:
        user_inut_courses.append(user_input)
        print(f"Added {course_catalog[user_input]['course_name']} to your enrollment list.")
    else:
        print("Course not found. Please try again.")

print("\nYou have enrolled in the following courses:")
# enumerate means to loop through the list and get the index of each item as well
for idx, course in enumerate(user_inut_courses, start=0):
    print(f"{idx}. {course_catalog[course]['course_name']} - Duration: {course_catalog[course]['course_duration']}, Fee: ${course_catalog[course]['course_fee']}")  
for course in user_inut_courses:
    print(f"{course_catalog[course]['course_name']} - Duration: {course_catalog[course]['course_duration']}, Fee: ${course_catalog[course]['course_fee']}") 

