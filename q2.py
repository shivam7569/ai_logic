def substring(main_string, search_string):
  
  s = main_string.lower()
  t = search_string.lower()
  if main_string == search_string: return main_string
  
  len_t = len(t)

  found, ans = 0, None
  for search_len in range(len_t, len(s)):
    if not found:
      for i in range(len(s)):
        if s[i] in t:
          last_index = min(i+search_len, len(s))
          check_string = s[i: last_index]
          if len(set(check_string).intersection(set(t))) == len_t:
            found = 1
            ans = [i, last_index]
            break

  return main_string[ans[0]: ans[1]]
