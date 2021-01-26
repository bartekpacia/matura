def fibonacci(k: int) -> int:
  while 
    return 1
  else:
    return (fibonacci(k - 1) + fibonacci(k - 2) % 26)

def szyfruj(s: str) -> str:
  szyfr = [0] * len(s)

  for i, _ in enumerate(s):
    szyfr[i] = chr(65 + (ord(s[i]) - 65 + fibonacci(i)) % 26)

  return "".join(szyfr)


print(szyfruj("JANKOWALSKIPOZDRAWIA"))
print(szyfruj("NIEPRZYJACIELNADCHODZI"))
