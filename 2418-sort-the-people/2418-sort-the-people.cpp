class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        int size = names.size();
        for (int index = 0; index < size; index++){
            bool flag = true;
            for (int val = 0; val < size - index-1; val++){
                if (heights[val] < heights[val+1]){
                    int temp = heights[val];
                    string name = names[val];
                    names[val] = names[val+1];
                    names[val+1] = name;
                    heights[val] = heights[val+1];
                    heights[val+1] = temp;
                    flag = false;
                }
            }
            if (flag){
                break;
            }
        }
        return names;
    }
};