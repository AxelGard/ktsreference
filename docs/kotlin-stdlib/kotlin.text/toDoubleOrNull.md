

# toDoubleOrNull

Parses the string as a Double number and returns the result or null if the string is not a valid representation of a number.

```kotlin
expect fun String.toDoubleOrNull(): Double?(source)
```

```kotlin
fun main() {
    val valid = "123.45"
    val invalid = "abc"

    println(valid.toDoubleOrNull())   // prints 123.45
    println(invalid.toDoubleOrNull()) // prints null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-double-or-null.html)

    