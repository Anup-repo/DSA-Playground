package Tree.LearnYard.Binary_Tree_Preoder_traversal;
import java.util.ArrayList;

class Node {
    int val;
    Node left, right;

    public Node(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

public class Preorder {
    public static void preorder_traversal(Node root, ArrayList<Integer> result) {
        if (root == null) {
            return;
        }
        result.add(root.val);
        preorder_traversal(root.left, result);
        preorder_traversal(root.right, result);
    }

    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);

        ArrayList<Integer> result = new ArrayList<Integer>();
        preorder_traversal(root, result);

        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
