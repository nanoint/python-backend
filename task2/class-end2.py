lesson_number = int(input())
end_time = 9 * 60 + lesson_number * 45 + (lesson_number // 2) * 15 + (lesson_number - 1 - lesson_number // 2) * 5
print(end_time // 60, end_time % 60)
