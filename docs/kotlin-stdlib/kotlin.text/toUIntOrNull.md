

# toUIntOrNull

Parses the string as an UInt number and returns the result or null if the string is not a valid representation of a number.

```kotlin
fun String.toUIntOrNull(): UInt?(source)
```

```kotlin
fun main() {
    val valid = "42".toUIntOrNull()
    val invalid = "not_a_number".toUIntOrNull()

    println(valid)   // 42
    println(invalid) // null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-u-int-or-null.html)

    