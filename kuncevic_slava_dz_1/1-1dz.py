duration = int(input("Duration: "))
if duration < 60:
    print(str(duration) + " сек ")
elif duration < 60 * 60:
    print(str(duration // 60) + " мин " + str(duration % 60) + " сек ")
elif duration < 60 * 60 * 24:
    print(str(duration // 3600) + " час " + str(duration % 3600 // 60) + " мин " + str(duration % 60) + " сек ")
else:
    print(str(duration // (24 * 3600)) + " дн " + str(duration % (24 * 3600) // 3600) + " час "
          + str(duration % (24 * 3600) % 3600 // 60) + " мин " + str(duration % 60) + " сек ")
