def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']
    pupil_times = intervals.get('pupil', [])
    tutor_times = intervals.get('tutor', [])

    def _normalize_and_clip_intervals(times: list[int]) -> list[tuple[int, int]]:

        if not times:
            return []

        if len(times) % 2 != 0:
            times = times[:-1]

        unmerged_intervals = []
        for i in range(0, len(times), 2):
            if times[i] < times[i + 1]:
                unmerged_intervals.append((times[i], times[i + 1]))

        if not unmerged_intervals:
            return []

        unmerged_intervals.sort()

        merged = []
        current_start, current_end = unmerged_intervals[0]

        for next_start, next_end in unmerged_intervals[1:]:
            if next_start <= current_end:
                current_end = max(current_end, next_end)
            else:
                merged.append((current_start, current_end))
                current_start, current_end = next_start, next_end

        merged.append((current_start, current_end))

        clipped = []
        for start, end in merged:
            overlap_start = max(start, lesson_start)
            overlap_end = min(end, lesson_end)

            if overlap_start < overlap_end:
                clipped.append((overlap_start, overlap_end))

        return clipped

    pupil_intervals = _normalize_and_clip_intervals(pupil_times)
    tutor_intervals = _normalize_and_clip_intervals(tutor_times)

    total_overlap = 0
    p_idx, t_idx = 0, 0

    while p_idx < len(pupil_intervals) and t_idx < len(tutor_intervals):
        p_start, p_end = pupil_intervals[p_idx]
        t_start, t_end = tutor_intervals[t_idx]

        overlap_start = max(p_start, t_start)
        overlap_end = min(p_end, t_end)

        if overlap_start < overlap_end:
            total_overlap += (overlap_end - overlap_start)

        if p_end < t_end:
            p_idx += 1
        else:
            t_idx += 1

    return total_overlap


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                             1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                             1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                             1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
    {
        'name': 'Простой случай с одним пересечением',
        'intervals': {'lesson': [100, 200],
                   'pupil': [110, 150],
                   'tutor': [130, 170]},
        'answer': 20
    },
    {
        'name': 'Нет пересечения',
        'intervals': {'lesson': [100, 200],
                      'pupil': [110, 130],
                      'tutor': [140, 160]},
        'answer': 0
    },
    {
        'name': 'Полное совпадение интервалов с уроком',
        'intervals': {'lesson': [100, 200],
                      'pupil': [100, 200],
                      'tutor': [100, 200]},
        'answer': 100
    }
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       print(f"Test {i}: calculated = {test_answer}, expected = {test['answer']}")
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
   print("All tests passed!")