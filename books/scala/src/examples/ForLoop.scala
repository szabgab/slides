object ForLoop {
    def main(args:Array[String]) {
        val planets = List("Mercury", "Venus", "Earth", "Mars")
        for(name <- planets) println(name)
        for(name <- planets) {
           println(name)
        }
    }
}
