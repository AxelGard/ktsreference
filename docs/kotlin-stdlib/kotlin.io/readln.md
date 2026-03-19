

# readln

Reads a line of input from the standard input stream and returns it, or throws a RuntimeException if EOF has already been reached when readln is called.

```kotlin
expect fun readln(): String(source)
```

```kotlin
fun main() {
    println("What is your name?")
    val name = readln()

    println("How old are you?")
    val age = readln()

    println("Hello, $name! You are $age years old.")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/readln.html)

    