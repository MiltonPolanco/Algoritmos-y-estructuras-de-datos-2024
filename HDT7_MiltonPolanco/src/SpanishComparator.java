//********************
// UNIVERSIDAD DEL VALLE DE GUATEMALA
// Departamento de Ciencias De La Computacion
// CC2016 - 20
// Milton Polanco / 23471
// Fecha: 4/4/2024
// Repositorio GitHub:https://github.com/MiltonPolanco/Algoritmos-y-estructuras-de-datos-2024
//********************
public class SpanishComparator implements LanguageComparator {
    @Override
    public int compare(Association a1, Association a2) {
        return a1.getSpanish().compareTo(a2.getSpanish());
    }

    @Override
    public String getText(Association association) {
        return association.getSpanish();
    }
}