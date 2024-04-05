
//********************
// UNIVERSIDAD DEL VALLE DE GUATEMALA
// Departamento de Ciencias De La Computacion
// CC2016 - 20
// Milton Polanco / 23471
// Fecha: 4/4/2024
// Repositorio GitHub:https://github.com/MiltonPolanco/Algoritmos-y-estructuras-de-datos-2024
//********************
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class Main {
    private static BinaryTree englishTree = new BinaryTree(new EnglishComparator());
    private static BinaryTree spanishTree = new BinaryTree(new SpanishComparator());
    private static BinaryTree frenchTree = new BinaryTree(new FrenchComparator());

    public static void main(String[] args) {
        loadDictionary();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Acciones:");
        System.out.println("1. Árboles del diccionario.");
        System.out.println("2. Traducción de texto");
        int option = scanner.nextInt();

        if (option == 1) {
            printTrees(scanner);
        } else if (option == 2) {
            System.out.println("Idioma destino:");
            System.out.println("1. Inglés");
            System.out.println("2. Español");
            System.out.println("3. Francés");
            int targetLanguage = scanner.nextInt();
            translateText(targetLanguage);
        } else {
            System.out.println("Error");
        }
        scanner.close();
    }

    private static void loadDictionary() {
        try (BufferedReader br = new BufferedReader(new FileReader("diccionario.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(",");
                Association association = new Association(parts[0], parts[1], parts[2]);
                englishTree.insert(association);
                spanishTree.insert(association);
                frenchTree.insert(association);
            }
        } catch (IOException e) {
            System.err.println("Error al leer diccionario: " + e.getMessage());
        }
    }

    private static void translateText(int targetLanguage) {
        BinaryTree targetTree = null;
        switch (targetLanguage) {
            case 1:
                targetTree = englishTree;
                break;
            case 2:
                targetTree = spanishTree;
                break;
            case 3:
                targetTree = frenchTree;
                break;
            default:
                System.out.println("Idioma inválido.");
                return;
        }

        try (BufferedReader br = new BufferedReader(new FileReader("texto.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                for (String word : line.split("\\s+")) {
                    String lowerWord = word.toLowerCase();
                    String translation = translateWord(lowerWord, targetTree);
                    System.out.print(translation + " ");
                }
                System.out.println();
            }
        } catch (IOException e) {
            System.err.println("Error al leer el archivo " + e.getMessage());
        }
    }

    private static String translateWord(String word, BinaryTree targetTree) {
        Association association = englishTree.search(word);
        if (association == null)
            association = spanishTree.search(word);
        if (association == null)
            association = frenchTree.search(word);

        if (association != null) {
            if (targetTree == englishTree) {
                return association.getEnglish();
            } else if (targetTree == spanishTree) {
                return association.getSpanish();
            } else if (targetTree == frenchTree) {
                return association.getFrench();
            } else {
                return "*" + word + "*";
            }
        }
        return "*" + word + "*";
    }

    private static void printTrees(Scanner scanner) {
        int languageChoice = 0;

        while (languageChoice < 1 || languageChoice > 3) {
            System.out.println("Idioma del árbol:");
            System.out.println("1. Inglés");
            System.out.println("2. Español");
            System.out.println("3. Francés");

            String languageChoiceInput = scanner.nextLine().trim();

            switch (languageChoiceInput) {
                case "1":
                    System.out.println("Arbol en ingles:");
                    englishTree.printTree(englishTree.getRoot(), null, false);
                    englishTree.printInOrder();
                    break;
                case "2":
                    System.out.println("Arbol en espanol:");
                    spanishTree.printTree(spanishTree.getRoot(), null, false);
                    spanishTree.printInOrder();
                    break;
                case "3":
                    System.out.println("Arbol en frances:");
                    frenchTree.printTree(frenchTree.getRoot(), null, false);
                    frenchTree.printInOrder();
                    break;
                default:
                    System.out.println("Selección no válida.");
                    languageChoice = 0;
                    break;
            }
        }
    }
}