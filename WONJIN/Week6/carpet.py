def solution(brown, yellow):
    for width in range(3, 5000):
        for height in range(3, width+1):
            b = width*2 + (height-2)*2
            y = (width-2)*(height-2)
            if b == brown and y == yellow:
                return [width, height]
    answer = [width, height]
    return answer