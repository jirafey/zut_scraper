## Finding Index Numbers of People from Specific Groups (Including Group Size)


### Adjust (if you try to search through before the start of the semester you can get no results)
Make sure 21 days in the future is actually after the semester has started or change to some other arbitrary value

```python
subtract_from_the_start = 0  # What day to start from? (today - subtract_from_the_start)
add_to_the_end = 21  # What day to end at? (today + add_to_the_end)
```

### Using Index Numbers Based on Results, e.g.
- Results from `Algorithms 2` exam
We can determine a person's **first and last name**.

#### Preferably use fast.py


## Example usage:

#### Changing only 2 last lines of `fast.py`:
```python
# search query can be as many terms long as you want, just bear in mind
# there is no fuzzy search so be extra careful with the spelling
    search_query = "Zarządzanie informacją 1 (L)", "Burak", "S1"
# "S1" - in-person studies, "last name of the professor",
# "Name of the subject add the (L)/(A)/(W) to hit the proper class"
# "221B" - the name of the group if you want to know all the members
# You can also input the dates, starting and ending time of the class

# "and" vs "or" in the query (usually u want to use "and" so that is the default)
    asyncio.run(search_requests(search_query, data_sheet, "and", True, False, False, True))
```

### example from scraping the data of the website using DevTools:
https://plan.zut.edu.pl/schedule_student.php?number=53879&start=2024-05-20T00%3A00%3A00%2B02%3A00&end=2024-05-27T00%3A00%3A00%2B02%3A00


### how to view this type of website by yourself?

1. Hit right click on your browser window and click `Inspect` or hit `F12` to open DevTools
2. Click on the `Network` tab
3. Send a `query` via the `GUI`, EXAMPLE:

![image](https://github.com/jirafey/zut_scraper/assets/97115044/600caee6-7230-4772-940c-f416758aace5)
4. Now in the `Network` tab there should be new entry
5. Double-click wherever on the blue highlighted area of the entry, EXAMPLE:

![image](https://github.com/jirafey/zut_scraper/assets/97115044/7c688786-2486-414a-a68a-3351b4ebda4c)
