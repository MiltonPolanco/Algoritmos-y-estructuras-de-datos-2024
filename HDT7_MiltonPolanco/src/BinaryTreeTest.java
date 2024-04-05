import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class BinaryTreeTest {
    private BinaryTree englishTree;

    @Before
    public void setUp() {
        englishTree = new BinaryTree(new EnglishComparator());
        // El diccionario.txt contiene estas asociaciones
        englishTree.insert(new Association("town", "pueblo", "ville"));
        englishTree.insert(new Association("dog", "perro", "chien"));
    }

    @Test
    public void whenInserted_thenShouldBeFound() {
        // Nueva asociación
        englishTree.insert(new Association("cat", "gato", "chat"));
        Association found = englishTree.search("cat");
        assertNotNull("La inserción de 'cat' debería ser encontrada.", found);
    }

    @Test
    public void whenSearchedForExistingWord_thenCorrectTranslationShouldBeReturned() {
        // Cuando buscamos una palabra que existe
        Association found = englishTree.search("town");
        // Entonces deberíamos obtener la traducción correcta
        assertNotNull(found);
        assertEquals("La traducción al español de 'town' debería ser 'pueblo'.", "pueblo", found.getSpanish());
    }

    @Test
    public void whenSearchedForNonExistingWord_thenShouldBeNull() {
        // Cuando buscamos una palabra que no existe
        Association found = englishTree.search("apple");
        // Entonces el resultado debería ser null
        assertNull("La búsqueda de 'apple' debería devolver null.", found);
    }

    @Test
    public void whenInsertedDuplicate_thenShouldNotInsert() {
        englishTree.insert(new Association("dog", "perro", "chien"));
    }
}
