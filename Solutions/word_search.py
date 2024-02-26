# https://leetcode.com/problems/word-search/

from collections import Counter
class Solution(object):
    def findNeighbours(self, seq, rows, columns):
        diff = [ (1, 0), (0, 1), (-1, 0), (0, -1) ]
        r, c = seq[-1]
        neighbours = []
        for d in diff:
            if 0 <= r + d[0] < rows and 0 <= c + d[1] < columns:
                neighbours.append((r + d[0], c + d[1]))
        return neighbours

    def exist(self, board, word):
        word_count = Counter(word)
        board_count = Counter(char for row in board for char in row)
        for letter in word_count:
            if word_count[letter] > board_count[letter]:
                return False
        rows = len(board)
        columns = len(board[0])
        word_len = len(word)
        sequences = []
        for r in range(rows):
            for c in range(columns):
                if board[r][c] == word[0]:
                    sequences.append([(r,c)])
        if len(sequences) < 1:
            return False
        if len(sequences[0]) == word_len:
            return True
        for letter in word[1:]:
            new_sequences = []
            for seq in sequences:
                potential_neighbours = self.findNeighbours(seq, rows, columns)
                for nei in potential_neighbours:
                    if board[nei[0]][nei[1]] == letter and nei not in seq:
                        new_sequences.append(seq + [nei])
            if not new_sequences:
                return False
            if len(new_sequences[0]) == word_len:
                return True
            sequences = new_sequences
        return False
