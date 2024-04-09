from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata.memory.open_ai import OpenAIMemory
from lyzr_automata import Agent, Task
from lyzr_automata.tasks.task_literals import InputType, OutputType

from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

open_ai_model_text = OpenAIModel(
api_key=OPENAI_API_KEY,
parameters={
    "model": "gpt-4-turbo-preview",
    "temperature": 0.3,
    "max_tokens": 1500,
    },
)

timetable_memory = OpenAIMemory(
    file_path='timeslot.txt'
)

timetable_agent = Agent(
    prompt_persona="You are an intelligent agent that can create efficient class timetables in a simple, concise and easy to read format",
    role="Timetable creator",
    memory=timetable_memory
)

timetable_task = Task(
    name="Timetable Creator",
    agent=timetable_agent,
    output_type=OutputType.TEXT,
    input_type=InputType.TEXT,
    model=open_ai_model_text,
    instructions="Using the time slots, student details and teacher details create a timetable that satisfies every requirement. Return only the timetable in a simple text format.",
    log_output=True,
    enhance_prompt=False,
).execute()

# sample = "Based on the provided details, here is a proposed class timetable that satisfies all student and teacher availability constraints:\n\n**Monday to Friday**\n\n**08:00 AM to 08:50 AM**\n- Subject: Math\n- Teacher: Alexander Lee\n- Students: Samantha Hayes, Lucas Martinez, Isabella Wong, Olivia Patel, Sophia Nguyen, Ava Khan, Noah Ramirez\n\n**08:55 AM to 09:45 AM**\n- Subject: English\n- Teacher: Emily Thompson (can only take 08:55 AM to 09:45 AM class)\n- Students: Samantha Hayes, Lucas Martinez, Isabella Wong, Olivia Patel, Sophia Nguyen, Ava Khan, Noah Ramirez\n\n**09:50 AM to 10:40 AM**\n- Subject: Science\n- Teacher: Mia Rodriguez\n- Students: Samantha Hayes, Lucas Martinez, Isabella Wong, Olivia Patel, Sophia Nguyen, Ava Khan, Noah Ramirez\n\n**10:45 AM to 11:35 AM**\n- Subject: Computer Science\n- Teacher: Jacob Brown\n- Students: Gabriel Anderson (can only take 10:45 AM to 11:35 AM class), Samantha Hayes, Lucas Martinez, Isabella Wong, Olivia Patel, Sophia Nguyen, Ava Khan, Noah Ramirez\n\n**11:40 AM to 12:30 PM**\n- Subject: Art\n- Teacher: Charlotte Kim\n- Students: Samantha Hayes, Lucas Martinez, Isabella Wong, Olivia Patel, Sophia Nguyen, Ava Khan, Noah Ramirez\n\n**02:00 PM to 02:50 PM**\n- Subject: History\n- Teacher: Benjamin Harris\n- Students: Samantha Hayes, Lucas Martinez, Isabella Wong, Olivia Patel, Sophia Nguyen, Ava Khan, Noah Ramirez (Caleb Mitchell cannot take 02:00 PM to 02:50 PM class)\n\n**02:55 PM to 03:45 PM**\n- Subject: Geography\n- Teacher: Harper Jones\n- Students: Samantha Hayes, Lucas Martinez, Isabella Wong, Olivia Patel, Caleb Mitchell, Sophia Nguyen, Ava Khan, Noah Ramirez\n\n**03:50 PM to 04:40 PM**\n- Subject: Physical Education\n- Teacher: William Chang\n- Students: Samantha Hayes, Lucas Martinez, Isabella Wong, Olivia Patel, Caleb Mitchell, Sophia Nguyen, Ava Khan, Noah Ramirez\n\n**04:45 PM to 05:35 PM**\n- Subject: Music\n- Teacher: Evelyn Sullivan\n- Students: Ethan Johnson (can only take 04:45 PM to 05:35 PM class), Samantha Hayes, Lucas Martinez, Isabella Wong, Olivia Patel, Caleb Mitchell, Sophia Nguyen, Ava Khan, Noah Ramirez\n\n**05:40 PM to 06:30 PM**\n- Subject: Philosophy\n- Teacher: Daniel Garcia (cannot take 05:40 PM to 06:30 PM class, not assigned this slot)\n- Students: Samantha Hayes, Lucas Martinez, Isabella Wong, Olivia Patel, Caleb Mitchell, Sophia Nguyen, Ava Khan, Noah Ramirez\n\nPlease note that specific subjects assigned to time slots are hypothetical to accommodate the teacher and student availability provided. The missing subject for the last slot (05:40 PM to 06:30 PM) implies either a free period for students or a need for further adjustment based on staff availability beyond the provided constraints."

with open("example_slot.txt", "a") as my_file:
    my_file.write("\n \n")
    my_file.write("GENERATED TIMETABLE")
    my_file.write("\n \n")
    my_file.write(timetable_task)
    my_file.write("\n")

# breakpoint()

timetable_checker_agent = Agent(
    prompt_persona="You are an intelligent agent that check if a generated timetable fulfils all the requirements and return if it is valid or not.",
    role="Timetable checker",
    memory=timetable_memory
)

timetable_checker_task = Task(
    name="Timetable Checker",
    agent=timetable_checker_agent,
    output_type=OutputType.TEXT,
    input_type=InputType.TEXT,
    model=open_ai_model_text,
    instructions="Verify that the generated timetable input fulfils the requirements mentioned in the file. Return true or false followed by the reasoning.",
    log_output=True,
    enhance_prompt=False,
    previous_output=timetable_task
).execute()

with open("example_slot.txt", "a") as my_file:
    my_file.write("\n \n")
    my_file.write("GENERATED VERIFICATION")
    my_file.write("\n \n")
    my_file.write(timetable_checker_task)
    my_file.write("\n")