import re

text = "שלום כיתה א"
print(text)
print(ord(text[-1]))
print(text[-1])

match = re.search(r"[א-ת]", text)
print(match.group(0))  # ש

match = re.search(r"[א-ת]*", text)
print(match.group(0))  # שלום

match = re.search(r"[ א-ת]*", text)
print(match.group(0))  # שלום כיתה א

# Hebrew has 22 letters, 5 of them have a different version at the end of the word
# A total of 27 letters
for ix in range(1488, 1488+27):
    print(f"{ix} {chr(ix)}")

# 1488 א
# 1489 ב
# 1490 ג
# 1491 ד
# 1492 ה
# 1493 ו
# 1494 ז
# 1495 ח
# 1496 ט
# 1497 י
# 1498 ך
# 1499 כ
# 1500 ל
# 1501 ם
# 1502 מ
# 1503 ן
# 1504 נ
# 1505 ס
# 1506 ע
# 1507 ף
# 1508 פ
# 1509 ץ
# 1510 צ
# 1511 ק
# 1512 ר
# 1513 ש
# 1514 ת

