import datetime


def calculate_fine(expected_date, actual_date):
    if actual_date <= expected_date:
        return 0
    elif actual_date.year == expected_date.year:
        if actual_date.month == expected_date.month:
            return 15 * (actual_date.day - expected_date.day)
        else:
            return 500 * (actual_date.month - expected_date.month)
    else:
        return 10000


if __name__ == '__main__':
    actual_date = list(map(int, input().strip().split()))
    expected_date = list(map(int, input().strip().split()))
    actual_date = datetime.datetime(
        actual_date[2], actual_date[1], actual_date[0])
    expected_date = datetime.datetime(
        expected_date[2], expected_date[1], expected_date[0])
    fine = calculate_fine(expected_date, actual_date)
    print(fine)
