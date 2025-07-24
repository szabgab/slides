object ValIsImmutable {
    def main(args:Array[String]) {
        val counter:Int = 0
        println(counter)
        counter = 1
        println(counter)
    }
}
