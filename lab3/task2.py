def find_common_participants(first_group, second_group, separator=','):
    first_list = first_group.split(separator)
    second_list = second_group.split(separator)

    participants = list(set(first_list).intersection(second_list))
    participants.sort()

    return participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, '|')
print("Общие участники:", common_participants)
