

# readlnOrNull

Reads a line of input from the standard input stream and returns it, or return null if EOF has already been reached when readlnOrNull is called.

```kotlin
expect fun readlnOrNull(): String?(source)
```

```kotlin
fun main() {
    println("Enter text (Ctrl+D to end):")
    while (true) {
        val line = readlnOrNull() ?: break   // returns null on EOF
        println("You entered: $line")
    }
    println("EOF reached.")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/readln-or-null.html)

    