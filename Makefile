all:
	echo "Hello $(LOGNAME), python codes does not need to be compiled."

run1: 
	PYTHONPATH=. /usr/bin/python3 task1.py
    
run2A: 
	PYTHONPATH=. /usr/bin/python3 task2a.py

run2B:
	PYTHONPATH=. /usr/bin/python3 task2b.py

run3: 
	PYTHONPATH=. /usr/bin/python3 task3.py

run4: 
	PYTHONPATH=. /usr/bin/python3 task4.py

run5: 
	PYTHONPATH=. /usr/bin/python3 task5.py

run6A:
	PYTHONPATH=. /usr/bin/python3 task6a.py

run6B:
	PYTHONPATH=. /usr/bin/python3 task6b.py

run7:
	PYTHONPATH=. /usr/bin/python3 task7.py

run8:
	PYTHONPATH=. /usr/bin/python3 task8.py

plot:
	PYTHONPATH=. /usr/bin/python3 src/plot.py

test:
	PYTHONPATH=.:./src /usr/bin/python3 -m unittest