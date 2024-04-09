import streamlit as st
from main import generate_basic_timetable

timeslot_input = st.text_area(
    "TIMESLOTS",
    '''08:00 AM - 09:00 AM
09:15 AM - 10:15 AM
10:30 AM - 11:30 AM
11:45 AM - 12:45 PM
01:00 PM - 02:00 PM
02:15 PM - 03:15 PM
03:30 PM - 04:30 PM
04:45 PM - 05:45 PM'''
)

# students_input = st.text_area(
#     "STUDENTS (10)",
#     '''Samantha Hayes
# Lucas Martinez
# Isabella Wong
# Ethan Johnson
# Olivia Patel
# Caleb Mitchell
# Sophia Nguyen
# Gabriel Anderson
# Ava Khan
# Noah Ramirez'''
# )

classrooms_input = st.text_area(
    "CLASSROOMS",
    '''Room 101
Room 102
Room 103
Room 104
Room 105'''
)

subjects_input = st.text_area(
    "SUBJECTS",
    '''Mathematics
Science
English Language Arts
Social Studies
History
Geography
Physical Education
Computer Science
Art
Music'''
)

# constraints_input = st.text_area(
#     "CONSTRAINTS",
#     '''Emily Thompson availability - 08:00 AM - 09:00 AM, 11:00 AM - 12:00 PM, 01:00 PM - 02:00 PM
# Alexander Lee availability - 08:00 AM - 09:00 AM, 09:30 AM - 10:30 AM, 01:00 PM - 02:00 PM, 02:30 PM - 03:30 PM
# Mia Rodriguez availability - 08:00 AM - 09:00 AM, 11:00 AM - 12:00 PM, 02:30 PM - 03:30 PM
# Jacob Brown availability - 09:30 AM - 10:30 AM, 11:00 AM - 12:00 PM, 01:00 PM - 02:00 PM, 02:30 PM - 03:30 PM
# Charlotte Kim availability - 08:00 AM - 09:00 AM, 09:30 AM - 10:30 AM, 01:00 PM - 02:00 PM, 02:30 PM - 03:30 PM'''
# )

constraints_input = st.text_area(
    "CONSTRAINTS",
    '''1. Mathematics - 5 classes a week
2. Science - 5 classes a week
3. English Language Arts - 3 classes a week
4. Social Studies - 3 classes a week
5. History - 3 classes a week
6. Geography - 3 classes a week
7. Physical Education - 3 classes a week
8. Computer Science - 5 classes a week
9. Art - 2 class a week
10. Music - 2 class a week
11. Each classroom is allocated once per time slot on any given day.
12. Same subjects cannot be assigned consecutively'''
)

@st.cache_data
def generate_timetable():
    generate_basic_timetable()

submit_inputs = st.button("Submit", type="primary")
if submit_inputs:
    with open("example_slot.txt", "w") as my_file:
        my_file.write("TIMESLOTS")
        my_file.write("\n \n")
        my_file.write(timeslot_input)
        my_file.write("\n \n")

        # my_file.write("STUDENTS")
        # my_file.write("\n \n")
        # my_file.write(students_input)
        # my_file.write("\n \n")

        my_file.write("CLASSROOMS")
        my_file.write("\n \n")
        my_file.write(classrooms_input)
        my_file.write("\n \n")

        my_file.write("SUBJECTS")
        my_file.write("\n \n")
        my_file.write(subjects_input)
        my_file.write("\n \n")

        my_file.write("CONSTRAINTS")
        my_file.write("\n \n")
        my_file.write(constraints_input)
    # breakpoint()
    generate_timetable()

    with open("example_result.txt", "r") as my_file:
        content = my_file.read()

    st.write(content)