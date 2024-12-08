package Tree.LearnYard.Preorder_Postorder_Inorder_in_a_single_traverse;

import java.util.*;

class Node {
    int val;
    Node left, right;

    Node(int val) {
        this.val = val;
        left = right = null;
    }
}

class Pair {
    Node node;
    int state;

    Pair(Node node, int state) {
        this.node = node;
        this.state = state;
    }
}

public class TreeTraversal {

    public static List<List<Integer>> preInPostTraversal(Node root) {
        List<Integer> preOrder = new ArrayList<>();
        List<Integer> inOrder = new ArrayList<>();
        List<Integer> postOrder = new ArrayList<>();

        if (root == null) {
            return Arrays.asList(preOrder, inOrder, postOrder);
        }

        Stack<Pair> stack = new Stack<>();
        stack.push(new Pair(root, 1)); // Initialize stack with root and state 1

        while (!stack.isEmpty()) {
            Pair current = stack.pop();

            if (current.state == 1) { // Pre-order traversal
                preOrder.add(current.node.val);
                current.state++;
                stack.push(current); // Push back with updated state
                if (current.node.left != null) {
                    stack.push(new Pair(current.node.left, 1)); // Push left child
                }
            } else if (current.state == 2) { // In-order traversal
                inOrder.add(current.node.val);
                current.state++;
                stack.push(current); // Push back with updated state
                if (current.node.right != null) {
                    stack.push(new Pair(current.node.right, 1)); // Push right child
                }
            } else { // Post-order traversal
                postOrder.add(current.node.val);
            }
        }

        return Arrays.asList(preOrder, inOrder, postOrder);
    }

    public static void main(String[] args) {
        // Creating a sample binary tree
        // 1
        // / \
        // 2 3
        // / \
        // 4 5

        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);

        List<List<Integer>> result = preInPostTraversal(root);
        System.out.println("Pre-order: " + result.get(0));
        System.out.println("In-order: " + result.get(1));
        System.out.println("Post-order: " + result.get(2));
    }
}
