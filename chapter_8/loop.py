#!/usr/bin/env python

def loop(f, t, step):
	if step > 0:
		t += 1
	elif step < 0:
		t -= 1
	else:
		return
	print [i for i in range(f, t, step)]

loop(2, 26, 4)
loop(-10, -1, 1)
loop(10, 20, 0)
