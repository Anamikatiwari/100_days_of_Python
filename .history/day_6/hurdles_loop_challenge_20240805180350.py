#Reeborg's World

#hurdle solution
def hurdle_right(velocities, max_height):
    n = len(velocities)
    time = [max_height / v for v in velocities]
    return min(time) * n



