from typing import Optional
def translate(json_data: dict, *, separator = ";", file = None, file_and_return = False) -> Optional[str]:
  """
  # translate
  ```python
  translate(json_data: dict, *, separator = ";", file = None, file_and_return = False) ->   Optional[str]
  A small and simple json to csv module with custom separators
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

  """
  lines = ["", ""]
  done = 0
  for i, j in json_data.items():
    lines[0] += str(i) + separator
    if type(j) is list:
      for k in range(len(j)):
        num = k + 1
        if not num in lines:
          lines.append(done*f"null{separator}")
        lines[num] += j[k] + separator
      del lines[-1]
    else:
      lines[1] += str(j) + separator
    done += 1
    nl = []
    for i in lines:
      nl.append(i[:-len(separator)])
  if file is None:
    return "\n".join(nl)
  if file_and_return:
    result = "\n".join(nl)
    file.write(result)
    return result
  file.write("\n".join(nl))
  return
