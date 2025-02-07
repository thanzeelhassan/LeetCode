class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)
        ans = []
        balls_colours = {}
        colours_count = {}

        for query in queries:
            u = query[0]
            v = query[1]
            if u in balls_colours:
                temp = balls_colours[u]
                balls_colours[u] = v
                colours_count[temp] -= 1
                if colours_count[temp] == 0:
                    del colours_count[temp]
                if v in colours_count :
                    colours_count[v] += 1
                else:
                    colours_count[v] = 1
            else:
                balls_colours[u] = v
                if v in colours_count :
                    colours_count[v] += 1
                else:
                    colours_count[v] = 1 
       
            ans.append(len(colours_count))

        return ans
