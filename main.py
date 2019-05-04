#function determines if board is valid
def is_board_valid(configuration):
    if configuration[0] > 0 and configuration[1] > 0 and configuration[2] > 0 \
    and configuration[3] > 0 and configuration[4] > 0 and configuration[5] > 0 \
    and configuration[6] > 0 and configuration[2] > configuration[1] \
    and configuration[4] - configuration[3] > configuration[2] \
    and configuration[6] - configuration[5]> configuration[4] \
    and configuration[6] < configuration[0]:
        return True
    else:
        return False
    
#function to obtain score
def get_score(configuration, position):
    pos_angle = abs(position[1])
    
    #if the dart lands on the wire then the score is 0
    if position[0] == configuration[1]/2 or position[0] == configuration[2]/2 \
    or position[0] == configuration[4] \
    or position[0] == (configuration[4] - configuration[3]) \
    or position[0] == configuration[6] \
    or position[0] == (configuration[6] - configuration[5]) \
    or position[0] > configuration[0]/2 \
    or (pos_angle - ((pos_angle//360) * 360)) == 9 \
    or (pos_angle - ((pos_angle//360) * 360)) == 27 \
    or (pos_angle - ((pos_angle//360) * 360)) == 45 \
    or (pos_angle - ((pos_angle//360) * 360)) == 63 \
    or (pos_angle - ((pos_angle//360) * 360)) == 81 \
    or (pos_angle - ((pos_angle//360) * 360)) == 99 \
    or (pos_angle - ((pos_angle//360) * 360)) == 117 \
    or (pos_angle - ((pos_angle//360) * 360)) == 135 \
    or (pos_angle - ((pos_angle//360) * 360)) == 153 \
    or (pos_angle - ((pos_angle//360) * 360)) == 171 \
    or (pos_angle - ((pos_angle//360) * 360)) == 189 \
    or (pos_angle - ((pos_angle//360) * 360)) == 207 \
    or (pos_angle - ((pos_angle//360) * 360)) == 225 \
    or (pos_angle - ((pos_angle//360) * 360)) == 243 \
    or (pos_angle - ((pos_angle//360) * 360)) == 261 \
    or (pos_angle - ((pos_angle//360) * 360)) == 279 \
    or (pos_angle - ((pos_angle//360) * 360)) == 297 \
    or (pos_angle - ((pos_angle//360) * 360)) == 315 \
    or (pos_angle - ((pos_angle//360) * 360)) == 333 \
    or (pos_angle - ((pos_angle//360) * 360)) == 351:
        return 0
        
    #if the dart lands on the inner bullseye, score 50
    if position[0] < configuration[1]/2:
        return 50
        
    #if the dart lands on the outter bullseye, score 25
    if position[0] < configuration[2]/2:
        return 25
        
    """
    if the dart lands on the triple value, score the triple value for that
    specific point value
    """
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 9:
        return 15
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3])\
    and  (pos_angle - ((pos_angle//360) * 360)) < 27:
        return 12
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3])\
    and  (pos_angle - ((pos_angle//360) * 360)) < 45:
        return 9
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 63:
        return 6
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 81:
        return 3
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 99:
        return 60
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 117:
        return 57
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 135:
        return 54
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 153:
        return 51
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3])\
    and  (pos_angle - ((pos_angle//360) * 360)) < 171:
        return 48
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 189:
        return 45
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 207:
        return 42
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 225:
        return 39
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 243:
        return 36
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 261:
        return 33
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 279:
        return 30
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 297:
        return 27
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 315:
        return 24
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3])  \
    and  (pos_angle - ((pos_angle//360) * 360)) < 333:
        return 21
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3])  \
    and  (pos_angle - ((pos_angle//360) * 360)) < 351:
        return 18
            
    """
    if the dart lands on the double value, score the double value for that
    specific point value
    """
    if position[0] < configuration[6] \
    and position[0] > (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 9:
        return 10
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3])\
    and  (pos_angle - ((pos_angle//360) * 360)) < 27:
        return 8
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3])\
    and  (pos_angle - ((pos_angle//360) * 360)) < 45:
        return 6
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 63:
        return 4
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 81:
        return 2
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 99:
        return 40
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 117:
        return 38
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 135:
        return 36
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 153:
        return 34
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3])\
    and  (pos_angle - ((pos_angle//360) * 360)) < 171:
        return 32
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 189:
        return 30
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 207:
        return 28
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 225:
        return 26
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 243:
        return 24
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 261:
        return 22
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 279:
        return 20
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 297:
        return 18
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 315:
        return 16
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3])  \
    and  (pos_angle - ((pos_angle//360) * 360)) < 333:
        return 14
    if position[0] < configuration[4] \
    and position[0] > (configuration[4] - configuration[3])  \
    and  (pos_angle - ((pos_angle//360) * 360)) < 351:
        return 12
            
    #score if the dart lands on blank spaces of its specific values
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 9:
        return 5
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 27:
        return 4
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 45:
        return 3
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 63:
        return 2
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 81:
        return 1
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 99:
        return 20
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 117:
        return 19
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 135:
        return 18
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 153:
        return 17
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 171:
        return 16
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 189:
        return 15
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 207:
        return 14
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 225:
        return 13
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 243:
        return 12
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 261:
        return 11
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 279:
        return 10
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 297:
        return 9
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 315:
        return 8
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 333:
        return 7
    if position[0] < (configuration[4] - configuration[3]) \
    or position[0] < (configuration[6] - configuration[5]) \
    and  (pos_angle - ((pos_angle//360) * 360)) < 351:
        return 6

print("Please enter dart board parameters below.")

"""asks for all dart board parameters, prints them, and converts them to 
float for calculation purposes
"""
board_diameter = input("Board diameter => ")
print(board_diameter)
board_diameter = float(board_diameter)

inner_diameter = input("Inner bull's eye diameter => ")
print(inner_diameter)
inner_diameter = float(inner_diameter)

outer_diameter = input("Outer bull's eye diameter => ")
print(outer_diameter)
outer_diameter = float(outer_diameter)

triple_ring_width = input("Triple ring width => ")
print(triple_ring_width)
triple_ring_width = float(triple_ring_width)

triple_ring_distance = input("Distance from the center to the outside edge " + 
                             "of the triple ring => ")
print(triple_ring_distance)
triple_ring_distance = float(triple_ring_distance)

double_ring_width = input("Double ring width => ")
print(double_ring_width)
double_ring_width = float(double_ring_width)

double_ring_distance = input("Distance from the center to the outside edge " + 
                             "of the double ring => ")
print(double_ring_distance)
double_ring_distance = float(double_ring_distance)

radial_coordinate = input("Enter the radial coordinate (r) of the point " + 
                          "where the dart landed => ")
print(radial_coordinate)
radial_coordinate = float(radial_coordinate)

angular_coordinate = input("Enter the angular coordinate (phi) of the point " + 
                           "where the dart landed => ")
print(angular_coordinate)
angular_coordinate = float(angular_coordinate)

"""
places all dartboard parameters in the configuration tuple which is used in 
the is_board_valid and the get_score funtion
"""
configuration = (board_diameter, inner_diameter, outer_diameter, \
                 triple_ring_width, triple_ring_distance, double_ring_width, \
                 double_ring_distance)

#places dart location in the position tuple, used in the get_score funtion
position = (radial_coordinate, angular_coordinate)

"""
If the dart board is not valid, state that there are invalid parameters
If the dart board is valid determine score of throw
"""
if is_board_valid(configuration) == False:
    print("Invalid dartboard parameter(s) specified.")
else:
    print("This throw scored " + str(get_score(configuration, position)) +".")