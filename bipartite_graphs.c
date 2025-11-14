/*Leetcode Bipartite Problem 785*/



bool isBipartite(int** graph, int graphSize, int* graphColSize)
{
    int *colors = malloc(sizeof(int) * graphSize);
    if (!colors) return false;

    for (int i = 0; i < graphSize; i++) {
        colors[i] = 0; 
    }

    int queue[101];
    int head = 0;
    int tail = 0;


    queue[tail] = 0;
    colors[tail] = 1;       
    tail++;

    while (head != tail)
    {
        int curr = queue[head++];
        int currColor = colors[curr];
        int nextColor = (currColor == 1) ? 2 : 1;


        for (int i = 0; i < graphColSize[curr]; i++)
        {
            int neighbor = graph[curr][i];

            if (colors[neighbor] == 0)
            {
                colors[neighbor] = nextColor;
                queue[tail++] = neighbor;
            }
            else if (colors[neighbor] == currColor)
            {
                free(colors);
                return false;
            }
        }
    }

    free(colors);
    return true;
}



