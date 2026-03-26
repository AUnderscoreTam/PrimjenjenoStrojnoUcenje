import numpy as np
import matplotlib.pyplot as mpl


def returnCheckerboard(boxSize=0, nBoxesVertical=0, nBoxesHorizontal=0):
    nBoxesHorizontal = nBoxesHorizontal - 1
    nBoxesVertical = nBoxesVertical-1
    checkerBoard = np.zeros((boxSize, boxSize))
    isWhite = False
    while (nBoxesVertical > 0):
        while (nBoxesHorizontal > 0):
            isWhite = not isWhite
            if (isWhite):
                checkerBoard = np.hstack(
                    (checkerBoard, np.ones((boxSize, boxSize))))
            else:
                checkerBoard = np.hstack(
                    (checkerBoard, np.zeros((boxSize, boxSize))))
            nBoxesHorizontal -= 1
            if (nBoxesHorizontal == 0):
                cNrow = checkerBoard
                cNrow = np.asarray(cNrow)
        cNrow = 1 - cNrow
        checkerBoard = np.vstack((checkerBoard, cNrow))
        nBoxesVertical -= 1
    return checkerBoard


mpl.imshow(returnCheckerboard(5, 2, 2), cmap='gray')
mpl.show()
