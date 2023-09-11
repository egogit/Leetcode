class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = dict();

        for i, types in enumerate(groupSizes):
            if types not in group:
                group[types] = list();
            
            if len(group[types]) == 0 or len(group[types][-1]) == types:
                group[types].append([i]);
            else:
                group[types][-1].append(i);
        
        group = sorted(group.items())
        
        ans = list();

        for _, g in group:
            for gps in g:
                ans.append(gps);

        return ans;