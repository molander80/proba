from graph import *
windowSize (600, 600)
canvasSize(600, 600)

alpha = 0.1
def fractal_rectangle(A, B, deep=15):
    if deep <1:
        return
    for M, N in (A, B), (B, A):
        rectangle(*M, *N)
    A1 = (A[0]*(1-alpha) + B[0]*alpha, A[1]*(1-alpha) + B[1]*alpha)
    B1 = (B[0]*(1-alpha) + A[0]*alpha, B[1]*(1-alpha) + A[1]*alpha)

    fractal_rectangle(A1, B1, deep-1)
fractal_rectangle((100,100),(500, 500))
run()