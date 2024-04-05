//********************
// UNIVERSIDAD DEL VALLE DE GUATEMALA
// Departamento de Ciencias De La Computacion
// CC2016 - 20
// Milton Polanco / 23471
// Fecha: 4/4/2024
// Repositorio GitHub:https://github.com/MiltonPolanco/Algoritmos-y-estructuras-de-datos-2024
//********************
public class Trunk {
    Trunk prev;
    String str;

    public Trunk(Trunk prev, String str) {
        this.prev = prev;
        this.str = str;
    }
}