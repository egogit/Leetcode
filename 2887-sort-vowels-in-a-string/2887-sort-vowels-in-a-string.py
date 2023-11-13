# insertion sort => Time Limit Exceed
# vowel을 뽑아서 sort하기 => 문제는 Memory Exceed..

class Solution:
    def sortVowels(self, s: str) -> str:
        sList = list(s);
        vowels = [65, 69, 73, 79, 85, 65+32, 69+32, 73+32, 79+32, 85+32];
        idx, vw = list(), list();

        for i in range(len(sList)):
            if ord(sList[i]) in vowels:
                idx.append(i);
                vw.append(sList[i]);
        vw.sort();
        
        iidx = 0;
        for i in idx:
            sList[i] = vw[iidx];
            iidx += 1;

        ans = ''.join(sList);

        return ans