//********************
// UNIVERSIDAD DEL VALLE DE GUATEMALA
// Departamento de Ciencias De La Computacion
// CC2016 - 20
// Milton Polanco / 23471
// Fecha: 4/4/2024
// Repositorio GitHub:https://github.com/MiltonPolanco/Algoritmos-y-estructuras-de-datos-2024
//********************
public class Association {
    private String english;
    private String spanish;
    private String french;

    public Association(String english, String spanish, String french) {
        this.english = english.toLowerCase();
        this.spanish = spanish.toLowerCase();
        this.french = french.toLowerCase();
    }

    public String getEnglish() {
        return english;
    }

    public String getSpanish() {
        return spanish;
    }

    public String getFrench() {
        return french;
    }

    public String getKey() {
        return getEnglish(); // Se devuelve el término en inglés
    }
}