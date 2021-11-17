import random


####### Game Logic Tool Ends ###########
class GuessingGameTools:


    def show_title(self):
        print("""
            **************************************************************************
            **************************************************************************
                                        Guessing Game
            **************************************************************************
            **************************************************************************
        
        """)


    def generat_random_number(self, min, max):
        return random.randrange(min, max)


    def show_rules(self, min, max):
        print(f"""
            $$$$ YOU CAN GUESS ANY INTEGER NUMBER from ({min}) to ({max}) $$$$
        """)
####### Game Logic Tool Ends ###########