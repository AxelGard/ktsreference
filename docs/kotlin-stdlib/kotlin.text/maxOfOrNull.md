

# maxOfOrNull

Returns the largest value among all values produced by selector function applied to each character in the char sequence or null if the char sequence is empty.

```kotlin
inline fun CharSequence.maxOfOrNull(selector: (Char) -> Double): Double?(source)
```

```kotlin
fun main() {
    val text = "kotlin 123"

    // Find the largest character code as a Double
    val maxCode = text.maxOfOrNull { it.code.toDouble() }
    println("Maximum character code: $maxCode")   // prints 114.0 for 't'

    // Example with an empty sequence
    val empty = "".maxOfOrNull { it.code.toDouble() }
    println("Empty string result: $empty")         // prints null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/max-of-or-null.html)

    