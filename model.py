class Habit:
    def __init__(self,name):
        self.name = name
        self.streak = 0
        self.xp = 0
        self.miss_count = 0
        
    def update_streak(self,completed):
        if completed:
            self.streak += 1
            self.miss_count = 0
        else:
            self.miss_count +=1 
            
            # trial miss (first miss no reset of streak)
            if self.miss_count == 1:
                self.streak = max(0, self.streak - 1)
            # for continuous miss/not following habit goals
            else: 
                self.streak = 0 #here the full strak will be reset to zero
                
    def gain_xp(self):
        # this should return base_xp + streak bonus
        base_xp = 10
        streak_multiplier = 1 + (self.streak//5)*0.5
        if self.streak >= 7:
            combo_bonus = 5
        else:
            combo_bonus = 0
        
        return int((base_xp * streak_multiplier) + combo_bonus)
    
    #status messages if you maintain streak
    def get_streak_title(self):
        if self.streak >= 10:
            return "Unstoppable"
        elif self.streak >= 5:
            return "On Fire"
        elif self.streak >= 3:
            return "Momentum has been built."
        else:
            return "Starting"
        
    #status messages if you are losing streak
    def get_status_message(self):
        if self.miss_count >= 2:
            return "Streak lost!"
        elif self.miss_count == 1:
            return "Careful! Don't break the streak!"
        else:
            return "Keep going!"


class Player: #for the player profile system
    def __init__(self):
        self.total_xp = 0
        self.level = 1
    
    def add_xp(self, xp):
        self.total_xp += xp
        self.level = self.total_xp // 100 + 1