import streamlit as st
from lyzr_functions import generate_basic_timetable

# Time Slots
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

# Subjects
subjects_input = st.text_area(
    "SUBJECTS",
    '''Mathematics
Science
English
Social Studies
History
Geography
Physical Education
Computer
Art
Music'''
)

# Constraints
constraints_input = st.text_area(
    "CONSTRAINTS",
    '''1. Mathematics - 5 classes a week
2. Science - 5 classes a week
3. English - 4 classes a week
4. Social Studies - 4 classes a week
5. History - 3 classes a week
6. Geography - 3 classes a week
7. Physical Education - 4 classes a week
8. Computer - 5 classes a week
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
    # Save inputs to a file
    with open("example_slot.txt", "w") as my_file:
        my_file.write("TIMESLOTS")
        my_file.write("\n \n")
        my_file.write(timeslot_input)
        my_file.write("\n \n")

        my_file.write("SUBJECTS")
        my_file.write("\n \n")
        my_file.write(subjects_input)
        my_file.write("\n \n")

        my_file.write("CONSTRAINTS")
        my_file.write("\n \n")
        my_file.write(constraints_input)

    # Call timetable generator
    generate_timetable()

    # Read and display from result file
    with open("example_result.txt", "r") as my_file:
        content = my_file.read()

    st.write(content)