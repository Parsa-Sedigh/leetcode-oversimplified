from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        hungry_num = 0

        while students:
            if students[0] == sandwiches[0]:
                hungry_num = 0
                students.pop(0)
                sandwiches.pop(0)
            else:
                hungry_num += 1
                students.append(students.pop(0))

            if hungry_num >= len(students):
                return len(students)

        return len(students)