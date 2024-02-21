import asyncio
import aiohttp
from datetime import datetime, timedelta

async def make_request(session, ids, targets, result, logical_operator, anticounter, start_days, end_days):
    current_time = datetime.now() - timedelta(days=start_days)
    formatted_current_time = current_time.strftime("%Y-%m-%dT%H:%M:%S%z")
    end_time = current_time + timedelta(days=end_days)
    formatted_end_time = end_time.strftime("%Y-%m-%dT%H:%M:%S%z")
    url = f"https://plan.zut.edu.pl/schedule_student.php?number={ids}&start={formatted_current_time}&end={formatted_end_time}"

    try:
        async with session.get(url) as response:
            data = await response.json()

            if logical_operator == "and":
                if all(target in str(data) for target in targets):
                    result.append(ids)
                else:
                    anticounter[0] += 1
            elif logical_operator == "or":
                if any(target in str(data) for target in targets):
                    result.append(ids)
                else:
                    anticounter[0] += 1
    except Exception as e:
        print(f"Request for {ids} failed with error: {e}")

async def search_requests(what_to_look_for, data_sheets, logical_operator, print_result, print_counter, print_anticounter, print_time):
    if logical_operator not in ["and", "or"]:
        print('Error: Invalid logical operator value. Please use "and" or "or".')
        return [], 0

    start_time = datetime.now()

    target = what_to_look_for
    result = []
    anticounter = [0]

    async with aiohttp.ClientSession() as session:
        tasks = []
        for ids in data_sheets:
            task = make_request(session, ids, target, result, logical_operator, anticounter, subtract_from_the_start, add_to_the_end)
            tasks.append(task)

        await asyncio.gather(*tasks)

    end_time = datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()

    if print_time:
        print("Elapsed time:", elapsed_time, "seconds")

    if print_counter:
        print("Full counter:", len(data_sheets))

    if print_anticounter:
        print("Anticounter:", anticounter[0])

    if print_result:
        unique_result = list(set(result))
        print(unique_result)
        print(len(unique_result))

    return result, anticounter[0]

if __name__ == "__main__":
    # Read the data from the file
    with open("data.txt", "r") as file:
        file_content = file.read()

    algo1 = eval(file_content.split("algo1 = ")[1].split("\n\n")[0])
    w22_algo2_term_01 = eval(file_content.split("w22_algo2_term_01 = ")[1].split("\n\n")[0])
    w21_algo2_term_01 = eval(file_content.split("w21_algo2_term_01 = ")[1].split("\n\n")[0])
    stacjo = eval(file_content.split("stacjo = ")[1].split("\n\n")[0])
    zdalne = eval(file_content.split("zdalne = ")[1].split("\n\n")[0])
    all = eval(file_content.split("all = ")[1].split("\n\n")[0])
    data_sheet = all

    subtract_from_the_start = 0  # What day to start from? (today - subtract_from_the_start)
    add_to_the_end = 21  # What day to end at? (today + add_to_the_end)

    search_query = "Transmisja danych (L)", "Śmietanka", "S1_I_L_220A"

    asyncio.run(search_requests(search_query, data_sheet, "or", True, False, False, True))
