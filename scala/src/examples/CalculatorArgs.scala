object CalculatorArgs {
    def main(args:Array[String]) {
        if (args.size != 3) {
            println("Usage: CalculatorArgs OPERAND OPERATOR OPERAND")
            sys.exit
        }
        val a  = args(0).toFloat
        val op = args(1)
        val b = args(2).toFloat
        if (op == "+") {
            println(a+b)
        } else if (op == "-") {
            println(a-b)
        }
    }
}
