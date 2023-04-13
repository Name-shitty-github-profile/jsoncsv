# jsoncsv
A small and simple json to csv module with custom separators
# translate
```python
translate(json_data: dict, *, separator = ";", file = None, file_and_return = False) -> Optional[str]
```
This function translate some json data into a csv data and returns it in a file or in a string
## json_data
The json data that will turned some json data into a csv string
## separator
The separator for the csv string (normaly ";", "," or " ")
## file
the file that the data will be written to (optional)
## file_and_return
if there is a file, does it return the result
