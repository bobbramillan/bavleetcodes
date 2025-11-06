/* 
    problem 62 unique paths
*/

/**
    python version:
    def uniquePaths(self, n, m):
        if n == 1 or m == 1:
            return 1
        else:
            return self.uniquePaths(n-1, m) + self.uniquePaths(n, m-1)
*/

int UP_rec(int m, int n, int **table) {
    if (m == 1 || n == 1)
        return 1;

    if (table[m][n] != -1)  
        return table[m][n];

    table[m][n] = UP_rec(m - 1, n, table) + UP_rec(m, n - 1, table);
    return table[m][n];
}

int uniquePaths(int m, int n) {

    int **table = malloc((m + 1) * sizeof(int *));
    for (int i = 0; i <= m; i++) {
        table[i] = malloc((n + 1) * sizeof(int));
        for (int j = 0; j <= n; j++) {
            table[i][j] = -1;
        }
    }

    int result = UP_rec(m, n, table);

    for (int i = 0; i <= m; i++)
        free(table[i]);
    free(table);

    return result;
}

