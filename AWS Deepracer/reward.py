def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    on_track = params['all_wheels_on_track']
    steering = params['steering_angle']
    speed = params['speed']
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        if speed > 3:
            reward = 5.0
        else:
            reward = 4.5
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track
        
    if -5 < steering < 5:
        if speed > 3:
            reward += 5.0
        elif speed > 2:
            reward += 1.0
    elif steering < -15 or steering > 15:
        if speed < 2:
            reward += 1.0
        elif speed < 2.5:
            reward += 2.0
    
    if on_track:
        reward += 1.0
    else:
        reward += 1e-5
        
    return float(reward)