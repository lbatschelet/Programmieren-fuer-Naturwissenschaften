# Serie 8
## Programmieren für Naturwissenschaften FS 2023
### Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet

### Aufgabe 1: Gegeben seien die folgenden Anweisungen, welche eine oder mehrere Zufallszahlen generieren:
	(a) int[1, 100[ nur ungerade	random.randrange(1, 100, 2)
	(b) int[2, 3, 4, 5, 9, 10]		random.choice([2, 3, 4, 5, 9, 10])
	(c) int[0, 100]					random.randint(0, 100)
	(d) float[50, 200[				random.uniform(50, 200)
	(e) liste mit 3 Elementen aus 11, 12, 13, 14, 15, 16, 17] 
					random.sample([11, 12, 13, 14, 15, 16, 17], 3)
	(f) float[0, 1[			random.random()

Geben Sie für jede Anweisung das Intervall an, in welchem die Zufallszahlen gewählt werden und welcher Datentyp die Zufallszahlen jeweils aufweisen.

### Aufgabe 2:
Was ist das Resultat der folgenden Ausdrücke?

	(a) 64	=	math.pow(4, 3)
	(b) -1 	=	math.cos(math.pi)
	(c) 4	=	math.floor(4.5)
	(d) 10	=	math.ceil(math.sqrt(99))
	(e) ln(2)	math.log(2)

### Aufgabe 3:
S8A3.py

benötigt passagierdaten.csv von Ilias