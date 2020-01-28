def catAndMouse(x, y, z):
    abs_valueX = abs(x - z) 
    abs_valueY = abs(y - z)
    if abs_valueX < abs_valueY:
        return 'Cat A'
    elif abs_valueY < abs_valueX:
        return 'Cat B'
    else:
        return 'Mouse C'

if __name__ == '__main__':
    fptr = open('Output', 'w')

    q = int(input('Input number of queries: '))

    for q_itr in range(q):
        xyz = input('Enter {} lines of space-sparated queries'.format(q)).split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print('{}\n'.format(result))
        fptr.write(result + '\n')
    fptr.close()
