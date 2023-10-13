# Serie 6B
## Programmieren für Naturwissenschaften FS 2023
### Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet

### Aufgabe 1:

	a, b = 2, 1
	c = 3

	d = c + a - b
	d = 4 (int)

	e = a * b + a
	e = 4 (int)

	e += a ** c
	e = 12 (int)

	f = e // a / b
	f = 6.0 (float)

	c *= c / b
	c = 3 (int)

	a = e + f - c
	a = 18.0 (float)

Code zum überprüfen: S6BA1.py

### Aufgabe 2:

Betrachten Sie die Liste values in folgender Abbildung:

	values 	-1 2 7 7 4 3 99 5 8
	index	 0 1 2 3 4 5  6 7 8
	
Was ist:

	(a) values[2]	
	7

	(b) values[1] + values[3]
	9

	(c) values[1+3]
	4

	(d) values.index(7)
	2

	(e) values.pop()
	8
	wird entfernt und zurückgegeben

	values 	-1 2 7 7 4 3 99 5
	index	 0 1 2 3 4 5  6 7

	(f) values[3:5] = [5, 7]
	values[3] = 5
	values[4] = 7
	values 	-1 2 7 5 7 3 99 5
	index	 0 1 2 3 4 5  6 7

	(g) values.sort()
	values 	-1 2 3 5 5 7 7 99
	index	 0 1 2 3 4 5 6  7

	(h) values[2::]
	3, 5, 5, 7, 7, 99

	(i) values[-1:1:-1]
	99, 7, 7, 5, 5, 3

	Welche Code-fragmente werden benötigt um folgende Aufgaben zu erledigen?
	(j) Addieren Sie zum Element an Position 4 denWert 18.
	values[4] += 18

	(k) Lesen Sie den Wert an Position 3 aus und speichern Sie ihn in der Variable number.
	number = values[3]

	(l) Ersetzen Sie den Wert an Position 2 mit demWert an Position 7 un umgekehrt.
	values[2], values[7] = values[7], values[2]

### Aufgabe 3:

	S6BA3.py
