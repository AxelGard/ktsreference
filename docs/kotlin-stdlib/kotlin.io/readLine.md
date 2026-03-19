

# readLine

Reads a line of input from the standard input stream.

```kotlin
fun readLine(): String?(source)
```

```kotlin
fun main() {
    print("Enter your name: ")
    val name = readLine() ?: "Stranger"
    println("Hello, $name!")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/read-line.html)

    