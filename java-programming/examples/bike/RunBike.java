public class RunBike {
    public static void bike_shop() {
        System.out.println(Bike.getCount());
        Bike a = new Bike();
        System.out.println(Bike.getCount());
        Bike b = new Bike();
        System.out.println(Bike.getCount());
        Bike c = new Bike();
        System.out.println(Bike.getCount());
        b = null;
        //System.gc();
        System.out.println(Bike.getCount());
    }
    public static void main(String[] args) {
        bike_shop();
        System.out.println(Bike.getCount());
    }
}

// The finalize methods is supposed to be similar to a destructor, but it might be never called in the life of the program. So we cannot rely on it.
