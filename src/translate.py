from typing import Optional
def translate(json_data: dict, *, separator = ";", file = None) -> Optional[str]:
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
  file.write("\n".join(nl))
  return
