class Solution(object):
    def queryResults(self, limit, queries):
        color_map = {}  # Stores the color assigned to each ball
        color_count = {}  # Keeps track of how many balls have each color
        distinct_colors = set()  # Tracks unique colors used
        result = []
        
        for x, y in queries:
            # Remove previous color if present
            if x in color_map:
                prev_color = color_map[x]
                color_count[prev_color] -= 1
                if color_count[prev_color] == 0:
                    distinct_colors.remove(prev_color)
            
            # Assign new color
            color_map[x] = y
            if y in color_count:
                color_count[y] += 1
            else:
                color_count[y] = 1
            
            # Add new color to distinct set
            distinct_colors.add(y)
            
            # Store the number of distinct colors
            result.append(len(distinct_colors))
        
        return result
        