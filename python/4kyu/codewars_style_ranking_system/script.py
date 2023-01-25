class User:

    def __init__(self, rank = int, progress = int):
        self.RANKS = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        self.rank = -8
        self.progress = 0

    def inc_progress(self, rank):
        current_rank_index, current_challenge_index = self.get_ranks(rank)
        difference = self.check_ranks(current_rank_index, current_challenge_index)
        self.update_progress(difference)
        if current_rank_index == 15:
            self.rank = 8
            self.progress = 0
            return  
        else:    
            self.upgrade_rank()

    def update_progress(self, difference):
        if difference == 0:
            self.progress += 3
        elif difference >= 1:
            self.progress += (difference * (10 * difference))
        elif difference == -1:
            self.progress += 1
        elif difference <= -2:
            self.progress += 0
        return

    def upgrade_rank(self):
        x = self.progress // 100
        if x == 0:
            self.progress = self.progress
            return
        
        if self.rank == 8:
            self.rank = 8
            self.progress = 0
            return

        if x >= 15:
            self.rank = 8
            self.progress = 0
            return

        if x >= 0:
            self.progress -= (x * 100)
            x = self.RANKS[self.RANKS.index(self.rank) + x]
            self.rank = x
            if self.rank == 8:
                self.rank = 8
                self.progress = 0
            return


    def check_ranks(self, curr_rank, curr_challenge):
        return curr_challenge - curr_rank

    def get_ranks(self, rank):
        return self.RANKS.index(self.rank), self.RANKS.index(rank)
    


user = User()

print("BEGINNING")

print(user.rank)
print(user.progress)

user.inc_progress(8)

print("*****************")
print(user.rank)
print(user.progress)





# test.assert_equals(user.progress, 0)
# user.inc_progress(-7)
# test.assert_equals(user.progress, 10)
# user.inc_progress(-5)
# test.assert_equals(user.progress, 0)
# test.assert_equals(user.rank, -7)


