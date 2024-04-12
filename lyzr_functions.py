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
    "temperature": 0.1,
    "max_tokens": 4096,
    },
)

timetable_memory = OpenAIMemory(
    file_path='example_slot.txt'
)

def generate_basic_timetable():
    timetable_agent = Agent(
        prompt_persona="You are an intelligent agent that can create efficient class timetables for a week in a simple, structured format. Do not assign more classes than required, assign free slots instead. Generate timetable for every day from Monday to Friday.",
        role="Timetable creator",
        memory=timetable_memory
    )

    timetable_task = Task(
        name="Timetable Creator",
        agent=timetable_agent,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
        model=open_ai_model_text,
        instructions="Using the time slots, subject details and requirements, create a timetable that satisfies every constraint. Return the timetable in a simple format and a count of number of classes scheduled for each subject.",
        log_output=True,
        enhance_prompt=False,
    ).execute()

    with open("example_result.txt", "w") as my_file:
        my_file.write("# GENERATED TIMETABLE - Timetable Agent")
        my_file.write("\n \n")
        my_file.write(timetable_task)
        my_file.write("\n")

    timetable_checker_agent = Agent(
        prompt_persona="You are an intelligent agent that can verify if a generated timetable fulfills all the constraints or not. Make sure all classes meet the exact requirements; not more, not less.",
        role="Timetable checker",
        memory=timetable_memory
    )

    timetable_checker_task = Task(
        name="Timetable Checker",
        agent=timetable_checker_agent,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
        model=open_ai_model_text,
        instructions="Verify that the generated timetable input fulfills the requirements mentioned in the file. If VALID, return <!VALID!> and the timetable in a table format; If INVALID, return <!INVALID!> the reason why invalid. Do not return anything else.",
        log_output=True,
        enhance_prompt=False,
        previous_output=timetable_task
    ).execute()

    with open("example_result.txt", "a") as my_file:
        my_file.write("\n \n")
        my_file.write("# GENERATED VERIFICATION - Verification Agent")
        my_file.write("\n \n")
        my_file.write(timetable_checker_task)
        my_file.write("\n")