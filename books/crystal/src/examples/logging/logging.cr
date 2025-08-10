require "log"

Log.setup(:trace) # set the level of logging

Log.trace { "Trace level" }
Log.debug { "Debug level" }
Log.info { "Info level" }
Log.notice { "Notice level" }
Log.warn { "Warn level" }
Log.error { "Error level" }
Log.fatal { "Fatal level" }
