import requests
import json
import os

if __name__ == "__main__":
    with open(f"{os.getcwd()}/secret.json") as file:
        secrets = json.load(file)
else:
    with open(f"{os.path.dirname(__file__)}/secret.json") as file:
        secrets = json.load(file)

AOC_COOKIE = secrets["AOC_COOKIE"]
YEAR = secrets["YEAR"]


def get_input(day: int, part=None):
    req = requests.get(
        f"https://adventofcode.com/{YEAR}/day/{day}/input",
        headers={"cookie": "session=" + AOC_COOKIE},
    )


    if req.text[-1] == "\n":
        return req.text[:-1].strip().split("\n")
    else:
        return req.text.strip().split("\n")


def get_example(day:int, part:int=1):
    req = requests.get(
        f"https://adventofcode.com/{YEAR}/day/{day}",
        headers={"cookie": "session=" + AOC_COOKIE},
    )
    return (
        req.text.split("<pre><code>")[part]
        .split("</code></pre>")[0]
        .strip()
        .split("\n")
    )


def submit_answer(day:int, level:int, answer:str):
    print("You are about to submit the following answer:")
    print(answer)
    input("Press enter to continue or Ctrl+C to abort. \n")
    data = {"level": str(level), "answer": str(answer)}

    response = requests.post(
        f"https://adventofcode.com/{YEAR}/day/{day}/answer",
        headers={"cookie": "session=" + AOC_COOKIE},
        data=data,
    )
    if "You gave an answer too recently" in response.text:
        # You will get this if you submitted a wrong answer less than 60s ago.
        print("VERDICT : TOO MANY REQUESTS")
    elif "not the right answer" in response.text:
        if "too low" in response.text:
            print("VERDICT : WRONG (TOO LOW)")
        elif "too high" in response.text:
            print("VERDICT : WRONG (TOO HIGH)")
        else:
            print("VERDICT : WRONG (UNKNOWN)")
    elif "seem to be solving the right level." in response.text:
        # You will get this if you submit on a level you already solved.
        # Usually happens when you forget to switch from `PART = 1` to `PART = 2`
        print("VERDICT : ALREADY SOLVED")
    else:
        print("VERDICT : OK !")


def load_input_from_file(file_name:str="input.txt"):
    if file_name == "input.txt":
        file_path = os.path.join(os.getcwd(), file_name)
    else:
        file_path = file_name

    with open(file_path) as file:
        return file.read().splitlines()
