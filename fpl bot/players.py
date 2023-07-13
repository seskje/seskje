possible_positions = ["keeper","defender","midfield","forward"]
class Player:

    def __init__(self,name,price,position,xp,xmin):
        
        if  isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name must be a string")
        
        if isinstance(price, float) and 16.0 > price > 0.0:
            self.price = price
        else:
            raise TypeError("Price must be a float between 0.0 and 16.0")
        
        if isinstance(position, str) and position in possible_positions:
            self.position = position
        else:
            raise TypeError("Position must be a string in possible positions")

        if isinstance(xp, float) and 0.0 < xp:
            self.xp = xp
        else:
            raise TypeError("Expected points must be a float greater than 0")
        
        if isinstance(xmin,int) and 0 < xmin < 90:
            self.xmin = xmin
        else:
            raise TypeError("Expected minutes must be an int between 0 and 90")


        
    
    def update_price(self,new_price):
         if isinstance(new_price, float) and 16.0 > new_price > 0.0:
            self.price = new_price
         else:
            raise TypeError("Price must be a float between 0.0 and 16.0")
    
    def update_xp(self,new_xp):
        if isinstance(new_xp, float) and 0.0 < new_xp:
            self.xp = new_xp
        else:
            raise TypeError("Expected points must be a float greater than 0")
    
    def upate_xmin(self,new_xmin):
        if isinstance(new_xmin,int) and 0 < new_xmin < 90:
            self.xmin = new_xmin
        else:
            raise TypeError("Expected minutes must be an int between 0 and 90")
    
    def show_stats(self):
        print("name: " + str(self.name) + "\n price: " + str(self.price) + "\n position: "+ str(self.position) + "\n expected points: "+ str(self.xp) + "\n xmin: " + str(self.xmin))
        



class Keeper(Player):

    def __init__(self,name,price,position,xp,xmin):
        super().__init__(name,price,position,xp,xmin)

class Defender(Player):

    def __init__(self,name,price,position,xp,xmin):
        super().__init__(name,price,position,xp,xmin)

class Midfield(Player):

    def __init__(self,name,price,position,xp,xmin):
        super().__init__(name,price,position,xp,xmin)

class Forward(Player):

    def __init__(self,name,price,position,xp,xmin):
        super().__init__(name,price,position,xp,xmin)
    