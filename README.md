# intconcat
Finding out how to concatonate integers for maximum value using... brute force!

## For example:
Input:
```
100 10 76 42 91
```

Output:
```
91764210100
```

Process:

```
100   10   76   42   91
 |    |    /    /    |
 |    |   /    /     \
 |    |  /    /       \
 |    \_/____/_        \
 \_____/____/__\____    \
      /    /    |    \   \
      |    |    |    |    |
      |    |    |    |    |
      |    |    |    |   /
     _|____|____|____|_/
    / |    |    |    |
   /  |    |    |    |
  /   |    |    |    |
 V    V    V    V    V
91   76   42   10   100

91764210100
```
