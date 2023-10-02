#include <iostream>
#include <vector>
using namespace std;

class Trie {
public:
    Trie() {
        children = vector<Trie*>(2, nullptr);
        is_end = false;
    }

    void insert(const string& binary) {
        Trie* curr = this;
        for (char c : binary) {
            int index = c - '0';
            if (curr->children[index] == nullptr) {
                curr->children[index] = new Trie();
            }
            curr = curr->children[index];
        }
        curr->is_end = true;
    }

    int search(const string& binary) {
        Trie* curr = this;
        int maxim = 0;
        int level = 30;
        for (char c : binary) {
            int index = c - '0';
            bool flag;
            if (c == '1') {
                if (curr && curr->children[0]) {
                    flag = false;
                } else {
                    flag = true;
                }
            } else {
                if (curr && curr->children[1]) {
                    flag = true;
                } else {
                    flag = false;
                }
            }
            if (flag) {
                if (curr) {
                    curr = curr->children[1];
                }
                maxim += (index ^ 1) * (1 << level);
            } else {
                if (curr) {
                    curr = curr->children[0];
                }
                maxim += (index ^ 0) * (1 << level);
            }
            level -= 1;
        }
        return maxim;
    }

private:
    vector<Trie*> children;
    bool is_end;
};

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        int ans = 0;
        Trie* obj = new Trie();
        unordered_map<int, string> dicts;
        for (int num : nums) {
            if (dicts.find(num) == dicts.end()) {
                dicts[num] = bitset<31>(num).to_string();
                obj->insert(dicts[num]);
            }
        }

        for (auto& entry : dicts) {
            ans = max(obj->search(entry.second), ans);
        }

        return ans;
    }
};
