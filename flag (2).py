class ArgumentError(Exception):
    pass    

def flag(N):

    try:
        N = int(N)
    except:
        raise ArgumentError("'{}' is not a valid integer number".format(N))
    else:
        if N % 2:
            raise ArgumentError("'{}' is not an even number".format(N))

    width = 3 * N
    vert_distance = int(N / 2)
    border_radius = vert_distance # radius of '*'-ring
    inner_radius = vert_distance-1 # radius of inner cyrcle ('o'-area)

    
    def half_hord_length(i):
        return int(round((inner_radius ** 2 - (inner_radius - i) ** 2) ** (1/2))) # half of inner cyrcle hord length by Pythagoras theorem


    border = '#' * (width + 2)
    top_part = border + '\n' + ('#' + ' ' * width + '#\n') * vert_distance # empty space under cyrcle        
    for i in range(border_radius):
      if i == 0 and N>2:
          stars_row_length = half_hord_length(1) - 1 # half-length of top part of cyrcle border
          stars_row_length = 1 if stars_row_length == 0 else stars_row_length
          left_half_row = '#' + ' ' * (int(width / 2) - stars_row_length) + '*' * stars_row_length
      else:
          left_half_row = '#' + ' ' * (int(width / 2) - half_hord_length(i) - 1) + '*' + 'o' * half_hord_length(i) # left part of row containing part of cyrcle
      top_part += (left_half_row + left_half_row[::-1] + '\n') # add row
    result = top_part[:len(top_part)-1:] + top_part[::-1] # add bottom half
    return result

#if __name__ == '__main__':
#  for i in range(1,20):
#      print('N = {}'.format(i*2))
#      print(flag(i*2))

#  N = input('N: ')    
#  print(flag(N))
