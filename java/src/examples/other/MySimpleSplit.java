public class MySimpleSplit {
    public static void main(String[] args) {
        String planetNames = "Mercury,Venus,Earth,Mars";
        System.out.println(planetNames);
        System.out.println(planetNames.length());

        String[] planets = planetNames.split(",");
        System.out.println(planets[0]);
        System.out.println(planets.length);
        System.out.println("");
        for (int i=0; i < planets.length; i++) {
            System.out.println(planets[i]);
        }
    }
}
