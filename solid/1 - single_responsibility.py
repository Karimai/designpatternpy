"""
The class should have only one main purposes.
The class should only have one reason to change.
It is also called Separation of concerns: different classes handling different, independent tasks/problems.
"""

class Candidates:
    # The primary responsibility is keeping the candidate data.
    # There should be only one reason to change a class, and it
    # should be related to the primary goal of the class.
    def __init__(self):
        self.candidates = []

    def add_candidate(self, candidate: str):
        self.candidates.append(f"{len(self.candidates)}: {candidate}")

    def remove_candidate(self, pos):
        del self.candidates[pos]

    def __str__(self):
        return '\n'.join(self.candidates)

    def clear(self):
        self.candidates.clear()

    # Wrong design. save and load with file system
    # should not be part of this class
    # It is a secondary responsibility.
    # Avoid Anti-pattern!
    # def save(self, file_name: str):
    #     with open(file_name, 'w') as fh:
    #         fh.write(str(self))
    #
    # def load(self, file_name: str):
    #     with open(file_name, 'r') as fh:
    #         lines = fh.readlines()
    #         for line in lines:
    #             self.add_candidate(line.split(': ')[1])


class PersistanceManager:
    @staticmethod
    def save(data: Candidates, file_name: str):
        with open(file_name, 'w') as fh:
            fh.write(str(data))

    @staticmethod
    def load(data: Candidates, file_name: str):
        with open(file_name, 'r') as fh:
            lines = fh.readlines()
            for line in lines:
                data.add_candidate(line.split(': ')[1])


c = Candidates()
c.add_candidate('Karim')
c.add_candidate('Javad')

print(c)

# c.save('candidates.txt')
# c.clear()
# c.load('candidates.txt')
# print(c)

PersistanceManager.save(c, 'candidates.txt')
c.clear()
PersistanceManager.load(c, 'candidates.txt')
print(c)
