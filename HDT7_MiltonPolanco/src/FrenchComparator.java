//********************
// UNIVERSIDAD DEL VALLE DE GUATEMALA
// Departamento de Ciencias De La Computacion
// CC2016 - 20
// Milton Polanco / 23471
// Fecha: 4/4/2024
// Repositorio GitHub:https://github.com/MiltonPolanco/Algoritmos-y-estructuras-de-datos-2024
//********************
public class FrenchComparator implements LanguageComparator {
    @Override
    public int compare(Association a1, Association a2) {
        return a1.getFrench().compareTo(a2.getFrench());
    }

    @Override
    public String getText(Association association) {
        return association.getFrench();
    }
}