def second_index(text, some_str):
  first_id = text.find(some_str)

  if first_id == -1:
      return None

  second_id = text.find(some_str, first_id + 1)
  if second_id == -1:
    return None

  return second_id # some_string.index(some_str)

print(second_index("Hello, hello", "lo"))