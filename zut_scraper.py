import requests
import threading
import time
from datetime import datetime, timedelta

algo1 = [
    54948, 54935, 54603, 53978, 53977, 53976, 53974, 53973, 53971, 53970,
    53968, 53967, 53965, 53964, 53962, 53961, 53960, 53959, 53957, 53956,
    53955, 53954, 53953, 53952, 53951, 53950, 53949, 53947, 53946, 53945,
    53944, 53943, 53942, 53941, 53940, 53938, 53937, 53935, 53934, 53932,
    53931, 53928, 53927, 53926, 53924, 53923, 53922, 53920, 53918, 53916,
    53915, 53914, 53913, 53912, 53911, 53910, 53909, 53908, 53907, 53906,
    53905, 53904, 53903, 53902, 53901, 53900, 53898, 53896, 53895, 53894,
    53891, 53889, 53887, 53883, 53882, 53881, 53879, 53878, 53877, 53876,
    53874, 53873, 53872, 53871, 53869, 53868, 53867, 53865, 53863, 53861,
    53860, 53859, 53858, 53857, 53856, 53855, 53854, 53852, 53849, 53848,
    53847, 53844, 53843, 53841, 53840, 53839, 53838, 53837, 53836, 53834,
    53833, 53831, 53828, 53825, 53824, 53823, 53821, 53819, 53816, 53814,
    53811, 53809, 53808, 53807, 53805, 53804, 53803, 53801, 53800, 53799,
    53798, 53796, 53795, 53793, 53791, 53790, 53789, 53788, 53787, 53786,
    53785, 53784, 53783, 53782, 53781, 53780, 53779, 53776, 53775, 53774,
    53773, 53772, 53771, 53770, 53769, 53768, 53767, 53766, 53762, 53761,
    53760, 53759, 53757, 53755, 53753, 53752, 53751, 53750, 53749, 53748,
    53747, 53746, 53745, 53743, 53740, 53739, 53737, 53736, 53735, 53734,
    53733, 53732, 53731, 53730, 53729, 53728, 53727, 53726, 53725, 53723,
    53722, 53721, 53720, 53717, 53716, 53715, 53714, 53713, 53712, 53711,
    53710, 53709, 53708, 53707, 53706, 53705, 53704, 53703, 53702, 53700,
    53699, 53698, 53697, 53695, 53693, 53692, 53691, 53690, 53689, 53688,
    53687, 53686, 53683, 53682, 53680, 53678, 53677, 53676, 53675, 53674,
    53673, 53672, 53671, 53668, 53667, 53666, 53665, 53664, 53663, 53662,
    53661, 53660, 53659, 53535, 53021, 52447, 52367, 52087, 51602, 51498,
    51466, 51459, 51264, 51168, 51130, 51104, 51102, 51071, 51059, 51041,
    50969, 50948, 50822, 50787, 49366, 49261, 47393, 46622, 44762, 42451,
    41572
]

w22_algo2_term_01 = [
    55241, 54935, 54603, 54134, 53978, 53976, 53974, 53964, 53962, 53961,
    53960, 53953, 53952, 53947, 53945, 53944, 53940, 53935, 53928, 53916,
    53914, 53909, 53908, 53903, 53896, 53891, 53889, 53882, 53879, 53878,
    53877, 53876, 53874, 53873, 53872, 53869, 53868, 53861, 53855, 53852,
    53848, 53847, 53844, 53841, 53840, 53837, 53833, 53828, 53825, 53824,
    53823, 53821, 53819, 53816, 53814, 53807, 53801, 53793, 53790, 53788,
    53785, 53782, 53781, 53780, 53775, 53771, 53770, 53766, 53760, 53750,
    53749, 53748, 53740, 53739, 53737, 53736, 53734, 53733, 53732, 53730,
    53728, 53722, 53717, 53713, 53709, 53708, 53707, 53706, 53703, 53702,
    53698, 53697, 53692, 53688, 53683, 53680, 53678, 53674, 53673, 53663,
    53660, 53021, 52524, 51602, 51459, 51264, 51174, 51168, 51157, 51153,
    51152, 51151, 51146, 51120, 51119, 51111, 51107, 51106, 51102, 51095,
    51092, 51075, 51054, 51047, 51045, 51043, 51042, 51041, 51038, 51029,
    51022, 51020, 51013, 51004, 50993, 50983, 50974, 50973, 50972, 50962,
    50929, 50928, 50923, 50822, 50266, 49464, 49463, 49423, 49366, 49340,
    49270, 49234, 48938, 46587, 46565, 46460, 44762, 44406, 42451, 40423,
    39512, 39325, 39274, 34993, 32921
]

w21_algo2_term_01 = [
    56868, 54948, 54134, 53971, 53967, 53965, 53957, 53956, 53955, 53949,
    53947, 53943, 53942, 53938, 53937, 53935, 53934, 53931, 53927, 53926,
    53920, 53915, 53913, 53912, 53911, 53910, 53907, 53906, 53905, 53902,
    53900, 53894, 53887, 53873, 53871, 53867, 53860, 53859, 53856, 53854,
    53843, 53839, 53838, 53837, 53836, 53811, 53809, 53805, 53804, 53803,
    53800, 53799, 53798, 53796, 53791, 53789, 53787, 53786, 53785, 53784,
    53779, 53776, 53774, 53773, 53772, 53769, 53767, 53762, 53761, 53759,
    53757, 53753, 53752, 53751, 53747, 53746, 53745, 53736, 53735, 53731,
    53730, 53729, 53727, 53726, 53725, 53723, 53721, 53720, 53717, 53716,
    53715, 53712, 53711, 53710, 53704, 53699, 53697, 53693, 53690, 53689,
    53686, 53682, 53680, 53677, 53675, 53673, 53671, 53668, 53667, 53666,
    53665, 53664, 53662, 53661, 53659, 53535, 52932, 52524, 52447, 52367,
    52087, 51672, 51498, 51171, 51167, 51163, 51158, 51151, 51136, 51120,
    51119, 51117, 51104, 51101, 51100, 51097, 51092, 51088, 51087, 51074,
    51070, 51066, 51050, 51048, 51046, 51045, 51042, 51031, 51022, 51013,
    50973, 50972, 50965, 50963, 50961, 50950, 50936, 50929, 50920, 50822,
    50787, 49470, 49463, 49410, 49378, 49312, 49298, 49277, 49261, 49249,
    49234, 49230, 46587, 46554, 46501, 44406, 42451, 41503, 40423, 39274,
    32921
]

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
    formatted_current_time = current_time.strftime('%Y-%m-%dT%H:%M:%S%z')
    end_time = current_time + timedelta(days=end_days)
    formatted_end_time = end_time.strftime('%Y-%m-%dT%H:%M:%S%z')
    url = (f"https://plan.zut.edu.pl/schedule_student.php?number={ids}"
           f"&start={formatted_current_time}&end={formatted_end_time}")

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


def search_requests(what_to_look_for, data_sheets, print_result, print_counter, print_anticounter, print_time):
    start_time = time.time()
    target = what_to_look_for
    result = []
    anticounter = [0]
    lock = threading.Lock()

    threads = []
    for ids in data_sheets:
        thread = threading.Thread(target=make_request, args=(
            ids, target, result, anticounter, lock, subtract_from_the_start, add_to_the_end))
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


if __name__ == '__main__':
    # variables to change:
    subtract_from_the_start = 0  # What day to start from? (today - subtract_from_the_start)
    add_to_the_end = 21  # What day to end at? (today + add_to_the_end)
    search_query = "PO2_Moijwib_L_gr.4"  # What to search for? Literally anything i.e. can be a name of a professor
    data_sheet = w21_algo2_term_01
    # data_sheet = algo1 # or just w22_algo2_term_01 or w21_algo2_term_01

    delay = 5

    result1, anticounter1 = search_requests(search_query, data_sheet, False, False, False, False)
    data_sheet = w22_algo2_term_01
    time.sleep(delay)
    result2, anticounter2 = search_requests(search_query, data_sheet, False, False, False, False)
    unique_result = list(set(result1 + result2))
    print(unique_result)
