/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int Depth(struct TreeNode* root, int d){
    int d1 = 0, d2 = 0;
    if(root == NULL) return d;
    d = d + 1;
    d1 = Depth(root->left, d);
    d2 = Depth(root->right, d);
    return d1 >= d2 ? d1 : d2;
}
int maxDepth(struct TreeNode* root) {
    int d = 0;
    return Depth(root, d);
}