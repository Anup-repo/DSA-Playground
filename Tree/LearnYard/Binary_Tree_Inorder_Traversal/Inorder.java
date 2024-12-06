package Tree.LearnYard.Binary_Tree_Inorder_Traversal;

import java.util.ArrayList;

class Node {
    int val;
    Node left, right;
    Node(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

public class Inorder {
    public static void inorder_traversal(Node root, ArrayList<Integer> result) {
        if (root == null) {
            return;
        }
        inorder_traversal(root.left, result);
        result.add(root.val);
        inorder_traversal(root.right, result);
    }
    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);

        ArrayList<Integer> result = new ArrayList<>();
        inorder_traversal(root, result);

        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
