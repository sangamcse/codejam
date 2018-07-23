# Problem GBus Count

There exists a straight line along which cities are built.

Each city is given a number starting from 1. So if there are 10 cities, city 1 has a number 1, city 2 has a number 2,... city 10 has a number 10.

Different buses (named GBus) operate within different cities, covering all the cities along the way. The cities covered by a GBus are represented as 'first_city_number last_city_number' So, if a GBus covers cities 1 to 10 inclusive, the cities covered by it are represented as '1 10'

We are given the cities covered by all the GBuses. We need to find out how many GBuses go through a particular city.

## Input


The first line contains the number of test cases (T), after which T cases follow each separated from the next with a blank line.

For each test case,

The first line contains the number of GBuses.(N) 
Second line contains the cities covered by them in the form 
a<sub>1</sub> b<sub>1</sub> a<sub>2</sub> b<sub>2</sub> a<sub>3</sub> b<sub>3</sub>...a<sub>n</sub> b<sub>n</sub> 
where GBus<sub>1</sub> covers cities numbered from a<sub>1</sub> to b<sub>1</sub>, GBus<sub>2</sub> covers cities numbered from a<sub>2</sub> to b<sub>2</sub>, GBus<sub>3</sub> covers cities numbered from a<sub>3</sub> to b<sub>3</sub>, upto N GBuses.

Next line contains the number of cities for which GBus count needs to be determined (P).

The below P lines contain different city numbers.

## Output

For each test case, output one line containing "Case #T<sub>i</sub>:" followed by P numbers corresponding to the number of cities each of those P GBuses goes through. 

## Limits

1 <= T <= 10

a<sub>i</sub> and b<sub>i</sub> will always be integers.

### Sample

```py
Input 
 	
2
4
15 25 30 35 45 50 10 20
2
15
25

10
10 15 5 12 40 55 1 10 25 35 45 50 20 28 27 35 15 40 4 5
3
5
10
27


Output 
 
Case #1: 2 1
Case #2: 3 3 4
```
