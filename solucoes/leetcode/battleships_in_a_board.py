# LeetCode - Battleships in a Board
# https://leetcode.com/problems/battleships-in-a-board/
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        total_ships = 0
        size = len(board)

        for i in range(len(board)):
            same_ship = False
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    if (i > 0 and board[i-1][j] == "X") or same_ship is True:
                        continue
                    total_ships += 1
                    same_ship = True
                else:
                    same_ship = False

        return total_ships
