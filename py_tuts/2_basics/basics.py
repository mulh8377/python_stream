"""
@author: Jared M
"""
def int_ex():
    """
    @function_name      :   int_ex
    @parameters         :   
    @return             :   void
    @description        :   Int Examples
    """
    x = 5           # x := 5
    print(x)        # println(x)
    x = 3
    print(x)
    
    print(x + 5)
    print(x - 5)
    print(x * 5)
    print(int(x / 2))    # notice this!
    
    print(x < 4)        # false
    print(x > 2)        # true
    print(x == 5)       # true
    print(x != 5)       # false
                                        # 0, 1, 2, 3
    x_storage = [5, 10, 15, 20]         # 5, 10, 15, 20
    print(x_storage)
    
    for pokimane in x_storage:
        print(pokimane)
        pokimane = 10
        
    print(pokimane)
    
def flt_ex():
    #print('flt test')
    x = 5.0
    print(x + 2.0)
    
    print(x - 2.0)
    
    print(x * 3.0)
    
    print(x / 3.0)
    
    print(x < 2.0)
    print(x > 4.0)
    print(x == 5.0)
    print(x != 5.0)
    
    flt_store = [5.0, 10.0, 15.0, 20.0]
    print(flt_store)
    
    total = 0
    for f in flt_store:
        total += f
    print(total)
    print(sum(flt_store))
    
    print(total == sum(flt_store))
    
def str_ex():
    twitch = "tosstosstoss"
    mixer = "3xtoss"
    caffeine_tv = "3xtoss"
    
    
    twitter = "3xtoss"
    github = "mulh8377"
    email = "3xtoss@gmail.com"
    
    print("# " +  "Streams:")
    print("## TTV: " + twitch)
    print("## MIX: " + mixer)
    print("## CAF: " + caffeine_tv)
    
    print("# " +  "Contact:")
    print("## Tweeter: " + twitter)
    print("## Git: " + github)
    print("## Email :" + email)
    
    print(len(twitch))
    
"""
while True:

1. Base Condition ----> break from the loop
2. Other Possible Outcomes. ---> thats the sign to do an operation.
3. Error Condition ----> system exit


== (equal to), != (not equal to)

> (greather than), < (not greater than)

1 ---> True
0 ---> False

"""

def bool_ex():
    girl = "Stacy"
    boy = "Chad"
    girl_single = False
    boy_single = True
    girl_age = 19
    boy_age = 22
    
    can_they_date = girl_single == boy_single
    print(can_they_date)
    
    will_chad_try = girl_single != boy_single
    print(will_chad_try)
    
    # <, >, <=, >=
    
    is_it_legal = girl_age > 18 and boy_age > 18
    print(is_it_legal)
    
    is_he_older = boy_age > girl_age
    print(is_he_older)
    
    is_she_younger = girl_age < boy_age
    print(is_she_younger)
    
    same_name = girl == boy
    print(same_name)
    
    

def main():
    int_ex()
    flt_ex()
    str_ex()
    bool_ex()

if __name__ == "__main__":              # fn main() { }
    main()