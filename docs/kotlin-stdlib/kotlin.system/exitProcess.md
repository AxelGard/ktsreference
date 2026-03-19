

# exitProcess

Terminates the currently running process.

```kotlin
inline fun exitProcess(status: Int): Nothing(source)
```

```kotlin
import kotlin.system.exitProcess

fun main() {
    println("Starting the program.")
    val shouldExit = true
    if (shouldExit) {
        println("Exiting now with status 0.")
        exitProcess(0)
    }
    println("This line will not be reached.")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.system/exit-process.html)

    