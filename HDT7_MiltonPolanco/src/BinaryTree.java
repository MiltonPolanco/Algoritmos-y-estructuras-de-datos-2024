
//********************
// UNIVERSIDAD DEL VALLE DE GUATEMALA
// Departamento de Ciencias De La Computacion
// CC2016 - 20
// Milton Polanco / 23471
// Fecha: 4/4/2024
// Repositorio GitHub:https://github.com/MiltonPolanco/Algoritmos-y-estructuras-de-datos-2024
//********************
import java.util.ArrayList;
import java.util.List;

public class BinaryTree {
    private TreeNode root;
    private LanguageComparator comparator;

    public BinaryTree(LanguageComparator comparator) {
        this.root = null;
        this.comparator = comparator;
    }

    public TreeNode getRoot() {
        return root;
    }

    public void insert(Association association) {
        root = insertRecursive(root, association);
    }

    private TreeNode insertRecursive(TreeNode current, Association association) {
        if (current == null) {
            return new TreeNode(association);
        }

        if (comparator.compare(association, current.association) < 0) {
            current.left = insertRecursive(current.left, association);
        } else if (comparator.compare(association, current.association) > 0) {
            current.right = insertRecursive(current.right, association);
        }

        return current;
    }

    private void showTrunks(Trunk p) {
        if (p != null) {
            showTrunks(p.prev);
            System.out.print(p.str);
        }
    }

    public void printTree(TreeNode root, Trunk prev, boolean isLeft) {
        if (root == null) {
            return;
        }

        String prev_str = "    ";
        Trunk trunk = new Trunk(prev, prev_str);

        printTree(root.right, trunk, true);

        if (prev == null) {
            trunk.str = "---";
        } else if (isLeft) {
            trunk.str = ".---";
            prev_str = "   |";
        } else {
            trunk.str = "`---";
            prev.str = prev_str;
        }

        showTrunks(trunk);
        System.out.println(" " + comparator.getText(root.association));

        if (prev != null) {
            prev.str = prev_str;
        }
        trunk.str = "   |";

        printTree(root.left, trunk, false);
    }

    public void printInOrder() {
        List<Association> words = new ArrayList<>();
        inOrderRecursive(root, words);
        for (Association a : words) {
            System.out.print("(" + a.getEnglish() + ", " + a.getSpanish() + ", " + a.getFrench() + ") ");
        }
        System.out.println();
    }

    private void inOrderRecursive(TreeNode node, List<Association> words) {
        if (node != null) {
            inOrderRecursive(node.left, words);
            words.add(node.association);
            inOrderRecursive(node.right, words);
        }
    }

    public Association search(String word) {
        return searchRecursive(root, word);
    }

    private Association searchRecursive(TreeNode current, String word) {
        if (current == null) {
            return null;
        } else if (current.association.getKey().equals(word)) {
            return current.association;
        } else if (current.association.getKey().compareTo(word) > 0) {
            return searchRecursive(current.left, word);
        } else {
            return searchRecursive(current.right, word);
        }
    }

}