

# toULongOrNull

Parses the string as an ULong number and returns the result or null if the string is not a valid representation of a number.

```kotlin
fun String.toULongOrNull(): ULong?(source)
```

```kotlin
fun main() {
    val valid = "1234567890".toULongOrNull()
    println(valid)          // prints 1234567890

    val invalid = "not_a_number".toULongOrNull()
    println(invalid)        // prints null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-u-long-or-null.html)

    