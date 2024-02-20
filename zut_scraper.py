import requests
import threading
import time
from datetime import datetime, timedelta

# Read the data from the file
with open("data.txt", "r") as file:
    # Extract the content of the file
    file_content = file.read()

# Use eval to extract the lists from the content
algo1 = eval(file_content.split("algo1 = ")[1].split("\n\n")[0])
w22_algo2_term_01 = eval(file_content.split("w22_algo2_term_01 = ")[1].split("\n\n")[0])
w21_algo2_term_01 = eval(file_content.split("w21_algo2_term_01 = ")[1].split("\n\n")[0])

# Concatenate w21_algo2_term_01 and w22_algo2_term_01
algo2_term_01 = w21_algo2_term_01 + w22_algo2_term_01


def search_in_data(data, target):
    if isinstance(data, list):
        for item in data:
            if search_in_data(item, target):
                return True
    elif isinstance(data, dict):
        for value in data.values():
            if search_in_data(value, target):
                return True
    elif isinstance(data, str):
        if target in data:
            return True
    return False


def make_request(ids, target, result, anticounter, lock, start_days, end_days):
    current_time = datetime.now() - timedelta(days=start_days)
    formatted_current_time = current_time.strftime("%Y-%m-%dT%H:%M:%S%z")
    end_time = current_time + timedelta(days=end_days)
    formatted_end_time = end_time.strftime("%Y-%m-%dT%H:%M:%S%z")
    url = (
        f"https://plan.zut.edu.pl/schedule_student.php?number={ids}"
        f"&start={formatted_current_time}&end={formatted_end_time}"
    )

    try:
        page = requests.get(url)
        data = page.json()
        if search_in_data(data, target):
            with lock:
                result.append(ids)
        else:
            with lock:
                anticounter[0] += 1
    except requests.exceptions.RequestException as e:
        print(f"Request for {ids} failed with error: {e}")


def search_requests(
        what_to_look_for,
        data_sheets,
        print_result,
        print_counter,
        print_anticounter,
        print_time,
):
    start_time = time.time()
    target = what_to_look_for
    result = []
    anticounter = [0]
    lock = threading.Lock()

    threads = []
    for ids in data_sheets:
        thread = threading.Thread(
            target=make_request,
            args=(
                ids,
                target,
                result,
                anticounter,
                lock,
                subtract_from_the_start,
                add_to_the_end,
            ),
        )
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    end_time = time.time()
    elapsed_time = end_time - start_time
    if print_time:
        print("Elapsed time:", elapsed_time, "seconds")
    if print_counter:
        print("Full counter:", len(w21_algo2_term_01 + w22_algo2_term_01))
    if print_anticounter:
        print("Anticounter:", anticounter[0])
    if print_result:
        for item in result:
            print(item)
    return result, anticounter[0]


if __name__ == "__main__":
    # variables to change:
    subtract_from_the_start = (
        0  # What day to start from? (today - subtract_from_the_start)
    )
    add_to_the_end = 21  # What day to end at? (today + add_to_the_end)
    search_query = "PO2_Moijwib_L_gr.4"  # What to search for? Literally anything i.e. can be a name of a professor
    data_sheet = w21_algo2_term_01
    # data_sheet = algo1 # or just w22_algo2_term_01 or w21_algo2_term_01

    delay = 5

    result1, anticounter1 = search_requests(
        search_query, data_sheet, False, False, False, False
    )
    data_sheet = w22_algo2_term_01
    time.sleep(delay)
    result2, anticounter2 = search_requests(
        search_query, data_sheet, False, False, False, False
    )
    unique_result = list(set(result1 + result2))
    print(unique_result)
