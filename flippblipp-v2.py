def flippblipp(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 != 0:
            return 'flipp'
        elif i % 5 == 0 and i % 3 != 0:
            return 'blipp'
        elif i % 5 == 0 and i % 3 == 0:
            return 'flipp blipp'         
        else:
            return str(i)
        
        

        


flippblipp(3)