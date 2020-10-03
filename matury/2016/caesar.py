def encrypt(s: str, k: int) -> str:
  k = k % 26

  result = []
  for char in s:
    result_index = ord(char) + k

    while result_index > 90:
      result_index = result_index - 26

    schar = chr(result_index)

    result.append(schar)

  return "".join(result)

def decrypt(s: str, k: int) -> str:
  k = k % 26

  result = []
  for char in s:
    result_index = ord(char) - k

    while result_index < 65:
      result_index = result_index + 26

    schar = chr(result_index)

    result.append(schar)

  return "".join(result)
