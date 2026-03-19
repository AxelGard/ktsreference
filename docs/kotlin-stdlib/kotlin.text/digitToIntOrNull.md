

# digitToIntOrNull

Returns the numeric value of the decimal digit that this Char represents, or null if this Char is not a valid decimal digit.

```kotlin
fun Char.digitToIntOrNull(): Int?(source)
```

```kotlin
fun main() {
    val chars = "a5f2"

    for (c in chars) {
        val value = c.digitToIntOrNull()
        println("Character: '$c' → ${value ?: "not a digit"}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/digit-to-int-or-null.html)

    