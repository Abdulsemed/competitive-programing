class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        student = deque(students)
        index = 0
        while count < len(student) and index < len(sandwiches):
            curr = student.popleft()
            if curr == sandwiches[index]:
                count = 0
                index += 1
            else:
                count += 1
                student.append(curr)
                
        return len(student)