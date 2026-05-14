class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = []
        l_t = []
        for elem in strs:
            d = dict()
            for item in elem:
                if item not in d:
                    d[item] = 0
                d[item] += 1
            l_t.append((elem, d))
        print(l_t)
        for i, ele1 in enumerate(l_t):
            l_i = []
            l = [item for sublist in final_list for item in sublist]
            if ele1[0] not in l:
                l_i.append(ele1[0])
                print(f'Before loop {l_i}')
            if len(l_t) > i+1:

                for j, ele2 in enumerate(l_t[i+1::]):
                    if ele1[1] == ele2[1]:
                        if ele2[0] not in l:
                            print(f'sublist: {l}')
                            l_i.append(ele2[0])
                            print(f'After loop {l_i}')
            if l_i != []:
                final_list.append(l_i)
            print(f'Final List: {final_list}')
        return final_list