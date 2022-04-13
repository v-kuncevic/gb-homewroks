done_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
recount_list = [j for i, j in zip(done_list, done_list[1:]) if j > i]
print(recount_list)
