

# toIntOrNull

Parses the string to an Int number or returns null if the string is not a valid representation of an Int.

```kotlin
fun String.toIntOrNull(): Int?(source)
```

```kotlin
fun main() {
    val validInput = "42"
    val invalidInput = "hello"

    val number1: Int? = validInput.toIntOrNull()
    val number2: Int? = invalidInput.toIntOrNull()

    println("validInput -> $number1")   // prints: validInput -> 42
    println("invalidInput -> $number2") // prints: invalidInput -> null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-int-or-null.html)

    